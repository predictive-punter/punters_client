from datetime import datetime
import multiprocessing
import re
from threading import BoundedSemaphore
import time

import pytz
import tzlocal

from . import __version__
from .html_utils import *


class Scraper:
    """Provide web scraping functionality for www.punters.com.au"""

    AUSTRALIAN_STATES = (
        'australian-capital-territory',
        'new-south-wales',
        'northern-territory',
        'queensland',
        'south-australia',
        'tasmania',
        'victoria',
        'western-australia'
    )

    SOURCE_TIMEZONE = pytz.timezone('Australia/Melbourne')

    URL_ROOT = 'https://www.punters.com.au/'

    def __init__(self, http_client, html_parser, local_timezone=tzlocal.get_localzone(), concurrent_requests=multiprocessing.cpu_count() * 5):

        self.http_client = http_client
        self.parse_html = html_parser

        self.local_timezone = local_timezone

        self.request_lock = BoundedSemaphore(concurrent_requests)

    def fix_url(self, url, url_root=URL_ROOT):
        """Ensure the specified URL is fully qualified by prepending url_root if necessary"""

        if not re.search('[a-z]+://.*', url):
            if url.startswith('/') and url_root.endswith('/'):
                url = url_root[:-1] + url
            elif url.startswith('/') or url_root.endswith('/'):
                url = url_root + url
            else:
                url = url_root + '/' + url
        return url

    def get_html(self, url, retry_count=0, max_retries=5):
        """Get the root HTML element from the specified URL"""

        try:

            with self.request_lock:

                response = self.http_client.get(url)
                
                if response.status_code >= 500:
                    response.raise_for_status()
                elif response.status_code >= 400:
                    return None
                else:
                    return self.parse_html(response.text)

        except BaseException:

            if retry_count < max_retries:
                time.sleep(1)
                return self.get_html(url, retry_count + 1, max_retries)

            else:
                raise

    def is_compatible_with(self, version):
        """Return True if the current scraper version is compatible with the specified version"""

        return version.split('.')[0] == __version__.split('.')[0]
    
    def scrape_meets(self, date, meet_url_pattern='/({states})/'.format(states='|'.join(AUSTRALIAN_STATES))):
        """Scrape a list of meets occurring on the specified date"""

        meets = []

        try:
            date = self.local_timezone.localize(date)
        except ValueError:
            pass
        date = date.astimezone(self.SOURCE_TIMEZONE).replace(hour=0, minute=0, second=0, microsecond=0)
        date_string = date.strftime('%Y-%m-%d')

        html = self.get_html('https://www.punters.com.au/racing-results/{date}/'.format(date=date_string))
        if html is not None:

            for link in html.cssselect('a.label-link'):
                link_href = link.get('href')
                if date_string in link_href:
                    if meet_url_pattern is not None and re.search(meet_url_pattern, link_href):

                        meets.append({
                            'date':             date,
                            'track':            link.text_content().strip(),
                            'url':              self.fix_url(link.get('href')),
                            'scraper_version':  __version__
                        })

        return meets

    def scrape_races(self, meet):
        """Scrape a list of races occurring at the specified meet"""

        def parse_prize_pool(header_cell):
            groups = get_child_text_match_groups(header_cell, 'div.details-line span.capitalize', 'Total \$([\d.]+)([a-zA-Z])', index=0)
            if groups is not None and len(groups) > 0:
                prize_pool = float(groups[0])
                if len(groups) > 1:
                    if groups[1] in ('k', 'K'):
                        prize_pool *= 1000
                    elif groups[1] in ('m', 'M'):
                        prize_pool *= 1000000
                return prize_pool

        def parse_start_time(header_cell):
            value = parse_child_attribute(header_cell, 'div.details-line abbr.timestamp', 'data-utime', int)
            if value is not None:
                return datetime.fromtimestamp(value, self.SOURCE_TIMEZONE)

        races = []

        html = self.get_html(meet['url'])
        if html is not None:
            
            for table in html.cssselect('table.results-table'):
                header_cell = get_child(table, 'thead tr th')
                if header_cell is not None:

                    race = {
                        'number':           parse_child_text_match_group(header_cell, 'b.capitalize', '(\d+)', int),
                        'distance':         parse_child_attribute(header_cell, 'span.distance abbr.conversion', 'data-value', int),
                        'prize_pool':       parse_prize_pool(header_cell),
                        'track_condition':  get_child_text(header_cell, 'div.details-line span.capitalize', index=1),
                        'start_time':       parse_start_time(header_cell),
                        'url':              self.fix_url(get_child_attribute(header_cell, 'div.details-line span.capitalize a', 'href')),
                        'group':            None,
                        'entry_conditions': None,
                        'track_circ':       None,
                        'track_straight':   None,
                        'track_rail':       None,
                        'scraper_version':  __version__
                    }

                    html2 = self.get_html(race['url'])
                    if html2 is not None:

                        race['group'] = get_child_text(html2, 'span.event-name-title strong')

                        race['entry_conditions'] = [span.text_content().replace('.', '').strip() for span in html2.cssselect('div.event-details span.entry-conditions-text span')]

                        spans = html2.cssselect('div.event-details-bottom div span')
                        for index in range(0, len(spans) - 1, 2):
                            key = 'track_' + spans[index].text_content().strip().lower()

                            if key in ('track_circ', 'track_straight'):
                                race[key] = parse_child_attribute(spans[index + 1], 'abbr.conversion', 'data-value', int)

                            elif key == 'track_rail':
                                race[key] = spans[index + 1].text_content().strip()

                    races.append(race)

        return races

    def scrape_runners(self, race):
        """Scrape a list of runners competing in the specified race"""

        runners = []

        html = self.get_html(race['url'])
        if html is not None:
            
            for row in html.cssselect('table.form-guide-overview__table tbody tr'):

                runners.append({
                    'number':               parse_child_text_match_group(row, 'td.form-guide-overview__competitor-number', '(\d+)', int),
                    'is_scratched':         row.get('class') is not None and 'scratched' in row.get('class').lower(),
                    'horse_url':            self.fix_url(get_child_attribute(row, 'a.form-guide-overview__horse-link', 'href')),
                    'horse_has_blinkers':   get_child(row, 'div.has-blinkers') is not None,
                    'jockey_url':           self.fix_url(get_child_attribute(row, 'a.form-guide-overview__jockey-link', 'href')),
                    'jockey_is_apprentice': get_child(row, 'a.form-guide-overview__jockey-link span') is not None,
                    'jockey_claiming':      parse_child_text_match_group(row, 'a.form-guide-overview__jockey-link span', '\(a([\d.]+)\)', float, default=0.0),
                    'trainer_url':          self.fix_url(get_child_attribute(row, 'a.form-guide-overview__trainer-link', 'href')),
                    'weight':               parse_child_text(row, 'td.form-guide-overview__competitor-weight', float),
                    'barrier':              parse_child_text(row, 'td.form-guide-overview__competitor-barrier', int),
                    'scraper_version':      __version__
                })

        return runners

    def scrape_profile(self, url):
        """Scrape a profile from the specified URL"""

        def parse_name(html):
            name = get_child_text(html, 'h1')
            if name is not None:
                span_text = get_child_text(html, 'h1 span')
                if span_text is not None:
                    name = name.replace(span_text, '').strip()
            return name

        if url != self.URL_ROOT:
            html = self.get_html(url)
            if html is not None:

                profile = {
                    'url':              url,
                    'name':             parse_name(html),
                    'scraper_version':  __version__
                }

                for row in html.cssselect('div.moduleItem table tr'):
                    label = get_child_text(row, 'th')
                    if label is not None:
                        label = label.replace(':', '').lower()

                        if label == 'profile':
                            groups = get_child_text_match_groups(row, 'td', 'year old (.*) (.*)')
                            if groups is not None and len(groups) > 1:
                                profile['colour'] = groups[0]
                                profile['sex'] = groups[1]

                        elif label == 'pedigree':
                            groups = get_child_text_match_groups(row, 'td', '(.*) x (.*)')
                            if groups is not None and len(groups) > 1:
                                profile['sire'] = groups[0]
                                profile['dam'] = groups[1]

                        elif label == 'country':
                            profile['country'] = get_child_text(row, 'td')

                        elif label == 'foaled':
                            value = get_child_text(row, 'td')
                            if value is not None:
                                profile['foaled'] = self.SOURCE_TIMEZONE.localize(datetime.strptime(value, '%d/%m/%Y'))

                return profile

    def scrape_horse(self, runner):
        """Scrape the profile of the horse associated with the specified runner"""

        return self.scrape_profile(runner['horse_url'])

    def scrape_jockey(self, runner):
        """Scrape the profile of the jockey associated with the specified runner"""

        return self.scrape_profile(runner['jockey_url'])

    def scrape_trainer(self, runner):
        """Scrape the profile of the trainer associated with the specified runner"""

        return self.scrape_profile(runner['trainer_url'])

    def scrape_performances(self, profile):
        """Scrape a list of performances associated with the specified profile"""

        def parse_date(ul):
            value = get_child_text(ul, 'li.timeline-disc b span.date')
            if value is not None:
                return self.SOURCE_TIMEZONE.localize(datetime.strptime(value, '%d-%b-%y'))

        def parse_money(ul, pattern):
            value = get_child_text_match_group(ul, 'li.timeline-disc', pattern)
            if value is not None:
                value = value.replace(',', '')
                value = re.sub('\.+', '.', value)
                while value[0] == '.':
                    value = value[1:]
                while value[-1] == '.':
                    value = value[:-1]
                return float(value)

        def parse_winning_time(ul):
            value = get_child_text_match_group(ul, 'li.timeline-disc', 'Winning Time: ([\d:.]+)')
            if value is not None:
                value_parts = value.split(':')
                if len(value_parts) > 0:
                    winning_time = float(value_parts[-1])
                    if len(value_parts) > 1:
                        winning_time += int(value_parts[0]) * 60
                    return round(winning_time, 2)

        performances = []

        html = self.get_html(profile['url'])
        if html is not None:
            
            for ul in html.cssselect('ul.timeline'):
                if 'TRIAL' not in ul.text_content().upper():
                    result_text = get_child_text(ul, 'span.formSummaryPosition')
                    if result_text != 'Abn':

                        performance = {
                            'track':            get_child_text(ul, 'li.timeline-disc b span.simlight'),
                            'date':             parse_date(ul),
                            'distance':         parse_child_text_match_group(ul, 'li.timeline-disc span.dist', '(\d+)', int),
                            'track_condition':  get_child_text(ul, 'span.badge'),
                            'prize_money':      parse_money(ul, '\$([\d,.]+) \(of'),
                            'prize_pool':       parse_money(ul, '\(of \$([\d,.]+)'),
                            'barrier':          parse_child_text_match_group(ul, 'li.timeline-disc', 'Barrier (\d+)', int),
                            'winning_time':     parse_winning_time(ul),
                            'starting_price':   parse_money(ul, 'SP: \$([\d.]+)'),
                            'horse_url':        None,
                            'jockey_url':       None,
                            'weight':           None,
                            'carried':          None,
                            'lengths':          parse_child_text_match_group(ul, 'span.timeline-right.placed', '([\d.]+)L', float, default=0.0),
                            'result':           try_parse(result_text, int),
                            'starters':         parse_child_text(ul, 'span.starters', int),
                            'scraper_version':  __version__
                        }

                        for link in ul.cssselect('span.timeline-right.placed a'):
                            link_href = link.get('href')
                            for key in ('horse', 'jockey'):
                                if key in link_href:
                                    performance[key + '_url'] = self.fix_url(link_href)
                                    break

                        weights = [float(abbr.get('data-value')) for abbr in ul.cssselect('span.timeline-right.placed abbr') if abbr.get('data-type') == 'weight']
                        if len(weights) > 0:
                            performance['weight'] = performance['carried'] = weights[-1]
                            if len(weights) > 1:
                                performance['weight'] = weights[0]

                        performances.append(performance)

        return performances

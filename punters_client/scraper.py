from datetime import datetime
import re

import pytz
import tzlocal

from . import __version__
from .html_utils import *


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


class Scraper:
    """Provide web scraping functionality for www.punters.com.au"""

    SOURCE_TIMEZONE = pytz.timezone('Australia/Melbourne')

    def __init__(self, http_client, html_parser, local_timezone=tzlocal.get_localzone()):

        self.http_client = http_client
        self.parse_html = html_parser

        self.local_timezone = local_timezone

    def fix_url(self, url, url_root='https://www.punters.com.au'):
        """Ensure the specified URL is fully qualified by prepending url_root if necessary"""

        if not re.search('[a-z]+://.*', url):
            if url.startswith('/') and url_root.endswith('/'):
                url = url_root[:-1] + url
            elif url.startswith('/') or url_root.endswith('/'):
                url = url_root + url
            else:
                url = url_root + '/' + url
        return url

    def get_html(self, url):
        """Get the root HTML element from the specified URL"""

        response = self.http_client.get(url)
        response.raise_for_status()
        return self.parse_html(response.text)
    
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

                    races.append({
                        'number':           parse_child_text_match_group(header_cell, 'b.capitalize', '(\d+)', int),
                        'distance':         parse_child_attribute(header_cell, 'span.distance abbr.conversion', 'data-value', int),
                        'prize_pool':       parse_prize_pool(header_cell),
                        'track_condition':  get_child_text(header_cell, 'div.details-line span.capitalize', index=1),
                        'start_time':       parse_start_time(header_cell),
                        'url':              self.fix_url(get_child_attribute(header_cell, 'div.details-line span.capitalize a', 'href')),
                        'scraper_version':  __version__
                    })

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

        html = self.get_html(url)
        if html is not None:

            profile = {
                'url':              url,
                'name':             get_child_text(html, 'div.moduleItem table caption').replace('Details', '').strip(),
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

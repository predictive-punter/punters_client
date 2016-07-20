import re

import pytz
import tzlocal

from . import __version__


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
            if not (url.startswith('/') or url_root.endswith('/')):
                url = '/' + url
            url = url_root + url
        return url

    def get_html(self, url):
        """Get the root HTML element from the specified URL"""

        response = self.http_client.get(url)
        response.raise_for_status()
        return self.parse_html(response.text)
    
    def scrape_meets(self, date):
        """Scrape a list of meets occurring on the specified date"""

        meets = []

        try:
            date = self.local_timezone.localize(date)
        except ValueError:
            pass
        date = date.astimezone(self.SOURCE_TIMEZONE).replace(hour=0, minute=0, second=0, microsecond=0)

        html = self.get_html('https://www.punters.com.au/racing-results/{date:%Y-%m-%d}/'.format(date=date))
        if html is not None:
            
            for link in html.cssselect('a.label-link'):

                meets.append({
                    'date':             date,
                    'track':            link.text_content().strip(),
                    'url':              self.fix_url(link.get('href')),
                    'scraper_version':  __version__
                })

        return meets

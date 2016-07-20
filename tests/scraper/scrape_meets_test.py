from datetime import datetime

import punters_client
import pytest
import tzlocal

from common import check_expected_items, check_unexpected_items


@pytest.fixture(scope='module', params=[datetime(2016, 2, 1), tzlocal.get_localzone().localize(datetime(2016, 2, 1))])
def date(request):

    return request.param


@pytest.fixture(scope='module')
def expected_meets(date, source_timezone):

    try:
        date = source_timezone.localize(date)
    except ValueError:
        date = date.astimezone(source_timezone)
    date = date.replace(hour=0, minute=0, second=0, microsecond=0)

    return [
        {
            'date':             date,
            'track':            'Kilmore',
            'url':              'https://www.punters.com.au/racing-results/victoria/Kilmore/2016-02-01/',
            'scraper_version':  punters_client.__version__
        },
        {
            'date':             date,
            'track':            'Nowra',
            'url':              'https://www.punters.com.au/racing-results/new-south-wales/Nowra/2016-02-01/',
            'scraper_version':  punters_client.__version__
        }
    ]


@pytest.fixture(scope='module')
def scraped_meets(date, scraper):

    return scraper.scrape_meets(date)


def test_expected_meets(expected_meets, scraped_meets):
    """The scrape_meets method should return a list of dictionaries containing all expected values"""

    check_expected_items(expected_meets, scraped_meets, ['date', 'track'])


def test_unexpected_meets(expected_meets, scraped_meets):
    """The scrape_meets method should return a list of dictionaries that does not contain any unexpected values"""

    check_unexpected_items(expected_meets, scraped_meets, ['date', 'track'])

from datetime import datetime

import punters_client
import pytest
import pytz
import tzlocal


@pytest.fixture(scope='module', params=[datetime(2016, 2, 1), tzlocal.get_localzone().localize(datetime(2016, 2, 1))])
def date(request):

    return request.param


@pytest.fixture(scope='module')
def expected_meets(date):

    source_timezone = pytz.timezone('Australia/Melbourne')
    try:
        date = source_timezone.localize(date)
    except ValueError:
        date = date.astimezone(source_timezone)

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

    for expected_meet in expected_meets:

        found_meet = None
        for scraped_meet in scraped_meets:
            if scraped_meet['date'] == expected_meet['date'] and scraped_meet['track'] == expected_meet['track']:
                found_meet = scraped_meet
                break

        for key in expected_meet:
            assert found_meet[key] == expected_meet[key]
        for key in found_meet:
            assert expected_meet[key] == found_meet[key]


def test_unexpected_meets(expected_meets, scraped_meets):
    """The scrape_meets method should return a list of dictionaries that does not contain any unexpected values"""

    for scraped_meet in scraped_meets:

        found_meet = None
        for expected_meet in expected_meets:
            if expected_meet['date'] == scraped_meet['date'] and expected_meet['track'] == scraped_meet['track']:
                found_meet = expected_meet
                break

        assert found_meet is not None

from datetime import datetime

import punters_client
import pytest


@pytest.fixture(scope='module')
def expected_values(runner, source_timezone):

    return {
        'url':              runner['horse_url'],
        'name':             'Tycoon Tony',
        'colour':           'bay',
        'sex':              'gelding',
        'sire':             'Written Tycoon',
        'dam':              'Real Ruby',
        'country':          'Australia',
        'foaled':           source_timezone.localize(datetime(2011, 10, 1)),
        'scraper_version':  punters_client.__version__
    }


@pytest.fixture(scope='module')
def scraped_values(runner, scraper):

    return scraper.scrape_horse(runner)


def test_expected_values(expected_values, scraped_values):
    """The scrape_horse method should return a dictionary containing all expected values"""

    assert scraped_values == expected_values

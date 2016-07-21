from datetime import datetime

import punters_client
import pytest


@pytest.fixture(scope='module')
def runner():

    return {
        'number':               1,
        'is_scratched':         False,
        'horse_url':            'https://www.punters.com.au/horses/Tycoon-Tony_395471/',
        'horse_has_blinkers':   False,
        'jockey_url':           'https://www.punters.com.au/jockeys/Ben-E-Thompson_2143/',
        'jockey_is_apprentice': True,
        'jockey_claiming':      1.5,
        'trainer_url':          'https://www.punters.com.au/trainers/Scott-McIntosh_1010/',
        'weight':               61.0,
        'barrier':              2,
        'scraper_version':      punters_client.__version__
    }


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

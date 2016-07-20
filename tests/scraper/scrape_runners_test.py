from datetime import datetime

import punters_client
import pytest

from common import check_expected_items, check_unexpected_items


@pytest.fixture(scope='module')
def race(source_timezone):

    return {
        'number':           5,
        'distance':         1100,
        'prize_pool':       20000.00,
        'track_condition':  'Good 4',
        'start_time':       source_timezone.localize(datetime(2016, 2, 1, 15, 32)),
        'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/www.kilmoreracingclub.com.au-BM64-Handicap_411196/',
        'scraper_version':  punters_client.__version__
    }


@pytest.fixture(scope='module')
def expected_runners():

    return [
        {
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
        },
        {
            'number':               2,
            'is_scratched':         False,
            'horse_url':            'https://www.punters.com.au/horses/Chima_325128/',
            'horse_has_blinkers':   False,
            'jockey_url':           'https://www.punters.com.au/jockeys/Cory-Parish_2656/',
            'jockey_is_apprentice': False,
            'jockey_claiming':      0.0,
            'trainer_url':          'https://www.punters.com.au/trainers/David-Hayes-and-Tom-Dabernig_897/',
            'weight':               58.5,
            'barrier':              7,
            'scraper_version':      punters_client.__version__
        },
        {
            'number':               3,
            'is_scratched':         False,
            'horse_url':            'https://www.punters.com.au/horses/Thisgoingsomewhere_214653/',
            'horse_has_blinkers':   True,
            'jockey_url':           'https://www.punters.com.au/jockeys/Jarrod-Fry_686/',
            'jockey_is_apprentice': False,
            'jockey_claiming':      0.0,
            'trainer_url':          'https://www.punters.com.au/trainers/John-and-Chris-Ledger_938/',
            'weight':               58.0,
            'barrier':              5,
            'scraper_version':      punters_client.__version__
        },
        {
            'number':               4,
            'is_scratched':         False,
            'horse_url':            'https://www.punters.com.au/horses/Azzcool_158971/',
            'horse_has_blinkers':   False,
            'jockey_url':           'https://www.punters.com.au/jockeys/Chris-Symons_291/',
            'jockey_is_apprentice': False,
            'jockey_claiming':      0.0,
            'trainer_url':          'https://www.punters.com.au/trainers/Alexander-Rae_13641/',
            'weight':               57.5,
            'barrier':              4,
            'scraper_version':      punters_client.__version__
        },
        {
            'number':               6,
            'is_scratched':         False,
            'horse_url':            'https://www.punters.com.au/horses/Love-And-Lies_315909/',
            'horse_has_blinkers':   False,
            'jockey_url':           'https://www.punters.com.au/jockeys/Rebecca-Williams_2263/',
            'jockey_is_apprentice': True,
            'jockey_claiming':      1.5,
            'trainer_url':          'https://www.punters.com.au/trainers/Jennifer-Williams_4610/',
            'weight':               57.0,
            'barrier':              10,
            'scraper_version':      punters_client.__version__
        },
        {
            'number':               7,
            'is_scratched':         False,
            'horse_url':            'https://www.punters.com.au/horses/Our-Hussey_81386/',
            'horse_has_blinkers':   True,
            'jockey_url':           'https://www.punters.com.au/jockeys/Mitchell-Aitken_9402/',
            'jockey_is_apprentice': True,
            'jockey_claiming':      3.0,
            'trainer_url':          'https://www.punters.com.au/trainers/Russell-Green_8566/',
            'weight':               57.0,
            'barrier':              3,
            'scraper_version':      punters_client.__version__
        },
        {
            'number':               8,
            'is_scratched':         False,
            'horse_url':            'https://www.punters.com.au/horses/Aglaia_316893/',
            'horse_has_blinkers':   True,
            'jockey_url':           'https://www.punters.com.au/jockeys/Brandon-Stockdale_8506/',
            'jockey_is_apprentice': True,
            'jockey_claiming':      1.5,
            'trainer_url':          'https://www.punters.com.au/trainers/Mark-Riley_841/',
            'weight':               56.5,
            'barrier':              9,
            'scraper_version':      punters_client.__version__
        },
        {
            'number':               10,
            'is_scratched':         False,
            'horse_url':            'https://www.punters.com.au/horses/Sullivan-Bay_322748/',
            'horse_has_blinkers':   False,
            'jockey_url':           'https://www.punters.com.au/jockeys/Jye-McNeil_3183/',
            'jockey_is_apprentice': False,
            'jockey_claiming':      0.0,
            'trainer_url':          'https://www.punters.com.au/trainers/David-Hayes-and-Tom-Dabernig_897/',
            'weight':               55.5,
            'barrier':              1,
            'scraper_version':      punters_client.__version__
        },
        {
            'number':               5,
            'is_scratched':         True,
            'horse_url':            'https://www.punters.com.au/horses/All-Australian-Gal_323668/',
            'horse_has_blinkers':   False,
            'jockey_url':           'https://www.punters.com.au/jockeys/Brad-Rawiller_179/',
            'jockey_is_apprentice': False,
            'jockey_claiming':      0.0,
            'trainer_url':          'https://www.punters.com.au/trainers/Luke-Oliver_734/',
            'weight':               57.0,
            'barrier':              6,
            'scraper_version':      punters_client.__version__
        },
        {
            'number':               9,
            'is_scratched':         True,
            'horse_url':            'https://www.punters.com.au/horses/Rose-Dancer_315350/',
            'horse_has_blinkers':   False,
            'jockey_url':           'https://www.punters.com.au/jockeys/Ryan-Maloney_1490/',
            'jockey_is_apprentice': False,
            'jockey_claiming':      0.0,
            'trainer_url':          'https://www.punters.com.au/trainers/Luke-Oliver_734/',
            'weight':               56.5,
            'barrier':              8,
            'scraper_version':      punters_client.__version__
        }
    ]


@pytest.fixture(scope='module')
def scraped_runners(race, scraper):

    return scraper.scrape_runners(race)


def test_expected_runners(expected_runners, scraped_runners):
    """The scrape_runners method should return a list of dictionaries containing all expected values"""

    check_expected_items(expected_runners, scraped_runners, ['number'])


def test_unexpected_runners(expected_runners, scraped_runners):
    """The scrape_runners method should return a list of dictionaries that does not contain any unexpected values"""

    check_unexpected_items(expected_runners, scraped_runners, ['number'])

from datetime import datetime

import punters_client
import pytest

from common import check_expected_items, check_unexpected_items


@pytest.fixture(scope='module')
def horse(source_timezone):

    return {
        'url':              'https://www.punters.com.au/horses/Tycoon-Tony_395471/',
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
def expected_performances(source_timezone):

    return [
        {
            'track':            'Wangaratta',
            'date':             source_timezone.localize(datetime(2016, 4, 21)),
            'distance':         1170,
            'track_condition':  'GOOD 4',
            'prize_money':      500.00,
            'prize_pool':       20000.00,
            'barrier':          16,
            'winning_time':     68.66,
            'starting_price':   6.50,
            'horse_url':        'https://www.punters.com.au/horses/Tycoon-Tony_395471/',
            'jockey_url':       'https://www.punters.com.au/jockeys/Dylan-Dunn_7917/',
            'weight':           60.5,
            'carried':          60.5,
            'lengths':          4.15,
            'result':           10,
            'starters':         13,
            'scraper_version':  punters_client.__version__
        },
        {
            'track':            'Echuca',
            'date':             source_timezone.localize(datetime(2016, 4, 10)),
            'distance':         1209,
            'track_condition':  'GOOD 4',
            'prize_money':      1600.00,
            'prize_pool':       20000.00,
            'barrier':          15,
            'winning_time':     73.20,
            'starting_price':   6.50,
            'horse_url':        'https://www.punters.com.au/horses/Tycoon-Tony_395471/',
            'jockey_url':       'https://www.punters.com.au/jockeys/Mark-Pegus_980/',
            'weight':           60.5,
            'carried':          60.5,
            'lengths':          0.30,
            'result':           3,
            'starters':         12,
            'scraper_version':  punters_client.__version__
        },
        {
            'track':            'Yarra Valley',
            'date':             source_timezone.localize(datetime(2016, 3, 20)),
            'distance':         1200,
            'track_condition':  'HEAVY 9',
            'prize_money':      2000.00,
            'prize_pool':       25000.00,
            'barrier':          4,
            'winning_time':     76.55,
            'starting_price':   2.10,
            'horse_url':        'https://www.punters.com.au/horses/Tycoon-Tony_395471/',
            'jockey_url':       'https://www.punters.com.au/jockeys/Ben-Allen_9146/',
            'weight':           60.5,
            'carried':          59.0,
            'lengths':          2.95,
            'result':           3,
            'starters':         4,
            'scraper_version':  punters_client.__version__
        },
        {
            'track':            'Sandown Hillside',
            'date':             source_timezone.localize(datetime(2016, 2, 17)),
            'distance':         1300,
            'track_condition':  'SOFT 5',
            'prize_money':      700.00,
            'prize_pool':       35000.00,
            'barrier':          4,
            'winning_time':     79.18,
            'starting_price':   9.00,
            'horse_url':        'https://www.punters.com.au/horses/Tycoon-Tony_395471/',
            'jockey_url':       'https://www.punters.com.au/jockeys/Harry-Coffey_3109/',
            'weight':           61.0,
            'carried':          59.5,
            'lengths':          4.35,
            'result':           6,
            'starters':         11,
            'scraper_version':  punters_client.__version__
        },
        {
            'track':            'Kilmore',
            'date':             source_timezone.localize(datetime(2016, 2, 1)),
            'distance':         1100,
            'track_condition':  'GOOD 4',
            'prize_money':      3400.00,
            'prize_pool':       20000.00,
            'barrier':          2,
            'winning_time':     63.60,
            'starting_price':   4.00,
            'horse_url':        'https://www.punters.com.au/horses/Tycoon-Tony_395471/',
            'jockey_url':       'https://www.punters.com.au/jockeys/Ben-E-Thompson_2143/',
            'weight':           61.0,
            'carried':          59.5,
            'lengths':          0.10,
            'result':           2,
            'starters':         8,
            'scraper_version':  punters_client.__version__
        },
        {
            'track':            'Wangaratta',
            'date':             source_timezone.localize(datetime(2016, 1, 21)),
            'distance':         1300,
            'track_condition':  'GOOD 4',
            'prize_money':      500.00,
            'prize_pool':       20000.00,
            'barrier':          12,
            'winning_time':     77.55,
            'starting_price':   8.00,
            'horse_url':        'https://www.punters.com.au/horses/Tycoon-Tony_395471/',
            'jockey_url':       'https://www.punters.com.au/jockeys/Mitchell-Aitken_9402/',
            'weight':           61.0,
            'carried':          58.0,
            'lengths':          5.25,
            'result':           9,
            'starters':         12,
            'scraper_version':  punters_client.__version__
        },
        {
            'track':            'Wangaratta',
            'date':             source_timezone.localize(datetime(2016, 1, 4)),
            'distance':         1170,
            'track_condition':  'SOFT 5',
            'prize_money':      11000.00,
            'prize_pool':       20000.00,
            'barrier':          5,
            'winning_time':     68.51,
            'starting_price':   10.00,
            'horse_url':        'https://www.punters.com.au/horses/Tycoon-Tony_395471/',
            'jockey_url':       'https://www.punters.com.au/jockeys/Ben-E-Thompson_2143/',
            'weight':           60.0,
            'carried':          58.5,
            'lengths':          0.00,
            'result':           1,
            'starters':         14,
            'scraper_version':  punters_client.__version__
        },
        {
            'track':            'Echuca',
            'date':             source_timezone.localize(datetime(2015, 9, 25)),
            'distance':         1100,
            'track_condition':  'GOOD 4',
            'prize_money':      600.00,
            'prize_pool':       20000.00,
            'barrier':          1,
            'winning_time':     64.42,
            'starting_price':   7.00,
            'horse_url':        'https://www.punters.com.au/horses/Tycoon-Tony_395471/',
            'jockey_url':       'https://www.punters.com.au/jockeys/Jason-Collins_2265/',
            'weight':           59.0,
            'carried':          57.0,
            'lengths':          2.80,
            'result':           5,
            'starters':         11,
            'scraper_version':  punters_client.__version__
        },
        {
            'track':            'Echuca',
            'date':             source_timezone.localize(datetime(2015, 9, 5)),
            'distance':         1200,
            'track_condition':  'GOOD 4',
            'prize_money':      13000.00,
            'prize_pool':       20000.00,
            'barrier':          12,
            'winning_time':     72.04,
            'starting_price':   19.00,
            'horse_url':        'https://www.punters.com.au/horses/Tycoon-Tony_395471/',
            'jockey_url':       'https://www.punters.com.au/jockeys/Jason-Collins_2265/',
            'weight':           58.5,
            'carried':          56.5,
            'lengths':          0.00,
            'result':           1,
            'starters':         13,
            'scraper_version':  punters_client.__version__
        },
        {
            'track':            'Echuca',
            'date':             source_timezone.localize(datetime(2015, 8, 17)),
            'distance':         1400,
            'track_condition':  'GOOD 4',
            'prize_money':      900.00,
            'prize_pool':       20000.00,
            'barrier':          6,
            'winning_time':     85.74,
            'starting_price':   5.00,
            'horse_url':        'https://www.punters.com.au/horses/Tycoon-Tony_395471/',
            'jockey_url':       'https://www.punters.com.au/jockeys/Jason-Benbow_690/',
            'weight':           58.5,
            'carried':          58.5,
            'lengths':          5.25,
            'result':           4,
            'starters':         14,
            'scraper_version':  punters_client.__version__
        },
        {
            'track':            'Wodonga',
            'date':             source_timezone.localize(datetime(2015, 7, 29)),
            'distance':         1100,
            'track_condition':  'HEAVY 9',
            'prize_money':      1200.00,
            'prize_pool':       15000.00,
            'barrier':          15,
            'winning_time':     67.96,
            'starting_price':   21.00,
            'horse_url':        'https://www.punters.com.au/horses/Tycoon-Tony_395471/',
            'jockey_url':       'https://www.punters.com.au/jockeys/Jason-Benbow_690/',
            'weight':           58.5,
            'carried':          58.5,
            'lengths':          4.50,
            'result':           3,
            'starters':         11,
            'scraper_version':  punters_client.__version__
        }
    ]


@pytest.fixture(scope='module')
def scraped_performances(horse, scraper):

    return scraper.scrape_performances(horse)


def test_expected_performances(expected_performances, scraped_performances):
    """The scrape_performances method should return a list of dictionaries containing all expected values"""

    check_expected_items(expected_performances, scraped_performances, ['date', 'horse_url', 'track'])


def test_unexpected_performances(expected_performances, scraped_performances):
    """The scrape_performances method should return a list of dictionaries that does not contain any unexpected values"""

    check_unexpected_items(expected_performances, scraped_performances, ['date', 'horse_url', 'track'])

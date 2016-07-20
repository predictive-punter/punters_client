from datetime import datetime

import punters_client
import pytest

from common import check_expected_items, check_unexpected_items


@pytest.fixture(scope='module')
def meet(source_timezone):

    return {
        'date':             source_timezone.localize(datetime(2016, 2, 1)),
        'track':            'Kilmore',
        'url':              'https://www.punters.com.au/racing-results/victoria/Kilmore/2016-02-01/',
        'scraper_version':  punters_client.__version__
    }


@pytest.fixture(scope='module')
def expected_races(meet, source_timezone):

    return [
        {
            'number':           1,
            'distance':         1100,
            'prize_pool':       20000.00,
            'track_condition':  'Good 4',
            'start_time':       source_timezone.localize(datetime(2016, 2, 1, 13, 10)),
            'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/Wandong-Bus-and-Coach-Maiden-Plate_411192/',
            'scraper_version':  punters_client.__version__
        },
        {
            'number':           2,
            'distance':         1200,
            'prize_pool':       20000.00,
            'track_condition':  'Good 4',
            'start_time':       source_timezone.localize(datetime(2016, 2, 1, 13, 45)),
            'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/Book-now-for-Valentines-Day-14-Feb-Maiden-Plate_411193/',
            'scraper_version':  punters_client.__version__
        },
        {
            'number':           3,
            'distance':         1450,
            'prize_pool':       20000.00,
            'track_condition':  'Good 4',
            'start_time':       source_timezone.localize(datetime(2016, 2, 1, 14, 20)),
            'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/Montmorency-RSL-Maiden-Plate_411194/',
            'scraper_version':  punters_client.__version__
        },
        {
            'number':           4,
            'distance':         1600,
            'prize_pool':       20000.00,
            'track_condition':  'Good 4',
            'start_time':       source_timezone.localize(datetime(2016, 2, 1, 14, 55)),
            'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/Sunday-Sessions-%40-Trackside-7-Feb-Maiden-Plate_411195/',
            'scraper_version':  punters_client.__version__
        },
        {
            'number':           5,
            'distance':         1100,
            'prize_pool':       20000.00,
            'track_condition':  'Good 4',
            'start_time':       source_timezone.localize(datetime(2016, 2, 1, 15, 32)),
            'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/www.kilmoreracingclub.com.au-BM64-Handicap_411196/',
            'scraper_version':  punters_client.__version__
        },
        {
            'number':           6,
            'distance':         1200,
            'prize_pool':       16000.00,
            'track_condition':  'Good 4',
            'start_time':       source_timezone.localize(datetime(2016, 2, 1, 16, 12)),
            'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/Wilson-Medic-One-Rising-Stars-0-58-Handicap_411197/',
            'scraper_version':  punters_client.__version__
        },
        {
            'number':           7,
            'distance':         1900,
            'prize_pool':       20000.00,
            'track_condition':  'Good 4',
            'start_time':       source_timezone.localize(datetime(2016, 2, 1, 16, 52)),
            'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/Sportsmans-Lunch-%40-Trackside-26-Feb-BM64-Handicap_411198/',
            'scraper_version':  punters_client.__version__
        },
        {
            'number':           8,
            'distance':         1600,
            'prize_pool':       16000.00,
            'track_condition':  'Good 4',
            'start_time':       source_timezone.localize(datetime(2016, 2, 1, 17, 32)),
            'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/Book-Now-Jet-Roofing-Kilmore-Pacing-Cup-0-58-Handicap_411199/',
            'scraper_version':  punters_client.__version__
        }
    ]


@pytest.fixture(scope='module')
def scraped_races(meet, scraper):

    return scraper.scrape_races(meet)


def test_expected_races(expected_races, scraped_races):
    """The scrape_races method should return a list of dictionaries containing all expected values"""

    check_expected_items(expected_races, scraped_races, ['number'])


def test_unexpected_races(expected_races, scraped_races):
    """The scrape_races method should return a list of dictionaries that does not contain any unexpected values"""

    check_unexpected_items(expected_races, scraped_races, ['number'])

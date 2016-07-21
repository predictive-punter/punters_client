from datetime import datetime

import punters_client
import pytest

from common import check_expected_items, check_unexpected_items


@pytest.fixture(scope='module', params=[1, 2])
def meet_id(request):

    return request.param


@pytest.fixture(scope='module')
def meet(meet_id, source_timezone):

    if meet_id == 1:
        return {
            'date':             source_timezone.localize(datetime(2016, 2, 1)),
            'track':            'Kilmore',
            'url':              'https://www.punters.com.au/racing-results/victoria/Kilmore/2016-02-01/',
            'scraper_version':  punters_client.__version__
        }
    elif meet_id == 2:
        return {
            'date':             source_timezone.localize(datetime(2015, 11, 3)),
            'track':            'Flemington',
            'url':              'https://www.punters.com.au/racing-results/victoria/Flemington/2015-11-03/',
            'scraper_version':  punters_client.__version__
        }


@pytest.fixture(scope='module')
def expected_races(meet_id, source_timezone):

    if meet_id == 1:
        return [
            {
                'number':           1,
                'distance':         1100,
                'prize_pool':       20000.00,
                'track_condition':  'Good 4',
                'start_time':       source_timezone.localize(datetime(2016, 2, 1, 13, 10)),
                'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/Wandong-Bus-and-Coach-Maiden-Plate_411192/',
                'group':            '',
                'entry_conditions': [
                    'Three-Years-Old and Upwards',
                    'Maiden',
                    'No sex restriction',
                    'Set Weights'
                ],
                'track_circ':       1735,
                'track_straight':   320,
                'track_rail':       'True Entire Circuit',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           2,
                'distance':         1200,
                'prize_pool':       20000.00,
                'track_condition':  'Good 4',
                'start_time':       source_timezone.localize(datetime(2016, 2, 1, 13, 45)),
                'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/Book-now-for-Valentines-Day-14-Feb-Maiden-Plate_411193/',
                'group':            '',
                'entry_conditions': [
                    'Three-Years-Old',
                    'Maiden',
                    'Fillies',
                    'Set Weights'
                ],
                'track_circ':       1735,
                'track_straight':   320,
                'track_rail':       'True Entire Circuit',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           3,
                'distance':         1450,
                'prize_pool':       20000.00,
                'track_condition':  'Good 4',
                'start_time':       source_timezone.localize(datetime(2016, 2, 1, 14, 20)),
                'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/Montmorency-RSL-Maiden-Plate_411194/',
                'group':            '',
                'entry_conditions': [
                    'Three-Years-Old and Upwards',
                    'Maiden',
                    'No sex restriction',
                    'Set Weights'
                ],
                'track_circ':       1735,
                'track_straight':   320,
                'track_rail':       'True Entire Circuit',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           4,
                'distance':         1600,
                'prize_pool':       20000.00,
                'track_condition':  'Good 4',
                'start_time':       source_timezone.localize(datetime(2016, 2, 1, 14, 55)),
                'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/Sunday-Sessions-%40-Trackside-7-Feb-Maiden-Plate_411195/',
                'group':            '',
                'entry_conditions': [
                    'Three-Years-Old and Upwards',
                    'Maiden',
                    'No sex restriction',
                    'Set Weights'
                ],
                'track_circ':       1735,
                'track_straight':   320,
                'track_rail':       'True Entire Circuit',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           5,
                'distance':         1100,
                'prize_pool':       20000.00,
                'track_condition':  'Good 4',
                'start_time':       source_timezone.localize(datetime(2016, 2, 1, 15, 32)),
                'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/www.kilmoreracingclub.com.au-BM64-Handicap_411196/',
                'group':            '',
                'entry_conditions': [
                    'No age restriction',
                    'BenchMark 64',
                    'No sex restriction',
                    'Handicap'
                ],
                'track_circ':       1735,
                'track_straight':   320,
                'track_rail':       'True Entire Circuit',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           6,
                'distance':         1200,
                'prize_pool':       16000.00,
                'track_condition':  'Good 4',
                'start_time':       source_timezone.localize(datetime(2016, 2, 1, 16, 12)),
                'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/Wilson-Medic-One-Rising-Stars-0-58-Handicap_411197/',
                'group':            '',
                'entry_conditions': [
                    'No age restriction',
                    '0 - 58',
                    'No sex restriction',
                    'Handicap'
                ],
                'track_circ':       1735,
                'track_straight':   320,
                'track_rail':       'True Entire Circuit',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           7,
                'distance':         1900,
                'prize_pool':       20000.00,
                'track_condition':  'Good 4',
                'start_time':       source_timezone.localize(datetime(2016, 2, 1, 16, 52)),
                'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/Sportsmans-Lunch-%40-Trackside-26-Feb-BM64-Handicap_411198/',
                'group':            '',
                'entry_conditions': [
                    'No age restriction',
                    'BenchMark 64',
                    'No sex restriction',
                    'Handicap'
                ],
                'track_circ':       1735,
                'track_straight':   320,
                'track_rail':       'True Entire Circuit',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           8,
                'distance':         1600,
                'prize_pool':       16000.00,
                'track_condition':  'Good 4',
                'start_time':       source_timezone.localize(datetime(2016, 2, 1, 17, 32)),
                'url':              'https://www.punters.com.au/form-guide/Kilmore_69146/Book-Now-Jet-Roofing-Kilmore-Pacing-Cup-0-58-Handicap_411199/',
                'group':            '',
                'entry_conditions': [
                    'No age restriction',
                    '0 - 58',
                    'No sex restriction',
                    'Handicap'
                ],
                'track_circ':       1735,
                'track_straight':   320,
                'track_rail':       'True Entire Circuit',
                'scraper_version':  punters_client.__version__
            }
        ]
    elif meet_id == 2:
        return [
            {
                'number':           1,
                'distance':         1000,
                'prize_pool':       150000.00,
                'track_condition':  'Good 4',
                'start_time':       source_timezone.localize(datetime(2015, 11, 3, 10, 40)),
                'url':              'https://www.punters.com.au/form-guide/Flemington_64271/Emirates-Airline-Plate_382827/',
                'group':            'G3',
                'entry_conditions': [
                    'Two-Years-Old',
                    'No class restriction',
                    'Fillies',
                    'Set Weights'
                ],
                'track_circ':       2313,
                'track_straight':   448,
                'track_rail':       '-',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           2,
                'distance':         1700,
                'prize_pool':       100000.00,
                'track_condition':  'Good 4',
                'start_time':       source_timezone.localize(datetime(2015, 11, 3, 11, 20)),
                'url':              'https://www.punters.com.au/form-guide/Flemington_64271/tab.com.au-Trophy_382828/',
                'group':            '',
                'entry_conditions': [
                    'Four-Years-Old and Upwards',
                    'No class restriction',
                    'Mares',
                    'Handicap'
                ],
                'track_circ':       2313,
                'track_straight':   448,
                'track_rail':       '-',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           3,
                'distance':         2800,
                'prize_pool':       100000.00,
                'track_condition':  'Good 4',
                'start_time':       source_timezone.localize(datetime(2015, 11, 3, 12, 00)),
                'url':              'https://www.punters.com.au/form-guide/Flemington_64271/J.B.-Cummings-AM-Tribute-Plate_382829/',
                'group':            '',
                'entry_conditions': [
                    'No age restriction',
                    'BenchMark 96',
                    'No sex restriction',
                    'Handicap'
                ],
                'track_circ':       2313,
                'track_straight':   448,
                'track_rail':       '-',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           4,
                'distance':         1400,
                'prize_pool':       100000.00,
                'track_condition':  'Good 4',
                'start_time':       source_timezone.localize(datetime(2015, 11, 3, 12, 40)),
                'url':              'https://www.punters.com.au/form-guide/Flemington_64271/Lavazza-Short-Black_382830/',
                'group':            '',
                'entry_conditions': [
                    'Four-Years-Old and Five-Years-Old',
                    'BenchMark 90',
                    'No sex restriction',
                    'Handicap'
                ],
                'track_circ':       2313,
                'track_straight':   448,
                'track_rail':       '-',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           5,
                'distance':         1000,
                'prize_pool':       100000.00,
                'track_condition':  'Good 3',
                'start_time':       source_timezone.localize(datetime(2015, 11, 3, 13, 20)),
                'url':              'https://www.punters.com.au/form-guide/Flemington_64271/Schweppes-%23FlemingtonFling_382831/',
                'group':            '',
                'entry_conditions': [
                    'Three-Years-Old',
                    'No class restriction',
                    'No sex restriction',
                    'Set Weights plus Penalties'
                ],
                'track_circ':       2313,
                'track_straight':   448,
                'track_rail':       '-',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           6,
                'distance':         1400,
                'prize_pool':       150000.00,
                'track_condition':  'Good 3',
                'start_time':       source_timezone.localize(datetime(2015, 11, 3, 14, 00)),
                'url':              'https://www.punters.com.au/form-guide/Flemington_64271/Lexus-Hybrid-Plate_382832/',
                'group':            'LR',
                'entry_conditions': [
                    'Three-Years-Old',
                    'No class restriction',
                    'Fillies',
                    'Set Weights plus Penalties'
                ],
                'track_circ':       2313,
                'track_straight':   448,
                'track_rail':       '-',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           7,
                'distance':         3200,
                'prize_pool':       6000000.00,
                'track_condition':  'Good 3',
                'start_time':       source_timezone.localize(datetime(2015, 11, 3, 15, 00)),
                'url':              'https://www.punters.com.au/form-guide/Flemington_64271/Emirates-Melbourne-Cup_383401/',
                'group':            'G1',
                'entry_conditions': [
                    'No age restriction',
                    'No class restriction',
                    'No sex restriction',
                    'Handicap'
                ],
                'track_circ':       2313,
                'track_straight':   448,
                'track_rail':       '-',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           8,
                'distance':         1800,
                'prize_pool':       150000.00,
                'track_condition':  'Good 3',
                'start_time':       source_timezone.localize(datetime(2015, 11, 3, 15, 55)),
                'url':              'https://www.punters.com.au/form-guide/Flemington_64271/James-Boag%E2%80%99s-Symphony-Stakes_382833/',
                'group':            'LR',
                'entry_conditions': [
                    'No age restriction',
                    'No class restriction',
                    'No sex restriction',
                    'Handicap'
                ],
                'track_circ':       2313,
                'track_straight':   448,
                'track_rail':       '-',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           9,
                'distance':         1200,
                'prize_pool':       150000.00,
                'track_condition':  'Good 3',
                'start_time':       source_timezone.localize(datetime(2015, 11, 3, 16, 35)),
                'url':              'https://www.punters.com.au/form-guide/Flemington_64271/MSS-Security-Sprint_382834/',
                'group':            'LR',
                'entry_conditions': [
                    'No age restriction',
                    'No class restriction',
                    'No sex restriction',
                    'Handicap'
                ],
                'track_circ':       2313,
                'track_straight':   448,
                'track_rail':       '-',
                'scraper_version':  punters_client.__version__
            },
            {
                'number':           10,
                'distance':         1400,
                'prize_pool':       200000.00,
                'track_condition':  'Good 3',
                'start_time':       source_timezone.localize(datetime(2015, 11, 3, 17, 15)),
                'url':              'https://www.punters.com.au/form-guide/Flemington_64271/Hong-Kong-Jockey-Club-Stakes_382835/',
                'group':            'G3',
                'entry_conditions': [
                    'Four-Years-Old and Upwards',
                    'No class restriction',
                    'Mares',
                    'Set Weights plus Penalties'
                ],
                'track_circ':       2313,
                'track_straight':   448,
                'track_rail':       '-',
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

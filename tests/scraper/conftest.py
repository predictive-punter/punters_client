import cache_requests
from lxml import html
import punters_client
import pytest
import pytz
import redis
import requests


@pytest.fixture(scope='session')
def scraper():

    http_client = None
    try:
        http_client = cache_requests.Session(connection=redis.fromurl('redis://localhost:6379/punters_client_test'))
    except BaseException:
        try:
            http_client = cache_requests.Session()
        except BaseException:
            http_client = requests.Session()

    html_parser = html.fromstring

    return punters_client.Scraper(http_client, html_parser)


@pytest.fixture(scope='session')
def source_timezone():

    return pytz.timezone('Australia/Melbourne')


@pytest.fixture(scope='session')
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

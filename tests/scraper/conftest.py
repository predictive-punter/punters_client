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

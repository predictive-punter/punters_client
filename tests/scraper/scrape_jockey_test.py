import punters_client
import pytest


@pytest.fixture(scope='module')
def expected_values(runner, source_timezone):

    return {
        'url':              runner['jockey_url'],
        'name':             'Ben E Thompson',
        'scraper_version':  punters_client.__version__
    }


@pytest.fixture(scope='module')
def scraped_values(runner, scraper):

    return scraper.scrape_jockey(runner)


def test_expected_values(expected_values, scraped_values):
    """The scrape_jockey method should return a dictionary containing all expected values"""

    assert scraped_values == expected_values


def test_in_memorium(scraper):
    """The scrape_jockey method should return the expected values on jockey in memorium profiles"""

    runner = {
        'jockey_url':   'https://www.punters.com.au/jockeys/Timothy-Bell_1685/'
    }

    expected_values = {
        'url':              'https://www.punters.com.au/jockeys/Timothy-Bell_1685/',
        'name':             'Timothy Bell',
        'scraper_version':  punters_client.__version__
    }

    scraped_values = scraper.scrape_jockey(runner)

    assert scraped_values == expected_values

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

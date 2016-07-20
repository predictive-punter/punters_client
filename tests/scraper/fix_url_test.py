import pytest


@pytest.fixture(scope='module', params=['test/path', '/test/path'])
def url(request):

    return request.param


@pytest.fixture(scope='module', params=['http://www.example.com', 'http://www.example.com/'])
def url_root(request):

    return request.param


def test_slashes(scraper, url, url_root):
    """The fix_url method should always return the correct number of slashes between url_root and url"""

    assert scraper.fix_url(url, url_root) == 'http://www.example.com/test/path'

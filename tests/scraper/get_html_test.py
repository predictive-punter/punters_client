import pytest


def test_4xx(scraper):
    """The get_html method should return None when receiving a HTTP 4xx status code"""

    assert scraper.get_html('http://httpstat.us/404') is None


def test_5xx(scraper):
    """The get_html method should raise an exception when receiving a HTTP 5xx status code"""

    with pytest.raises(BaseException):
        scraper.get_html('http://httpstat.us/500')

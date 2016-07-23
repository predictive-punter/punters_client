import pytest


def test_raises(scraper):
    """The get_html method should raise an exception when receiving a HTTP error status code"""

    with pytest.raises(BaseException):
        scraper.get_html('http://httpstat.us/500')

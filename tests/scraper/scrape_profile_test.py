def test_not_notified(scraper):
    """The scrape_profile method should return None when called with the URL root"""

    assert scraper.scrape_profile('https://www.punters.com.au/') is None

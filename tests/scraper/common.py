def check_expected_items(expected_items, scraped_items, keys):
    """Assert that all expected items exist in the scraped items collection"""

    for expected_item in expected_items:
        scraped_item = find(expected_item, scraped_items, keys)

        for key in expected_item:
            assert scraped_item[key] == expected_item[key]
        for key in scraped_item:
            assert expected_item[key] == scraped_item[key]


def check_unexpected_items(expected_items, scraped_items, keys):
    """Assert that all scraped items exist in the expected items collection"""

    for scraped_item in scraped_items:
        assert find(scraped_item, expected_items, keys) is not None


def find(item, collection, keys):
    """Find the item in the specified collection whose keys/values match those in the specified item"""

    for other_item in collection:
        is_match = True
        for key in keys:
            if other_item[key] != item[key]:
                is_match = False
                break
        if is_match:
            return other_item

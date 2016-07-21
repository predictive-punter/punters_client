import re

import punters_client
import pytest


@pytest.fixture(scope='module')
def version_parts():

    return re.search('(\d+).(\d+).(\d+)([a-z]+)?(\d+)?', punters_client.__version__).groups()


def generate_version(parts):
    """Generate a version number string from the specified parts"""

    version = '.'.join([str(part) for part in parts[0:2]])
    if len(parts) > 3:
        version += parts[3]
        if len(parts) > 4:
            version += str(parts[4])
    return version


def test_equal(scraper):
    """is_compatible_with(same_version) should return True"""

    assert scraper.is_compatible_with(punters_client.__version__) is True


def test_major(scraper, version_parts):
    """is_compatible_with(new_major_version) should return False"""

    new_version_parts = list(version_parts)
    new_version_parts[0] = int(new_version_parts[0]) + 1

    assert scraper.is_compatible_with(generate_version(new_version_parts)) is False


def test_minor(scraper, version_parts):
    """is_compatible_with(new_minor_version) should return True"""

    new_version_parts = list(version_parts)
    new_version_parts[1] = int(new_version_parts[1]) + 1

    assert scraper.is_compatible_with(generate_version(new_version_parts)) is True


def test_patch(scraper, version_parts):
    """is_compatible_with(new_patch_version) should return True"""

    new_version_parts = list(version_parts)
    new_version_parts[2] = int(new_version_parts[2]) + 1

    assert scraper.is_compatible_with(generate_version(new_version_parts)) is True


def test_pre_release(scraper, version_parts):
    """is_compatible_with(new_pre_release_version) should return True"""

    new_version_parts = list(version_parts)
    if len(new_version_parts) > 4:
        new_version_parts[4] = int(new_version_parts[4]) + 1
    elif len(new_version_parts) > 3:
        new_version_parts.append(1)
    else:
        new_version_parts.extend(['a', 1])

    assert scraper.is_compatible_with(generate_version(new_version_parts)) is True

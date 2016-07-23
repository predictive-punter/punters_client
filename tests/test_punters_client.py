import punters_client


def test_version():
    """punters_client.__version__ should return the correct version string"""

    assert punters_client.__version__ == '1.0.0b2'

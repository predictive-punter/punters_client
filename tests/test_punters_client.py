import punters_client
import setuptools_scm


def test_version():
    """punters_client.__version__ should return the correct version string"""

    assert punters_client.__version__ == setuptools_scm.get_version()

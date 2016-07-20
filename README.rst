==============
punters_client
==============


This project aims to provide client functionality for the www.punters.com.au web site in Python.


.. image:: https://travis-ci.org/justjasongreen/punters_client.svg?branch=master
    :target: https://travis-ci.org/justjasongreen/punters_client
    :alt: Build Status
.. image:: https://coveralls.io/repos/github/justjasongreen/punters_client/badge.svg?branch=master
    :target: https://coveralls.io/github/justjasongreen/punters_client?branch=master
    :alt: Coverage Status
.. image:: https://landscape.io/github/justjasongreen/punters_client/master/landscape.svg?style=flat
    :target: https://landscape.io/github/justjasongreen/punters_client/master
    :alt: Code Health


************
Installation
************


Prior to using punters_client, the package must be installed in your current Python environment. In most cases, an automated installation via PyPI and pip will suffice, as follows::

    pip install punters_client

If you would prefer to gain access to new (unstable) features via a pre-release version of the package, specify the 'pre' option when calling pip, as follows::

    pip install --pre punters_client

To gain access to bleeding edge developments, the package can be installed from a source distribution. To do so, you will need to clone the git repository and execute the setup.py script from the root directory of the source tree, as follows::

    git clone https://github.com/justjasongreen/punters_client.git
    cd punters_client
    python setup.py install

If you would prefer to install the package as a symlink to the source distribution (for development purposes), execute the setup.py script with the 'develop' option instead, as follows::

    python setup.py develop


***********
Basic Usage
***********


To access the functionality described below, you must first import the punters_client package into your Python interpreter, as follows::

    >>> import punters_client


***********************
Development and Testing
***********************


The source distribution includes a test suite based on pytest. To ensure compatibility with all supported versions of Python, it is recommended that the test suite be run via tox.

To install all development and test requirements into your current Python environment, execute the following command from the root directory of the source tree::

    pip install -e .[dev,test]

To run the test suite included in the source distribution, execute the tox command from the root directory of the source tree as follows::

    tox

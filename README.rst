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


To access the functionality described below, you must first create an instance of the punters_client.Scraper class. To do so, you will need to provide a compatible HTTP client and a HTML parser. The HTTP client can be any object that implements the requests.Session API, supporting calls such as the following::

    response = http_client.get(url)
    response.raise_for_status()
    content = response.text

The HTML parser can be any callable that implements the lxml.html.fromstring API, supporting calls such as the following::

    html = html_parser(content)

punters_client has only been tested with cache_requests.Session as a HTTP client and lxml.html.fromstring as a HTML parser. To set up the required dependencies in your own project using the same packages, execute the following code in your Python interpreter::

    >>> import cache_requests
    >>> http_client = cache_requests.Session()
    >>> from lxml import html
    >>> html_parser = html.fromstring

With these dependencies in place, you can now create an instance of the punters_client.Scraper class as follows::

    >>> import punters_client
    >>> scraper = punters_client.Scraper(http_client, html_parser)

The scraper instance can now be used to scrape a range of racing data from the web, as illustrated in the following sections...


Scraping Meets
==============

Meets represent a collection of races occurring at a given track on a given date. To scrape a list of meets occurring on a specified date, execute the following code in your Python interpreter::

    >>> from datetime import datetime
    >>> date = datetime(2016, 2, 1)
    >>> meets = scraper.scrape_meets(date)

The scrape_meets method will return a list of dictionaries representing all meets occurring in Australia on the specified date. Accordingly, a meet's details can be accessed as follows::

    >>> meet = meets[index]
    >>> track = meet['track']


Scraping Races
==============

Races represent a collection of runners competing in a single event at a meet. To scrape a list of races occurring at a specified meet, execute the following code in your Python interpreter::

    >>> races = scraper.scrape_races(meet)

The scrape_races method will return a list of dictionaries representing all races occurring at the specified meet. Accordingly, a race's details can be accessed as follows::

    >>> race = races[index]
    >>> number = race['number']


Scraping Runners
================

Runners represent a single combination of horse, jockey and trainer competing in a race. To scrape a list of runners competing in a specified race, execute the following code in your Python interpreter::

    >>> runners = scraper.scrape_runners(race)

The scrape_runners method will return a list of dictionaries representing all runners occurring at the specified race. Accordingly, a runner's details can be accessed as follows::

    >>> runner = runners[index]
    >>> number = runner['number']


Scraping Horses, Jockeys and Trainers
=====================================

Horses, jockeys and trainers represent the distinct components of a runner. To scrape the profile for a runner's horse, jockey or trainer, execute the following code in your Python interpreter as appropriate::

    >>> horse = scraper.scrape_horse(runner)
    >>> jockey = scraper.scrape_jockey(runner)
    >>> trainer = scraper.scrape_trainer(runner)

The scrape_horse, scrape_jockey and scrape_trainer methods all return a dictionary representing the horse/jockey/trainer's profile. Accordingly, profile details can be accessed as follows::

    >>> name = horse['name']
    >>> name = jockey['name']
    >>> name = trainer['name']


Scraping Performances
=====================

Performances represent the results of completed runs for a horse/jockey. To scrape a list of performances for a given horse/jockey, execute the following code in your Python interpreter as appropriate::

    >>> performances = scraper.scrape_performances(horse)
    >>> performances = scraper.scrape_performances(jockey)

NOTE: Due to the sheer volume of performances associated with any given jockey, it is only possible to recover a short and incomplete list of the most recent performances as at the time of scraping from www.punters.com.au. This should not be an issue with most horses.

The scrape_performances method returns a list of dictionaries representing the past performances for the specified horse/jockey. Accordingly, a performance's details can be accessed as follows::

    >>> performance = performances[index]
    >>> result = performance['result']


***********************
Development and Testing
***********************


The source distribution includes a test suite based on pytest. To ensure compatibility with all supported versions of Python, it is recommended that the test suite be run via tox.

To install all development and test requirements into your current Python environment, execute the following command from the root directory of the source tree::

    pip install -e .[dev,test]

To run the test suite included in the source distribution, execute the tox command from the root directory of the source tree as follows::

    tox

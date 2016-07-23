# Change Log

All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](http://semver.org/).


## [1.0.0b2] - 2016-07-24

### Changed

- Increase concurrent HTTP requests limit to CPU count x 5 (from @justjasongreen)

### Fixed

- Fix PyPI package classifiers (from @justjasongreen)


## [1.0.0b1] - 2016-07-23

### Changed

- Limit the number of concurrent HTTP requests in multithreading environments (from @justjasongreen)


## [1.0.0a4] - 2016-07-23

### Changed

- Scraper.get_html will retry failed HTTP requests several times before raising exception (from @justjasongreen)


## [1.0.0a3] - 2016-07-23

### Added

- Scraper.URL_ROOT constant (from @justjasongreen)

### Changed

- Moved AUSTRALIAN_STATES constant into Scraper class (from @justjasongreen)

### Fixed

- Fix AttributeError when calling scrape_profile(URL_ROOT) (from @justjasongreen)


## [1.0.0a2] - 2016-07-22

### Added

- Scraper.is_compatible_with(version) method (from @justjasongreen)
- Automate manifest checking by Travis CI (from @justjasongreen)

### Fixed

- Package version reported correctly when utilised within foreign SCM (from @justjasongreen)


## [1.0.0a1] - 2016-07-21

### Added

- Scrape a list of meets occurring on a given date (from @justjasongreen)
- Scrape a list of races occurring at a given meet (from @justjasongreen)
- Scrape a list of runners competing in a given race (from @justjasongreen)
- Scrape the horse associated with a given runner (from @justjasongreen)
- Scrape the jockey associated with a given runner (from @justjasongreen)
- Scrape the trainer associated with a given runner (from @justjasongreen)
- Scrape a list of performances associated with a given profile (from @justjasongreen)


## [1.0.0a0] - 2016-07-20

### Added

- Create Python package (from @justjasongreen)
- Implement DevOps support (from @justjasongreen)


[1.0.0b2]: https://github.com/justjasongreen/punters_client/compare/1.0.0b1...1.0.0b2
[1.0.0b1]: https://github.com/justjasongreen/punters_client/compare/1.0.0a4...1.0.0b1
[1.0.0a4]: https://github.com/justjasongreen/punters_client/compare/1.0.0a3...1.0.0a4
[1.0.0a3]: https://github.com/justjasongreen/punters_client/compare/1.0.0a2...1.0.0a3
[1.0.0a2]: https://github.com/justjasongreen/punters_client/compare/1.0.0a1...1.0.0a2
[1.0.0a1]: https://github.com/justjasongreen/punters_client/compare/1.0.0a0...1.0.0a1
[1.0.0a0]: https://github.com/justjasongreen/punters_client/tree/1.0.0a0

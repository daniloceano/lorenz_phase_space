# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.0.9] - 2024-01-02

### Bug fixes

- Fixed ploting "zoom=True" when maximum values are lower than 0 and minimum values are higher than 0 (set them to 1 and -1, respectively).

## [0.0.8] - 2024-01-02

### Bug fixes

- Standardized input data as pd.Series for avoinding bugs.

## [0.0.7] - 2024-01-02

### Bug fixes

## [0.0.6] - 2024-01-02

### Bug fixes

## [0.0.5] - 2024-01-02

### Updated Documentation

## [0.0.4] - 2024-01-02

### Bug fixes

## [0.0.3] - 2024-01-02

### Modified

- Updated **README.md**

## [0.0.2] - 2024-01-02

### Modified

- **setup.py**: Integrated with README.md
- **gitignore.py**: included figures generated from testing 
- **.cicleci/congif.yml**: included variables for CircleCI authentication

### Added

- **CHANGELOG.md**
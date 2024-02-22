# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [1.0.0] - 2024-02-22

### Added
- **Dynamic Plotting**: Introduced functionality for dynamic zoom and plotting data with randomized factors to better test the robustness of the plotting functionalities.
- **Flexible Data Handling**: Added capabilities to handle data plotting more flexibly, allowing for plotting multiple datasets on the same plot structure by calling the data plotting method multiple times.
- **Test Suite Enhancements**: Expanded the test suite to cover new functionalities, including zoom effects and data randomization, ensuring the reliability of new features.

### Changed
- **Refactored Plotting Methodology**: Shifted from a single method handling both plot creation and data plotting to a more modular approach with `create_lps_plot` for setting up the plot environment and `plot_data` for adding data to the plot.
- **Enhanced Plot Customization**: Enhanced the plot customization options, including automatic axis limit adjustments based on the data being plotted and customization of plot annotations and labels.
- **Updated Dependencies**: Addressed deprecation warnings by updating the handling of color maps to align with newer versions of dependencies like `matplotlib` and `cmocean`.

### Fixed
- **Axis Limit Calculation**: Fixed issues related to axis limit calculation in zoomed plots to ensure that plots dynamically adjust to the data's range.
- **Highlighting Specific Data Points**: Implemented functionality to highlight specific data points, such as the point with the maximum marker size, improving the visual analysis capabilities of the plots.
- **Modular Test Architecture**: Refined the test architecture to better align with the refactored plotting functionalities, ensuring that each component of the class is reliably tested.


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
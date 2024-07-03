# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [1.2.4] - 2024-07-03

### Bug Fixes
- Wrong parenthesis on labels
- Diagonal line on mixed-zoom plot

## [1.2.3] - 2024-07-01

### Changed
- Barotropic LPS changed to "imports", which uses BKe and BAe. 

## [1.2.2] - 2024-06-27

### Changed
- Changed barotropic LPS for using BKe instead of BKz.
- Test cases on main file now include multiple LPS types.

## [1.2.1] - 2024-02-28

### Changed
- Adjusted automatically setting dynamic limits for colorbar whenever zoom flag is True so the values are always centered around zero.

## [1.2.0] - 2024-02-28

### Changed
- Improved naming conventions for the script and class to enhance clarity and usability and updated repository structure.

## [1.1.1] - 2024-02-28

### Fixed
- `___init__.py` file was missing, causing import errors.

## [1.1.0] - 2024-02-23

### Added
- Dynamic zoom functionality in `LorenzPhaseSpace` class, allowing users to dynamically adjust plot limits based on the dataset's range.
- The ability to pass custom limits for x-axis, y-axis, color, and marker size during class initialization and plotting to enable more flexible visualizations.
- Enhanced error handling for colorbar and legend creation to prevent duplication when plotting multiple datasets.

### Changed
- Modified `LorenzPhaseSpace` class initialization to support new parameters for dynamic limits and zoom functionality, offering improved flexibility for users.
- Updated plot_data method to incorporate dynamic zoom and limit adjustments, ensuring that the visualizations accurately reflect the data being plotted.
- Improved test suite to cover new functionalities and ensure the reliability of dynamic limit adjustments and zoom features.

### Fixed
- Issue where multiple colorbars and legends were created when plotting multiple datasets, now ensuring only the latest colorbar and legend are displayed.

### Optimization
- Enhanced the efficiency of plotting large datasets by optimizing colorbar and legend updates to avoid unnecessary recalculations.


## [1.0.1] - 2024-02-22

### Changed
- **Updated DOcumentation**: Updated 'usage' so it incorporates changes done in 1.0.0

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
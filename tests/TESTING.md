# Testing Guide

## Lorenz Phase Space Testing Framework

This guide explains how to run and interpret tests for the Lorenz Phase Space package.

---

## Table of Contents

1. [Running Tests](#running-tests)
2. [Test Structure](#test-structure)
3. [Visual Verification](#visual-verification)
4. [Test Coverage](#test-coverage)
5. [Adding New Tests](#adding-new-tests)

---

## Running Tests

### Basic Test Run

From the project root directory:

```bash
python -m pytest tests/test_lps.py -v
```

Or using unittest:

```bash
python -m unittest tests/test_lps.py
```

### Running with Visual Inspection

The test suite includes a special function for generating visual output:

```bash
cd tests
python test_lps.py
```

This will:
1. Run all tests
2. Generate diagnostic plots in `tests/test_outputs/`
3. Print a summary of generated plots for manual inspection

### Running Specific Test Classes

```bash
# Test only initialization
python -m pytest tests/test_lps.py::TestVisualizerInitialization -v

# Test only data plotting
python -m pytest tests/test_lps.py::TestDataPlotting -v

# Test with sample data
python -m pytest tests/test_lps.py::TestRealDataScenarios -v
```

### Running with Coverage

```bash
pip install pytest-cov
python -m pytest tests/test_lps.py --cov=lorenz_phase_space --cov-report=html
```

Then open `htmlcov/index.html` to view coverage report.

---

## Test Structure

The test suite is organized into multiple test classes:

### 1. TestHelperFunctions
Tests utility functions used by the Visualizer.

**Tests:**
- `test_get_max_min_values_all_negative`: Validates behavior with all negative values
- `test_get_max_min_values_all_positive`: Validates behavior with all positive values
- `test_get_max_min_values_mixed`: Validates behavior with mixed values

### 2. TestVisualizerInitialization
Tests Visualizer class initialization with various parameters.

**Tests:**
- `test_default_initialization`: Default settings
- `test_mixed_type_no_zoom`: Mixed LPS without zoom
- `test_baroclinic_type_no_zoom`: Baroclinic LPS
- `test_imports_type_no_zoom`: Imports LPS
- `test_with_zoom`: Zoom mode enabled
- `test_with_custom_limits`: Custom axis limits

### 3. TestVisualizerMethods
Tests individual methods of the Visualizer class.

**Tests:**
- `test_calculate_marker_size_no_zoom`: Marker sizing in standard mode
- `test_calculate_marker_size_with_zoom`: Marker sizing in zoom mode
- `test_get_labels_mixed`: Label generation for mixed LPS
- `test_get_labels_baroclinic`: Label generation for baroclinic LPS
- `test_get_labels_imports`: Label generation for imports LPS
- `test_set_limits_default`: Default axis limits
- `test_set_limits_custom`: Custom axis limits

### 4. TestDataPlotting
Tests data plotting functionality with various scenarios.

**Tests:**
- `test_plot_data_basic`: Basic plotting
- `test_plot_data_with_zoom`: Plotting with zoom
- `test_plot_multiple_datasets`: Multiple trajectories on one plot
- `test_plot_data_with_custom_alpha`: Custom transparency
- `test_plot_data_pandas_input`: Pandas Series input

### 5. TestEdgeCases
Tests edge cases and error handling.

**Tests:**
- `test_empty_data`: Empty arrays
- `test_single_point`: Single data point
- `test_very_large_values`: Very large numbers
- `test_negative_marker_sizes`: Negative marker sizes

### 6. TestVisualOutput
Integration tests that generate actual plot files for visual inspection.

**Tests:**
- `test_save_mixed_no_zoom`: Standard mixed LPS
- `test_save_mixed_with_zoom`: Zoomed mixed LPS
- `test_save_baroclinic`: Baroclinic LPS
- `test_save_imports`: Imports LPS
- `test_save_multiple_trajectories`: Multiple trajectories with custom limits

**Output Location:** `tests/test_outputs/*.png`

### 7. TestRealDataScenarios
Tests with actual sample data files (if available).

**Tests:**
- `test_sample_data_mixed`: Plot sample data in mixed mode
- `test_sample_data_dynamic_limits`: Multiple sample datasets with dynamic limits

**Requirements:** Sample CSV files in `samples/` directory

---

## Visual Verification

### Why Visual Verification?

The Lorenz Phase Space diagrams are highly visual, and automated tests can only verify functionality, not aesthetic correctness. Visual verification ensures:
- Proper layout and proportions
- Correct color schemes
- Appropriate annotation placement
- Readable labels and legends
- Correct trajectory arrows

### How to Perform Visual Verification

1. **Run Tests with Visual Output:**
   ```bash
   cd tests
   python test_lps.py
   ```

2. **Locate Generated Plots:**
   Check `tests/test_outputs/` for PNG files

3. **Inspect Each Plot:**
   - Open each PNG file
   - Verify against expected output
   - Check for any visual anomalies

4. **What to Look For:**

   #### Layout Checks
   - [ ] Plot fills the figure appropriately
   - [ ] Colorbar positioned correctly on the right
   - [ ] Legend positioned correctly on the right
   - [ ] No overlapping elements

   #### Color and Markers
   - [ ] Color gradient from blue (negative) to red (positive)
   - [ ] Marker sizes increase with energy magnitude
   - [ ] Start point ('A') clearly visible
   - [ ] End point ('Z') clearly visible
   - [ ] Maximum intensity point has thick black outline

   #### Annotations (Standard Mode Only)
   - [ ] Axis labels readable and properly positioned
   - [ ] Quadrant descriptions visible (if not zoomed)
   - [ ] Color-coded text matches diagram regions
   - [ ] Reference lines visible with appropriate opacity

   #### Trajectories
   - [ ] Arrows connect consecutive points
   - [ ] Arrow directions consistent with data flow
   - [ ] Multiple trajectories distinguishable (if applicable)

   #### Type-Specific Checks
   
   **Mixed LPS:**
   - [ ] Diagonal line present in non-zoom mode
   - [ ] Four quadrants clearly delineated
   - [ ] Quadrant labels describe instability types
   
   **Baroclinic LPS:**
   - [ ] Labels reference Ce and Ca
   - [ ] Upper-right quadrant labeled for baroclinic instability
   
   **Imports LPS:**
   - [ ] Labels reference BAe and BKe
   - [ ] Wider y-axis range (-200 to 200)

### Visual Regression Testing (Optional)

For more rigorous testing, save reference images and compare:

```python
import numpy as np
from PIL import Image

def compare_images(img1_path, img2_path, threshold=0.95):
    """Compare two images and return similarity score"""
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    
    # Convert to numpy arrays
    arr1 = np.array(img1)
    arr2 = np.array(img2)
    
    # Calculate similarity
    diff = np.abs(arr1 - arr2)
    similarity = 1 - (diff.sum() / (arr1.size * 255))
    
    return similarity >= threshold
```

---

## Test Coverage

### Current Coverage Areas

✅ **Covered:**
- Initialization with all parameter combinations
- All three LPS types (mixed, baroclinic, imports)
- Zoom and non-zoom modes
- Custom limit setting
- Marker size calculation
- Label generation
- Basic plotting functionality
- Multiple trajectory plotting
- Pandas and numpy input handling
- Edge cases (empty data, single point, large values)

⚠️ **Partially Covered:**
- Visual output correctness (requires manual verification)
- Error messages and exceptions
- Performance with very large datasets

❌ **Not Covered:**
- Interactive matplotlib features
- Different matplotlib backends
- Thread safety
- Memory usage with large datasets

### Measuring Coverage

```bash
# Install coverage tool
pip install coverage

# Run tests with coverage
coverage run -m unittest tests/test_lps.py

# Generate report
coverage report -m

# Generate HTML report
coverage html
```

---

## Adding New Tests

### Test Template

```python
class TestNewFeature(unittest.TestCase):
    """Test description"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Initialize test data
        self.test_data = ...
    
    def tearDown(self):
        """Clean up after tests"""
        plt.close('all')
    
    def test_specific_behavior(self):
        """Test specific behavior"""
        # Arrange
        lps = Visualizer(...)
        
        # Act
        result = lps.some_method(...)
        
        # Assert
        self.assertEqual(result, expected_value)
```

### Guidelines for New Tests

1. **Naming Convention:**
   - Test classes: `TestFeatureName`
   - Test methods: `test_specific_behavior`
   - Use descriptive names

2. **Docstrings:**
   - Every test class and method should have a docstring
   - Explain what is being tested and why

3. **Independence:**
   - Tests should not depend on other tests
   - Use setUp/tearDown for initialization/cleanup

4. **Cleanup:**
   - Always close matplotlib figures: `plt.close('all')`
   - Clean up any created files

5. **Assertions:**
   - Use appropriate assertion methods
   - Provide meaningful error messages

6. **Edge Cases:**
   - Test boundary conditions
   - Test with invalid inputs
   - Test with empty/null data

### Example: Adding a Test for New Feature

```python
class TestColorNormalization(unittest.TestCase):
    """Test color normalization for different data ranges"""
    
    def tearDown(self):
        plt.close('all')
    
    def test_symmetric_color_range(self):
        """Test that color normalization is symmetric around zero"""
        lps = Visualizer(
            LPS_type='mixed',
            zoom=True,
            color_limits=[-10, 10]
        )
        
        # Check normalization
        self.assertEqual(lps.norm.vmin, -10)
        self.assertEqual(lps.norm.vmax, 10)
        self.assertEqual(lps.norm.vcenter, 0)
    
    def test_asymmetric_color_adjustment(self):
        """Test that asymmetric ranges are adjusted to be symmetric"""
        lps = Visualizer(
            LPS_type='mixed',
            zoom=True,
            color_limits=[-5, 15]
        )
        
        # Should adjust to max absolute value
        max_abs = max(abs(-5), abs(15))
        self.assertEqual(lps.norm.vmin, -max_abs)
        self.assertEqual(lps.norm.vmax, max_abs)
```

---

## Continuous Integration

### Setting Up CI

Example GitHub Actions workflow (`.github/workflows/test.yml`):

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests
      run: |
        pytest tests/test_lps.py -v --cov=lorenz_phase_space
    
    - name: Upload coverage
      uses: codecov/codecov-action@v2
```

---

## Troubleshooting Tests

### Common Test Failures

**1. Import Errors**
```
ModuleNotFoundError: No module named 'lorenz_phase_space'
```
**Solution:** Install package in development mode:
```bash
pip install -e .
```

**2. Missing Dependencies**
```
ModuleNotFoundError: No module named 'cmocean'
```
**Solution:** Install all dependencies:
```bash
pip install -r requirements.txt
```

**3. Display Issues**
```
UserWarning: Matplotlib is currently using agg
```
**Solution:** This is normal for headless testing. Plots are still saved correctly.

**4. Sample Data Not Found**
```
FileNotFoundError: sample_results_1.csv
```
**Solution:** Tests will skip gracefully if sample data is missing. This is expected.

**5. Test Output Directory Errors**
```
PermissionError: [Errno 13] Permission denied: 'test_outputs'
```
**Solution:** Ensure write permissions for tests directory.

### Debugging Failed Tests

1. **Run single test with verbose output:**
   ```bash
   python -m pytest tests/test_lps.py::TestClass::test_method -v -s
   ```

2. **Add debug prints:**
   ```python
   def test_something(self):
       result = function_under_test()
       print(f"Debug: result = {result}")
       self.assertEqual(result, expected)
   ```

3. **Use debugger:**
   ```python
   import pdb; pdb.set_trace()
   ```

4. **Check generated plots:**
   If visual tests fail, manually open the generated PNG files to see what went wrong.

---

## Test Maintenance

### When to Update Tests

- After adding new features
- After fixing bugs (add regression test)
- When API changes
- When default behavior changes
- After refactoring (ensure behavior unchanged)

### Test Review Checklist

- [ ] All tests pass
- [ ] New features have tests
- [ ] Edge cases covered
- [ ] Documentation updated
- [ ] Visual outputs verified
- [ ] No test warnings
- [ ] Coverage maintained or improved

---

## Additional Resources

- [pytest Documentation](https://docs.pytest.org/)
- [unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [matplotlib Testing](https://matplotlib.org/stable/devel/testing.html)
- [Coverage.py Documentation](https://coverage.readthedocs.io/)

---

## Questions?

For testing-related questions or issues:
- Open an issue on GitHub
- Contact: danilo.oceano@gmail.com

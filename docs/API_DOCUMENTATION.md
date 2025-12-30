# API Documentation

## Lorenz Phase Space Visualization Package

Complete API reference for the Lorenz Phase Space visualization tool.

---

## Table of Contents

1. [Visualizer Class](#visualizer-class)
2. [Helper Functions](#helper-functions)
3. [Data Requirements](#data-requirements)
4. [Examples](#examples)
5. [Customization Options](#customization-options)

---

## Visualizer Class

### `class Visualizer(LPS_type='mixed', zoom=False, x_limits=None, y_limits=None, color_limits=None, marker_limits=None, **kwargs)`

Main class for creating Lorenz Phase Space diagrams.

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `LPS_type` | str | `'mixed'` | Type of LPS diagram: `'mixed'`, `'baroclinic'`, or `'imports'` |
| `zoom` | bool | `False` | Enable dynamic axis limits based on data |
| `x_limits` | tuple/list | `None` | Custom x-axis limits `[min, max]` (only with `zoom=True`) |
| `y_limits` | tuple/list | `None` | Custom y-axis limits `[min, max]` (only with `zoom=True`) |
| `color_limits` | tuple/list | `None` | Custom colorbar limits (only with `zoom=True`) |
| `marker_limits` | tuple/list | `None` | Custom marker size limits `[min, max]` (only with `zoom=True`) |
| `**kwargs` | dict | `{}` | Additional customization options (see below) |

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `fig` | matplotlib.figure.Figure | Figure object containing the plot |
| `ax` | matplotlib.axes.Axes | Axes object for the main plot |
| `cbar` | matplotlib.colorbar.Colorbar | Colorbar showing the color scale |
| `norm` | matplotlib.colors.TwoSlopeNorm | Color normalization centered at zero |
| `LPS_type` | str | Type of phase space diagram |
| `zoom` | bool | Whether zoom mode is enabled |

#### Methods

##### `plot_data(x_axis, y_axis, marker_color, marker_size, **kwargs)`

Plot data points on the Lorenz Phase Space diagram.

**Parameters:**
- `x_axis` (array-like): X-axis values
  - For 'mixed': Ck (Conversion from mean to eddy kinetic energy)
  - For 'baroclinic': Ce (Conversion from zonal to eddy kinetic energy)
  - For 'imports': BAe (Eddy APE transport across boundaries)
- `y_axis` (array-like): Y-axis values
  - For 'mixed'/'baroclinic': Ca (Conversion from zonal to eddy potential energy)
  - For 'imports': BKe (Eddy KE transport across boundaries)
- `marker_color` (array-like): Values determining marker colors (typically Ge - Generation of eddy potential energy)
- `marker_size` (array-like): Values determining marker sizes (typically Ke - Eddy kinetic energy)
- `**kwargs`: Additional options
  - `alpha` (float): Transparency of markers (default: 1.0)
  - `cmap`: Colormap for markers (default: cmocean.cm.curl)

**Returns:**
- `tuple`: (fig, ax) - Figure and axes objects

**Example:**
```python
lps = Visualizer(LPS_type='mixed', zoom=False)
lps.plot_data(
    x_axis=data['Ck'],
    y_axis=data['Ca'],
    marker_color=data['Ge'],
    marker_size=data['Ke']
)
```

##### `get_labels()`

Get axis labels and annotations for the current LPS type.

**Returns:**
- `dict`: Dictionary containing all text labels specific to the LPS type

**Keys in returned dictionary:**
- `x_label`: X-axis label
- `y_label`: Y-axis label
- `color_label`: Colorbar label
- `size_label`: Marker size legend label
- `y_upper`: Upper y-axis region description
- `y_lower`: Lower y-axis region description
- `x_left`: Left x-axis region description
- `x_right`: Right x-axis region description
- `col_upper`: Upper colorbar region description
- `col_lower`: Lower colorbar region description
- `lower_left`: Lower-left quadrant label
- `upper_left`: Upper-left quadrant label
- `lower_right`: Lower-right quadrant label
- `upper_right`: Upper-right quadrant label

##### `set_limits(x_limits=None, y_limits=None)`

Set axis limits for the plot.

**Parameters:**
- `x_limits` (tuple/list, optional): Custom x-axis limits `[min, max]`
- `y_limits` (tuple/list, optional): Custom y-axis limits `[min, max]`

**Returns:**
- `tuple`: (x_min, x_max, y_min, y_max) - Applied axis limits

**Default Limits:**
- X-axis: `(-70, 70)` for all types
- Y-axis mixed: `(-20, 20)`
- Y-axis baroclinic: `(-20, 20)`
- Y-axis imports: `(-200, 200)`

##### `calculate_marker_size(term, zoom=False)` (static method)

Calculate marker sizes and intervals for legend.

**Parameters:**
- `term` (array-like): Energy values to be represented by marker sizes
- `zoom` (bool): If True, calculates intervals based on quantiles

**Returns:**
- `tuple`: (sizes, intervals)
  - `sizes` (pd.Series): Marker sizes for each data point
  - `intervals` (list): Threshold values for legend

**Marker Sizes:**
- Options: [200, 400, 600, 800, 1000]
- Default intervals (non-zoom): [3e5, 4e5, 5e5, 6e5]
- Zoom intervals: Based on quantiles [0.2, 0.4, 0.6, 0.8]

##### `annotate_plot(ax, cbar, **kwargs)`

Add annotations, labels, and descriptions to the plot.

**Parameters:**
- `ax` (matplotlib.axes.Axes): Axes object to annotate
- `cbar` (matplotlib.colorbar.Colorbar): Colorbar object to label
- `**kwargs`: Customization options
  - `labelpad`: Padding for axis labels
  - `fontsize`: Font size for annotations
  - `label_fontsize`: Font size for axis labels

##### `plot_legend(ax, intervals, msizes, title_label)` (static method)

Create and position the marker size legend.

**Parameters:**
- `ax` (matplotlib.axes.Axes): Axes object to add legend to
- `intervals` (list): Threshold values defining size categories
- `msizes` (list): Marker sizes [200, 400, 600, 800, 1000]
- `title_label` (str): Title for the legend

##### `plot_lines(limits, **kwargs)`

Draw reference lines on the plot.

**Parameters:**
- `limits` (tuple): Axis limits (x_min, x_max, y_min, y_max)
- `**kwargs`: Line styling options
  - `line_alpha`: Transparency (default: 0.2)
  - `lw`: Line width (default: 20)
  - `c`: Line color (default: '#383838')

##### `plot_gradient_lines(**kwargs)`

Draw gradient lines around reference axes (standard mode only).

**Parameters:**
- `**kwargs`: Line styling options
  - `lw`: Line width (default: 0.5)
  - `c`: Line color (default: '#383838')

---

## Helper Functions

### `get_max_min_values(series)`

Calculate adjusted maximum and minimum values from a series.

**Parameters:**
- `series` (array-like): Data series to analyze

**Returns:**
- `tuple`: (max_val, min_val) - Adjusted maximum and minimum values

**Purpose:**
Ensures both positive and negative values are present in the range by adjusting boundaries if necessary. Useful for creating balanced color normalizations centered around zero.

**Example:**
```python
series = np.array([-5, -3, -1])
max_val, min_val = get_max_min_values(series)
# Returns: (1, -5)
```

---

## Data Requirements

### Input Data Format

The package accepts array-like data (numpy arrays, pandas Series, lists).

### Required Variables by LPS Type

#### Mixed LPS
- **X-axis (Ck)**: Conversion from mean to eddy kinetic energy (W m⁻²)
- **Y-axis (Ca)**: Conversion from mean to eddy potential energy (W m⁻²)
- **Color (Ge)**: Generation of eddy potential energy (W m⁻²)
- **Size (Ke)**: Eddy kinetic energy (J m⁻²)

#### Baroclinic LPS
- **X-axis (Ce)**: Conversion from zonal to eddy kinetic energy (W m⁻²)
- **Y-axis (Ca)**: Conversion from zonal to eddy potential energy (W m⁻²)
- **Color (Ge)**: Generation of eddy potential energy (W m⁻²)
- **Size (Ke)**: Eddy kinetic energy (J m⁻²)

#### Imports LPS
- **X-axis (BAe)**: Eddy APE transport across boundaries (W m⁻²)
- **Y-axis (BKe)**: Eddy KE transport across boundaries (W m⁻²)
- **Color (Ge)**: Generation of eddy potential energy (W m⁻²)
- **Size (Ke)**: Eddy kinetic energy (J m⁻²)

### Data Preparation Tips

1. **Temporal Ordering**: Ensure data points are ordered chronologically for proper trajectory arrows
2. **Units**: Check that all energy values are in correct SI units
3. **Missing Values**: Remove or interpolate missing values before plotting
4. **Data Length**: Minimum 2 points required (for arrows); 5+ points recommended

---

## Examples

### Basic Usage - Single Dataset

```python
from lorenz_phase_space.phase_diagrams import Visualizer
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('cyclone_data.csv')

# Create standard LPS
lps = Visualizer(LPS_type='mixed', zoom=False)

# Plot data
lps.plot_data(
    x_axis=data['Ck'],
    y_axis=data['Ca'],
    marker_color=data['Ge'],
    marker_size=data['Ke']
)

# Save figure
plt.savefig('lps_diagram.png', dpi=300, bbox_inches='tight')
```

### Zoom Mode for Detailed Analysis

```python
# Create zoomed LPS
lps = Visualizer(LPS_type='mixed', zoom=True)

# Plot data
lps.plot_data(
    x_axis=data['Ck'],
    y_axis=data['Ca'],
    marker_color=data['Ge'],
    marker_size=data['Ke']
)

plt.savefig('lps_zoomed.png', dpi=300, bbox_inches='tight')
```

### Multiple Datasets with Custom Limits

```python
# Load two datasets
data1 = pd.read_csv('cyclone1.csv')
data2 = pd.read_csv('cyclone2.csv')

# Calculate dynamic limits across both datasets
x_min = min(data1['Ck'].min(), data2['Ck'].min())
x_max = max(data1['Ck'].max(), data2['Ck'].max())
y_min = min(data1['Ca'].min(), data2['Ca'].min())
y_max = max(data1['Ca'].max(), data2['Ca'].max())
color_min = min(data1['Ge'].min(), data2['Ge'].min())
color_max = max(data1['Ge'].max(), data2['Ge'].max())
size_min = min(data1['Ke'].min(), data2['Ke'].min())
size_max = max(data1['Ke'].max(), data2['Ke'].max())

# Create LPS with custom limits
lps = Visualizer(
    LPS_type='mixed',
    zoom=True,
    x_limits=[x_min, x_max],
    y_limits=[y_min, y_max],
    color_limits=[color_min, color_max],
    marker_limits=[size_min, size_max]
)

# Plot both datasets with transparency
lps.plot_data(
    x_axis=data1['Ck'],
    y_axis=data1['Ca'],
    marker_color=data1['Ge'],
    marker_size=data1['Ke'],
    alpha=0.7
)

lps.plot_data(
    x_axis=data2['Ck'],
    y_axis=data2['Ca'],
    marker_color=data2['Ge'],
    marker_size=data2['Ke'],
    alpha=0.7
)

plt.savefig('lps_comparison.png', dpi=300, bbox_inches='tight')
```

### Baroclinic LPS

```python
lps = Visualizer(LPS_type='baroclinic', zoom=False)

lps.plot_data(
    x_axis=data['Ce'],
    y_axis=data['Ca'],
    marker_color=data['Ge'],
    marker_size=data['Ke']
)

plt.savefig('lps_baroclinic.png', dpi=300, bbox_inches='tight')
```

### Imports LPS

```python
lps = Visualizer(LPS_type='imports', zoom=False)

lps.plot_data(
    x_axis=data['BAe'],
    y_axis=data['BKe'],
    marker_color=data['Ge'],
    marker_size=data['Ke']
)

plt.savefig('lps_imports.png', dpi=300, bbox_inches='tight')
```

---

## Customization Options

### kwargs for Visualizer Constructor

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `line_alpha` | float | 0.2 | Transparency of reference lines |
| `lw` | float | 20 (standard)<br>0.5 (gradient) | Line width for reference lines |
| `c` | str | '#383838' | Color for reference lines |
| `labelpad` | int | 5 (zoom)<br>38 (standard) | Padding for axis labels |
| `fontsize` | int | 10 | Font size for annotations |
| `label_fontsize` | int | 14 (zoom)<br>10 (standard) | Font size for axis labels |

### kwargs for plot_data Method

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `alpha` | float | 1.0 | Transparency of data markers |
| `cmap` | colormap | cmocean.cm.curl | Colormap for markers |

### Example with Custom Styling

```python
lps = Visualizer(
    LPS_type='mixed',
    zoom=False,
    line_alpha=0.3,
    lw=15,
    c='#555555',
    labelpad=40,
    fontsize=12,
    label_fontsize=14
)

lps.plot_data(
    x_axis=data['Ck'],
    y_axis=data['Ca'],
    marker_color=data['Ge'],
    marker_size=data['Ke'],
    alpha=0.8
)
```

---

## Interpretation Guide

### Mixed LPS Quadrants

| Quadrant | Ck | Ca | Physical Interpretation |
|----------|----|----|------------------------|
| Upper-Left | - | + | Barotropic and baroclinic instabilities |
| Upper-Right | + | + | Baroclinic instability |
| Lower-Left | - | - | Barotropic instability |
| Lower-Right | + | - | Eddy feeding local circulation |

### Color Scale Interpretation

- **Red colors (positive Ge)**: Latent heat release feeds eddy potential energy
- **Blue colors (negative Ge)**: Subsidence decreases eddy potential energy

### Marker Size Interpretation

- **Larger markers**: Higher eddy kinetic energy
- **Smaller markers**: Lower eddy kinetic energy

### Special Markers

- **'A'**: Start of trajectory (first time step)
- **'Z'**: End of trajectory (last time step)
- **Thick black outline**: Point of maximum intensity (highest Ke)

---

## Best Practices

1. **Standardized Comparisons**: Use `zoom=False` when comparing multiple systems
2. **Detailed Analysis**: Use `zoom=True` for single-system detailed analysis
3. **Multiple Trajectories**: Calculate common limits when overlaying multiple datasets
4. **Data Quality**: Ensure temporal continuity for meaningful arrow connections
5. **Visual Inspection**: Always visually inspect generated plots for correctness
6. **Color Scheme**: Use default colormap (cmocean.cm.curl) for consistency with literature
7. **Resolution**: Save at 300 dpi for publication-quality figures

---

## Troubleshooting

### Common Issues

1. **Arrows not appearing**: Check that data has at least 2 points
2. **Weird axis limits**: Verify data units and ranges
3. **Colorbar appears off**: Check color_limits match data range
4. **Legend shows wrong values**: Verify marker_size data and units
5. **Plot looks different than expected**: Avoid modifying plotting methods

### Getting Help

For issues or questions:
- Email: danilo.oceano@gmail.com
- GitHub Issues: [github.com/daniloceano/lorenz_phase_space](https://github.com/daniloceano/lorenz_phase_space)

---

## References

If you use this package in your research, please cite:

```
Lorenz Phase Space Visualization Tool
Danilo Couto de Souza
https://github.com/daniloceano/lorenz_phase_space
```

Related publications:
- Hart, R. E. (2003). A Cyclone Phase Space derived from thermal wind and thermal asymmetry. Monthly Weather Review, 131(4), 585-616.
- Lorenz, E. N. (1955). Available potential energy and the maintenance of the general circulation. Tellus, 7(2), 157-167.

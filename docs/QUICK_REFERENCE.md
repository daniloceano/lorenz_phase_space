# Quick Reference Guide

## Lorenz Phase Space - Quick Reference

---

## Basic Usage

```python
from lorenz_phase_space.phase_diagrams import Visualizer
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('your_data.csv')

# Create and plot
lps = Visualizer(LPS_type='mixed', zoom=False)
lps.plot_data(data['Ck'], data['Ca'], data['Ge'], data['Ke'])
plt.savefig('lps.png', dpi=300, bbox_inches='tight')
```

---

## LPS Types

| Type | X-axis | Y-axis | Purpose |
|------|--------|--------|---------|
| `'mixed'` | Ck | Ca | Both baroclinic and barotropic instabilities |
| `'baroclinic'` | Ce | Ca | Baroclinic processes only |
| `'imports'` | BAe | BKe | Energy imports/exports |

---

## Common Parameters

```python
Visualizer(
    LPS_type='mixed',      # 'mixed', 'baroclinic', or 'imports'
    zoom=False,            # True for dynamic limits
    x_limits=[-50, 50],    # Custom x-axis range
    y_limits=[-30, 30],    # Custom y-axis range
    color_limits=[-20, 20],# Custom colorbar range
    marker_limits=[1e5, 8e5] # Custom marker size range
)
```

---

## plot_data() Parameters

```python
lps.plot_data(
    x_axis=data['Ck'],        # X values
    y_axis=data['Ca'],        # Y values
    marker_color=data['Ge'],  # Color values
    marker_size=data['Ke'],   # Size values
    alpha=0.8                 # Transparency (0-1)
)
```

---

## When to Use zoom=True vs zoom=False

| Use zoom=False when... | Use zoom=True when... |
|------------------------|----------------------|
| Comparing multiple systems | Analyzing single system |
| Need standard reference | Want detailed view |
| Publishing comparisons | Exploring data range |

---

## Required Data Variables

### Mixed LPS
- **Ck**: Conversion from mean to eddy KE (W m⁻²)
- **Ca**: Conversion from mean to eddy APE (W m⁻²)
- **Ge**: Generation of eddy APE (W m⁻²)
- **Ke**: Eddy kinetic energy (J m⁻²)

### Baroclinic LPS
- **Ce**: Conversion from zonal to eddy KE (W m⁻²)
- **Ca**: Conversion from zonal to eddy APE (W m⁻²)
- **Ge**: Generation of eddy APE (W m⁻²)
- **Ke**: Eddy kinetic energy (J m⁻²)

### Imports LPS
- **BAe**: Eddy APE transport across boundaries (W m⁻²)
- **BKe**: Eddy KE transport across boundaries (W m⁻²)
- **Ge**: Generation of eddy APE (W m⁻²)
- **Ke**: Eddy kinetic energy (J m⁻²)

---

## Multiple Trajectories

```python
# Calculate common limits
x_min = min(data1['Ck'].min(), data2['Ck'].min())
x_max = max(data1['Ck'].max(), data2['Ck'].max())
# ... (repeat for y, color, size)

# Create with custom limits
lps = Visualizer(
    LPS_type='mixed', zoom=True,
    x_limits=[x_min, x_max],
    y_limits=[y_min, y_max],
    color_limits=[color_min, color_max],
    marker_limits=[size_min, size_max]
)

# Plot both
lps.plot_data(data1['Ck'], data1['Ca'], data1['Ge'], data1['Ke'], alpha=0.7)
lps.plot_data(data2['Ck'], data2['Ca'], data2['Ge'], data2['Ke'], alpha=0.7)
```

---

## Interpretation

### Mixed LPS Quadrants

```
Upper-Left  |  Upper-Right
(Ca+, Ck-)  |  (Ca+, Ck+)
Baro+Baro   |  Baroclinic
------------+-------------
Lower-Left  |  Lower-Right
(Ca-, Ck-)  |  (Ca-, Ck+)
Barotropic  |  Eddy feeding
```

### Color Interpretation
- 🔴 **Red (positive Ge)**: Latent heat release
- 🔵 **Blue (negative Ge)**: Subsidence

### Marker Size
- **Large**: High eddy kinetic energy
- **Small**: Low eddy kinetic energy

### Special Markers
- **A**: Start of trajectory
- **Z**: End of trajectory
- **Thick outline**: Maximum intensity

---

## Testing

```bash
# Run all tests
python -m unittest tests.test_lps -v

# Run with visual inspection
cd tests && python test_lps.py
```

Check outputs in `tests/test_outputs/*.png`

---

## Common Issues

| Problem | Solution |
|---------|----------|
| No arrows appearing | Need at least 2 data points |
| Strange axis limits | Check data units (W m⁻², J m⁻²) |
| Wrong colors | Verify Ge sign (+ for generation) |
| Plot looks different | Don't modify plotting methods |

---

## Best Practices

1. ✅ Use `zoom=False` for comparisons
2. ✅ Use `zoom=True` for detailed analysis
3. ✅ Save at 300 dpi for publications
4. ✅ Always visually inspect outputs
5. ✅ Ensure temporal continuity in data
6. ✅ Use default colormap for consistency

---

## File Organization

```
your_project/
├── data/
│   └── cyclone_data.csv
├── scripts/
│   └── create_lps.py
└── figures/
    └── lps_diagrams/
```

---

## Example Script Template

```python
#!/usr/bin/env python
"""Generate Lorenz Phase Space diagram"""

from lorenz_phase_space.phase_diagrams import Visualizer
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load data
    data = pd.read_csv('data/cyclone_data.csv')
    
    # Create visualizer
    lps = Visualizer(LPS_type='mixed', zoom=False)
    
    # Plot data
    lps.plot_data(
        x_axis=data['Ck'],
        y_axis=data['Ca'],
        marker_color=data['Ge'],
        marker_size=data['Ke']
    )
    
    # Customize if needed
    plt.title('Cyclone Evolution in LPS')
    
    # Save
    plt.savefig('figures/lps_diagram.png', 
                dpi=300, bbox_inches='tight')
    print("Saved: figures/lps_diagram.png")

if __name__ == '__main__':
    main()
```

---

## Documentation Links

- 📖 **[README](../README.md)**: Overview and examples
- 📚 **[API Documentation](API_DOCUMENTATION.md)**: Complete reference
- 📓 **[Example Notebook](example_usage.ipynb)**: Interactive examples
- 🧪 **[Testing Guide](../tests/TESTING.md)**: How to test
- 📝 **[Changelog](../CHANGELOG.md)**: Version history

---

## Getting Help

- 📧 **Email**: danilo.oceano@gmail.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/daniloceano/lorenz_phase_space/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/daniloceano/lorenz_phase_space/discussions)

---

## Citation

```bibtex
@software{lorenz_phase_space,
  author = {Couto de Souza, Danilo},
  title = {Lorenz Phase Space Visualization Tool},
  year = {2025},
  url = {https://github.com/daniloceano/lorenz_phase_space},
  version = {1.3.0}
}
```

---

**Quick Reference** | Version 1.3.0 | Last Updated: December 30, 2025

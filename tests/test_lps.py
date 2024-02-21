import pandas as pd
from LPS import LorenzPhaseSpace
import matplotlib.pyplot as plt

def test_lorenz_phase_space_variants():
    sample_file = 'samples/sample_results_1.csv'
    df = pd.read_csv(sample_file, parse_dates={'Datetime': ['Date', 'Hour']}, date_format='%Y-%m-%d %H')

    x_axis = df['Ck'].values
    y_axis = df['Ca'].values
    marker_color = df['Ge'].values
    marker_size = df['Ke'].values

    title = 'sample'
    datasource = 'sample'
    start = pd.to_datetime(df['Datetime'].iloc[0]).strftime('%Y-%m-%d %H:%M')
    end = pd.to_datetime(df['Datetime'].iloc[-1]).strftime('%Y-%m-%d %H:%M')

    # Test without zoom
    lps_mixed = LorenzPhaseSpace(x_axis, y_axis, marker_color, marker_size, title=title, datasource=datasource, start=start, end=end)
    fig, ax = lps_mixed.plot()
    plt.savefig('samples/sample_1_LPS_mixed.png', dpi=300)
    plt.close(fig)  # Ensure matplotlib clears the figure

    # Assertions for mixed type without zoom
    assert fig is not None
    assert ax is not None

    # Test with zoom
    lps_zoom = LorenzPhaseSpace(x_axis, y_axis, marker_color, marker_size, zoom=True, title=title, datasource=datasource, start=start, end=end)
    fig_zoom, ax_zoom = lps_zoom.plot()
    plt.savefig('samples/sample_1_LPS_mixed_zoom.png', dpi=300)
    plt.close(fig_zoom)

    # Assertions for mixed type with zoom
    assert fig_zoom is not None
    assert ax_zoom is not None

    # Test LPS_type "baroclinic"
    lps_baroclinic = LorenzPhaseSpace(x_axis, y_axis, marker_color, marker_size, LPS_type='baroclinic', title=title, datasource=datasource, start=start, end=end)
    fig_baroclinic, ax_baroclinic = lps_baroclinic.plot()
    plt.savefig('samples/sample_1_LPS_baroclinic.png', dpi=300)
    plt.close(fig_baroclinic)

    # Assertions for baroclinic type
    assert fig_baroclinic is not None
    assert ax_baroclinic is not None

    # Test LPS_type "barotropic"
    lps_barotropic = LorenzPhaseSpace(x_axis, y_axis, marker_color, marker_size, LPS_type='barotropic', title=title, datasource=datasource, start=start, end=end)
    fig_barotropic, ax_barotropic = lps_barotropic.plot()
    plt.savefig('samples/sample_1_LPS_barotropic.png', dpi=300)
    plt.close(fig_barotropic)

    # Assertions for barotropic type
    assert fig_barotropic is not None
    assert ax_barotropic is not None

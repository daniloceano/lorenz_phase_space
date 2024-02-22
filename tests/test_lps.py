import unittest
import numpy as np
import pandas as pd
from LPS import LorenzPhaseSpace, get_max_min_values

class TestLorenzPhaseSpace(unittest.TestCase):

    def setUp(self):
        # Sample data for testing, no longer passed during initialization
        self.x_axis = np.array([1, 2, 3])
        self.y_axis = np.array([4, 5, 6])
        self.marker_color = np.array([7, 8, 9])
        self.marker_size = np.array([10, 11, 12])
        # Initialize without data
        self.lps = LorenzPhaseSpace(LPS_type='mixed', zoom=False)

    def test_initialization(self):
        self.assertEqual(self.lps.LPS_type, 'mixed')
        self.assertFalse(self.lps.zoom)

    def test_calculate_marker_size(self):
        sizes, intervals = LorenzPhaseSpace.calculate_marker_size(self.marker_size)
        self.assertTrue(len(sizes) > 0)
        self.assertTrue(len(intervals) > 0)

    def test_get_labels(self):
        labels = self.lps.get_labels()
        self.assertIsInstance(labels, dict)
        self.assertIn('x_label', labels)
        self.assertIn('y_label', labels)

    def test_plot_data(self):
        # Ensure plot_data method can be called without errors
        # Note: This test assumes matplotlib is configured to run in a headless environment if tests are automated
        self.lps.create_lps_plot(x_axis=self.x_axis, y_axis=self.y_axis)  # Prepare plot first
        try:
            self.lps.plot_data(self.x_axis, self.y_axis, self.marker_color, self.marker_size)
            self.assertTrue(True)  # Confirm plot_data ran without error
        except Exception as e:
            self.fail(f"plot_data method failed with an exception: {e}")

    def test_zoom_with_random_factors(self):
        # Test zoom functionality with random factors applied to data
        n = len(self.x_axis)
        random_factors = np.random.randint(1, 11, size=n)
        x_axis_rdm = self.x_axis * random_factors
        y_axis_rdm = self.y_axis * random_factors
        marker_color_rdm = self.marker_color * random_factors
        marker_size_rdm = self.marker_size * random_factors

        self.lps.zoom = True  # Enable zoom
        self.lps.create_lps_plot()  # Recreate plot for zoom
        try:
            self.lps.plot_data(x_axis_rdm, y_axis_rdm, marker_color_rdm, marker_size_rdm)
            self.assertTrue(True)  # Confirm plot_data with zoom and random factors ran without error
        except Exception as e:
            self.fail(f"plot_data with zoom and random factors failed with an exception: {e}")

if __name__ == '__main__':
    unittest.main()

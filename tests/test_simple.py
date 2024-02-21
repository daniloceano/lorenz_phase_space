import unittest
import numpy as np
import pandas as pd
from LPS import LorenzPhaseSpace, get_max_min_values

class TestLorenzPhaseSpace(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.x_axis = np.array([1, 2, 3])
        self.y_axis = np.array([4, 5, 6])
        self.marker_color = np.array([7, 8, 9])
        self.marker_size = np.array([10, 11, 12])
        self.lps = LorenzPhaseSpace(self.x_axis, self.y_axis, self.marker_color, self.marker_size)

    def test_initialization(self):
        self.assertEqual(self.lps.x_axis.iloc[0], 1)
        self.assertEqual(self.lps.y_axis.iloc[0], 4)
        self.assertEqual(self.lps.marker_color.iloc[0], 7)
        self.assertEqual(self.lps.marker_size.iloc[0], 10)
        self.assertEqual(self.lps.LPS_type, 'mixed')
        self.assertFalse(self.lps.zoom)

    def test_calculate_marker_size(self):
        sizes, intervals = LorenzPhaseSpace.calculate_marker_size(pd.Series(self.marker_size))
        self.assertTrue(len(sizes) > 0)
        self.assertTrue(len(intervals) > 0)

    def test_get_labels(self):
        labels = self.lps.get_labels()
        self.assertIsInstance(labels, dict)
        self.assertIn('x_label', labels)
        self.assertIn('y_label', labels)

    def test_plot(self):
        # This test checks if the plot method runs without error
        # More detailed tests can be added to verify plot properties
        try:
            fig, ax = self.lps.plot()
            self.assertTrue(True)  # Plot method ran without error
        except Exception as e:
            self.fail(f"Plot method failed with an exception: {e}")

if __name__ == '__main__':
    unittest.main()

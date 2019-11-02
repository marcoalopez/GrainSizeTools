import unittest
from tools import *

# import test dataset and store expected results
#TODO

class test_tools_function(unittest.TestCase):

    def test_calc_freq_grainsize(self):       
        # test default values
        self.assertAlmostEqual(calc_freq_grainsize(d), results_01)

        # test bin size methods
        self.assertAlmostEqual(calc_freq_grainsize(d, binsize='fd'), results_01)
        self.assertAlmostEqual(calc_freq_grainsize(d, binsize='scott'), results_01)
        self.assertAlmostEqual(calc_freq_grainsize(d, binsize='scott'), results_01)

    def test_calc_freq_grainsize_err(self):
        # make sure value errors are raised when necessary
        self.assertRaises(ValueError, calc_freq_grainsize, d, )

    def test_calc_freq_peak(self):
        # test default values
        self.assertAlmostEqual(calc_freq_peak(d), )

if __name__ == "__main__":
    unittest.main()

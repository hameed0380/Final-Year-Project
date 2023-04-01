import unittest
from ga import GenAlgorithm

# run with shell
# limited options and delt with float issues in the actual program

class TestGenAlgorithm(unittest.TestCase):
    def setUp(self):
        # set up ga with  constants
        self.ga = GenAlgorithm(2, 500, 0.001, 0.8, 0.7, -5.12, 5.12, 500)

    # test_binary_to_decimal verifies binary_to_decimal method  correctly converts a binary list to decimal values.
    def test_binary_to_decimal(self):
        binary_individual = [1, 1, 1, 0, 1]
        decimal = self.ga.binary_to_decimal(binary_individual)
        self.assertEqual(len(decimal), 2) # in compliance
        self.assertFalse(len(decimal) ==  3)

    def test_bit_count(self):
        min_bits, adjusted_precision = self.ga.bit_count()
        self.assertTrue(min_bits != 13)
        #self.assertAlmostEqual(adjusted_precision, 0.003937007874015748)


if __name__ == '__main__':
    unittest.main()

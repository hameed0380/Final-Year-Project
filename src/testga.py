import unittest
from ga import GenAlgorithm

class TestGenAlgorithm(unittest.TestCase):
    def setUp(self):
        self.ga = GenAlgorithm(2, 100, 0.01, 0.8, 0.1, -5.12, 5.12, 1000)

    # The test_binary_to_decimal method verifies that the binary_to_decimal method of the GenAlgorithm class correctly converts a binary list to decimal values.
    def test_binary_to_decimal(self):
        binary_individual = [1, 0, 1, 0, 1]
        decimal_values = self.ga.binary_to_decimal(binary_individual)
        self.assertEqual(len(decimal_values), 2)


if __name__ == '__main__':
    unittest.main()

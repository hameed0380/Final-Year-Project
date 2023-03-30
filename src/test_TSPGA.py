import unittest
import TSPGA
import numpy as np
import random
from TSPGA import *



class testTSP(unittest.TestCase):

	# Test case for euclidean distance method
	def test_distance(self):
		x=0
		y=0

		# inorder for the attribute x and y to be recognised 
		self.x = x
		self.y = y
		distance_solution = 70.71067811865476 
		distances = City.distance(self, City(x=50, y=50))
		# assert distances == distance_solution # TODO: Compare
		# Used numpy isclose() function to assert first to see if the two values are close enough
		assert np.isclose(distances, distance_solution, rtol=0.001)
		assert distances == distance_solution

		# test with random values
		# seed for reproducible results
		random.seed(0)
		distance_solution = 112.60994627474076
		distances = City.distance(self, City(x=int(random.random() * 100), y=int(random.random() * 100)))
		assert np.isclose(distances, distance_solution, rtol=0.001)







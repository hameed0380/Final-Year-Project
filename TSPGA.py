import numpy as np

# For the TSP a gene in this case would be a city with its coordinates. 

class City:
    def __init__(self, node, x, y):
        self.node = int(node)

    def distance(self, city):
        x_len = self.x - city.x
        y_len = self.y - city.y
        distance = math.sqrt((x_len ** 2) + (y_len ** 2))
        return distance
import numpy as np

# For the TSP a gene in this case would be a city with its coordinates. 

class City:
    def __init__(self, node, x, y):
        self.node = int(node)

    # Calculates the Euclidean distance between 2 points
    def distance(self, city):
        x_len = self.x - city.x
        y_len = self.y - city.y
        distance = math.sqrt((x_len ** 2) + (y_len ** 2))
        return distance

    def to_string(self):
        return "city" + str(self.node) + " x: " + str(self.x) + " y: " + str(self.y)

    def __repr__(self):
        return self.to_string()

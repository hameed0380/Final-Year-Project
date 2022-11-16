import numpy as np

# For the TSP a gene in this case would be a city with its coordinates. 
class City:
    def __init__(self, node, x, y):
        self.node = int(node)

   def getx(self):
      return self.x
   
   def gety(self):
      return self.y
   
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


# current fitness
# Use class for fitness function to define inverse of route
class FitnessFunc:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def routeDistance(self):
        if self.distance ==0:
            routDis = 0
            lenRoute = len(self.route)
            for n in range(0, len(lenRoute)):
                fromCity = self.route[n]
                toCity = None
                if n+1 < lenRoute:
                    toCity = self.route[n+1]
                else:
                    toCity = self.route[0]
                routDis += fromCity.distance(toCity)
            self.distance = routDis
        return self.distance


    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness

        # Look for another fitness function

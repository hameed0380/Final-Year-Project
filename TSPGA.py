import numpy as np
import random
import math
import operator
import pandas as pd
import matplotlib.pyplot as plt


# For the TSP a gene in this case would be a city with its coordinates.
# The x and y represent the coordinates for the city.
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Retrieves x
    def getx(self):
        return self.x
    
    # Retrieves y
    def gety(self):
        return self.y
   
    # Calculates the Euclidean distance between 2 points (cities)
    def distance(self, city):
        x_len = self.x - city.x
        y_len = self.y - city.y
        distance = math.sqrt((x_len ** 2) + (y_len ** 2))
        return distance

    # Used to represent the cities in a more formatted way
    def to_string(self):
        return "city" + str(self.node) + " x: " + str(self.x) + " y: " + str(self.y)

    def __repr__(self):
        return self.to_string()


# current fitness
# After researching I found that there were already suitable fitness functions created and it would be difficult 
# and a waste of time to implement a completely different one as a result I decided to use the one below from Eric Stoltz.


# Use class for fitness function to define inverse of route
# For the fitness function we are trying to minimize the route distance 
class FitnessFunc:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0


    # Distance between 2 cities
    def routeDistance(self):
        if self.distance ==0:
            routDis = 0
            lenRoute = len(self.route)
            for n in range(0, lenRoute):
                fromCity = self.route[n]
                toCity = None
                if n+1 < lenRoute:
                    toCity = self.route[n+1]
                else:
                    toCity = self.route[0]
                routDis += fromCity.distance(toCity)
            self.distance = routDis
        return self.distance


    # Here we calculate the ftiness value of the route which is the inverse
    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness

        # Look for another fitness function


# Here is an alternative fitness function 
# this fitness function makes use of inverse total distance

# def total_fitness(total_d):
#     if total_d!=0.0:
#         #make fitness inverse of total distance
#         fitness = 10000000000000000.0/ total_d
#     else:
#         print("Total distance cannot be zero. Check again")
#         sys.exit()
#     return fitness


# Generate popultation

# Randomly creating the routes for initial generation in pop
def genRouter(num_city):
    size = len(num_city)
    route1 = random.sample(num_city, size)
    return route1

# Creation of inital pop
# pop sample, only used for first instance
def initialize_pop(pop_size, num_city):
    pop = []
    for i in range(0, pop_size):
        pop.append(genRouter(c_list))
    return pop


# Crossover of parents to produce a new generation
def crossover_phase(parent_a, parent_b):
    offspring = []
    offspringA = []
    offspringB = []

    # gene from parents set to random values i.e use of random lib
    gene_fromA = int(random.random()* len(parent_a))
    gene_fromB = int(random.random()* len(parent_b))

    # Start and end gene set  for sequencing
    Beg_Seq = min(gene_fromA, gene_fromB)
    End_Seq = max(gene_fromA, gene_fromB)

    for i in range(Beg_Seq, End_Seq):
        offspringA.append(gene_fromA[i])
    offspringB = [item for item in a if item not in chioffspringAldA]
    # getting both genes from parents
    offspring = offspringA + offspringB
    return offspring

# will have a set mutation rate, route1 is retrieved from route generated above
def mutation_phase(route1, mutate_rate):
    # Set mutation rate outside, cannot set inside loop
    lenRoute = len(route1) # size route

    # swapping arround for mutations with random element
    for swap in range(lenRoute):
        if (mutate_rate > random.random()):
            swappedInd = int(random.random() * lenRoute)
            # Had to replace was getting out of index error
            # swappedInd = int(random.random() * lenRoute)

            # Swapping around
            swapped1 = route1[swap]
            swapped2 = route1[swappedInd]

            route1[swap] = swapped2
            route1[swappedInd] = swapped1
    return route1


# Simple selection process rather then using dataframe
# less complex and achieves the same outcome
def selection(rank, bestsize):
    selectionResults = []
    result = []

    for i in rank:
        result.append(i[0])
    for i in range(0, bestsize):
        selectionResults.append(result[i])
    
    return selectionResults

import numpy as np
import math
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt

# Creating this genetic algorithm for the TSP has helped me to 
# understand how they work by employing a series of phases backed
# by evolution we can create generations and see how they survive.

# This serves as the base reference for my genetic algorithm.



# For the TSP a gene in this case would be a city with its coordinates(x, y).
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
    # Decided from research this was the best metric for distance
    def distance(self, City):
        x_len = self.x - City.x
        y_len = self.y - City.y
        distance = math.sqrt((x_len ** 2) + (y_len ** 2))
        return distance

    # Used to represent the cities in a more formatted way
    def to_string(self):
        return "City " + " x: " + str(self.x) + " y: " + str(self.y)

    def __repr__(self):
        return self.to_string()


 # current fitness
 # After researching I found that there were already suitable fitness functions created 
 # and it would be difficult and a waste of time to implement a completely 
 # different one as a result I decided to use the one below from Eric Stoltz.
 # Other examples have used it


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

        # Look for another fitness function(reminder)


# Here is an alternative fitness function 
# this fitness function makes use of inverse total distance.
# However, I don't believe this method makes good use of the actual
# distance between the routes rather it uses a generic formula.


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
def genRouter(c_list):
    size = len(c_list)
    route1 = random.sample(c_list, size)
    return route1

# Creation of inital pop
# pop sample, only used for first instance
def initialize_pop(pop_size, c_list):
    pop = []
    for i in range(0, pop_size):
        pop.append(genRouter(c_list))
    return pop


# Had quite a bit of trouble understanding this part lucky by using 
# my previous knowledge of evolution I was able to understand. The idea of 
# tacking genes from both parents, I labelled them specifically in biological
# terms to help further my understanding

# Crossover of parents to produce a new generation
def crossover_phase(parent_a, parent_b):
    offspring = []
    offspringA = []
    offspringB = []

    # gene from parents set to random values i.e use of random lib
    gene_fromA = int(random.random()* len(parent_a))
    gene_fromB = int(random.random()* len(parent_b))

    # Start and end gene set for sequencing
    Beg_Seq = min(gene_fromA, gene_fromB)
    End_Seq = max(gene_fromA, gene_fromB)

    for i in range(Beg_Seq, End_Seq):
        offspringA.append(parent_a[i])

    offspringB = [item for item in parent_b if item not in offspringA]
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
# less complex and achieves outcome however, it does not work as well
# and has limitations in that it doesn't get the best ranked routes.


# def selection(rank, bestsize):
#     sltResults = []
#     result = []

#     for i in rank:
#         result.append(i[0])
#     for i in range(0, bestsize):
#         sltResults.append(result[i])
    
#     return sltResults



# Decided that this selection process was much better then one I previously 
# implemeneted it gets best routes via rank
# by 'Eric stolz'

def selection(rank, bestsize):
    sltResults = []
    df = pd.DataFrame(np.array(rank), columns=["Index","Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()
    
    for i in range(0, bestsize):
        sltResults.append(rank[i][0])
    for i in range(0, len(rank) - bestsize):
        pick = 100*random.random()
        for i in range(0, len(rank)):
            if pick <= df.iat[i,3]:
                sltResults.append(rank[i][0])
                break
    return sltResults



# ranked according to fitness value 
# By using the fitness function we can choose the best available
def rankRoutes(pop):

    # set for fitness results
    fitnessResults = {}
    lenPop = len(pop)
    for n in range(0, lenPop):
        fitnessResults[n] = FitnessFunc(pop[n]).routeFitness()
    # makes sure returned value is sorted
    return sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)


# Used to generate the mating pool and sore in array
def matingPool(pop, sltResults):
    matingpool = []
    for i in range(0, len(sltResults)):
        index = sltResults[i]
        matingpool.append(pop[index])
    return matingpool


def selectpop(matingpool, bestsize):
    offspring_1 = []
    length = len(matingpool) - bestsize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0,bestsize):
        offspring_1.append(matingpool[i])
    
    for i in range(0, length):
        child = crossover_phase(pool[i], pool[len(matingpool)-i-1])
        offspring_1.append(child)
    return offspring_1



def mutatepop(pop, mutate_rate):
    mutatedPop = []
    
    for ind in range(0, len(pop)):
        mutatedInd = mutation_phase(pop[ind], mutate_rate)
        mutatedPop.append(mutatedInd)
    return mutatedPop



# Here we want to use all processes i.e functions to creation of next generation.

# 1. rank current routes
# 2. select parents with selection phase
# 3. create a mating pool
# 4. create new generation
# 5. apply mutations(swapping process) 

def nextGeneration(currentGen, bestsize, mutate_rate):
    rank = rankRoutes(currentGen)
    sltResults = selection(rank, bestsize)
    matingpool = matingPool(currentGen, sltResults)
    offspring_1 = selectpop(matingpool, bestsize)
    nextGeneration = mutatepop(offspring_1, mutate_rate)
    return nextGeneration


# create initial population and run the GA processes
def initiateGA(pop, popSize, bestsize, mutate_rate, generations):
    pop1 = initialize_pop(popSize, pop)
    # Initial distance calculated without generation 
    print("Starting distance: " + str(1 / rankRoutes(pop1)[0][1]))
    current = []
    current.append((1 / rankRoutes(pop1)[0][1]))

    # Introduces other generation
    for i in range(0, generations):
        pop1 = nextGeneration(pop1, bestsize, mutate_rate)
        # Displays the current distance helps to show the process
        current.append((1 / rankRoutes(pop1)[0][1]))
        print("Gen =", i, " curr distance =", current[i])

    
    print("Final distance: " + str(1 / rankRoutes(pop1)[0][1]))
    elite_routeInd = rankRoutes(pop1)[0][0]
    elite_route = pop1[elite_routeInd]
    return elite_route


# Running GA
c_list = []

for i in range(0,10):
    c_list.append(City(x=int(random.random() * 100), y=int(random.random() * 100)))


# tested numeracy generation sizers and mutation rates
#initiateGA(pop=c_list, popSize=100, bestsize=20, mutate_rate=0.01, generations=200)
# initiateGA(pop=c_list, popSize=100, bestsize=20, mutate_rate=0.05, generations=200)
# initiateGA(pop=c_list, popSize=100, bestsize=20, mutate_rate=0.05, generations=1000)



# Conclusions 

# The higher the generation size the higher the time need to calculate distance and the higher the final distance is.
# The mutation rate also affects the distance as the higher the mutation rate the greater the final distance is.
# Using biological notation helps further understanding

# credits to: 'Eric stolz' for helping break it down


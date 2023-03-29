# genetic algorithm to solve the 0-1 knapsack problem
import random
import matplotlib.pyplot as plt

# generate a random population based on population size (genes denoted with simple binary)
def gen_pop(size):
	population = []
	for i in range(size):
		genes = [0, 1]
		chromosome = []
		for i in range(len(items)):
			chromosome.append(random.choice(genes))
		population.append(chromosome)
	print("Generated a random population of size", size)
	return population

# calculate the fitness of a chromosome but implementing knapsack
def fitness_func(chromosome):
	total_weight = 0
	total_value = 0
	for i in range(len(chromosome)):
		if chromosome[i] == 1:
			total_weight += items[i][0]
			total_value += items[i][1]
	if total_weight > max_weight:
		return 0
	else:
		return total_value

# selection of two chromosomes for crossover from parents
def selection(population):
	fitness_values = []
	for chromosome in population:
		fitness_values.append(fitness_func(chromosome))
	
	fitness_values = [float(i)/sum(fitness_values) for i in fitness_values]
	
	parent1 = random.choices(population, weights=fitness_values, k=1)[0]
	parent2 = random.choices(population, weights=fitness_values, k=1)[0]
	
	print("Selected two chromosomes for crossover")
	return parent1, parent2

# perform crossover between two chromosomes a slightly different method then in the previous examples
def crossover(parent1, parent2):
	crossover_point = random.randint(0, len(items)-1)
	child1 = parent1[0:crossover_point] + parent2[crossover_point:]
	child2 = parent2[0:crossover_point] + parent1[crossover_point:]
	
	print("Performed crossover between two chromosomes")
	return child1, child2

# perform mutation on a chromosome
def mutate(chromosome):
	mutation_point = random.randint(0, len(items)-1)
	if chromosome[mutation_point] == 0:
		chromosome[mutation_point] = 1
	else:
		chromosome[mutation_point] = 0
	print("Performed mutation on a chromosome")
	return chromosome

# function to get the best chromosome from the population
def best_gen(population):
	fitness_values = []
	for chromosome in population:
		fitness_values.append(fitness_func(chromosome))

	max_value = max(fitness_values)
	max_index = fitness_values.index(max_value)
	return population[max_index]


# items that can be put in the knapsack
items = [
		[1, 2],
		[2, 4],
		[3, 4],
		[4, 5],
		[5, 7],
		[6, 9]
	]

# print available items
print("Available items:\n", items)

# parameters for genetic algorithm
max_weight = 10
population_size = 10
mutation_probability = 0.2
generations = 10

print("\nGenetic algorithm parameters:")
print("Max weight:", max_weight)
print("Population:", population_size)
print("Mutation probability:", mutation_probability)
print("Generations:", generations, "\n")
print("Performing genetic evolution:")

# generate a random population
population = gen_pop(population_size)

# keep track of best fitness value over time
best_fitness_over_time = []

# evolve the population for specified number of generations
for i in range(generations):
    # select two chromosomes for crossover
    parent1, parent2 = selection(population)

    # perform crossover to generate two new chromosomes
    child1, child2 = crossover(parent1, parent2)

    # perform mutation on the two new chromosomes
    if random.uniform(0, 1) < mutation_probability:
        child1 = mutate(child1)
    if random.uniform(0, 1) < mutation_probability:
        child2 = mutate(child2)

    # replace the old population with the new population
    population = [child1, child2] + population[2:]

    # get the best fitness value from the population
    best_fitness = fitness_func(best_gen(population))
    best_fitness_over_time.append(best_fitness)

# plot the best fitness value over time
plt.plot(best_fitness_over_time)
plt.xlabel('Generation')
plt.ylabel('Best fitness value')
plt.title('Genetic algorithm performance')
plt.show()

# get the best chromosome from the population
best = best_gen(population)

# get the weight and value of the best solution
total_weight = 0
total_value = 0

for i in range(len(best)):
    if best[i] == 1:
        total_weight += items[i][0]
        total_value += items[i][1]

# print the best solution
print("\nThe best solution:")
print("Weight:", total_weight)
print("Value:", total_value)
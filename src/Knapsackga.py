import random
import pygame
#import time

# Constants
ITEMS = []
CAPACITY = 0
POPULATION_SIZE = 50
NUM_GENERATIONS = 100
MUTATION_PROBABILITY = 0.1

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Pygame initialization
pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Knapsack Problem")

# Item class
class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

# Population class (random)
class Population:
    def __init__(self, size):
        self.solutions = [generate_solution() for x in range(size)]

# Fitness function
def fitness(solution):
    total_value = 0
    total_weight = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_value += ITEMS[i].value
            total_weight += ITEMS[i].weight
    if total_weight > CAPACITY:
        return 0
    return total_value

# Selection function
def selection(population):
    fitnesses = [fitness(solution) for solution in population.solutions]
    total_fitness = sum(fitnesses)
    probabilities = [fitness/total_fitness for fitness in fitnesses]
    selected = []
    for i in range(len(population.solutions)):
        selected.append(random.choices(population.solutions, probabilities)[0])
    return selected

# Crossover function
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation function
def mutation(solution):
    mutated_solution = solution[:]
    for i in range(len(mutated_solution)):
        if random.random() < MUTATION_PROBABILITY:
            mutated_solution[i] = 1 - mutated_solution[i]
    return mutated_solution

# Generate initial solution
def generate_solution():
    solution = []
    i = 0
    for i in range(len(ITEMS)):
        solution.append(random.randint(0, 1))
    return solution

# Draw knapsack function
def draw_knapsack(solution):
    SCREEN.fill(WHITE)
    total_value = 0
    total_weight = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_value += ITEMS[i].value
            total_weight += ITEMS[i].weight
    font = pygame.font.SysFont("arial", 20)
    text = font.render("Total value: {}".format(total_value), True, BLACK)
    SCREEN.blit(text, (20, 20))
    text = font.render("Total weight: {}".format(total_weight), True, BLACK)
    SCREEN.blit(text, (20, 50))
    for i in range(len(solution)):
        if solution[i] == 1:
            pygame.draw.rect(SCREEN, BLACK, (300, 50*i+100, ITEMS[i].value, ITEMS[i].weight)) # represents items

# Main function
def main():
    global ITEMS, CAPACITY, POPULATION_SIZE, NUM_GENERATIONS, MUTATION_PROBABILITY
    ITEMS = [
        Item("Item 1", 10, 5),
        Item("Item 2", 4, 4),
        Item("Item 3", 8, 3),
        Item("Item 4", 6, 6),
        Item("Item 5", 2, 1),
        Item("Item 6", 5, 2),
        Item("Item 7", 7, 4),
        Item("Item 8", 1, 1),
        Item("Item 9", 3, 3),
        Item("Item 10", 6, 5),
        Item("Item 11", 9, 7),
        Item("Item 12", 8, 4),
        Item("Item 13", 5, 2),
        Item("Item 14", 3, 1),
        Item("Item 15", 2, 1)
    ]
    CAPACITY = 20
    POPULATION_SIZE = 50
    NUM_GENERATIONS = 1000
    MUTATION_PROBABILITY = 0.1

    # Initialize population
    population = Population(POPULATION_SIZE)

    # Evolve population
    for generation in range(NUM_GENERATIONS):
        parents = selection(population)
        offspring = []
        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[i+1]
            child1, child2 = crossover(parent1, parent2)
            child1 = mutation(child1)
            child2 = mutation(child2)
            offspring.append(child1)
            offspring.append(child2)
        population.solutions = offspring

        # Draw best solution
        best_solution = max(population.solutions, key=fitness)
        # Print best solution
        best_solution = max(population.solutions, key=fitness)
        total_value = 0
        total_weight = 0
        for i in range(len(best_solution)):
            if best_solution[i] == 1:
                total_value += ITEMS[i].value
                total_weight += ITEMS[i].weight
        print("Best solution found: ", best_solution)
        print("Total value: ", total_value)
        print("Total weight: ", total_weight)
        draw_knapsack(best_solution)
        pygame.display.update()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()

# Have been working to fix some of the mistakes so far it just blinks but does display weights and values so plus

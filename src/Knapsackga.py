import random
import pygame
import time
import sys

# Constants
ITEMS = [] # List to store the items
CAPACITY = 0  # Stores maximum capacity of the knapsack
POPULATION_SIZE = 50 # num of solutions in the population
NUM_GENERATIONS = 100 # num of generations for the genetic algorithm
MUTATION_PROBABILITY = 0.1 # Probability of mutation

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Pygame initialization
pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Knapsack Problem")

class Item:
    """ Item class represents an item with a name, value, and weight. """
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight


class Population:
    """ Population class represents a population of solutions """
    def __init__(self, size):
        self.solutions = [generate_solution() for x in range(size)]

# Fitness function calculates the total value of a solution considering the maximum capacity
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

# Selection function selects solutions based on their fitness (using roulette wheel selection) --> discussed in project
def selection(population):
    fitnesses = [fitness(solution) for solution in population.solutions]
    total_fitness = sum(fitnesses)
    probabilities = [fitness/total_fitness for fitness in fitnesses]
    selected = []
    for i in range(len(population.solutions)):
        selected.append(random.choices(population.solutions, probabilities)[0])
    return selected

# Crossover function combines two parent solutions to create two offspring solutions
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation function modifies a solution with given probability
def mutation(solution):
    mutated_solution = solution[:]
    for i in range(len(mutated_solution)):
        if random.random() < MUTATION_PROBABILITY:
            mutated_solution[i] = 1 - mutated_solution[i]
    return mutated_solution

# Generate initial solution (creates a random solution)
def generate_solution():
    solution = []
    for i in range(len(ITEMS)):
        solution.append(random.randint(0, 1))
    return solution

# Draw knapsack function
def draw_knapsack(solution):
    SCREEN.fill((40, 40, 40))

    # Get the list of selected items from the solution
    selected_items = [ITEMS[i] for i in range(len(solution)) if solution[i] == 1]
    # If no items are selected, display the message and return
    if not selected_items:
        font = pygame.font.SysFont("arial", 20)
        text = font.render("No items selected", True, (255, 255, 255))
        SCREEN.blit(text, (20, 20))
        return

    total_weight = sum(item.weight for item in selected_items) # Calculate total weight of the selected items
    total_value = sum(item.value for item in selected_items) # Calculate total value of the selected items

    # Displays total value and total weight on the screen
    font = pygame.font.SysFont("arial", 20)
    text = font.render("Total value: {}".format(total_value), True, (255, 255, 255))
    SCREEN.blit(text, (20, 20))
    text = font.render("Total weight: {}".format(total_weight), True, (255, 255, 255))
    SCREEN.blit(text, (20, 50))

    # for drawing the items
    x = 50 # Initialize the x coordinate 
    y = 600 // 2 # Initialize the y coordinate 

    # Sets the maximum height, width, and color of the item bars
    max_height = 600 // 2 - 100
    bar_width = 800 - 100
    bar_height = max_height - len(selected_items) * 10
    bar_color = (70, 70, 70)

    pygame.draw.rect(SCREEN, bar_color, (x, y, bar_width, bar_height))  # Draw the background bar

     # Calculate the height, color, and spacing for each item
    item_heights = [int(item.weight / total_weight * max_height) for item in selected_items]
    item_colors = [(0, 100, 200), (200, 100, 0), (0, 200, 100), (200, 0, 100), (100, 0, 200)]
    item_spacings = [10] * len(selected_items)

    # To adjust the item heights and spacings to fit within the bar height
    while sum(item_heights) > bar_height:
        for i in range(len(item_heights)):
            if item_heights[i] > 10:
                item_heights[i] -= 10
                break
            elif item_spacings[i] > 1:
                item_spacings[i] -= 1
                break
            elif i == len(item_heights) - 1:
                item_heights[-1] -= 1

    # Draw the items as colored bars with labels attached
    for i, item in enumerate(selected_items):
        item_width = int(item.value / total_value * (bar_width - sum(item_spacings)))
        item_color = item_colors[i % len(item_colors)]
        item_rect = (x, y - item_heights[i], item_width, item_heights[i])
        pygame.draw.rect(SCREEN, item_color, item_rect)

        # Display the item's value as a label above the bar
        item_label = font.render(str(item.value), True, (255, 255, 255))
        SCREEN.blit(item_label, (item_rect[0] + item_rect[2] // 2 - item_label.get_width() // 2, item_rect[1] - 20))

        x += item_width + item_spacings[i]


# Main function
def main():
    global ITEMS, CAPACITY, POPULATION_SIZE, NUM_GENERATIONS, MUTATION_PROBABILITY
    # Items and their properties (name, value, weight)
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

    # Problem parameters
    CAPACITY = 20
    POPULATION_SIZE = 50
    NUM_GENERATIONS = 1000
    MUTATION_PROBABILITY = 0.1

    # Evolve the population through generations
    population = Population(POPULATION_SIZE)
    for generation in range(NUM_GENERATIONS):
        # selects parents from the population based on fitness
        parents = selection(population)
        offspring = []

        # Perform crossover and mutation to generate offspring
        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[i+1]
            child1, child2 = crossover(parent1, parent2)
            child1 = mutation(child1)
            child2 = mutation(child2)
            offspring.append(child1)
            offspring.append(child2)

        # Replace the old population with the offspring
        population.solutions = offspring

        # Find the best solution within the current population
        best_solution = max(population.solutions, key=fitness)

        # Calculates the total value and weight of the best solution
        total_value = 0
        total_weight = 0
        for i in range(len(best_solution)):
            if best_solution[i] == 1:
                total_value += ITEMS[i].value
                total_weight += ITEMS[i].weight

        # Print the best solution with value and weight        
        print("Best solution found: ", best_solution)
        print("Total value: ", total_value)
        print("Total weight: ", total_weight)
        draw_knapsack(best_solution)
        pygame.display.update()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                

    pygame.display.update()
    time.sleep(30)

if __name__ == "__main__":
    main()


# The constraints for the knapsack problem are the maximum capacity of the knapsack and the weight of the items
# The fitness function enforces this constraint by checking if the total weight of the items in a solution exceeds the maximum capacity

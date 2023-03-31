import pygame
import random
import sys

# Constants
BOARD_SIZE = 8
POPULATION_SIZE = 100
MUTATION_RATE = 0.1
WINDOW_SIZE = (480, 480)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
RED = (255, 0, 0)
ELITISM_COUNT = 2 # Elitism -> per
max_iterations = 1000

# Load the queen image
queen_image = pygame.image.load('queen1.png')
queen_image = pygame.transform.scale(queen_image, (WINDOW_SIZE[0] // BOARD_SIZE, WINDOW_SIZE[1] // BOARD_SIZE))

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("N-Queens Problem with Genetic Algorithm")

# Define the fitness function
def fitness(chromosome):
    conflicts = 0
    for i in range(BOARD_SIZE):
        for j in range(i + 1, BOARD_SIZE):
            if chromosome[i] == chromosome[j]:
                conflicts += 1
            elif abs(chromosome[i] - chromosome[j]) == j - i:
                conflicts += 1
    return 1 / (conflicts + 1)

# Define the selection function
def selection(population):
    # Roulette wheel selection
    fitness_sum = sum(fitness(chromosome) for chromosome in population)
    selection_probs = [fitness(chromosome) / fitness_sum for chromosome in population]
    parent1 = random.choices(population, weights=selection_probs)[0]
    parent2 = random.choices(population, weights=selection_probs)[0]
    return parent1, parent2

# Define the crossover function
def crossover(parent1, parent2):
    # Single-point crossover
    crossover_point = random.randint(1, BOARD_SIZE - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Define the mutation function
def mutation(chromosome):
    # Convert the chromosome tuple to a list
    chromosome = list(chromosome)
    
    # Swap two random positions in the chromosome
    i = random.randint(0, BOARD_SIZE - 1)
    j = random.randint(0, BOARD_SIZE - 1)
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    
    # Convert the chromosome list back to a tuple and return it
    return tuple(chromosome)


# Generate the initial population
population = [tuple(random.randint(0, BOARD_SIZE - 1) for i in range(BOARD_SIZE)) for j in range(POPULATION_SIZE)]


# Initialize font system
pygame.font.init()
font = pygame.font.Font(None, 36)  # Choose the font and size

# Main loop
def main():
    iteration_counter = 0
    global population

    while iteration_counter < max_iterations:
        # Check if the user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        iteration_counter += 1
        # Run one iteration of the genetic algorithm
        # Select two parents
        parent1, parent2 = selection(population)

        # Create two children through crossover
        child1, child2 = crossover(parent1, parent2)

        # Mutate the children
        child1 = mutation(child1)
        child2 = mutation(child2)

        # Replace two least fit chromosomes with the children
        population = sorted(population, key=lambda chromosome: fitness(chromosome))
        population = population[:ELITISM_COUNT] + population[ELITISM_COUNT + 2:] # preserving the best chromosomes (elitism)
        population.append(child1)
        population.append(child2)

        # Draw the chessboard and the best candidate
        square_size = WINDOW_SIZE[0] // BOARD_SIZE
        screen.fill(WHITE)

        # Draw the chessboard
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if (i + j) % 2 == 0:
                    color = BROWN
                else:
                    color = WHITE
                pygame.draw.rect(screen, color, (i * square_size, j * square_size, square_size, square_size))

        # Draw the queens for the best candidate
        best_chromosome = max(population, key=lambda c: fitness(c))
        for i in range(BOARD_SIZE):
            screen.blit(queen_image, (i * square_size, best_chromosome[i] * square_size))
        
        iteration_counter += 1
        iteration_text = font.render(f"Iteration: {iteration_counter}", True, BLACK)
        screen.blit(iteration_text, (10, 10))  # Position the text in the top-left corner
        # Update the Pygame display
        pygame.display.update()

        # Check if a solution has been found
        if iteration_counter >= max_iterations:
            pygame.time.wait(5000)  # Wait 5 seconds before restarting
            break

        # Wait for a short amount of time to control the frame rate
        pygame.time.wait(100)  # Increase the delay to 100 ms for easier observation

if __name__ == "__main__":
    main()

# from experimentation it can be seen that whilst a ga can be usd to solve the n-queen problem it may not always be optimal with the iterations often surpassing 1000.
# It is worth noting that this program has some constraints that can affect its performance and efficiency in solving the N-Queens problem
# have added an ELITISM  to control the number of best chromosomes to preserve
# This will help ensure that the best solution found so far is not lost due to selection, crossover, or mutation.

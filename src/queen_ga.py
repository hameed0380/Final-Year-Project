import pygame
import random
import sys
import numpy as np

# Constants
board = 8
population_size = 100
mutation_rate = 0.1
size_window = (480, 480)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
brown = (139, 69, 19)
elitism_cnt = 2 # Elitism -> per
max_iterations = 1000
k = 2 # tournament size

# Load the queen image adn scale to tile
queen_image = pygame.image.load('queen1.png')
queen_image = pygame.transform.scale(queen_image, (size_window[0] // board, size_window[1] // board))

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("N-Queens Problem with Genetic Algorithm")

# computes score for each chromosome(solution) in the population
def fitness(solutions):
    threat = 0 # threat counter
    # Count for when pieces threaten each other
    for i in range(board):
        for j in range(i + 1, board):
            if solutions[i] == solutions[j]:
                threat += 1
            elif abs(solutions[i] - solutions[j]) == j - i:
                threat += 1
    return 1 / (threat + 1)


def selection(population, k):
    # k individuals from population selected and perform a tournament amongst them
    tournament = random.sample(population, k)
    parent_a = max(tournament, key=lambda solutions: fitness(solutions))
    tournament = random.sample(population, k)
    parent_b = max(tournament, key=lambda solutions: fitness(solutions))
    return parent_a, parent_b

# Single point crossover function combines two parent to create two offspring solutions (recycled)
# crossover point randomly generated which determines the point for exchange of information between parents to form offspring
def crossover(parent_a, parent_b):
    x = random.randint(1, len(parent_a)-1)
    Offspring1 = np.append(parent_a[:x] , parent_b[x:])
    Offspring2 = np.append(parent_b[:x] , parent_a[x:])
    return Offspring1, Offspring2

# Define the mutation function
def mutation(solutions):
    # Convert the solutions tuple to a list
    solutions = list(solutions)
    
    # Swap two random positions in the solutions
    i = random.randint(0, board - 1)
    j = random.randint(0, board - 1)
    solutions[i], solutions[j] = solutions[j], solutions[i]
    
    # Convert the solutions list back to a tuple and return it
    return tuple(solutions)


# Generate the initial population
population = [tuple(random.randint(0, board - 1) for i in range(board)) for j in range(population_size)]


# Initialize font system
pygame.font.init()
font = pygame.font.Font(None, 36)  # Choose the font and size

# Main loop to run ga
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
        parent_a, parent_b = selection(population, k)

        # Create two children through crossover
        Offspring1, Offspring2 = crossover(parent_a, parent_b)

        # Mutate the children
        Offspring1 = mutation(Offspring1)
        Offspring2 = mutation(Offspring2)

        # Replace two least fit solutionss with the children
        population = sorted(population, key=lambda solutions: fitness(solutions))
        population = population[:elitism_cnt] + population[elitism_cnt + 2:] # preserving the best solutionss (elitism)
        population.append(Offspring1)
        population.append(Offspring2)

        # Draw the chessboard and the best candidate
        square_size = size_window[0] // board
        screen.fill(white)

        # Draw the chessboard
        for i in range(board):
            for j in range(board):
                if (i + j) % 2 == 0:
                    color = brown
                else:
                    color = white
                pygame.draw.rect(screen, color, (i * square_size, j * square_size, square_size, square_size))

        # Draw the queens for the best candidate
        best_solutions = max(population, key=lambda c: fitness(c))
        for i in range(board):
            screen.blit(queen_image, (i * square_size, best_solutions[i] * square_size))
        
        iteration_counter += 1
        iteration_text = font.render(f"Iteration: {iteration_counter}", True, black)
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
# have added an ELITISM  to control the number of best solutionss to preserve
# This will help ensure that the best solution found so far is not lost due to selection, crossover, or mutation.

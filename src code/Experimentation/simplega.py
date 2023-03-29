# A simple genetic algorithm to satisfy the expression below in th function foo
# ref https://www.youtube.com/watch?v=4XZoVQOt-0I

import random
import matplotlib.pyplot as plt

# The function to be optimized
def foo(x,y,z):
    return 6*x**3 + 9*y**2 + 90*z - 25

# Fitness function to calculate the closeness of the solution to the target value
def fitness(x,y,z):
    ans = foo(x,y,z)

    # Return a high fitness value for a solution that satisfies the target value
    if ans == 0:
        return 99999
    else:
        # Return a value proportional to the inverse of the absolute value of the solution 
        return abs(1/ans)


# Generate the initial population of 1000 solutions
solutions = []
for s in range(1000):
    solutions.append( (random.uniform(0,10000), random.uniform(0,10000), random.uniform(0,1000)))

# Initialize variables for the plot
best_solutions = []
generation_nums = []

# Run the genetic algorithm for 10000 generations
for i in range(10000):

    # Evaluate the fitness of all solutions in the current population
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append( (fitness(s[0],s[1],s[2]),s) )
        
    # Sort the solutions based on their fitness in descending order
    rankedsolutions.sort()
    rankedsolutions.reverse()
    
    # Print the best solution of the current generation
    print(f"=== Gen {i} best solutions === ")
    print(rankedsolutions[0])

    # Add the best solution of the current generation to the plot variables
    best_solutions.append(rankedsolutions[0][0])
    generation_nums.append(i)

    # Exit the loop if the best solution satisfies the target value
    if rankedsolutions[0][0] > 999:
        break	

    # Select the top 100 solutions from the current population
    bestsolutions = rankedsolutions[:100]

    # Extract the elements of the best solutions
    elements = []
    for s in bestsolutions:
        elements.append(s[1][0])
        elements.append(s[1][1])
        elements.append(s[1][2])

    # Create a new generation of 1000 solutions by mutating the elements of the best solutions
    newGen = []
    for _ in range(1000):
        e1 = random.choice(elements) * random.uniform(0.99,1.01)
        e2 = random.choice(elements) * random.uniform(0.99,1.01)
        e3 = random.choice(elements) * random.uniform(0.99,1.01)

        # Add the mutated solution to the new generation
        newGen.append( (e1,e2,e3) )

    # Set the current population to the new generation
    solutions = newGen

# Plot the fitness of the best solution over time
plt.plot(generation_nums, best_solutions)
plt.xlabel('Generation')
plt.ylabel('Fitness of Best Solution')
plt.title('Genetic Algorithm Performance')
plt.show()

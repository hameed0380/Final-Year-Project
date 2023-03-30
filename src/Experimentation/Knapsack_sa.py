# I took some inspiration from: https://machinelearningmastery.com/simulated-annealing-from-scratch-in-python/

# Imports
import random
import math
import matplotlib.pyplot as plt


# generate a random initial state
def gen_initial_state():
    return [random.randint(0, 1) for i in range(len(items))]


# calculate the value of a state
def value(state):
    total_value = sum(state[i]*items[i][1] for i in range(len(state)))
    total_weight = sum(state[i]*items[i][0] for i in range(len(state)))
    if total_weight > max_weight:
        return 0
    else:
        return total_value


# generate a new neighbor state
def neighbor(state):
    new_state = state.copy() # returns a copy of state 
    index = random.randint(0, len(state)-1)
    new_state[index] = 1 - new_state[index]  # flip bit
    return new_state


# probability of accepting a worse solution
def acceptance_probability(delta, temperature):
    if delta <= 0:
        return 1.0
    else:
        return math.exp(-delta / temperature)


# simulated annealing algorithm
def simulated_annealing():
    current_state = gen_initial_state()
    best_state = current_state.copy()
    temperature = 100.0
    cooling_rate = 0.03
    values = [value(current_state)]

    # Tested for 400 iterations as it seems to solve it in this time.
    for i in range(400):
        new_state = neighbor(current_state) # carrying out the different stages
        current_value = value(current_state)
        new_value = value(new_state)
        delta = new_value - current_value
        if acceptance_probability(delta, temperature) > random.uniform(0, 1):
            current_state = new_state
            if current_value > value(best_state):
                best_state = current_state
        temperature *= 1 - cooling_rate
        values.append(value(best_state))
    return values


# items that can be put in the knapsack
items = [
    [1, 2],
    [2, 4],
    [3, 4],
    [4, 5],
    [5, 7],
    [6, 9]
]

# parameters for simulated annealing algorithm
max_weight = 10

# run simulated annealing and get the best state and its value
values = simulated_annealing()
best_value = max(values)

# print the best solution
print("The best solution:")
print("Value:", best_value)

# plot the performance of simulated annealing over time so it can be used for comparison later on
plt.plot(values)
plt.xlabel("Iterations")
plt.ylabel("Value")
plt.title("Simulated Annealing Performance over Time")
plt.show()
# From testing it is important to note the  an element of randomness is involved and as such the plot often changes.

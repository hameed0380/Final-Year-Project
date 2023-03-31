import numpy as np

class GenAlgorithm:
    """GenAlgorithm class - provides the core functionality"""
    def __init__(self, var_count, pop_size, precision, crossover_prob, mutation_prob, start, end, max_iterations):
        self.var_count = var_count
        self.pop_size = pop_size
        self.precision = float(precision)
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.start = start
        self.end = end
        self.max_iterations = max_iterations


    def create_population(self):
        """Generates a random population"""
        return np.random.randint(2, size=(self.pop_size, self.var_count * self.end))

    # Tried to implement constraints but due to time constraints couldn't finish
    def constraint_penalty(self, x):
        """Method returns the penalty term based on the constraints"""
        g1 = x[0] + x[1] - 10  # example constraint g1(x) = x1 + x2 - 10 <= 0
        g2 = 20 - x[0] - x[1]  # example constraint g2(x) = 20 - x1 - x2 <= 0

        penalty = 0
        if g1 > 0:
            penalty += g1
        if g2 > 0:
            penalty += g2

        return penalty

    @staticmethod
    def objective_function(x, formula):
        """Evaluates the objective function at the given point (x1, x2)"""
        x1, x2 = x
        return eval(formula)

    @staticmethod
    def selection(pop, eval_pop):
        """Performs selection using the roulette wheel method"""
        # Reverse the evaluation scores and adjust if necessary
        eval_pop = -1 * eval_pop
        if eval_pop.min() < 0:
            eval_pop += np.abs(eval_pop.min()) + 1

        # Calculate selection probabilities
        selection_probs = np.array(eval_pop / np.sum(eval_pop))
        new_pop = np.array(pop[np.random.choice(pop.shape[0], len(pop), replace=True, p=selection_probs), :]) # Perform roulette wheel selection to create the new population

        # Return the updated population
        return new_pop


    @staticmethod
    def crossover(pop, crossover_prob):
        """Performs crossover on the population"""
        # Iterate through pairs of individuals in the population
        for idx in range(int(len(pop) / 2)):
            
            # Check if crossover should be performed based on the crossover probability
            if np.random.choice([0, 1], p=[1 - crossover_prob, crossover_prob]):
                
                # Select a random crossover point
                crossover_point = np.random.randint(1, len(pop[0]))
                
                # Perform crossover between two individuals and create offspring
                offspring1 = np.append(pop[2 * idx][:crossover_point], pop[2 * idx + 1][crossover_point:])
                offspring2 = np.append(pop[2 * idx + 1][:crossover_point], pop[2 * idx][crossover_point:])
                
                # Replace the original individuals with the new offspring
                pop[2 * idx] = offspring1
                pop[2 * idx + 1] = offspring2

        return pop

    @staticmethod
    def mutation(population, mutation_rate):
        """Performs mutation on the population"""
        # Generate a probability matrix for mutation
        mutation_prob = np.random.choice([1, 0], size=(len(population), len(population[0])), p=[mutation_rate, 1 - mutation_rate])

        # Perform mutation by XORing the population with the probability matrix
        mutated_pop = np.logical_xor(population, mutation_prob).astype(int)
        return mutated_pop

    def bit_count(self):
        """Determines the number of bits needed for each individual"""
        # Compute range length and the number of values it can represent
        range_length = (self.end - self.start) / self.precision + 1

        min_bits = int(np.ceil(range_length / self.precision)).bit_length() # the minimum number of bits required
        
        # Calculate the new precision based on the minimum number of bits
        adjusted_precision = (self.end - self.start) / (2 ** min_bits - 1)
        return min_bits, adjusted_precision

    def binary_to_decimal(self, individual):
        """Translates a binary individual into decimal format"""
        # Divide the input individual into equal segments based on the variable count
        segments = np.array_split(individual, self.var_count)

        # Process each segment to obtain decimal values
        decimal_values = []
        for segment in segments:
            
            # Convert the binary segment into a string and eliminate unnecessary characters
            str_segment = np.array2string(segment, separator="").strip("[]")
            str_segment = str_segment.replace("\n ", "")

            # Calculate the decimal equivalent of the binary string
            decimal_value = self.start + (int(str_segment, 2) * self.precision)
            decimal_values.append(decimal_value) # Append the decimal value to the list

        # Return the list of decimal values
        return decimal_values

    def assess_population(self, func, population, evaluation_function):
        """Evaluates the fitness of the population"""
        return np.apply_along_axis(func, -1,
                                np.apply_along_axis(self.binary_to_decimal, 1, population), evaluation_function) # Convert the binary population to decimal and apply the fitness function
    
    @staticmethod
    def find_best(population, evaluated_population):
        """Finds the best individual in the population"""
        # Determine the best fitness score and its index
        optimal_value = np.min(evaluated_population)
        optimal_idx = np.where(evaluated_population == optimal_value)

        # Extract the best individual from the population
        top_individual = population[optimal_idx[0]]

        # Return the best individual and its fitness value
        return *top_individual, optimal_value


# Not sure the particular video but I borrowed some ideas from here: https://www.youtube.com/watch?v=JWPgodXQLV4
# MATLAB: https://uk.mathworks.com/help/gads/gamultiobj-plot-vectorize.html


# def main():
#     var_count = 2
#     pop_size = 100
#     precision = 0.01
#     crossover_prob = 0.8
#     mutation_prob = 0.1
#     start t = -5.12
# #     end = 5.12
# #     max_iterations = 1000

# #     ga = GenAlgorithm(var_count, pop_size, precision, crossover_prob, mutation_prob, start, end, max_iterations)

# #     population = ga= -5.12
#     end = 5.12
#     max_iterations = 1000

#     ga = GenAlgorithm(var_count, pop_size, precision, crossover_prob, mutation_prob, start, end, max_iterations)

#     best_individual, best_value = run_genetic_algorithm(ga, max_iterations)
#     print("\nFinal Result:")
#     print(f"Best Individual: {best_individual}, Best Value: {best_value}")

# if __name__ == "__main__":
#     main()



# # def main():
# #     var_count = 2
# #     pop_size = 100
# #     precision = 0.01
# #     crossover_prob = 0.8
# #     mutation_prob = 0.1
# #     star

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

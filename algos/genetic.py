import random

def solve_tsp(matrix, params):
    n = len(matrix)

    def calculate_cost(path):
        return sum(matrix[path[i]][path[i + 1]] for i in range(len(path) - 1)) + matrix[path[-1]][path[0]]

    def create_individual():
        individual = list(range(1, n))
        random.shuffle(individual)
        return [0] + individual + [0]

    def mutate(individual):
        if random.random() < params["mutation_rate"]:
            i, j = random.sample(range(1, n), 2)
            individual[i], individual[j] = individual[j], individual[i]

    def crossover(parent1, parent2):
        start, end = sorted(random.sample(range(1, n), 2))
        child = [-1] * len(parent1)
        child[start:end] = parent1[start:end]
        pointer = 1
        for gene in parent2[1:-1]:
            if gene not in child:
                while child[pointer] != -1:
                    pointer += 1
                child[pointer] = gene
        return [0] + child[1:-1] + [0]

    # Initialize population
    population = [create_individual() for _ in range(params["population_size"])]
    best_individual = None
    best_cost = float('inf')

    for _ in range(params["num_generations"]):
        population = sorted(population, key=calculate_cost)
        if calculate_cost(population[0]) < best_cost:
            best_cost = calculate_cost(population[0])
            best_individual = population[0]

        # Elitism
        num_elites = int(params["elitism_rate"] * params["population_size"])
        new_population = population[:num_elites]

        # Crossover and mutation
        while len(new_population) < params["population_size"]:
            parent1, parent2 = random.sample(population[:50], 2)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)

        population = new_population

    return best_individual

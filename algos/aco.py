import random

def initialize_pheromone_matrix(n):
    """Initialize the pheromone matrix with uniform values."""
    return [[1.0 for _ in range(n)] for _ in range(n)]

def initialize_heuristic_matrix(matrix, n):
    """Initialize the heuristic matrix based on the distance matrix."""
    return [[0 if i == j else 1 / matrix[i][j] for j in range(n)] for i in range(n)]

def select_next_city(current, unvisited, pheromone, heuristic, params):
    """Select the next city based on pheromone and heuristic values."""
    probabilities = []
    for city in unvisited:
        tau = pheromone[current][city] ** params["alpha"]
        eta = heuristic[current][city] ** params["beta"]
        probabilities.append((city, tau * eta))

    total = sum(p[1] for p in probabilities)
    r = random.uniform(0, total)
    cumulative = 0

    for city, prob in probabilities:
        cumulative += prob
        if cumulative >= r:
            return city

def construct_solution(n, pheromone, heuristic, params):
    """Construct a single solution (path) using ACO."""
    path = [0]
    unvisited = set(range(1, n))

    while unvisited:
        current = path[-1]
        next_city = select_next_city(current, unvisited, pheromone, heuristic, params)
        path.append(next_city)
        unvisited.remove(next_city)

    path.append(0)  # return to the start city
    return path

def calculate_cost(path, matrix):
    """Calculate the cost of a given path."""
    return sum(matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))

def update_pheromone_matrix(pheromone, all_paths, all_costs, best_path, best_cost, params, n):
    """Update the pheromone matrix based on evaporation, reinforcement, and elitism."""
    # Evaporation
    for i in range(n):
        for j in range(n):
            pheromone[i][j] *= (1 - params["evaporation_rate"])

    # Reinforcement by all ants
    for k in range(len(all_paths)):
        path = all_paths[k]
        cost = all_costs[k]
        for i in range(len(path) - 1):
            a = path[i]
            b = path[i + 1]
            pheromone[a][b] += params["pheromone_constant"] / cost
            pheromone[b][a] = pheromone[a][b]

    # Elitist reinforcement (best path only)
    for i in range(len(best_path) - 1):
        a = best_path[i]
        b = best_path[i + 1]
        pheromone[a][b] += params["elitist_factor"] * (params["pheromone_constant"] / best_cost)
        pheromone[b][a] = pheromone[a][b]

def solve_tsp(matrix, params):
    """Solve the TSP problem using Ant Colony Optimization."""
    n = len(matrix)
    pheromone = initialize_pheromone_matrix(n)
    heuristic = initialize_heuristic_matrix(matrix, n)

    best_path = None
    best_cost = float('inf')

    for _ in range(params["num_iterations"]):
        all_paths = []
        all_costs = []

        # Simulate all ants' paths
        for _ in range(params["num_ants"]):
            path = construct_solution(n, pheromone, heuristic, params)
            cost = calculate_cost(path, matrix)
            all_paths.append(path)
            all_costs.append(cost)

            if cost < best_cost:
                best_cost = cost
                best_path = path

        # Update pheromone matrix
        update_pheromone_matrix(pheromone, all_paths, all_costs, best_path, best_cost, params, n)

    return best_path

import random

def solve_tsp(matrix, params):
    n = len(matrix)
    pheromone = [[params["pheromone_max"] for _ in range(n)] for _ in range(n)]
    heuristic = [[0 if i == j else 1 / matrix[i][j] for j in range(n)] for i in range(n)]

    best_path = None
    best_cost = float('inf')

    for _ in range(params["num_iterations"]):
        all_paths = []
        all_costs = []

        for _ in range(params["num_ants"]):
            path = [0]
            unvisited = set(range(1, n))

            while unvisited:
                current = path[-1]
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
                        path.append(city)
                        unvisited.remove(city)
                        break

            path.append(0)
            cost = sum(matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))
            all_paths.append(path)
            all_costs.append(cost)

            if cost < best_cost:
                best_cost = cost
                best_path = path

        # Evaporation
        for i in range(n):
            for j in range(n):
                pheromone[i][j] *= (1 - params["evaporation_rate"])

        # Reinforcement by best ant
        for i in range(len(best_path) - 1):
            a = best_path[i]
            b = best_path[i + 1]
            pheromone[a][b] += params["pheromone_constant"] / best_cost
            pheromone[b][a] = pheromone[a][b]  # symmetric TSP

        # Enforce pheromone limits
        for i in range(n):
            for j in range(n):
                pheromone[i][j] = max(params["pheromone_min"], min(params["pheromone_max"], pheromone[i][j]))

    return best_path

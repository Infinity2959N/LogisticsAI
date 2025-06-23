import json
import random

# ========== Block 1: Input Loader ==========
def load_input(filename="matrix.json"):
    with open(filename, "r") as file:
        data = json.load(file)
    return data["locations"], data["matrix"]

# ========== Block 2: EAS Configurable Parameters ==========
EAS_PARAMS = {
    "num_ants": 20,
    "num_iterations": 100,
    "alpha": 1.0,
    "beta": 5.0,
    "evaporation_rate": 0.5,
    "pheromone_constant": 100.0,
    "elitist_factor": 5  # Additional pheromone reinforcement for the best path
}

# ========== Block 3: Display Map ==========
def display_map(locations):
    print("Map of Nodes:")
    for index, location in enumerate(locations):
        print(f"Node {index}: {location}")
    print()

# ========== Block 4: Elitist Ant System Solver ==========
def solve_tsp(matrix, params):
    n = len(matrix)
    pheromone = [[1.0 for _ in range(n)] for _ in range(n)]
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

        # Reinforcement by all ants
        for k in range(len(all_paths)):
            path = all_paths[k]
            cost = all_costs[k]
            for i in range(len(path) - 1):
                a = path[i]
                b = path[i + 1]
                pheromone[a][b] += params["pheromone_constant"] / cost
                pheromone[b][a] = pheromone[a][b]  # symmetric TSP

        # Additional reinforcement by the best path (elitist ants)
        for i in range(len(best_path) - 1):
            a = best_path[i]
            b = best_path[i + 1]
            pheromone[a][b] += params["elitist_factor"] * (params["pheromone_constant"] / best_cost)
            pheromone[b][a] = pheromone[a][b]  # symmetric TSP

    return best_path

# ========== Block 5: Output Writer ==========
def save_output(path, locations, matrix, output_file="output.json"):
    total_time = sum(matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))
    result = {
        "route": [locations[i] for i in path],
        "indices": path,
        "total_time": round(total_time, 2)
    }
    with open(output_file, "w") as f:
        json.dump(result, f, indent=2)

    print("\nOptimal Route Found:")
    print(" -> ".join(result["route"]))
    print("Total Time:", result["total_time"], "mins")

# ========== Block 6: Main Driver ==========
if __name__ == "__main__":
    locations, matrix = load_input()
    display_map(locations)  # Display the map to the user
    path = solve_tsp(matrix, EAS_PARAMS)
    save_output(path, locations, matrix)

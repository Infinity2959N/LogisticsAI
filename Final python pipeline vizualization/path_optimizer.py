import requests
import time
import random
from typing import List, Dict

# API KEY directly passed from Flutter
def get_time_matrix(locations: List[str], api_key: str) -> List[List[int]]:
    n = len(locations)
    matrix = [[0] * n for _ in range(n)]
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    for i in range(n):
        origin = locations[i]
        for j in range(n):
            if i == j:
                matrix[i][j] = 0
                continue
            try:
                dest = locations[j]
                params = {
                    "origins": origin,
                    "destinations": dest,
                    "key": api_key,
                    "mode": "driving"
                }
                response = requests.get(url, params=params)
                data = response.json()
                if (data["status"] != "OK" or
                        data["rows"][0]["elements"][0]["status"] != "OK"):
                    raise Exception(f"Invalid API response for {origin} -> {dest}")
                seconds = data["rows"][0]["elements"][0]["duration"]["value"]
                matrix[i][j] = seconds
                time.sleep(1)  # To avoid rate-limiting
            except Exception as e:
                matrix[i][j] = 9999
    return matrix

EAS_PARAMS = {
    "num_ants": 20,
    "num_iterations": 100,
    "alpha": 1.0,
    "beta": 5.0,
    "evaporation_rate": 0.5,
    "pheromone_constant": 100.0,
    "elitist_factor": 5
}

def solve_tsp(matrix: List[List[int]], params: Dict) -> List[int]:
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
        for i in range(n):
            for j in range(n):
                pheromone[i][j] *= (1 - params["evaporation_rate"])
        for k in range(len(all_paths)):
            path = all_paths[k]
            cost = all_costs[k]
            for i in range(len(path) - 1):
                a = path[i]
                b = path[i + 1]
                pheromone[a][b] += params["pheromone_constant"] / cost
                pheromone[b][a] = pheromone[a][b]
        for i in range(len(best_path) - 1):
            a = best_path[i]
            b = best_path[i + 1]
            pheromone[a][b] += params["elitist_factor"] * (params["pheromone_constant"] / best_cost)
            pheromone[b][a] = pheromone[a][b]
    return best_path

# Main callable function from Flutter
def run_optimizer(input_data):
    locations = input_data.get("locations", [])
    api_key = input_data.get("key", "")
    if not locations or len(locations) < 2:
        return "Error: At least two locations required"

    matrix = get_time_matrix(locations, api_key)
    path = solve_tsp(matrix, EAS_PARAMS)
    route = [locations[i].replace(" ", "+") for i in path]

    # Return a URL-safe Google Maps path string
    return "/".join(route)
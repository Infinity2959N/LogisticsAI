import os
import time
import json
import csv

# Adjusted imports
from algos.aco import solve_tsp as solve_aco
from algos.elitist import solve_tsp as solve_elist
from algos.genetic import solve_tsp as solve_genetic
from algos.minmax import solve_tsp as solve_minmax

ACO_PARAMS = {
    "num_ants": 20,
    "num_iterations": 100,
    "alpha": 1.0,
    "beta": 5.0,
    "evaporation_rate": 0.5,
    "pheromone_constant": 100.0
}

EAS_PARAMS = {**ACO_PARAMS, "elitist_factor": 5}
MMAS_PARAMS = {**ACO_PARAMS, "pheromone_min": 0.1, "pheromone_max": 10.0}
GA_PARAMS = {
    "population_size": 100,
    "num_generations": 200,
    "mutation_rate": 0.1,
    "elitism_rate": 0.1
}

def load_data(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return data["locations"], data["matrix"]

def evaluate_algorithm(name, solver_func, matrix, params):
    start_time = time.time()
    path = solver_func(matrix, params)
    duration = round(time.time() - start_time, 4)
    cost = sum(matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))
    return {
        "algorithm": name,
        "cost": round(cost, 2),
        "time_sec": duration,
        "path": path
    }

def main():
    input_dir = "./Input_Data" 
    json_files = sorted([f for f in os.listdir(input_dir) if f.startswith("tsp_data_") and f.endswith(".json")])
    
    results = []
    
    for file in json_files:
        locations, matrix = load_data(os.path.join(input_dir, file))
        num_nodes = len(locations)

        for name, func, params in [
            ("ACO", solve_aco, ACO_PARAMS),
            ("EAS", solve_elist, EAS_PARAMS),
            ("MMAS", solve_minmax, MMAS_PARAMS),
            ("GA", solve_genetic, GA_PARAMS)
        ]:
            result = evaluate_algorithm(name, func, matrix, params)
            result.update({
                "filename": file,
                "num_nodes": num_nodes
            })
            results.append(result)
            print(f"Completed: {name} on {file} -> Cost: {result['cost']}, Time: {result['time_sec']}s")

    # Write CSV output
    with open("benchmark_results.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[
            "algorithm", "filename", "num_nodes", "cost", "time_sec", "path"
        ])
        writer.writeheader()
        for row in results:
            writer.writerow(row)

    print("\nBenchmarking complete. Results saved to benchmark_results.csv")

if __name__ == "__main__":
    main()

import json
import random
import os

def generate_tsp_data(num_locations, file_name):
    locations = ["Warehouse"] + [f"Point {chr(65 + i)}" for i in range(1, num_locations)]
    
    # Generate symmetric distance matrix with 0 on diagonals
    matrix = [[0]*num_locations for _ in range(num_locations)]
    for i in range(num_locations):
        for j in range(i+1, num_locations):
            distance = random.randint(10, 60)
            matrix[i][j] = matrix[j][i] = distance

    data = {
        "locations": locations,
        "matrix": matrix,
        "warehouse": 0
    }

    with open(file_name, "w") as f:
        json.dump(data, f, indent=2)

# Generate files for various location sizes
for n in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]:
    filename = f"tsp_data_{n}.json"
    generate_tsp_data(n, filename)
    print(f"Generated {filename}")

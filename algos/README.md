# 🧮 LogisticsAI Optimization Algorithms

This directory contains four metaheuristic algorithms specifically designed for solving the Traveling Salesman Problem (TSP) in logistics applications. Each algorithm offers unique strengths and is optimized for different scenarios.

## 📚 Algorithm Overview

| Algorithm | File | Type | Best Use Case | Key Advantages |
|-----------|------|------|---------------|----------------|
| **ACO** | `aco.py` | Ant Colony Optimization | Balanced performance | Natural parallelization, good exploration |
| **Genetic** | `genetic.py` | Evolutionary Algorithm | Complex landscapes | Population diversity, global search |
| **Elitist** | `elitist.py` | Enhanced ACO | High-quality solutions | Elite reinforcement, faster convergence |
| **MinMax** | `minmax.py` | Bounded ACO | Exploration control | Prevents stagnation, balanced search |

## 🐜 Ant Colony Optimization (ACO)

**File**: `aco.py`

Classic ACO implementation inspired by the foraging behavior of ants. Uses pheromone trails and heuristic information to construct solutions probabilistically.

### Key Features
- **Pheromone Matrix**: Stores learned information about good edges
- **Heuristic Matrix**: Uses inverse distance as attractiveness measure
- **Probabilistic Selection**: Balances exploration and exploitation
- **Evaporation**: Prevents premature convergence

### Parameters
```python
params = {
    "alpha": 1.0,      # Pheromone trail importance (τ^α)
    "beta": 2.0,       # Heuristic information importance (η^β)
    "rho": 0.1,        # Evaporation rate (1-ρ retention)
    "num_ants": 20,    # Colony size
    "iterations": 100  # Maximum iterations
}
```

### Algorithm Flow
1. Initialize pheromone and heuristic matrices
2. For each iteration:
   - Each ant constructs a complete tour
   - Calculate tour costs
   - Update pheromone trails based on solution quality
   - Apply evaporation to all edges

### Complexity
- **Time**: O(iterations × ants × n²)
- **Space**: O(n²)

## 🧬 Genetic Algorithm

**File**: `genetic.py`

Evolutionary approach that maintains a population of candidate solutions and evolves them through selection, crossover, and mutation operations.

### Key Features
- **Population-based**: Maintains diverse solution set
- **Order Crossover (OX)**: Preserves city order in offspring
- **Swap Mutation**: Random city pair exchanges
- **Tournament Selection**: Competitive selection pressure

### Parameters
```python
params = {
    "population_size": 50,    # Number of individuals
    "generations": 100,       # Evolution cycles
    "mutation_rate": 0.02,    # Probability of mutation
    "elite_size": 20,         # Top performers retained
    "tournament_size": 5      # Selection competition size
}
```

### Algorithm Flow
1. Initialize random population
2. For each generation:
   - Evaluate fitness (inverse of tour cost)
   - Select parents using tournament selection
   - Create offspring through crossover
   - Apply mutation to maintain diversity
   - Replace population with elite + offspring

### Complexity
- **Time**: O(generations × population × n²)
- **Space**: O(population × n)

## 👑 Elitist ACO

**File**: `elitist.py`

Enhanced ACO variant that gives additional pheromone reinforcement to the best solution found so far, accelerating convergence to high-quality solutions.

### Key Features
- **Elite Reinforcement**: Best-so-far solution gets extra pheromone
- **Dual Updates**: Regular ant updates + elite ant updates
- **Faster Convergence**: Quicker identification of good regions
- **Quality Focus**: Emphasizes exploitation of best solutions

### Parameters
```python
params = {
    "alpha": 1.0,           # Pheromone importance
    "beta": 2.0,            # Heuristic importance  
    "rho": 0.1,             # Evaporation rate
    "num_ants": 20,         # Colony size
    "iterations": 100,      # Maximum iterations
    "elite_weight": 2.0     # Elite solution reinforcement factor
}
```

### Algorithm Flow
1. Standard ACO initialization
2. For each iteration:
   - Ants construct solutions normally
   - Apply standard pheromone updates
   - **Additional**: Elite ant deposits extra pheromone on best-so-far tour
   - Track and update global best solution

### Complexity
- **Time**: O(iterations × ants × n²)
- **Space**: O(n²)

## ⚖️ MinMax ACO

**File**: `minmax.py`

ACO variant that imposes bounds on pheromone values to prevent premature convergence and maintain exploration throughout the search process.

### Key Features
- **Pheromone Bounds**: τ_min ≤ τ_ij ≤ τ_max
- **Stagnation Prevention**: Maintains minimum exploration
- **Only Best Updates**: Only iteration-best or global-best ants deposit pheromone
- **Reinitialization**: Periodic restart when stagnation detected

### Parameters
```python
params = {
    "alpha": 1.0,           # Pheromone importance
    "beta": 2.0,            # Heuristic importance
    "rho": 0.02,            # Evaporation rate (typically smaller)
    "num_ants": 20,         # Colony size
    "iterations": 100,      # Maximum iterations
    "tau_max": 1.0,         # Maximum pheromone value
    "tau_min": 0.01         # Minimum pheromone value
}
```

### Algorithm Flow
1. Initialize pheromones to τ_max
2. For each iteration:
   - Ants construct solutions
   - Only best ant updates pheromones
   - Apply evaporation
   - **Clamp pheromones**: Enforce τ_min ≤ τ_ij ≤ τ_max
   - Check for stagnation and reinitialize if needed

### Complexity
- **Time**: O(iterations × ants × n²)
- **Space**: O(n²)

## 🔧 Usage Examples

### Basic Usage
```python
import json
from aco import solve_tsp as aco_solve
from genetic import solve_tsp as genetic_solve
from elitist import solve_tsp as elitist_solve
from minmax import solve_tsp as minmax_solve

# Load TSP data
with open('tsp_data_20.json', 'r') as f:
    data = json.load(f)

matrix = data['matrix']
params = {
    "alpha": 1.0,
    "beta": 2.0,
    "rho": 0.1,
    "num_ants": 20,
    "iterations": 100
}

# Run different algorithms
aco_result = aco_solve(matrix, params)
genetic_result = genetic_solve(matrix, params)
elitist_result = elitist_solve(matrix, params)
minmax_result = minmax_solve(matrix, params)

print(f"ACO Best Cost: {aco_result['best_cost']}")
print(f"Genetic Best Cost: {genetic_result['best_cost']}")
print(f"Elitist Best Cost: {elitist_result['best_cost']}")
print(f"MinMax Best Cost: {minmax_result['best_cost']}")
```

### Parameter Tuning Guidelines

#### ACO Parameters
- **α (alpha)**: Higher values favor pheromone trails (exploitation)
- **β (beta)**: Higher values favor heuristic information (short edges)
- **ρ (rho)**: Higher evaporation rates increase exploration
- **num_ants**: More ants provide better exploration but increase computation

#### Genetic Parameters
- **population_size**: Larger populations maintain more diversity
- **mutation_rate**: Balance between exploration (high) and exploitation (low)
- **elite_size**: Higher values preserve good solutions but may reduce diversity

## 📊 Performance Characteristics

### Convergence Behavior
- **ACO**: Gradual improvement with occasional plateaus
- **Genetic**: Rapid initial improvement, then gradual refinement
- **Elitist**: Fast convergence, risk of premature optimization
- **MinMax**: Steady exploration with maintained diversity

### Problem Size Scalability
- **Small (5-15 cities)**: All algorithms perform well
- **Medium (20-35 cities)**: ACO variants show advantages
- **Large (40+ cities)**: MinMax and Genetic maintain better exploration

### Computational Efficiency
- **Fastest**: Basic ACO (simple operations)
- **Moderate**: Elitist and MinMax ACO (additional bookkeeping)
- **Slowest**: Genetic Algorithm (population management overhead)

## 🔍 Algorithm Selection Guide

Choose your algorithm based on:

| Scenario | Recommended Algorithm | Reason |
|----------|----------------------|---------|
| **Quick solution needed** | ACO | Fast convergence, simple implementation |
| **Best quality required** | Elitist ACO | Superior solution quality |
| **Large problem instances** | MinMax ACO | Better exploration, avoids stagnation |
| **Unknown problem landscape** | Genetic Algorithm | Robust across diverse problems |
| **Real-time applications** | ACO | Predictable runtime, anytime algorithm |

## 🧪 Testing and Validation

All algorithms are validated using:
- **Synthetic TSP instances** (5-60 cities)
- **Benchmark comparison** against known optimal solutions
- **Statistical significance testing** across multiple runs
- **Runtime performance analysis**

See the `Algorithm Testing/` directory for comprehensive benchmarking results.

## 🔗 References

1. Dorigo, M., & Gambardella, L. M. (1997). Ant colony system: a cooperative learning approach to the traveling salesman problem.
2. Holland, J. H. (1992). Adaptation in natural and artificial systems.
3. Stützle, T., & Hoos, H. H. (2000). MAX–MIN ant system.
4. Dorigo, M., & Stützle, T. (2004). Ant colony optimization.

## 👨‍💻 Author

**Bhavesh (B Infinity)**
- GitHub: [@Infinity2959N](https://github.com/Infinity2959N)
- Email: [binfinity321@gmail.com](mailto:binfinity321@gmail.com)

---

**Note**: These implementations are optimized for educational purposes and practical logistics applications. For production use, consider additional optimizations like parallel processing and adaptive parameter control.

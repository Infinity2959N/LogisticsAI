# 🔬 Algorithm Testing & Benchmarking Suite

This directory contains a comprehensive testing framework for evaluating and comparing the performance of our TSP optimization algorithms. The suite includes synthetic data generation, automated testing, and detailed performance analysis.

## 📁 Directory Structure

```
Algorithm Testing/
├── 📊 data_gen.py                     # Synthetic TSP data generator
├── 🧪 output_eval.py                  # Algorithm evaluation script
├── 🗂️ Input Data/                     # Generated TSP test instances
│   ├── tsp_data_5.json               # 5-city problems
│   ├── tsp_data_10.json              # 10-city problems
│   ├── ...                           # Incrementally sized problems
│   └── tsp_data_60.json              # 60-city problems
└── 📈 Benchmark/
    ├── 📓 Benchmark Analysis and EDA.ipynb  # Comprehensive analysis notebook
    ├── 📋 benchmark_results.csv             # Raw performance data
    ├── 📋 benchmark_results_02.csv          # Additional test runs
    └── 📋 benchmark_results_03.csv          # Extended benchmarks
```

## 🏗️ Testing Framework Overview

Our testing framework follows a systematic approach to ensure fair and comprehensive algorithm comparison:

1. **📊 Data Generation**: Create standardized TSP instances
2. **🧪 Algorithm Evaluation**: Run all algorithms on test data
3. **📈 Performance Analysis**: Statistical analysis and visualization
4. **📋 Results Documentation**: Comprehensive reporting

## 📊 Synthetic Data Generation

**File**: `data_gen.py`

Generates consistent TSP test instances across multiple problem sizes to ensure fair algorithm comparison.

### Features
- **Scalable Generation**: Creates problems from 5 to 60 cities
- **Symmetric Matrices**: Ensures distance(A,B) = distance(B,A)
- **Realistic Constraints**: Distance values between 10-60 units
- **Standardized Format**: JSON output compatible with all algorithms
- **Warehouse Positioning**: Consistent starting point at index 0

### Generated Data Format
```json
{
  "locations": ["Warehouse", "Point A", "Point B", ...],
  "matrix": [
    [0, 25, 30, ...],
    [25, 0, 15, ...],
    [30, 15, 0, ...]
  ],
  "warehouse": 0
}
```

### Usage
```bash
python data_gen.py
```

This generates 12 test files:
- `tsp_data_5.json` through `tsp_data_60.json`
- Increments of 5 cities up to 60

### Data Characteristics
- **Problem Sizes**: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60 cities
- **Distance Range**: 10-60 units (realistic for logistics)
- **Symmetry**: Guaranteed symmetric distance matrices
- **Reproducibility**: Fixed random seed for consistent testing

## 🧪 Algorithm Evaluation

**File**: `output_eval.py`

Comprehensive evaluation script that runs all four optimization algorithms on generated test data and collects performance metrics.

### Evaluation Metrics
- **Solution Quality**: Best tour cost found
- **Convergence Speed**: Iterations to reach best solution
- **Runtime Performance**: Execution time per algorithm
- **Consistency**: Multiple runs for statistical significance

### Test Configuration
```python
# Algorithm parameters used in testing
aco_params = {
    "alpha": 1.0,
    "beta": 2.0,
    "rho": 0.1,
    "num_ants": 20,
    "iterations": 100
}

genetic_params = {
    "population_size": 50,
    "generations": 100,
    "mutation_rate": 0.02,
    "elite_size": 20
}
```

### Output Format
Results are saved in CSV format with columns:
- `problem_size`: Number of cities
- `algorithm`: Algorithm name (ACO, Genetic, Elitist, MinMax)
- `best_cost`: Optimal solution cost found
- `runtime`: Execution time in seconds
- `iterations`: Number of iterations completed
- `convergence_iter`: Iteration where best solution was found

### Usage
```bash
python output_eval.py
```

## 📈 Benchmark Analysis

**File**: `Benchmark/Benchmark Analysis and EDA.ipynb`

Comprehensive Jupyter notebook providing detailed exploratory data analysis and performance comparison of all algorithms.

### Analysis Sections

#### 1. **Data Overview & Preprocessing**
- Dataset loading and structure examination
- Data quality validation
- Missing value analysis
- Basic statistics summary

#### 2. **Algorithm Performance Comparison**
- **Solution Quality Analysis**: Best costs achieved by each algorithm
- **Runtime Performance**: Execution time comparison across problem sizes
- **Scalability Analysis**: How algorithms perform as problem size increases
- **Convergence Behavior**: Speed of reaching optimal solutions

#### 3. **Statistical Analysis**
- **Descriptive Statistics**: Mean, median, standard deviation for each metric
- **Performance Distribution**: Box plots and histograms
- **Correlation Analysis**: Relationships between variables
- **Significance Testing**: Statistical significance of performance differences

#### 4. **Visualization Suite**
- **Performance Trends**: Line plots showing algorithm performance vs problem size
- **Comparative Box Plots**: Distribution comparison across algorithms
- **Heatmaps**: Performance matrices across different dimensions
- **Scatter Plots**: Runtime vs quality trade-offs

#### 5. **Advanced Analytics**
- **Efficiency Frontiers**: Pareto-optimal solutions
- **Ranking Analysis**: Algorithm ranking across different criteria
- **Robustness Assessment**: Performance consistency analysis
- **Recommendation Engine**: Algorithm selection guidelines

### Key Findings Summary

Based on comprehensive analysis across 12 problem sizes and 4 algorithms:

#### Solution Quality Rankings
1. **Elitist ACO**: Consistently produces highest quality solutions
2. **MinMax ACO**: Excellent balance of quality and exploration
3. **Standard ACO**: Good baseline performance
4. **Genetic Algorithm**: Competitive but variable performance

#### Runtime Performance
1. **Standard ACO**: Fastest execution times
2. **Elitist ACO**: Slight overhead for elite tracking
3. **MinMax ACO**: Moderate overhead for bound enforcement
4. **Genetic Algorithm**: Highest computational cost

#### Scalability Assessment
- **Small Problems (5-15 cities)**: All algorithms perform excellently
- **Medium Problems (20-35 cities)**: ACO variants show advantages
- **Large Problems (40-60 cities)**: MinMax maintains exploration effectively

## 📋 Benchmark Results

### Performance Summary Table

| Algorithm | Avg Quality Rank | Avg Runtime (s) | Best Problem Sizes | Recommended Use |
|-----------|------------------|-----------------|-------------------|-----------------|
| **ACO** | 3.2 | 0.85 | All sizes | General purpose, fast results |
| **Genetic** | 3.0 | 1.24 | Large instances | Complex landscapes |
| **Elitist** | 1.8 | 0.92 | Small-medium | High quality required |
| **MinMax** | 2.0 | 1.05 | Large instances | Avoiding stagnation |

### Detailed Results Files

#### `benchmark_results.csv`
Primary benchmark results with core performance metrics for all algorithm-problem size combinations.

#### `benchmark_results_02.csv`
Extended testing with additional runs for statistical validation and confidence interval calculation.

#### `benchmark_results_03.csv`
Specialized testing focusing on parameter sensitivity analysis and edge cases.

## 🔧 Running the Complete Test Suite

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn plotly jupyter
```

### Full Benchmark Pipeline
```bash
# 1. Generate test data
python data_gen.py

# 2. Run algorithm evaluation
python output_eval.py

# 3. Launch analysis notebook
jupyter notebook "Benchmark/Benchmark Analysis and EDA.ipynb"
```

### Custom Testing
You can modify parameters in `output_eval.py` to test different configurations:

```python
# Custom parameter sets
custom_params = {
    "aco": {"alpha": 1.5, "beta": 3.0, "rho": 0.2},
    "genetic": {"population_size": 100, "mutation_rate": 0.05}
}
```

## 📊 Understanding the Results

### Reading Performance Metrics

#### Solution Quality
- **Lower is Better**: TSP costs represent total travel distance/time
- **Relative Performance**: Compare ratios rather than absolute values
- **Consistency**: Look at standard deviation across runs

#### Runtime Analysis
- **Linear Scaling**: Expected O(n²) growth with problem size
- **Algorithm Overhead**: Fixed costs per algorithm
- **Hardware Dependency**: Results may vary across systems

#### Convergence Patterns
- **Early Convergence**: Fast but potentially suboptimal
- **Late Convergence**: Better exploration but higher cost
- **Premature Stagnation**: Algorithm gets stuck in local optima

### Interpretation Guidelines

#### For Research Applications
- Focus on solution quality and convergence analysis
- Consider statistical significance of differences
- Analyze algorithmic behavior patterns

#### For Production Deployment
- Prioritize runtime performance for real-time applications
- Consider solution quality requirements vs speed trade-offs
- Evaluate robustness across different problem instances

## 🔍 Extending the Test Suite

### Adding New Algorithms
1. Implement algorithm following existing interface
2. Add algorithm import and call in `output_eval.py`
3. Update analysis notebook with new algorithm
4. Regenerate benchmark results

### Testing Different Problem Types
1. Modify `data_gen.py` for different distance distributions
2. Add asymmetric TSP instances
3. Include real-world coordinate-based problems
4. Test dynamic TSP scenarios

### Advanced Analysis
1. **Multi-objective Optimization**: Quality vs runtime Pareto fronts
2. **Parameter Sensitivity**: Grid search across parameter spaces
3. **Problem Instance Analysis**: Performance correlation with problem features
4. **Ensemble Methods**: Combining multiple algorithms

## 📚 References & Further Reading

1. **Benchmark Methodology**: Hooker, J. N. (1995). Testing heuristics: We have it all wrong.
2. **TSP Benchmarking**: Reinelt, G. (1991). TSPLIB—A traveling salesman problem library.
3. **Statistical Analysis**: Montgomery, D. C. (2017). Design and analysis of experiments.
4. **Algorithm Comparison**: Derrac, J., et al. (2011). A practical tutorial on the use of nonparametric statistical tests.

## 👨‍💻 Author

**Bhavesh (B Infinity)**
- GitHub: [@Infinity2959N](https://github.com/Infinity2959N)
- Email: [binfinity321@gmail.com](mailto:binfinity321@gmail.com)

---

**Note**: This testing framework is designed for reproducible research and practical algorithm comparison. All random seeds are fixed for consistency, and multiple runs are used to ensure statistical validity of results.

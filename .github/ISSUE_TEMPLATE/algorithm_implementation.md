---
name: 🧮 New Algorithm Implementation
about: Propose or implement a new optimization algorithm
title: '[ALGORITHM] Implement [Algorithm Name] for TSP optimization'
labels: ['enhancement', 'algorithm', 'research']
assignees: ''
---

## Algorithm Overview

**Algorithm Name**: 
**Algorithm Type**: (e.g., Metaheuristic, Swarm Intelligence, Evolutionary)
**Reference Paper/Source**: 

## Algorithm Description

### Core Concept
Brief description of how the algorithm works and its inspiration.

### Key Features
- Feature 1
- Feature 2
- Feature 3

### Expected Advantages
- Why this algorithm might perform well for TSP
- Specific scenarios where it excels
- Unique characteristics compared to existing algorithms

## Implementation Plan

### Algorithm Parameters
List the main parameters this algorithm will need:
- Parameter 1: Description and typical range
- Parameter 2: Description and typical range

### Interface Compatibility
- [ ] Will follow existing `solve_tsp(matrix, params)` interface
- [ ] Returns dictionary with `best_cost`, `best_path`, `convergence_iter`
- [ ] Compatible with current benchmarking framework

### Testing Strategy
- [ ] Unit tests for algorithm components
- [ ] Integration with benchmarking suite
- [ ] Performance comparison with existing algorithms
- [ ] Documentation and examples

## Implementation Checklist

- [ ] Algorithm implementation in `algos/new_algorithm.py`
- [ ] Unit tests in `algos/tests/`
- [ ] Integration with `Algorithm Testing/output_eval.py`
- [ ] Documentation in `algos/README.md`
- [ ] Parameter tuning and optimization
- [ ] Benchmark analysis and comparison

## Research Context

### Known Performance
If you have information about this algorithm's performance:
- Time complexity: 
- Space complexity:
- Typical convergence behavior:

### References
- Link to papers or resources about this algorithm
- Previous implementations (if any)
- Theoretical analysis

## Additional Notes

Any other relevant information about the algorithm or implementation approach.

---

**For Maintainers:**
- [ ] Assign appropriate difficulty label
- [ ] Link to related issues or discussions
- [ ] Provide guidance on implementation approach

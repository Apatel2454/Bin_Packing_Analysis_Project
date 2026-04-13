# Bin Packing Algorithms Analysis

## Overview
This project focuses on analyzing and comparing the performance of multiple algorithms designed to solve the Bin Packing Problem, a classic optimization problem in computer science and operations research.

The goal is to evaluate how different algorithmic approaches perform in terms of efficiency, solution quality, and computational cost when packing items of varying sizes into a limited number of bins.

Contributors: 
  -[Alex Patel](https://github.com/Apatel2454) 
  -[Dante Haman](https://github.com/dhaman43) 
## Objectives
- Implement multiple bin packing algorithms in C++  
- Compare their efficiency and accuracy  
- Analyze trade-offs between optimality and runtime  
- Evaluate performance across different datasets  

## Algorithms Implemented

### Greedy Algorithms
These algorithms make locally optimal choices at each step:

- First Fit (FF)  
  Places each item into the first bin that has enough remaining space.

- Best Fit (BF)  
  Places each item into the bin that leaves the least leftover space.

- Worst Fit (WF)  
  Places each item into the bin with the most available space.

### Exact Algorithm
- Branch and Bound (B&B)  
  Explores all possible solutions but prunes inefficient branches to find an optimal solution. Guarantees optimality but can be computationally expensive.

### Metaheuristic Algorithms
These algorithms aim to find near-optimal solutions efficiently:

- Ant Colony Optimization (ACO)  
  Inspired by the behavior of ants, this algorithm uses probabilistic decision-making and pheromone trails to guide solution construction.

- Simulated Annealing (SA)  
  Mimics the cooling process of metals, allowing occasional worse solutions to escape local minima and gradually converge to a strong solution.

## Performance Metrics
The algorithms are evaluated based on:

- Number of bins used (primary objective)  
- Execution time  
- Scalability with input size  
- Consistency across datasets  

## How to run
 - Download or clone the repository and open the project folder on your computer.
- Make sure you have a C++ compiler installed, such as g++.
- Open a terminal or command prompt and navigate to the project folder.
- Compile the C++ file to create an executable program.
- Run the executable from the terminal to execute the algorithm.
- If there are multiple files, compile and run each one separately.
- If it does not work, check that the compiler is installed and that you are in the correct folder.

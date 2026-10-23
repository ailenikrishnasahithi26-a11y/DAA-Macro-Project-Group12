# Project 14 – TSP Branch and Bound Search Tree

## Description
This project implements the Traveling Salesperson Problem (TSP) using the
Branch and Bound technique. It finds the minimum cost Hamiltonian cycle
visiting all 4 cities exactly once and returning to the start.

## Input
Cost Matrix (4 cities):

|       | City0 | City1 | City2 | City3 |
|-------|------:|------:|------:|------:|
| City0 |  INF  |  10   |   8   |   9   |
| City1 |   10  |  INF  |   5   |   7   |
| City2 |    8  |   5   |  INF  |   6   |
| City3 |    9  |   7   |   6   |  INF  |

## Algorithm
A priority queue (min-heap) is used to explore nodes ordered by their lower
bound. Each node represents a partial tour. The lower bound is computed by
reducing the cost matrix (row and column reduction). Branches whose bound
exceeds the current best solution are pruned.

See `Algorithm_Pseudocode.txt` for the complete pseudocode.

## Prompt Used
See `Prompt.txt`.

## Visualization
`Visualization.png` shows the Branch and Bound search tree with node bounds,
pruned branches (red), and the optimal path (green).

## Output
The program prints the cost matrix, each node explored with its bound,
pruned branches, and the final optimal tour.

Optimal Path: **City0 → City3 → City1 → City2 → City0**

Minimum Cost: **29**

Nodes Explored: **6**

## Complexity
- Time Complexity: **O(n² × 2ⁿ)** (worst case)
- Space Complexity: **O(n² × 2ⁿ)**

## Learning Outcome
- Understood Branch and Bound as a systematic search strategy.
- Learned how matrix reduction gives a valid lower bound for TSP.
- Understood how pruning reduces the search space significantly.
- Practiced algorithm documentation and prompt-based visualization.
- Prepared a project structure suitable for GitHub submission.

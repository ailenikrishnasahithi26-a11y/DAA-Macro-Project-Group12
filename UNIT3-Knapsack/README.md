# Unit III — Project 9: 0/1 Knapsack using Dynamic Programming

## Overview
This repository contains an academic implementation of the classic **0/1 Knapsack Problem** using bottom-up **Dynamic Programming (DP)**. The project is developed for **Design and Analysis of Algorithms (DAA) — Unit III, Project 9**, featuring modular Java code, step-by-step backtracking, prompt-engineered table visualization, and complexity analysis.

---

## Problem Definition
Given a set of $n = 4$ discrete items, each characterized by an integer weight and profit, determine the subset of items to pack into a knapsack of maximum capacity $W = 10$ such that total profit is maximized without exceeding the capacity.

Each item $i$ can either be selected ($x_i = 1$) or excluded ($x_i = 0$):

$$\text{Maximize } \sum_{i=1}^{n} p_i \cdot x_i \quad \text{subject to} \quad \sum_{i=1}^{n} w_i \cdot x_i \le W, \quad x_i \in \{0, 1\}$$

---

## Input Dataset
The project evaluates the following distinct item configuration:

| Item | Weight ($w_i$) | Profit ($p_i$) | Profit-to-Weight Ratio |
| :---: | :---: | :---: | :---: |
| **Item 1** | 1 | 10 | 10.0 |
| **Item 2** | 2 | 20 | 10.0 |
| **Item 3** | 4 | 35 | 8.75 |
| **Item 4** | 5 | 45 | 9.0 |

- **Total Items ($n$):** 4
- **Knapsack Capacity ($W$):** 10

---

## Dynamic Programming Approach

### 1. Recurrence Relation
Let `dp[i][w]` represent the maximum obtainable profit considering a subset of the first `i` items with a knapsack capacity limit of `w`.

- **Base Case:**
  $$\text{dp}[0][w] = 0 \quad \text{for all } w \in [0, W]$$
  $$\text{dp}[i][0] = 0 \quad \text{for all } i \in [0, n]$$

- **Transition Step:**
  - If current item weight $w_i \le w$:
    $$\text{dp}[i][w] = \max\Big(\text{dp}[i-1][w],\; p_i + \text{dp}[i-1][w - w_i]\Big)$$
  - If current item weight $w_i > w$:
    $$\text{dp}[i][w] = \text{dp}[i-1][w]$$

### 2. Backtracking for Item Selection
Starting from the optimal solution cell `dp[n][W]`:
1. If `dp[i][w] != dp[i-1][w]`, Item $i$ was included in the optimal knapsack.
2. Deduct $w_i$ from remaining capacity ($w \leftarrow w - w_i$) and proceed to row $i-1$.
3. If `dp[i][w] == dp[i-1][w]`, Item $i$ was excluded; move directly to row $i-1$.

---

## DP Tabulation Matrix

| Row / Sub-capacity | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Item 0 (Base)** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Item 1 (w=1, p=10)** | 0 | **10** | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| **Item 2 (w=2, p=20)** | 0 | **10** | 20 | 30 | 30 | 30 | 30 | 30 | 30 | 30 | 30 |
| **Item 3 (w=4, p=35)** | 0 | 10 | 20 | 30 | 35 | **45** | 55 | 65 | 65 | 65 | 65 |
| **Item 4 (w=5, p=45)** | 0 | 10 | 20 | 30 | 35 | 45 | 55 | 65 | 75 | 80 | **90** |

*Note: Bold numbers trace the optimal backtracking route.*

---

## Optimal Solution Summary
- **Maximum Profit:** **90** (`dp[4][10]`)
- **Optimal Items Selected:** **Item 1, Item 3, Item 4**
  - Item 1: Weight = 1, Profit = 10
  - Item 3: Weight = 4, Profit = 35
  - Item 4: Weight = 5, Profit = 45
- **Total Selected Weight:** $1 + 4 + 5 = \mathbf{10} \le 10$ (100% capacity utilization)
- **Constraint Satisfaction:** Fully satisfied ($10 \le 10$)

---

## Complexity Analysis
- **Time Complexity:** $\mathcal{O}(n \times W)$  
  Filling the $(n + 1) \times (W + 1)$ table requires nested loops executing $(4 + 1) \times (10 + 1) = 55$ constant-time cell evaluations. Backtracking takes $\mathcal{O}(n)$ steps.
- **Space Complexity:** $\mathcal{O}(n \times W)$  
  Auxiliary 2D matrix storage of size $5 \times 11$.

---

## Project Artifacts
- [`Project9_Knapsack_DP.java`](file:///c:/Users/Krishnasahithi/OneDrive/Documents/Desktop/UNIT3-Knapsack/Project9_Knapsack_DP.java): Modular Java implementation with clean class design and output formatting.
- [`Algorithm_Pseudocode.txt`](file:///c:/Users/Krishnasahithi/OneDrive/Documents/Desktop/UNIT3-Knapsack/Algorithm_Pseudocode.txt): Formal algorithm specification and pseudocode.
- [`Prompt.txt`](file:///c:/Users/Krishnasahithi/OneDrive/Documents/Desktop/UNIT3-Knapsack/Prompt.txt): Prompt engineered for generating the academic DP visualization.
- [`Visualization.png`](file:///c:/Users/Krishnasahithi/OneDrive/Documents/Desktop/UNIT3-Knapsack/Visualization.png): High-resolution visualization of the DP table and optimal backtracking route.
- [`Sample_Output.txt`](file:///c:/Users/Krishnasahithi/OneDrive/Documents/Desktop/UNIT3-Knapsack/Sample_Output.txt): Verifiable execution log.
- [`Project9_Knapsack_DP.pptx`](file:///c:/Users/Krishnasahithi/OneDrive/Documents/Desktop/UNIT3-Knapsack/Project9_Knapsack_DP.pptx): Academic slide presentation updated with the new dataset, slides, and embedded graphic.

---

## How to Compile & Run
```bash
# Compile Java source
javac Project9_Knapsack_DP.java

# Execute class
java Project9_Knapsack_DP
```

---

## Learning Outcomes
- Demonstrated how bottom-up DP eliminates redundant overlapping subproblems.
- Understood inclusion versus exclusion decision logic.
- Mastered backward pointer traversal for optimal solution reconstruction.
- Practiced complete end-to-end documentation suitable for institutional academic review.

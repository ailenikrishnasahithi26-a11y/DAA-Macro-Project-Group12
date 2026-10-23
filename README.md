# DAA Macro Project — Group 12

Welcome to the **Design and Analysis of Algorithms (DAA)** Macro Project repository for **Group 12** (B.Tech Computer Science & Engineering). 

This repository is organized into dedicated topic branches, where each branch represents an in-depth algorithmic unit complete with source code, formal mathematical logic, state space/infographic visualizations, prompts, and documentation.

---

## Branch Directory & Navigation Guide

| Branch Name | Algorithmic Unit | Technique / Paradigm | Programming Language | Key Deliverables |
| :--- | :--- | :--- | :--- | :--- |
| [`main`](https://github.com/ailenikrishnasahithi26-a11y/DAA-Macro-Project-Group12/tree/main) | **Project Index** | — | Markdown | Repository overview, branch mapping & documentation |
| [`UNIT1-Asymptotic`](https://github.com/ailenikrishnasahithi26-a11y/DAA-Macro-Project-Group12/tree/UNIT1-Asymptotic) | **Unit 1: Asymptotic Analysis** | Mathematical & Asymptotic Bounds | Python (Pillow) | Asymptotic script, concept map, semi-log growth curve |
| [`UNIT2_Greedy_Job_Sequencing_Flowchart`](https://github.com/ailenikrishnasahithi26-a11y/DAA-Macro-Project-Group12/tree/UNIT2_Greedy_Job_Sequencing_Flowchart) | **Unit 2: Greedy Job Sequencing** | Greedy Paradigm | Python | Job sequencing script, decision flowchart & summary deck |
| [`UNIT3-Knapsack`](https://github.com/ailenikrishnasahithi26-a11y/DAA-Macro-Project-Group12/tree/UNIT3-Knapsack) | **Unit 3: 0/1 Knapsack** | Dynamic Programming (DP) | Java | DP table implementation, pseudocode & execution output |
| [`UNIT4-subset`](https://github.com/ailenikrishnasahithi26-a11y/DAA-Macro-Project-Group12/tree/UNIT4-subset) | **Unit 4: Sum of Subsets** | Backtracking | Java | Recursive backtracking code, pruning state space tree |
| [`UNIT5-branch`](https://github.com/ailenikrishnasahithi26-a11y/DAA-Macro-Project-Group12/tree/UNIT5-branch) | **Unit 5: Traveling Salesperson Problem (TSP)** | Branch and Bound (LCBB / Min-Heap) | Python | Search tree script, matrix reduction pseudocode, sample trace, PDF report & tree visualization |
| [`ppt`](https://github.com/ailenikrishnasahithi26-a11y/DAA-Macro-Project-Group12/tree/ppt) | **Comprehensive Presentation** | Multi-Unit Presentation Deck | PowerPoint (.pptx) | Complete 36-slide Group 12 Master Presentation |

---

## Detailed Unit Overviews

### 1. `UNIT1-Asymptotic` — Asymptotic Analysis & Growth Comparison
- **Focus**: Formal bounding of algorithmic time and space complexity as input size \( n \to \infty \).
- **Core Concepts**:
  - **Big-O (\(O\))**: Asymptotic upper bound (worst-case ceiling).
  - **Big-Omega (\(\Omega\))**: Asymptotic lower bound (best-case floor).
  - **Big-Theta (\(\Theta\))**: Asymptotically tight bound, established when \( f(n) \in O(g(n)) \land f(n) \in \Omega(g(n)) \).
  - **Mathematical Analysis**: Algebraic proof for \( f(n) = 3n^2 + 2n + 1 \in \Theta(n^2) \).
  - **Semi-Logarithmic Plotting**: Visual comparison of \( n \), \( n \log_2 n \), \( n^2 \), and \( 2^n \) for \( n = 1 \) to \( 10 \).
- **Files in Branch**:
  - `AsymptoticGrowth.py`: Python visualization engine generating the concept infographic and semi-log curves.
  - `Explanation.txt`: Detailed theoretical breakdowns and 5 essential lab viva Q&A.
  - `Prompt.txt`: Engineering prompt used for graphic generation.
  - `README.md`: Unit-level overview, equations, and console execution logs.
  - `Visualization.png`: High-resolution concept map and growth plot.

---

### 2. `UNIT2_Greedy_Job_Sequencing_Flowchart` — Greedy Job Sequencing
- **Focus**: Scheduling jobs with given deadlines and associated profits to maximize overall return.
- **Core Concepts**:
  - **Greedy Strategy**: Sorting jobs in descending order of profit and placing each job in the latest available free time slot before its deadline.
  - **Feasibility Checking**: Preventing deadline collisions using disjoint-set / slot reservation logic.
- **Files in Branch**:
  - `Project1_GreedyJobSequencing.py`: Python implementation of greedy scheduling and flowchart rendering.
  - `Projects_Summary.pptx`: Individual topic summary slide deck.
  - `Prompt.txt`: Prompt specifying flowchart and schedule visualization guidelines.
  - `README.md`: Problem statement, algorithmic walkthrough, and results.
  - `Visualization.png`: Graphical scheduling flowchart and timeline diagram.

---

### 3. `UNIT3-Knapsack` — 0/1 Knapsack Problem (Dynamic Programming)
- **Focus**: Optimal subset selection from items with given weights and values to maximize value within weight capacity \( W \).
- **Core Concepts**:
  - **Optimal Substructure**: The optimal solution incorporates optimal solutions to smaller sub-problems.
  - **Recurrence Relation**: 
    \[
    dp[i][w] = \max(dp[i-1][w],\; dp[i-1][w - w_i] + v_i) \quad \text{for } w \ge w_i
    \]
  - **Backtracking from Table**: Tracing back through the DP matrix to identify the exact subset of items included.
- **Files in Branch**:
  - `Knapsack_DP.java`: Complete Java implementation computing the DP table and selected item set.
  - `Algorithm_Pseudocode.txt`: Step-by-step algorithmic pseudocode and recurrence formulation.
  - `Sample_Output.txt`: Terminal execution log with test datasets.
  - `Prompt.txt`: Visualization prompt for the DP matrix state diagram.
  - `README.md`: Theoretical complexity analysis, DP table walkthrough, and documentation.
  - `Visualization.png`: High-contrast DP matrix visualization.

---

### 4. `UNIT4-subset` — Sum of Subsets (Backtracking)
- **Focus**: Finding all subsets of a given set of positive integers whose elements sum up to a specified target \( M \).
- **Core Concepts**:
  - **Recursive State Space Search**: Building combinations through a binary decision tree (Include element vs. Exclude element).
  - **Bounding Function & Pruning**: Since all integers are positive, any branch where \( \text{currentSum} > M \) is immediately abandoned (pruned), eliminating unnecessary subtree traversal.
- **Files in Branch**:
  - `SumOfSubsets.java`: Recursive Java solution with backtracking and bounding checks.
  - `Explanation.txt`: Detailed explanation of state tree levels, branching decisions, and viva Q&A.
  - `Prompt.txt`: Prompt used for rendering the complete state space tree.
  - `README.md`: Problem description, pseudocode, terminal outputs, and learning outcomes.
  - `Visualization.png`: Color-coded state space tree highlighting valid solution nodes, pruned branches, and leaf states.

---

### 5. `UNIT5-branch` — Traveling Salesperson Problem (Branch and Bound)
- **Focus**: Solving the Traveling Salesperson Problem (TSP) to determine the minimum-cost Hamiltonian cycle visiting every city exactly once and returning to the starting city using Least Cost Branch and Bound (LCBB).
- **Core Concepts**:
  - **Branch and Bound State Space Search**: Formulating the TSP search space as a state space tree where each node represents a partial tour starting from City 0. Exploration order is governed by a min-heap priority queue keyed on lower bound.
  - **Matrix Reduction & Lower Bounding**:
    - Computing a valid lower bound via row and column reduction of the cost matrix:
      \[
      \text{Reduction Cost} = \sum_{i=1}^n \min(\text{row}_i) + \sum_{j=1}^n \min(\text{col}_j)
      \]
    - For transition from city \( i \) to city \( j \):
      \[
      \hat{c}(\text{child}) = \hat{c}(\text{parent}) + \text{cost}[i][j] + r
      \]
      where row \( i \) and column \( j \) are eliminated (set to \( \infty \)), and back-edge \( (j, 0) \) is set to \( \infty \) to prevent premature cycle formation.
  - **Bounding Function & Pruning**: Tracking the current best upper bound (cost of complete tour). Any sub-tree whose lower bound is greater than or equal to the best solution (\( \text{Bound} \ge \text{Best} \)) is immediately pruned, eliminating redundant exponential search branches.
- **Files in Branch**:
  - `Project14_TSP_BnB.py`: Complete Python script implementing min-heap priority queue, dynamic matrix reduction, terminal trace, and network search tree generation.
  - `Algorithm_Pseudocode.txt`: Step-by-step algorithm pseudocode, matrix reduction logic, and lower bounding steps.
  - `Sample_Output.txt`: Complete execution log displaying node exploration order, dynamic bounds, pruned branches, and optimal tour (`City0 -> City3 -> City1 -> City2 -> City0`, Min Cost: 29).
  - `Prompt.txt`: Engineering visualization prompt detailing node labeling, color-coded pruning, and optimal path styling.
  - `README.md`: Unit-level problem definition, input cost matrix, algorithm explanation, worst-case complexity (\( O(n^2 \cdot 2^n) \)), and key learning outcomes.
  - `TSP_BnB.pdf`: Formal academic project documentation and report covering TSP Branch and Bound analysis.
  - `Visualization.png`: High-resolution state space search tree highlighting node bounds, pruned branches (red), and the optimal Hamiltonian cycle (green).

---

### 6. `ppt` — Master Macro Project Presentation
- **Focus**: Consolidated final project presentation for **Group 12**.
- **File**: `Group12_DAA_Macro_Project.pptx` (16:9 Widescreen, 36 Slides)
- **Slide Architecture**:
  - **Slide 1**: Master Cover Slide with **Group 12** branding, course information, and multi-unit syllabus overview.
  - **Slides 2–11**: Unit 1 — Asymptotic Analysis, formal bounds, dry runs, case studies, and charts.
  - **Slides 12–19**: Unit 2 — Greedy Job Sequencing, algorithm logic, flowchart, datasets, and complexities.
  - **Slides 20–26**: Unit 3 — 0/1 Knapsack Dynamic Programming, table visualization, and outcomes.
  - **Slides 27–36**: Unit 4 — Sum of Subsets Backtracking, state space tree, dry run trace, and conclusions.

---

## How to Switch Between Branches

To clone this repository and explore a specific unit:

```bash
# Clone the repository
git clone https://github.com/ailenikrishnasahithi26-a11y/DAA-Macro-Project-Group12.git

# Enter project directory
cd DAA-Macro-Project-Group12

# List all available branches
git branch -r

# Checkout a specific unit branch
git checkout UNIT1-Asymptotic
git checkout UNIT2_Greedy_Job_Sequencing_Flowchart
git checkout UNIT3-Knapsack
git checkout UNIT4-subset
git checkout UNIT5-branch
git checkout ppt
```

---

## Technologies & Tools Used
- **Languages**: Python 3.13, Java 21+
- **Libraries**: Pillow (PIL), `python-pptx`, Matplotlib, NetworkX
- **Visualization**: Prompt-engineered infographics, coordinate growth plots, and state space trees
- **Version Control**: Git & GitHub
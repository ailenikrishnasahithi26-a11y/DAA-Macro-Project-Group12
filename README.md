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

### 5. `ppt` — Master Macro Project Presentation
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
git checkout ppt
```

---

## Technologies & Tools Used
- **Languages**: Python 3.13, Java 21+
- **Libraries**: Pillow (PIL), `python-pptx`
- **Visualization**: Prompt-engineered infographics, coordinate growth plots, and state space trees
- **Version Control**: Git & GitHub
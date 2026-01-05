# Lesson 3: Understanding Optimization

Welcome to Lesson 3 of Prescriptive Analytics! This lesson deepens your understanding of what optimization actually does and how to interpret optimization results.

## Learning Objectives

By the end of this lesson, you will understand:

- **What Optimization Is**: How optimization systematically searches for the best solution
- **Feasible vs Infeasible**: When solutions are possible versus impossible
- **Optimal vs Acceptable**: Understanding solution quality and when acceptable solutions are sufficient
- **Deterministic Limits**: What optimization can and cannot do
- **Multiple Nearly Optimal Solutions**: Why there may be many good solutions
- **Interpreting Results**: How to understand and communicate optimization results

## Core Concepts

### 1. What Optimization Is
- Optimization is systematic search, not magic
- It finds the best solution from what is possible
- If all possible solutions are poor, optimization finds the best poor solution

### 2. Feasible vs Infeasible
- **Feasible**: Solutions that satisfy all constraints
- **Infeasible**: No solution exists that satisfies all constraints
- Understanding infeasibility helps identify problem formulation issues

### 3. Optimal vs Acceptable
- **Optimal**: The mathematically best solution
- **Acceptable**: Solutions that meet your requirements
- Sometimes acceptable solutions are preferable to optimal ones

### 4. Deterministic Limits
- Optimization works with the data and constraints you provide
- It cannot create perfect solutions from imperfect information
- Understanding limits helps set realistic expectations

### 5. Multiple Nearly Optimal Solutions
- There may be many solutions with similar objective values
- Different solutions may have different practical advantages
- Exploring the solution space provides flexibility

### 6. Interpreting Results
- Results must be interpreted in context
- Understanding solution quality and sensitivity is critical
- Results should be communicated clearly to stakeholders

## Notebooks

This lesson includes six interactive Jupyter notebooks. Each notebook is self-contained and includes extensive explanations, code examples, and visualizations.

### Notebook 1: What Is Optimization
**File**: `lesson03_concept01_what_is_optimization.ipynb`

This notebook explains what optimization actually does in plain English. You'll learn:
- How optimization systematically searches for solutions
- What optimization can and cannot do
- Why optimization is systematic search, not magic

**Key Learning**: Optimization finds the best solution from what is possible. If the possible solutions are all poor, optimization will find the best poor solution.

[📓 Open in Jupyter](./lesson03_concept01_what_is_optimization.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson03/lesson03_concept01_what_is_optimization.ipynb)

---

### Notebook 2: Feasible vs Infeasible
**File**: `lesson03_concept02_feasible_vs_infeasible.ipynb`

This notebook demonstrates the difference between feasible and infeasible problems. You'll see:
- What makes a solution feasible
- Why problems become infeasible
- How to identify and resolve infeasibility

**Key Learning**: Feasible solutions satisfy all constraints. Infeasible problems have no solution that satisfies all constraints, indicating a problem with the formulation.

[📓 Open in Jupyter](./lesson03_concept02_feasible_vs_infeasible.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson03/lesson03_concept02_feasible_vs_infeasible.ipynb)

---

### Notebook 3: Optimal vs Acceptable
**File**: `lesson03_concept03_optimal_vs_acceptable.ipynb`

This notebook explores the difference between optimal and acceptable solutions. You'll learn:
- When optimal solutions are necessary
- When acceptable solutions are sufficient
- How to evaluate solution quality beyond optimality

**Key Learning**: Optimal solutions are mathematically best, but acceptable solutions may be more practical, robust, or implementable.

[📓 Open in Jupyter](./lesson03_concept03_optimal_vs_acceptable.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson03/lesson03_concept03_optimal_vs_acceptable.ipynb)

---

### Notebook 4: Deterministic Limits
**File**: `lesson03_concept04_deterministic_limits.ipynb`

This notebook examines what optimization can and cannot do. You'll see:
- The limits of deterministic optimization
- Why optimization cannot create perfect solutions from imperfect data
- How to set realistic expectations

**Key Learning**: Optimization works with the data and constraints you provide. It cannot overcome fundamental limitations in your problem formulation or data quality.

[📓 Open in Jupyter](./lesson03_concept04_deterministic_limits.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson03/lesson03_concept04_deterministic_limits.ipynb)

---

### Notebook 5: Multiple Nearly Optimal Solutions
**File**: `lesson03_concept05_multiple_nearly_optimal_solutions.ipynb`

This notebook explores why there may be many solutions with similar objective values. You'll learn:
- Why multiple good solutions often exist
- How different solutions may have different practical advantages
- How to explore and evaluate alternative solutions

**Key Learning**: There are often many solutions with similar objective values. Exploring alternatives provides flexibility and robustness.

[📓 Open in Jupyter](./lesson03_concept05_multiple_nearly_optimal_solutions.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson03/lesson03_concept05_multiple_nearly_optimal_solutions.ipynb)

---

### Notebook 6: Interpreting Results
**File**: `lesson03_concept06_interpreting_results.ipynb`

This notebook demonstrates how to interpret and communicate optimization results. You'll see:
- How to understand solution quality
- How to evaluate solution sensitivity
- How to communicate results effectively to stakeholders

**Key Learning**: Results must be interpreted in context and communicated clearly. Understanding solution quality and sensitivity is critical for effective decision-making.

[📓 Open in Jupyter](./lesson03_concept06_interpreting_results.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson03/lesson03_concept06_interpreting_results.ipynb)

---


# Lesson 2: Modeling Fundamentals

Welcome to Lesson 2 of Prescriptive Analytics! This lesson covers the fundamental distinctions and concepts needed to build effective prescriptive models.

## Learning Objectives

By the end of this lesson, you will understand:

- **Variables vs Inputs**: The critical distinction between what you control (decision variables) and what you know (inputs)
- **Objectives vs Constraints**: How to distinguish what you optimize from what you must satisfy
- **Hard vs Soft Constraints**: When constraints are absolute versus when they can be relaxed
- **Tradeoffs**: How competing objectives create tradeoffs in decision-making
- **Heuristics vs Optimization**: When to use rules of thumb versus systematic optimization
- **Good Enough vs Optimal**: Understanding when "good enough" solutions are preferable to optimal ones

## Core Concepts

### 1. Decision Variables vs Inputs
- **Decision Variables**: What you control and what the model determines
- **Inputs**: Information you provide to the model (demand forecasts, costs, capacities)
- Confusing these leads to models that cannot be solved or answer the wrong question

### 2. Objectives vs Constraints
- **Objectives**: What you're trying to achieve (maximize or minimize)
- **Constraints**: Limits that must be respected
- Objectives are optimized; constraints are satisfied

### 3. Hard vs Soft Constraints
- **Hard Constraints**: Absolute limits that cannot be violated
- **Soft Constraints**: Preferences that can be relaxed with penalties
- Understanding this distinction helps structure problems appropriately

### 4. Tradeoffs
- Competing objectives create tradeoffs
- Improving one objective often requires sacrificing another
- Models help visualize and navigate these tradeoffs

### 5. Heuristics vs Optimization
- **Heuristics**: Rules of thumb that provide quick, reasonable solutions
- **Optimization**: Systematic search for the best solution
- Each has its place depending on problem complexity and time constraints

### 6. Good Enough vs Optimal
- Optimal solutions may be fragile or expensive to implement
- "Good enough" solutions may be more robust and practical
- Context determines which is more valuable

## Notebooks

This lesson includes six interactive Jupyter notebooks. Each notebook is self-contained and includes extensive explanations, code examples, and visualizations.

### Notebook 1: Variables vs Inputs
**File**: `lesson02_concept02_variables_vs_inputs.ipynb`

This notebook demonstrates the fundamental distinction between decision variables (what you control) and inputs (what you know or can estimate). You'll learn:
- How to identify decision variables versus inputs in a problem
- Why confusing these leads to modeling errors
- How to structure problems with clear variable definitions

**Key Learning**: You control decision variables; you observe or estimate inputs. The model finds the best values for variables given the inputs you provide.

[📓 Open in Jupyter](./lesson02_concept02_variables_vs_inputs.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson02/lesson02_concept02_variables_vs_inputs.ipynb)

---

### Notebook 2: Objectives vs Constraints
**File**: `lesson02_concept03_objectives_vs_constraints.ipynb`

This notebook explores the critical distinction between objectives (what you optimize) and constraints (what you must satisfy). You'll see:
- How objectives define what you're trying to achieve
- How constraints define what you cannot do
- Why this distinction matters for model formulation

**Key Learning**: Objectives are optimized; constraints are satisfied. The model finds the best solution that respects all constraints.

[📓 Open in Jupyter](./lesson02_concept03_objectives_vs_constraints.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson02/lesson02_concept03_objectives_vs_constraints.ipynb)

---

### Notebook 3: Hard vs Soft Constraints
**File**: `lesson02_concept04_hard_vs_soft_constraints.ipynb`

This notebook demonstrates the difference between hard constraints (absolute limits) and soft constraints (preferences with penalties). You'll learn:
- When constraints must be absolute versus when they can be relaxed
- How to model soft constraints using penalties
- When to use each approach

**Key Learning**: Hard constraints cannot be violated; soft constraints can be relaxed with penalties. Choose the approach that matches your problem's reality.

[📓 Open in Jupyter](./lesson02_concept04_hard_vs_soft_constraints.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson02/lesson02_concept04_hard_vs_soft_constraints.ipynb)

---

### Notebook 4: Tradeoffs
**File**: `lesson02_concept05_tradeoffs.ipynb`

This notebook explores how competing objectives create tradeoffs in decision-making. You'll see:
- How tradeoffs emerge from competing objectives
- How to visualize tradeoffs between objectives
- How models help navigate tradeoff spaces

**Key Learning**: When objectives compete, you must make tradeoffs. Models help you understand and navigate these tradeoffs systematically.

[📓 Open in Jupyter](./lesson02_concept05_tradeoffs.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson02/lesson02_concept05_tradeoffs.ipynb)

---

### Notebook 5: Heuristics vs Optimization
**File**: `lesson02_concept06_heuristics_vs_optimization.ipynb`

This notebook compares heuristics (rules of thumb) with systematic optimization. You'll learn:
- When heuristics provide good enough solutions quickly
- When optimization is worth the additional effort
- How to choose the right approach for your problem

**Key Learning**: Heuristics provide quick solutions; optimization provides the best solution. Choose based on problem complexity, time constraints, and solution quality requirements.

[📓 Open in Jupyter](./lesson02_concept06_heuristics_vs_optimization.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson02/lesson02_concept06_heuristics_vs_optimization.ipynb)

---

### Notebook 6: Good Enough vs Optimal
**File**: `lesson02_concept07_good_enough_vs_optimal.ipynb`

This notebook explores when "good enough" solutions are preferable to optimal ones. You'll see:
- Why optimal solutions may not always be best
- When good enough solutions are more robust or practical
- How to evaluate solution quality beyond optimality

**Key Learning**: Optimal solutions are best mathematically, but good enough solutions may be better practically. Context determines which matters more.

[📓 Open in Jupyter](./lesson02_concept07_good_enough_vs_optimal.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson02/lesson02_concept07_good_enough_vs_optimal.ipynb)

---


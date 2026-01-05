# Lesson 7: Discrete and Integer Optimization

Welcome to Lesson 7 of Prescriptive Analytics! This lesson explores discrete and integer optimization, where decisions must be whole numbers or come from discrete sets.

## Learning Objectives

By the end of this lesson, you will understand:

- **Discrete vs Continuous Decisions**: When decisions must be whole numbers versus when they can be fractional
- **Integer Constraints in Modeling**: How to model problems with integer requirements
- **Feasibility Challenges with Integers**: Why integer problems are harder to solve
- **Discrete Tradeoffs and Gaps**: How discrete decisions create gaps in solution spaces
- **Interpreting Integer Solutions**: How to understand and validate integer solutions
- **Over-constraining with Integers**: How integer constraints can make problems infeasible
- **Comprehensive Discrete Example**: A complete example combining discrete concepts

## Core Concepts

### 1. Discrete vs Continuous Decisions
- **Continuous**: Decisions can be any value (e.g., 3.7 units)
- **Discrete**: Decisions must be whole numbers or from discrete sets (e.g., 3 or 4 units)
- Many real-world decisions are naturally discrete

### 2. Integer Constraints in Modeling
- Integer constraints require variables to be whole numbers
- Binary constraints require variables to be 0 or 1
- Integer constraints make problems more complex

### 3. Feasibility Challenges with Integers
- Integer problems have fewer feasible solutions
- Integer problems are harder to solve
- Small changes can make integer problems infeasible

### 4. Discrete Tradeoffs and Gaps
- Discrete decisions create gaps in solution spaces
- Tradeoffs may be non-smooth with discrete decisions
- Solutions may jump between discrete options

### 5. Interpreting Integer Solutions
- Integer solutions must be validated for practicality
- Rounding continuous solutions doesn't always work
- Integer solutions may be suboptimal compared to continuous relaxations

### 6. Over-constraining with Integers
- Integer constraints can make problems infeasible
- Adding integer constraints reduces feasible space
- Sometimes relaxing integer constraints is necessary

### 7. Comprehensive Discrete Example
- Combining discrete concepts in a realistic problem
- Demonstrating best practices for discrete modeling
- Showing how to interpret and validate discrete solutions

## Notebooks

This lesson includes seven interactive Jupyter notebooks. Each notebook is self-contained and includes extensive explanations, code examples, and visualizations.

### Notebook 1: Discrete vs Continuous Decisions
**File**: `lesson07_concept01_discrete_vs_continuous_decisions.ipynb`

This notebook introduces the difference between discrete and continuous decisions. You'll learn:
- When decisions must be whole numbers
- When fractional decisions are acceptable
- How to identify which type applies to your problem

**Key Learning**: Discrete decisions must be whole numbers or from discrete sets. Continuous decisions can be any value. Many real-world decisions are naturally discrete.

[📓 Open in Jupyter](./lesson07_concept01_discrete_vs_continuous_decisions.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson07/lesson07_concept01_discrete_vs_continuous_decisions.ipynb)

---

### Notebook 2: Integer Constraints in Modeling
**File**: `lesson07_concept02_integer_constraints_in_modeling.ipynb`

This notebook demonstrates how to model problems with integer requirements. You'll see:
- How to add integer constraints to models
- When to use binary (0/1) variables
- How integer constraints affect model structure

**Key Learning**: Integer constraints require variables to be whole numbers. Binary constraints require variables to be 0 or 1. These constraints make problems more complex but more realistic.

[📓 Open in Jupyter](./lesson07_concept02_integer_constraints_in_modeling.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson07/lesson07_concept02_integer_constraints_in_modeling.ipynb)

---

### Notebook 3: Feasibility Challenges with Integers
**File**: `lesson07_concept03_feasibility_challenges_with_integers.ipynb`

This notebook explores why integer problems are harder to solve. You'll learn:
- Why integer problems have fewer feasible solutions
- Why integer problems are computationally harder
- How small changes can affect feasibility

**Key Learning**: Integer problems have fewer feasible solutions and are harder to solve. Small changes can make integer problems infeasible, requiring careful problem formulation.

[📓 Open in Jupyter](./lesson07_concept03_feasibility_challenges_with_integers.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson07/lesson07_concept03_feasibility_challenges_with_integers.ipynb)

---

### Notebook 4: Discrete Tradeoffs and Gaps
**File**: `lesson07_concept04_discrete_tradeoffs_and_gaps.ipynb`

This notebook demonstrates how discrete decisions create gaps in solution spaces. You'll see:
- How discrete decisions create non-smooth tradeoffs
- How solutions jump between discrete options
- How to navigate discrete solution spaces

**Key Learning**: Discrete decisions create gaps in solution spaces. Tradeoffs may be non-smooth, and solutions may jump between discrete options.

[📓 Open in Jupyter](./lesson07_concept04_discrete_tradeoffs_and_gaps.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson07/lesson07_concept04_discrete_tradeoffs_and_gaps.ipynb)

---

### Notebook 5: Interpreting Integer Solutions
**File**: `lesson07_concept05_interpreting_integer_solutions.ipynb`

This notebook demonstrates how to interpret and validate integer solutions. You'll learn:
- How to validate integer solutions for practicality
- Why rounding continuous solutions doesn't always work
- How to assess solution quality for integer problems

**Key Learning**: Integer solutions must be validated for practicality. Rounding continuous solutions doesn't always work, and integer solutions may be suboptimal compared to continuous relaxations.

[📓 Open in Jupyter](./lesson07_concept05_interpreting_integer_solutions.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson07/lesson07_concept05_interpreting_integer_solutions.ipynb)

---

### Notebook 6: Over-constraining with Integers
**File**: `lesson07_concept06_over_constraining_with_integers.ipynb`

This notebook explores how integer constraints can make problems infeasible. You'll see:
- How adding integer constraints reduces feasible space
- When integer constraints cause infeasibility
- How to relax constraints when necessary

**Key Learning**: Integer constraints can make problems infeasible by reducing the feasible space. Sometimes relaxing integer constraints is necessary to find feasible solutions.

[📓 Open in Jupyter](./lesson07_concept06_over_constraining_with_integers.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson07/lesson07_concept06_over_constraining_with_integers.ipynb)

---

### Notebook 7: Comprehensive Discrete Example
**File**: `lesson07_concept07_comprehensive_discrete_example.ipynb`

This notebook presents a complete example combining discrete concepts. You'll learn:
- How to model a realistic discrete problem
- Best practices for discrete modeling
- How to interpret and validate discrete solutions

**Key Learning**: Discrete modeling requires careful formulation and validation. A comprehensive example demonstrates best practices and common challenges.

[📓 Open in Jupyter](./lesson07_concept07_comprehensive_discrete_example.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson07/lesson07_concept07_comprehensive_discrete_example.ipynb)

---


# Lesson 8: Penalties and Goal Programming

Welcome to Lesson 8 of Prescriptive Analytics! This lesson explores how to handle multiple objectives and soft constraints using penalties and goal programming approaches.

## Learning Objectives

By the end of this lesson, you will understand:

- **Penalties in Practice**: How to use penalties to handle soft constraints and multiple objectives
- **Goal Programming Intuition**: How goal programming balances competing objectives
- **Stakeholder Conflicts**: How to model and resolve conflicts between stakeholders
- **Policy Realism**: How to ensure penalty-based solutions are realistic and implementable
- **Brittleness Demonstration**: How penalty-based solutions can be fragile
- **Penalty Sensitivity**: How sensitive solutions are to penalty values

## Core Concepts

### 1. Penalties in Practice
- Penalties convert soft constraints into objective terms
- Penalties allow tradeoffs between constraint violations and objectives
- Choosing penalty values is critical and challenging

### 2. Goal Programming Intuition
- Goal programming seeks to achieve target values for multiple objectives
- It minimizes deviations from goals
- It provides a structured way to balance competing objectives

### 3. Stakeholder Conflicts
- Different stakeholders have different objectives
- Models must balance competing stakeholder interests
- Penalties and goal programming help resolve conflicts

### 4. Policy Realism
- Penalty-based solutions must be realistic and implementable
- Solutions should align with organizational policies
- Validation ensures solutions make practical sense

### 5. Brittleness Demonstration
- Penalty-based solutions can be very sensitive to penalty values
- Small changes in penalties can cause large solution changes
- Understanding brittleness helps assess solution robustness

### 6. Penalty Sensitivity
- Solutions are sensitive to penalty values
- Choosing appropriate penalties is difficult
- Sensitivity analysis helps understand penalty impacts

## Notebooks

This lesson includes six interactive Jupyter notebooks. Each notebook is self-contained and includes extensive explanations, code examples, and visualizations.

### Notebook 1: Penalties in Practice
**File**: `lesson08_concept01_penalties_in_practice.ipynb`

This notebook demonstrates how to use penalties in optimization models. You'll learn:
- How penalties convert soft constraints into objectives
- How to choose penalty values
- When to use penalties versus hard constraints

**Key Learning**: Penalties allow tradeoffs between constraint violations and objectives. Choosing appropriate penalty values is critical and challenging.

[📓 Open in Jupyter](./lesson08_concept01_penalties_in_practice.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson08/lesson08_concept01_penalties_in_practice.ipynb)

---

### Notebook 2: Goal Programming Intuition
**File**: `lesson08_concept02_goal_programming_intuition.ipynb`

This notebook introduces goal programming as an approach to multiple objectives. You'll see:
- How goal programming balances competing objectives
- How to set goals and minimize deviations
- How goal programming differs from single-objective optimization

**Key Learning**: Goal programming seeks to achieve target values for multiple objectives by minimizing deviations from goals. It provides a structured way to balance competing objectives.

[📓 Open in Jupyter](./lesson08_concept02_goal_programming_intuition.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson08/lesson08_concept02_goal_programming_intuition.ipynb)

---

### Notebook 3: Stakeholder Conflicts
**File**: `lesson08_concept03_stakeholder_conflicts.ipynb`

This notebook explores how to model and resolve conflicts between stakeholders. You'll learn:
- How different stakeholders have different objectives
- How to balance competing stakeholder interests
- How penalties and goal programming help resolve conflicts

**Key Learning**: Different stakeholders have different objectives. Models must balance competing interests, and penalties/goal programming provide tools to do this.

[📓 Open in Jupyter](./lesson08_concept03_stakeholder_conflicts.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson08/lesson08_concept03_stakeholder_conflicts.ipynb)

---

### Notebook 4: Policy Realism
**File**: `lesson08_concept04_policy_realism.ipynb`

This notebook demonstrates how to ensure penalty-based solutions are realistic. You'll see:
- How to validate that solutions align with policies
- How to ensure solutions are implementable
- How to balance optimization with policy requirements

**Key Learning**: Penalty-based solutions must be realistic and implementable. Solutions should align with organizational policies and be validated for practicality.

[📓 Open in Jupyter](./lesson08_concept04_policy_realism.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson08/lesson08_concept04_policy_realism.ipynb)

---

### Notebook 5: Brittleness Demonstration
**File**: `lesson08_concept05_brittleness_demonstration.ipynb`

This notebook demonstrates how penalty-based solutions can be fragile. You'll learn:
- How solutions change with penalty values
- Why solutions can be brittle
- How to identify and address brittleness

**Key Learning**: Penalty-based solutions can be very sensitive to penalty values. Small changes in penalties can cause large solution changes, making solutions brittle.

[📓 Open in Jupyter](./lesson08_concept05_brittleness_demonstration.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson08/lesson08_concept05_brittleness_demonstration.ipynb)

---

### Notebook 6: Penalty Sensitivity
**File**: `lesson08_concept06_penalty_sensitivity.ipynb`

This notebook explores how sensitive solutions are to penalty values. You'll see:
- How to perform sensitivity analysis on penalties
- How to identify critical penalty values
- How to choose robust penalty values

**Key Learning**: Solutions are sensitive to penalty values. Sensitivity analysis helps understand penalty impacts and choose robust penalty values.

[📓 Open in Jupyter](./lesson08_concept06_penalty_sensitivity.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson08/lesson08_concept06_penalty_sensitivity.ipynb)

---


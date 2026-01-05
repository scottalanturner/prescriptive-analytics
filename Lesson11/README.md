# Lesson 11: Simulation and Risk Analysis

Welcome to Lesson 11 of Prescriptive Analytics! This lesson combines optimization with simulation to test solutions under uncertainty and assess risk.

## Learning Objectives

By the end of this lesson, you will understand:

- **Simulation as Risk Testing**: How simulation tests solutions under uncertainty
- **Deterministic Risks**: Risks that exist even in deterministic models
- **Monte Carlo Intuition**: How Monte Carlo simulation works and why it's useful
- **Interpreting Simulation Outputs**: How to understand and communicate simulation results
- **Optimization Plus Simulation**: How to combine optimization with simulation
- **Robust vs Fragile Solutions**: How to identify solutions that work well under uncertainty
- **Visualizing Plans vs Histories**: How to compare planned outcomes with actual results
- **Visualization Types**: Different ways to visualize simulation results
- **AI Assistance Validation**: How to validate AI-assisted optimization solutions
- **Bias in AI Suggestions**: How to identify and address bias in AI-generated solutions

## Core Concepts

### 1. Simulation as Risk Testing
- Simulation tests solutions under uncertainty
- It reveals how solutions perform in different scenarios
- It helps assess risk and identify vulnerabilities

### 2. Deterministic Risks
- Risks exist even in deterministic models
- Parameter uncertainty creates risk
- Understanding deterministic risks helps assess solution reliability

### 3. Monte Carlo Intuition
- Monte Carlo simulation samples from probability distributions
- It generates many scenarios to assess outcomes
- It provides probabilistic insights into solution performance

### 4. Interpreting Simulation Outputs
- Simulation produces distributions of outcomes
- Understanding these distributions is critical
- Results must be communicated clearly

### 5. Optimization Plus Simulation
- Optimization finds good solutions
- Simulation tests solutions under uncertainty
- Combining both provides robust solutions

### 6. Robust vs Fragile Solutions
- **Robust**: Solutions that work well across scenarios
- **Fragile**: Solutions that break down under uncertainty
- Preferring robust solutions when uncertainty is high

### 7. Visualizing Plans vs Histories
- Comparing planned outcomes with actual results
- Understanding gaps between plans and reality
- Learning from differences to improve models

### 8. Visualization Types
- Different visualizations serve different purposes
- Choosing the right visualization aids understanding
- Effective visualization communicates insights clearly

### 9. AI Assistance Validation
- AI-assisted solutions must be validated
- Checking for errors, biases, and unrealistic results
- Ensuring AI suggestions are implementable

### 10. Bias in AI Suggestions
- AI systems can introduce bias
- Identifying and addressing bias is critical
- Ensuring fair and unbiased recommendations

## Notebooks

This lesson includes ten interactive Jupyter notebooks. Each notebook is self-contained and includes extensive explanations, code examples, and visualizations.

### Notebook 1: Simulation as Risk Testing
**File**: `lesson11_concept01_simulation_as_risk_testing.ipynb`

This notebook introduces simulation as a tool for testing solutions under uncertainty. You'll learn:
- How simulation tests solutions in different scenarios
- How simulation reveals risks and vulnerabilities
- Why simulation complements optimization

**Key Learning**: Simulation tests solutions under uncertainty, revealing how solutions perform in different scenarios and helping assess risk.

[📓 Open in Jupyter](./lesson11_concept01_simulation_as_risk_testing.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson11/lesson11_concept01_simulation_as_risk_testing.ipynb)

---

### Notebook 2: Deterministic Risks
**File**: `lesson11_concept02_deterministic_risks.ipynb`

This notebook explores risks that exist even in deterministic models. You'll see:
- How parameter uncertainty creates risk
- Why deterministic models have risks
- How to assess deterministic risks

**Key Learning**: Risks exist even in deterministic models. Parameter uncertainty creates risk, and understanding this helps assess solution reliability.

[📓 Open in Jupyter](./lesson11_concept02_deterministic_risks.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson11/lesson11_concept02_deterministic_risks.ipynb)

---

### Notebook 3: Monte Carlo Intuition
**File**: `lesson11_concept03_monte_carlo_intuition.ipynb`

This notebook explains how Monte Carlo simulation works. You'll learn:
- How Monte Carlo simulation samples from distributions
- Why Monte Carlo simulation is useful
- How to interpret Monte Carlo results

**Key Learning**: Monte Carlo simulation samples from probability distributions to generate many scenarios. This provides probabilistic insights into solution performance.

[📓 Open in Jupyter](./lesson11_concept03_monte_carlo_intuition.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson11/lesson11_concept03_monte_carlo_intuition.ipynb)

---

### Notebook 4: Interpreting Simulation Outputs
**File**: `lesson11_concept04_interpreting_simulation_outputs.ipynb`

This notebook demonstrates how to interpret simulation results. You'll see:
- How to understand distributions of outcomes
- How to identify key insights from simulation
- How to communicate simulation results effectively

**Key Learning**: Simulation produces distributions of outcomes. Understanding these distributions is critical for assessing solution performance and communicating results.

[📓 Open in Jupyter](./lesson11_concept04_interpreting_simulation_outputs.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson11/lesson11_concept04_interpreting_simulation_outputs.ipynb)

---

### Notebook 5: Optimization Plus Simulation
**File**: `lesson11_concept05_optimization_plus_simulation.ipynb`

This notebook demonstrates how to combine optimization with simulation. You'll learn:
- How optimization finds good solutions
- How simulation tests solutions under uncertainty
- How combining both provides robust solutions

**Key Learning**: Optimization finds good solutions; simulation tests them under uncertainty. Combining both provides robust solutions that work well across scenarios.

[📓 Open in Jupyter](./lesson11_concept05_optimization_plus_simulation.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson11/lesson11_concept05_optimization_plus_simulation.ipynb)

---

### Notebook 6: Robust vs Fragile Solutions
**File**: `lesson11_concept06_robust_vs_fragile_solutions.ipynb`

This notebook explores how to identify robust versus fragile solutions. You'll see:
- How to identify robust solutions
- How to identify fragile solutions
- When to prefer robust over optimal

**Key Learning**: Robust solutions work well across scenarios; fragile solutions break down under uncertainty. When uncertainty is high, robust solutions are often preferable.

[📓 Open in Jupyter](./lesson11_concept06_robust_vs_fragile_solutions.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson11/lesson11_concept06_robust_vs_fragile_solutions.ipynb)

---

### Notebook 7: Visualizing Plans vs Histories
**File**: `lesson11_concept07_visualizing_plans_vs_histories.ipynb`

This notebook demonstrates how to compare planned outcomes with actual results. You'll learn:
- How to visualize planned versus actual outcomes
- How to understand gaps between plans and reality
- How to learn from differences to improve models

**Key Learning**: Comparing planned outcomes with actual results reveals gaps and helps improve models. Understanding these differences is essential for continuous improvement.

[📓 Open in Jupyter](./lesson11_concept07_visualizing_plans_vs_histories.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson11/lesson11_concept07_visualizing_plans_vs_histories.ipynb)

---

### Notebook 8: Visualization Types
**File**: `lesson11_concept08_visualization_types.ipynb`

This notebook explores different ways to visualize simulation results. You'll see:
- Different types of visualizations for simulation results
- When to use each visualization type
- How effective visualization communicates insights

**Key Learning**: Different visualizations serve different purposes. Choosing the right visualization aids understanding and communicates insights clearly.

[📓 Open in Jupyter](./lesson11_concept08_visualization_types.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson11/lesson11_concept08_visualization_types.ipynb)

---

### Notebook 9: AI Assistance Validation
**File**: `lesson11_concept09_ai_assistance_validation.ipynb`

This notebook demonstrates how to validate AI-assisted optimization solutions. You'll learn:
- How to check AI suggestions for errors
- How to validate that solutions are realistic
- How to ensure AI suggestions are implementable

**Key Learning**: AI-assisted solutions must be validated. Checking for errors, biases, and unrealistic results ensures solutions are implementable and reliable.

[📓 Open in Jupyter](./lesson11_concept09_ai_assistance_validation.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson11/lesson11_concept09_ai_assistance_validation.ipynb)

---

### Notebook 10: Bias in AI Suggestions
**File**: `lesson11_concept10_bias_in_ai_suggestions.ipynb`

This notebook explores how to identify and address bias in AI-generated solutions. You'll see:
- How AI systems can introduce bias
- How to identify bias in AI suggestions
- How to ensure fair and unbiased recommendations

**Key Learning**: AI systems can introduce bias. Identifying and addressing bias is critical for ensuring fair and unbiased recommendations.

[📓 Open in Jupyter](./lesson11_concept10_bias_in_ai_suggestions.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson11/lesson11_concept10_bias_in_ai_suggestions.ipynb)

---


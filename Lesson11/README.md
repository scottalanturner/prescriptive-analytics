# Lesson 11: AI-Enhanced Prescriptive Analytics and Simulation

**Position in course:** Week 14 — final content lesson before project presentations  
**Theme:** Extending prescriptive analytics with simulation, AI/ML pipelines, generative AI tools, and ethical responsibility

---

## Learning Objectives

By the end of this lesson, students will be able to:

1. Use Monte Carlo simulation to test a decision against thousands of realistic scenarios and interpret the resulting outcome distribution
2. Apply an optimize-then-simulate workflow to stress-test a recommended plan and compare candidate decisions by reliability, not just expected value
3. Explain how ML predictions feed into prescriptive optimization models and identify where that pipeline can break down
4. Use generative AI (LLMs) as a modeling partner for formulation, interpretation, and communication — with appropriate human validation at each step
5. Apply a four-stage ethical audit framework to identify and address bias, constraint omission, and accountability gaps in AI-assisted decision systems

---

## Notebooks

One notebook per lesson section. Each teaches a single concept. The notebooks include **plain-language explanations** before each step (written for analytics students who are not programmers): what the code is computing, what to look for in the output, and how the charts support the decision story.

| # | File | Topic | Section |
|---|------|--------|---------|
| 1 | `lesson11_concept01_monte_carlo_simulation.ipynb` | Monte Carlo simulation for testing decisions under uncertainty | Section 1 |
| 2 | `lesson11_concept02_optimize_then_simulate.ipynb` | The optimize-then-simulate workflow; side-by-side plan comparison | Section 2 |
| 3 | `lesson11_concept03_ml_prescriptive_workflows.ipynb` | ML demand forecasting feeding inventory optimization; the handoff problem | Section 3 |
| 4 | `lesson11_concept04_genai_modeling_partner.ipynb` | GenAI as formulation, interpretation, and communication assistant; validation rule | Section 4 |
| 5 | `lesson11_concept05_ethical_considerations.ipynb` | Bias in AI-assisted hiring; four-stage ethical audit; fairness constraints | Section 5 |

### Open in Jupyter or Google Colab

Use the same Colab URL pattern as other lessons: `main` branch on `scottalanturner/prescriptive-analytics`.

| # | Jupyter (local) | Google Colab |
|---|-----------------|--------------|
| 1 | [Open notebook](./lesson11_concept01_monte_carlo_simulation.ipynb) | [Open in Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson11/lesson11_concept01_monte_carlo_simulation.ipynb) |
| 2 | [Open notebook](./lesson11_concept02_optimize_then_simulate.ipynb) | [Open in Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson11/lesson11_concept02_optimize_then_simulate.ipynb) |
| 3 | [Open notebook](./lesson11_concept03_ml_prescriptive_workflows.ipynb) | [Open in Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson11/lesson11_concept03_ml_prescriptive_workflows.ipynb) |
| 4 | [Open notebook](./lesson11_concept04_genai_modeling_partner.ipynb) | [Open in Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson11/lesson11_concept04_genai_modeling_partner.ipynb) |
| 5 | [Open notebook](./lesson11_concept05_ethical_considerations.ipynb) | [Open in Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson11/lesson11_concept05_ethical_considerations.ipynb) |

---

## Notebook Summaries

### concept01 — Monte Carlo Simulation

**Scenario:** Hospital shift staffing — how many nurses per shift?  
**Teaches:** The difference between a deterministic model (one answer) and Monte Carlo simulation (a distribution of outcomes). Students run 1,000 demand scenarios across four staffing levels, read the resulting distributions, and use tail risk (P5, P95) alongside mean cost to make a risk-informed staffing decision.  
**Key concepts:** Deterministic vs. simulation, outcome distribution, tail risk, when to use simulation  
**Packages:** numpy, matplotlib, pandas

---

### concept02 — Optimize Then Simulate

**Scenario:** Weekly production planning with uncertain demand  
**Teaches:** The two-step workflow: optimize first (get a principled starting point), then simulate (test robustness under uncertainty). Students compare three candidate production plans — lean, optimal, and buffered — under the same 1,000 demand scenarios and learn that mean outcome alone is not the whole story.  
**Key concepts:** Optimize-then-simulate pipeline, side-by-side plan comparison, tail risk vs. mean, common mistakes  
**Packages:** numpy, matplotlib, pandas, pulp

---

### concept03 — ML in Prescriptive Workflows

**Scenario:** Grocery store inventory optimization fed by a demand forecast model  
**Teaches:** How ML predictions (demand forecasts, risk scores) become optimization inputs — and what happens when those predictions are wrong. Students train a simple linear regression forecast, feed the point forecast into an inventory optimizer, observe the "handoff problem" when the forecast is off, and then improve the process by passing forecast uncertainty into simulation.  
**Key concepts:** Data → ML prediction → optimization → recommendation pipeline, handoff problem, end-to-end validation, what ML cannot do  
**Packages:** numpy, matplotlib, pandas, scikit-learn, pulp

---

### concept04 — GenAI as a Modeling Partner

**Scenario:** Call center staffing optimization  
**Teaches:** Three practical GenAI roles — formulation assistant (translating a business problem into model components), interpretation assistant (explaining model output in plain English), and communication assistant (drafting stakeholder memos). Each role is demonstrated with a simulated LLM response followed by a structured human validation step showing what the LLM got right and wrong.  
**Key concepts:** Formulation / interpretation / communication roles, validation rule, trust-but-verify, professional GenAI competency  
**Packages:** numpy, matplotlib, pandas, pulp  
**Note:** LLM responses are simulated as pre-written text; no API key required.

---

### concept05 — Ethical Considerations

**Scenario:** AI-assisted hiring — ML scoring + optimization for interview slot allocation  
**Teaches:** How bias in historical hiring data propagates through an ML model into an optimization recommendation, producing discriminatory outcomes even when group membership is not an explicit model input. Students observe the biased pipeline in action, apply a four-stage ethical audit framework, then add a fairness constraint and compare outcomes with and without it.  
**Key concepts:** Bias in training data, disparate impact, four-stage ethical audit (before / during / after / AI-specific), fairness constraints, constraint omission as an ethical choice, human accountability  
**Packages:** numpy, matplotlib, pandas, pulp

---

## Deduplication Notes

The following topics are covered in earlier lessons and are deliberately excluded from Lesson 11 notebooks:

- Sensitivity / what-if analysis → Lesson 5
- Robust vs. fragile decisions as a standalone concept → Lesson 5
- General model validation techniques → Lesson 5
- Gantt charts → Lesson 9
- Sankey diagrams → Lesson 6
- Visualization types as a standalone topic → not repeated in Lesson 11

Where Lesson 11 builds on prior material, the connection is noted explicitly in notebook introductions so students see continuity rather than repetition.

---

## Files to Remove

The following old notebooks are superseded and should be deleted:

- `lesson11_concept01_simulation_as_risk_testing.ipynb`
- `lesson11_concept02_deterministic_risks.ipynb`
- `lesson11_concept03_monte_carlo_intuition.ipynb`
- `lesson11_concept04_interpreting_simulation_outputs.ipynb`
- `lesson11_concept05_optimization_plus_simulation.ipynb`
- `lesson11_concept06_robust_vs_fragile_solutions.ipynb`
- `lesson11_concept07_visualizing_plans_vs_histories.ipynb`
- `lesson11_concept08_visualization_types.ipynb`
- `lesson11_concept09_ai_assistance_validation.ipynb`
- `lesson11_concept10_bias_in_ai_suggestions.ipynb`

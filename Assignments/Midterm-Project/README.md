# Mid-Term Project: Multi-Constraint Portfolio Allocation

## Overview

This mid-term project asks you to design and solve a realistic prescriptive analytics problem in your own professional field. You will choose an allocation decision, create a synthetic dataset with 8–10 options, build a multi-constraint optimization model, explore near-optimal alternatives, run deep sensitivity analysis and validation, then respond to two stakeholder changes of mind. You will turn in one Jupyter notebook with clear documentation and an executive summary suitable to hand off to a manager.

This project builds directly on Assignment 2. The modeling approach is the same (PuLP, continuous variables), but every dimension is larger: more options, more constraints, deeper analysis, and more stakeholder engagement.

## Learning Objectives

- Identify a resource allocation decision in your field with multiple competing constraints
- Create and document a synthetic dataset (8–10 options, 3 constraint parameters) using an LLM
- Distinguish decision variables vs inputs; document 5 key parameters with uncertainty sources
- Build a multi-constraint PuLP model (budget cap + category coverage + concentration cap); handle infeasibility if it arises
- Identify two near-optimal alternative solutions and explain why a stakeholder might prefer them
- Perform sensitivity analysis across 5 parameters at ±20% **and** ±40%; identify the most critical
- Test extreme values; run one what-if scenario
- Apply validation: 2–3 sanity checks; fragile vs. robust assessment
- Respond to **two** stakeholder changes of mind; produce a three-way comparison visualization
- Communicate all findings in an executive summary suitable for a non-technical decision-maker

## Assignment Structure

### Part 1: Problem Framing and Dataset
- Decision statement, decision variables vs inputs
- All constraints labeled as hard with explanation
- Synthetic dataset (8–10 options, 4 columns including a category field)
- 5 key parameters with uncertainty (source, why it might differ, magnitude)

### Part 2: Optimization Model and Near-Optimal Exploration
- Multi-constraint PuLP model (3 constraints): solve and interpret
- Feasibility check: if infeasible, diagnose and relax; report the tradeoff
- Two near-optimal alternatives within 5–10% of optimal; explain why a stakeholder might prefer each
- One visualization of the base solution

### Part 3: Sensitivity Analysis and Validation
- Vary 5 parameters at ±20% **and** ±40%; tornado/summary chart; most critical parameter identified
- Extreme value testing: test at the absolute plausible limits
- One additional what-if scenario
- 2–3 sanity checks (pass/fail); fragile vs. robust assessment

### Part 4: Two Stakeholder Changes of Mind
- **Change 1 (Constraint change):** A new hard constraint is imposed; update model, solve, check feasibility
- **Change 2 (Objective or scope change):** Goal or scope shifts; update model, solve
- Three-way comparison visualization (base vs. Change 1 vs. Change 2)
- Impact analysis for each change

### Part 5: Executive Summary
- 400–700 words; professional write-up for a non-technical decision-maker
- Covers: decision and model, near-optimal alternatives, most critical uncertainty, both stakeholder changes, final recommendation with caveats
- At least two figure references

## Choose Your Context

Pick **one** context for your allocation problem (do not reuse Assignment 1 or Assignment 2's context):

| Context | What you allocate | Category grouping | Example objective |
|---------|-------------------|-------------------|-------------------|
| **Marketing** | Ad spend across 8–10 channels | Paid / Organic / Brand | Maximize total expected reach or conversions |
| **Healthcare** | Staff hours or program funding | Preventive / Acute / Chronic | Maximize patient outcomes or coverage |
| **Tech / Product** | Engineering time across initiatives | Core / Growth / Exploratory | Maximize expected product value delivered |
| **Nonprofit / Govt** | Grant dollars across programs | Population group or region | Maximize beneficiaries reached |
| **Finance / Investing** | Capital across opportunities | Asset class or sector | Maximize expected return |
| **Operations / Logistics** | Resources across locations or shifts | Region or shift type | Maximize service coverage |
| **Generic** | Budget or hours across options | Any three logical groupings | Maximize total benefit |

## Creating Your Synthetic Dataset

There is no provided dataset. You will **create a synthetic dataset** using a language model (ChatGPT, Claude, or Copilot). Your dataset must have **8–10 rows** (one per option) and **4 columns**:

1. **option** — name or label for each option (e.g. "Channel_A", "Program_ICU")
2. **category** — which of 3 logical groups this option belongs to (e.g. "Paid", "Organic", "Brand")
3. **benefit_rate** — the expected return per dollar (or hour, or unit) allocated; this is the coefficient in your objective function. Use a decimal (e.g. 0.04 = 4% return).
4. **[your_field_column]** — one additional numeric attribute meaningful in your field (e.g. quality_score, risk_rating, reach_index, priority_score). You will use this in your parameter uncertainty table.

You will also get **three global constraint values** from the LLM — set these in your notebook code, not in the CSV:

- `budget_total` — total resource available (e.g. $50,000 or 1,000 staff-hours)
- `min_alloc_per_category` — minimum each category must receive (ensures balanced coverage)
- `concentration_cap` — maximum fraction any single option can receive (e.g. 0.35 means no option gets more than 35% of total budget)

**Step-by-step LLM prompt:**

1. Open a **new** conversation with ChatGPT, Claude, or Copilot.
2. Say: "I need a synthetic dataset for a prescriptive analytics portfolio allocation problem. I will use Python (pandas, PuLP). I need the output as **CSV only**."
3. Tell it your field and context (e.g. "I am modeling marketing ad spend across channels").
4. Say: "Create a CSV with **exactly [8 or 9 or 10] rows** and these columns: option (name), category (one of exactly 3 groups: [name your 3 groups]), benefit_rate (decimal, realistic for my context), [your_field_column] (numeric, realistic). Use realistic but simple numbers. Also give me three constraint values: budget_total, min_alloc_per_category, concentration_cap. Output only the CSV and the three values; no other text."
5. Paste the CSV into your notebook. Set the three constraint values in code.
6. Document in one sentence that you used an LLM and what the dataset contains.

**Important:** Make sure `min_alloc_per_category × 3` is less than `budget_total`, and `concentration_cap × budget_total` is greater than `min_alloc_per_category`. If not, your model will be infeasible before you even start — adjust the values.

## Getting Started

### Option 1: Open in Google Colab (Recommended)

Click the link below to open the assignment notebook directly in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Assignments/Midterm-Project/assignment_template.ipynb)

**Direct Link:** [Open Mid-Term Notebook in Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Assignments/Midterm-Project/assignment_template.ipynb)

### Option 2: Run Locally

1. Clone or download this repository
2. Navigate to `Assignments/Midterm-Project/`
3. Install required packages:
   ```bash
   pip install pulp pandas matplotlib numpy
   ```
4. Open `assignment_template.ipynb` in Jupyter Notebook or JupyterLab

## Deliverables (What to Turn In)

- **Completed Jupyter Notebook** (`assignment_template.ipynb` or renamed with your name): All cells run in order with no errors; all TODOs completed; no placeholder text remaining. Your synthetic dataset (8–10 options) must be pasted into the notebook in the data cell—no separate CSV file is required.
- **GitHub repository**: notebook accessible via the link you submit
- **README in your repo**: your name, field chosen, and one-sentence description of your allocation problem
- **Submission**: GitHub repository link submitted through the course submission system

## Expectations: What to Check Before Submitting

Run through this checklist before you submit:

- **Is the Executive Summary complete?** All five subsections filled in (decision and model, near-optimal alternatives, sensitivity findings, stakeholder changes, final recommendation). No "[TODO]" remaining.
- **Does every figure have a title and labeled axes?** Every chart must have a clear title, labeled x- and y-axes, and a reference in the surrounding text ("As shown in the chart above…").
- **Are all three comparison charts present?** (1) Base solution visualization, (2) sensitivity summary chart, (3) three-way comparison of base vs. Change 1 vs. Change 2.
- **Did you check feasibility?** For each model solve, print and check the status. Do not interpret an Infeasible solution as if it were Optimal.
- **Is the notebook suitable to hand to a manager?** A non-technical reader should be able to follow the narrative cells and executive summary without reading the code.
- **Did you run all cells top to bottom?** Restart and run all before submitting.

The rubric used for grading is provided separately.

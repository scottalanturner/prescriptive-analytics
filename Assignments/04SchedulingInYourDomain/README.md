# Assignment 04: Scheduling in Your Domain

## Overview

This assignment asks you to apply **Lesson 9** scheduling ideas in **your own field**. You will choose a realistic workforce/resource scheduling problem, define time-indexed decisions and demand coverage requirements, build and solve a PuLP model, visualize the schedule, analyze a cost-vs-service tradeoff, and respond to one stakeholder constraint change.  

This assignment is designed to be focused and manageable: one primary scheduling model, one what-if tradeoff scenario, one stakeholder change, and one professional reflection.

## Learning Objectives

- Model a **time-based scheduling** problem with demand that varies across periods.
- Define decision variables indexed over **time periods or shifts**.
- Build and solve a **PuLP scheduling model** with coverage constraints and a cost objective.
- Produce a **Gantt-style or coverage visualization** using matplotlib.
- Explain the **cost-vs-service tradeoff** to a non-technical stakeholder.
- Respond to one **stakeholder constraint change** and compare before/after results.

## Assignment Structure

### Section 1: Choose Your Domain and Scheduling Problem
- Choose a domain/context and define what is being scheduled.
- Write a 2-4 sentence decision statement: what is scheduled, across what time periods, and to what objective.

### Section 2: Define the Schedule Structure
- Define time periods, resources, period demand, and objective.
- Create a synthetic demand table (6-8 time periods) using an LLM.
- Document in one sentence that you used an LLM and what the table contains.

### Section 3: Build and Solve the Scheduling Model
- Build a PuLP model with time-indexed decision variables.
- Add period-by-period coverage constraints and one capacity/resource limit.
- Solve, report status, and interpret the schedule in plain language.
- If infeasible, diagnose and relax one constraint.
- Create one visualization (Gantt-style schedule chart or coverage vs demand chart).

### Section 4: Cost vs Service Tradeoff Analysis
- Run one what-if scenario (e.g., tighter budget or higher coverage requirement).
- Compare base vs scenario in one table.
- Explain the cost-vs-service tradeoff in plain language for a non-technical manager.

### Section 5: Stakeholder Change and Reflection
- Choose one stakeholder change:
  - fairness constraint (no single resource handles more than X% of load), or
  - higher minimum coverage floor, or
  - objective change (cost minimization to service maximization).
- Update model, solve, and compare with one visualization.
- Write a 2-3 paragraph professional reflection on what changed and what you learned.

## Choose Your Context

Pick **one** context for your scheduling problem (**do not reuse a context from a prior assignment**):

| Context | What you schedule | Time unit | Example objective |
|--------|--------------------|-----------|-------------------|
| **Healthcare** | Nurse/staff coverage by shift | Shift or hour block | Meet patient demand at minimum staffing cost |
| **Retail / Service** | Front-line staff coverage | Hourly periods | Meet customer demand while controlling labor spend |
| **Operations / Logistics** | Dispatches, vehicles, or crews | Time windows or shifts | Minimize operating cost while meeting delivery coverage |
| **Project Management** | Task starts/assignments across teams | Day or week | Meet deadlines with balanced workload and cost |
| **Generic** | Any resource assigned across periods | Any repeating period | Balance service level and cost under constraints |

## Creating Your Synthetic Dataset

Because each student chooses a different context, there is no single provided dataset. You will create a synthetic table with **6-8 time periods** and at least these columns:

- `time_period`
- `demand_required`
- `cost_per_unit`

You may include additional columns if useful for your context.

Use a language model (ChatGPT, Claude, Copilot, etc.) with this process:

1. Open a **new** chat.
2. State your context and scheduling decision.  
   Example: "I am modeling staff scheduling for a retail store across 8 shifts."
3. Ask for a CSV with exactly 6-8 rows (one per time period), with columns:
   - `time_period`
   - `demand_required`
   - `cost_per_unit`
4. Ask for realistic but simple values, and request **CSV output only**.
5. Copy the CSV into the notebook and load with pandas.
6. In your notebook, include one sentence documenting that you used an LLM and what data it generated.

## Getting Started

### Option 1: Open in Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Assignments/04SchedulingInYourDomain/assignment_template.ipynb)

**Direct Link:** [Open Assignment in Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Assignments/04SchedulingInYourDomain/assignment_template.ipynb)

### Option 2: Run Locally

1. Clone or download this repository.
2. Navigate to `Assignments/04SchedulingInYourDomain/`.
3. Install required packages: `pip install pulp pandas matplotlib`
4. Open `assignment_template.ipynb` in Jupyter Notebook or JupyterLab.
5. Follow the notebook sections in order and complete all TODO prompts.

## Deliverables (What to Turn In)

- **Completed Jupyter Notebook** (`assignment_template.ipynb` or renamed copy):
  - All sections completed.
  - All code cells run top-to-bottom with no errors.
  - No leftover `[TODO]` placeholders in final narrative responses.
- **GitHub repository**:
  - Notebook committed and pushed.
  - Any saved data files included (if you created them).
  - Repository is accessible from the submitted link.
- **Submission**:
  - Submit the GitHub repository link through the course submission system.

## Expectations: What to Check Before Submitting

Run through this checklist before you submit:

- **Does the model solve without errors?** The base model and stakeholder-change model both run and return interpretable outputs (or you clearly diagnose infeasibility and relax one constraint).
- **Is your visualization complete and readable?** Your schedule chart has a clear title, labeled axes, and is referenced in your written interpretation.
- **Is the stakeholder change section complete?** You implemented one change, solved again, and compared before/after in both a figure/table and short analysis.
- **Is your writing executive-quality?** Plain language, professional tone, grammatically clean, and understandable to a non-technical manager.
- **Is your GitHub repo accessible and organized?** The notebook is present, runs cleanly, and the submitted repository link works.

The rubric used for grading is provided separately.

## Resources

- [PuLP Documentation](https://coin-or.github.io/pulp/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- Lesson 9 materials on scheduling, coverage, and cost-service tradeoffs

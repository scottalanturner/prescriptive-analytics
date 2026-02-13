# Assignment 02: Resource Allocation Under Uncertainty

## Overview

This assignment asks you to apply prescriptive analytics in **your own field**: you choose a resource allocation problem (e.g. ad spend across channels, credit across segments, staff across shifts), create a small synthetic dataset, build an optimization model, run sensitivity analysis and validation, then respond to a **stakeholder change of mind** with an updated model and comparison. You will turn in one Jupyter notebook with clear documentation and an executive summary suitable to hand off to a manager.

## Learning Objectives

- Identify a **resource allocation** decision in your field (what to allocate, across what options, to what objective).
- Distinguish **decision variables** vs **inputs/parameters**; list **3 key parameters** with uncertainty (source and why they might differ from reality).
- Perform **sensitivity analysis** (vary 3 parameters ±20%); identify which parameter is **most critical**.
- Run **one what-if scenario** (e.g. budget -20%, demand +20%) and compare to base.
- Apply **validation**: 1–2 **sanity checks** and a **robust vs fragile** assessment.
- **Part 2:** Respond to a **stakeholder change of mind** (e.g. new constraint, different objective, budget cut); update the model, compare Part 1 vs Part 2 solutions, and create a comparison visualization.
- Communicate results in an **elegant final write-up** suitable for a decision-maker.

## Assignment Structure

### Part 1: Base Analysis
- Create your synthetic dataset (CSV, 5 options) using the step-by-step in the notebook.
- Decision statement, decision variables vs inputs, objectives and constraints.
- Key parameters and uncertainty (table: name, source, why it might differ from reality).
- PuLP model: build, solve, interpret base solution.
- Sensitivity analysis: vary 3 parameters ±20%; identify most critical; **one sensitivity visualization**.
- One what-if scenario (e.g. budget -20%); compare to base.
- Validation: 1–2 sanity checks; robust vs fragile assessment.

### Part 2: Stakeholder Change of Mind
- Choose **one** scenario (e.g. budget cut 15–20%; minimum allocation to one option; different objective; new constraint such as “no option &gt; 40% of total”).
- Update the PuLP model and solve.
- **At least one comparison visualization** (Part 1 vs Part 2 allocation or objective).
- Impact analysis: what changed, why it matters, what you would brief the stakeholder.

### Executive Summary
- Professional write-up covering: key decision and model, sensitivity findings, validation, stakeholder change impact, final recommendation, key insights. No placeholders or [TODO] left.

## Choose Your Context

Pick **one** context for your allocation problem (do not reuse Assignment 1’s conference travel):

| Context | What you allocate | Limited resource | Example objective |
|--------|--------------------|------------------|--------------------|
| **Marketing** | Ad spend across channels | Total budget | Maximize conversions/reach |
| **Credit risk** | Credit/approval across segments | Capital or exposure limit | Balance return and risk |
| **Staff/operations** | Staff or shifts to meet demand | Headcount or hours | Meet requests at acceptable cost |
| **Baseball** | Playing time, lineup, or roster | Roster/salary cap/rules | Maximize runs or win probability |
| **Generic** | Budget or time across options | Budget or time cap | Maximize benefit |

## Creating Your Synthetic Dataset

There is no single provided dataset; your problem is field-specific. You will **create a synthetic (made-up) dataset** as **CSV** with **exactly 5 rows** (5 options) and one constraint value. Use a language model (e.g. ChatGPT, Claude, Copilot) following the **step-by-step instructions in the notebook** (what to ask for, how to request CSV, how to load it). Document in one sentence that you used an LLM and what the dataset contains (number of options, constraint name and value).

## Getting Started

### Option 1: Open in Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Assignments/02ResourceAllocationSensitivity/assignment_template.ipynb)

**Direct Link:** [Open Assignment in Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Assignments/02ResourceAllocationSensitivity/assignment_template.ipynb)

### Option 2: Run Locally

1. Clone or download this repository.
2. Navigate to `Assignments/02ResourceAllocationSensitivity/`.
3. Install required packages: `pip install pulp pandas matplotlib`
4. Open `assignment_template.ipynb` in Jupyter Notebook or JupyterLab.
5. Follow the notebook: create your synthetic CSV (or paste it into the data cell), then complete all parts.

## Deliverables (What to Turn In)

- **Completed Jupyter Notebook** (`assignment_template.ipynb` or the same notebook renamed with your name): All cells run in order with no errors; all TODOs completed (no bare “[TODO]” or empty prompts left).
- **GitHub repository**: The notebook and any data files (e.g. `options_data.csv` if you saved one) in the repo. Repository must be accessible via the link you submit.
- **README in the repo**: Your name and any notes (e.g. context chosen, how you generated the synthetic data). Optionally a one-line description of the project.
- **Submission**: The GitHub repository link submitted through the course submission system.

Nothing elset.

## Expectations: What to Check Before Submitting

Run through this checklist before you submit:

- **Is the Executive Summary there?** The final write-up section is complete, with all subsections filled in (key decision and model, sensitivity findings, validation, stakeholder change, final recommendation, key insights). No placeholder text or “[TODO]” left in the summary.
- **Are there grammatical errors?** Proofread the markdown and narrative cells (especially the Executive Summary and impact analysis). Fix spelling, punctuation, and sentence structure.
- **Are there formatting errors?** Headings, lists, and code output look correct. The notebook runs from top to bottom without errors. No broken or inconsistent formatting.
- **Is this in a format you would hand off to a manager?** The narrative is professional and clear. A reader could use the Executive Summary and key findings without reading the code. It is suitable to share with a non-technical stakeholder.
- **Are the graphics properly labeled and referenced in the text?** Every figure (sensitivity chart, Part 1 vs Part 2 comparison, etc.) has a clear title and axis labels. In the markdown or summary, each figure is referred to (e.g. “As shown in the sensitivity chart…”, “The comparison below…”). The reader knows what each graphic shows and why it matters.

The rubric used for grading is provided separately.

## Resources

- [PuLP Documentation](https://coin-or.github.io/pulp/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- Lesson 4 and Lesson 5 course materials (parameters, sensitivity, validation)



# Assignment 03: Logical Policy Mapping in Your Domain

## Overview

This assignment asks you to apply **Lesson 8** ideas to a decision problem in **your own field**. You will:

- Choose a context you care about (your current job, an industry you want to work in, a side project, etc.).
- Identify binary decisions (yes/no choices) in that context.
- Collect real or realistic **policies** that govern those decisions.
- Rewrite those policies as clear **IF–THEN rules**.
- Classify each rule as a type of **logical constraint** (activation, suppression, either-or, mutually exclusive, complementary).
- Build a simple **policy stack** table that shows which decisions trigger which policies.
- Reflect on **feasibility**, **policy conflicts**, and what “no feasible solution” would look like in your context.

You will turn in **one Jupyter notebook** with clear explanations. Light use of Python (mostly for tables) is expected, but the emphasis is on your **conceptual understanding** and the quality of your reasoning, not on math or coding.

## Learning Objectives

- Identify a realistic decision problem in your domain and describe **binary decision variables** (0/1 yes/no choices).
- Translate natural language **business policies** into explicit **IF–THEN rules**.
- Classify policies as **activation**, **suppression**, **either-or**, **mutually exclusive**, or **complementary** constraints.
- Build a **policy stack** view (decisions × policies) and reason about which rules apply where.
- Explain how combinations of logical constraints can create **tension** or **infeasibility**.
- Describe, in plain language, what “**no feasible solution**” would look like in your domain and which policies you might renegotiate or relax.

## Assignment Structure

The assignment notebook is organized into the following sections:

### Section 1: Choose Your Domain and Decision Problem

- Describe a decision problem from a domain you care about, for example:
  - **Healthcare**: staffing nurses across shifts and units.
  - **Marketing**: selecting campaigns or channels to run.
  - **Operations**: choosing which facilities, routes, or warehouses to operate.
  - **Education**: assigning courses or projects to students.
  - **Nonprofit / Public sector**: selecting programs or projects under limited resources.
- Write a short **decision statement** (2–4 sentences): what is being decided, and why it matters.
- List **5–8 binary decision variables**, each clearly defined as a yes/no choice (e.g., “Open facility A (1 = open, 0 = closed)”).

### Section 2: Collect and Rewrite Policies as IF–THEN Rules

- Write down **6–8 real or realistic policies** that apply to your decision problem. These can come from:
  - Company/industry rules, regulations, safety requirements.
  - Manager preferences that are treated like rules (“we never…”, “we always…”).
  - Operational realities (e.g., “if we run night shift, we must have a supervisor on-site”).
- For each policy:
  - Identify the **IF** (trigger condition).
  - Identify the **THEN** (required outcome).
  - Rewrite the policy as an explicit **IF–THEN** sentence.

### Section 3: Classify Logical Constraint Types

- For each IF–THEN rule from Section 2:
  - Classify the policy as one of:
    - **Activation** (IF A is chosen, THEN B must also be chosen).
    - **Suppression** (IF A is chosen, THEN B cannot be chosen).
    - **Either-or** (at least one of two options must be chosen).
    - **Mutually exclusive** (at most one of two options may be chosen).
    - **Complementary** (two options must be chosen together or not at all).
  - In 1–2 sentences, explain **why** you chose that type.
  - If there is potential ambiguity (e.g., “either-or” could be read as “exactly one”), briefly describe how you would clarify this with a policy owner.

### Section 4: Build a Policy Stack (Decisions × Policies)

- Create a small **policy stack table** where:
  - Rows are your **binary decisions** from Section 1.
  - Columns are your **policies** from Section 2.
  - Each cell indicates whether that decision is affected by that policy (for example, with an `X`, `1`, or short label).
- You can build this table using:
  - A **pandas DataFrame** in Python, or
  - A Markdown table (if you strongly prefer). Using pandas is recommended.
- In 1–2 paragraphs, interpret your policy stack:
  - Which decisions are **heavily constrained** (many policies apply)?
  - Which decisions are **lightly constrained** (few or no policies)?
  - Are there any **surprisingly unconstrained** decisions you might have missed?

### Section 5: Feasibility, Conflicts, and “No Feasible Solution”

- Using your policies and policy stack:
  - Identify at least **one pair or trio of policies** that could realistically **conflict** with each other or with resource limits.
  - Explain, in words, how these could make the model **infeasible** (no combination of 0/1 decisions satisfies all rules).
- Answer prompts such as:
  - What would “**no feasible solution**” look like in this context? Give a concrete example narrative.
  - If that happened, **which policy (or policies)** would you consider **relaxing, reinterpreting, or renegotiating** first, and why?
  - How would you explain this situation to a **non-technical stakeholder** (manager, director, etc.)?

### Section 6: Reflection

- Briefly reflect on:
  - Which part of the assignment was **most challenging**: identifying binary decisions, rewriting policies as IF–THEN, classifying constraint types, or reasoning about feasibility?
  - One thing you learned about how **real-world policies** interact when you try to model them precisely.

## Getting Started

### Option 1: Open in Google Colab

You can open the assignment notebook directly in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Assignments/03LogicalPolicyMapping/assignment_template.ipynb)

**Direct Link:**  
[Open Assignment in Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Assignments/03LogicalPolicyMapping/assignment_template.ipynb)

> Note: If this link does not work yet in your fork, you can open the notebook in Colab by uploading it or by using the “GitHub” tab in Colab and navigating to your repository.

### Option 2: Run Locally

1. Clone or download this repository.
2. Navigate to `Assignments/03LogicalPolicyMapping/`.
3. (Optional but recommended) Create and activate a virtual environment.
4. Install the required package:
   ```bash
   pip install pandas
   ```
5. Open `assignment_template.ipynb` in Jupyter Notebook, JupyterLab, or VS Code with the Jupyter extension.

## Deliverables (What to Turn In)

- **Completed Jupyter Notebook** (`assignment_template.ipynb` or a copy renamed with your name):
  - All sections are completed.
  - All Markdown prompts are answered in full sentences.
  - Any code cells you use (e.g., for the policy stack table) run without errors.
- **GitHub Repository**:
  - The notebook is committed and pushed to a repository you control.
  - The repository is accessible via the link you submit.
  - Include a short `README` in your repo with your name and a one-line description of your chosen domain.
- **Submission**:
  - Submit the GitHub repository link through the course submission system.

## Expectations: What to Check Before Submitting

Before you submit, check:

- **Clarity of your decision problem**:
  - Is your domain and decision statement clear to a reader unfamiliar with your field?
  - Are your binary decisions clearly defined as yes/no choices?
- **Quality of IF–THEN rules**:
  - Does each policy have a clearly identified IF (trigger) and THEN (required outcome)?
  - Are the rules written precisely enough that someone else could encode them?
- **Correctness and justification of constraint types**:
  - Did you classify each rule using the Lesson 8 categories?
  - Did you briefly explain why each type fits?
- **Completeness of the policy stack**:
  - Does your table cover all decisions and all policies?
  - Did you interpret what the stack tells you about your decision space?
- **Feasibility reasoning and explanation**:
  - Did you identify at least one potential conflict between policies?
  - Did you explain what “no feasible solution” would look like and how you would respond?
- **Professional communication**:
  - Writing is clear, grammatically correct, and suitable to share with a manager.
  - All prompts in the notebook are answered; no bare `[TODO]` markers remain.

If you meet these expectations, your work will be appropriate for the full credit available on this 5% assignment.


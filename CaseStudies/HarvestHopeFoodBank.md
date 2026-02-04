# Week 5 — Prescriptive Analytics in Practice

**Case Study: Harvest Hope Food Bank (Integer Programming in the Real World)**

**Read the paper:** <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3093136" target="_blank" rel="noopener noreferrer">Harvest Hope Food Bank Optimizes Its Promotional Strategy to Raise Donations Using Integer Programming</a>

---

## 📌 What This Week Is About

Up to this point in the course, we've focused on how to think about prescriptive analytics: how to frame decisions, define objectives, model constraints, and interpret optimization results.

This week, we shift from learning concepts in isolation to seeing how prescriptive analytics works in a real organization, with real constraints, real tradeoffs, and real consequences.

Instead of a live lecture, you will work through a long-form, in-depth industry case study that shows how optimization models are actually used in practice.

- **This is not about learning new math.**
- **This is about learning how prescriptive analytics fits into decision-making in the real world.**

---

## 📄 The Case Study You'll Read

You will read the following paper:

**<a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3093136" target="_blank" rel="noopener noreferrer">Harvest Hope Food Bank Optimizes Its Promotional Strategy to Raise Donations Using Integer Programming</a>**

This is a practitioner-oriented case study describing how a nonprofit organization used an optimization model to decide how to allocate a limited marketing budget across multiple promotional options in order to maximize donations.

The paper walks through:

- The decision problem
- The objectives and constraints
- The structure of the optimization model
- How results were interpreted
- How insights were communicated to decision-makers

---

## 🎯 Learning Objectives for This Week

By the end of this case study, you should be able to:

- Recognize how prescriptive analytics is applied in a real organization
- Identify the decision statement behind an optimization model
- Translate a business problem into:
  - Decision variables
  - Objectives
  - Constraints
- Understand why real-world models often differ from "clean" classroom examples
- Explain optimization results in plain English, as you would to a manager or executive
- Reflect on organizational adoption, limitations, and lessons learned

You are not expected to understand the algorithmic details or mathematical formulation.

---

## ✅ What You Already Know (and Will Use Here)

Everything you need conceptually for this reading has already been covered in Weeks 1–4.

As you read, you should actively look for:

### 1. The Decision Statement

You already know how to ask:

- What decision is being made?
- Who is making it?
- What are they trying to optimize?

This case has a clear decision at its core:

> How should a limited marketing budget be allocated across different promotional options to maximize donations?

### 2. Decision Variables

You've learned that decision variables represent choices the model is allowed to make.

In this case, those choices look like:

- Whether or not to run specific promotions
- How many promotional efforts to select
- Which combinations fit within the budget

Even if the paper uses formal language, your job is to recognize:

**"What are the actual choices being decided?"**

### 3. Objectives

You already know that prescriptive models optimize one or more objectives.

Here, the objective is intuitive:

- **Maximize expected donations** (or fundraising effectiveness)

As you read, ask:

- Is the objective clearly defined?
- Are there tradeoffs implied by that objective?

### 4. Constraints

You've learned that constraints reflect real-world limits.

This case includes constraints such as:

- Budget limits
- Operational rules
- Practical limitations on promotions

You should be able to identify these without any math.

---

## ⚠️ Things You Will See That We Have Not Covered Yet

There are a few concepts in the <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3093136" target="_blank" rel="noopener noreferrer">paper</a> that you are not expected to fully understand at this point. This is intentional.

### 1. "Integer Programming"

You will see the term **integer programming** used throughout the paper.

For now, think of it this way:

**Analogy:** Linear optimization lets you turn knobs smoothly. Integer optimization forces you to flip switches.

In earlier examples, models might:

- Allocate fractional resources
- Spread effort smoothly across options

In this case, many decisions are all-or-nothing:

- Run a promotion or don't
- Select a campaign or don't
- Choose whole units, not fractions

That's what "integer" means here: some decisions must be whole numbers or yes/no choices.

We will cover integer programming formally later in the course. For now, just understand **why** it's used, not **how** it works.

### 2. Solver or Algorithm Details

You may see references to:

- Optimization solvers
- Model formulation
- Technical implementation details

You are **not** responsible for understanding:

- How the algorithm works
- How the solver finds the solution
- Any mathematical notation

You can safely skim those sections and refocus on:

- The decision logic
- The insights produced
- The implications for the organization

### 3. Statistical or Estimation Components

The paper may reference:

- Estimates
- Forecasts
- Expected values

Treat these as **inputs** to the model, not the focus of the reading.

At this stage, what matters is:

- How those inputs influence decisions
- How uncertainty affects confidence in results

---

## 🧠 How to Read This Paper Productively

As you read the <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3093136" target="_blank" rel="noopener noreferrer">case study paper</a>, keep asking yourself:

- What decision problem is being solved?
- What constraints matter most in reality?
- What tradeoffs does the model force the organization to confront?
- What insights would not be obvious without the model?
- How would you explain the results to a non-technical stakeholder?

You should read the <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3093136" target="_blank" rel="noopener noreferrer">paper</a> as a **decision analyst**, not as a mathematician.

---

## 🧩 Why We're Doing This Now

This case study is meant to:

- Bridge the gap between theory and practice
- Show why real prescriptive analytics problems are messier than classroom examples
- Prepare you for more advanced models later in the course

By seeing an integer optimization case before learning the math, you'll better understand **why** those tools exist when we introduce them formally.

---

## ✅ Final Reassurance

If at any point you think:

> "I don't understand the math here"

**That's okay — you're not supposed to yet.**

If you can:

- Explain the decision
- Identify objectives and constraints
- Interpret the results in plain English

Then you are doing exactly what this week is designed to teach you.

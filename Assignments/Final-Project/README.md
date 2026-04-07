# Final Project: The Organizational Decision Playbook

**ISYS 320U Prescriptive Analytics — Final Project**
**Presentation Date:** April 21 (last day of class)
**Deliverables Due:** By 11:59 PM the night before presentations

---

## Overview

Your final project asks you to apply the full prescriptive analytics toolkit — everything from Lessons 1 through 10 — to a real decision problem in your own professional domain. You will build a working optimization model, test its assumptions, and present your findings to a fictional VP who will challenge you on your choices.

You will turn in two deliverables: a Jupyter notebook containing your full analysis, and a 5–8 slide presentation deck. **The notebook and the slides are graded separately.** The notebook is the technical record. The slides are the story. Do not share your notebook during the presentation.

---

## The Scenario

You have been asked by a VP at your organization (real or realistic) to evaluate a recurring decision problem and provide a data-driven recommendation. The VP is intelligent but not technical. They care about outcomes, tradeoffs, and confidence — not model structure or code. Your job is to build a credible analysis and present it clearly in 5–7 minutes.

---

## Learning Objectives

By completing this project, you will demonstrate that you can:

- Distinguish a prescriptive problem from a descriptive or predictive one and articulate why optimization applies (Lesson 1)
- Frame a business decision precisely: objectives, decision variables, constraints, and tradeoffs (Lesson 2)
- Build and solve a linear and/or integer optimization model using PuLP (Lessons 3, 4, 8)
- Connect model outputs to real-world implementation considerations (Lesson 5)
- Test model assumptions through sensitivity analysis and identify critical parameters (Lesson 6)
- Incorporate a time dimension into your analysis (Lesson 9)
- Identify where linear assumptions break down and explain the implications honestly (Lesson 10)

---

## Project Structure

### Section 1 — Why This Problem Is Prescriptive

Write 2–4 sentences placing your problem on the analytics continuum. Descriptive analytics tells you what has happened. Predictive analytics tells you what will happen. What is the decision that neither of those can make for you — and why does prescriptive analytics apply here?

Then write a crisp **decision statement**: who is deciding, what they are deciding, and what success looks like.

### Section 2 — Decision Framing

Define each of the following clearly. This is not optional detail — a weak framing produces a weak model.

- **Decision variables** — what the model controls (what choices can be made)
- **Objective** — what the model optimizes (maximize or minimize what, exactly?)
- **Constraints** — what limits the decision (hard limits that cannot be violated)
- **Key tradeoffs** — what competing goals create tension in this decision

### Section 3 — The Optimization Model

Build and solve a PuLP model that includes:

- A linear objective function
- At least two meaningful constraints that reflect real business rules
- **At least one integer or binary decision variable** — a yes/no or whole-number choice

Solve the model and interpret the result in plain language: what does the model recommend, and what does that mean in practice? If your model is infeasible, diagnose which constraints conflict, relax one with justification, and report the tradeoff.

### Section 4 — Sensitivity Analysis

Identify the three parameters you are least confident about. For each:

- Vary it by ±20% and show how the recommendation changes
- State whether the recommendation is robust or fragile to that parameter

End with 2–3 sentences answering: **how confident should the VP be in this recommendation, and under what conditions would it change?**

### Section 5 — Time Dimension

Show how your recommendation plays out over time. Approaches include:

- Your model already includes time periods — describe the resulting schedule or sequence
- Your recommendation is implemented in phases — show the rollout timeline
- Demand or constraints vary across periods — show how the model handles this

If time genuinely is not a factor in your problem, explain why in one paragraph, and describe the circumstances under which it would become relevant.

### Section 6 — Where This Model Simplifies Reality

Identify at least one relationship in your problem where the linear assumption is suspect. Where would you expect diminishing returns? Where does doubling an input *not* double the output?

You do not need to solve a nonlinear model. You do need to show that you understand where your model's assumptions would mislead a decision-maker if taken at face value. This section should feel like an honest caveat, not a checkbox.

### Section 7 — What the Organization Should Actually Do

A concrete recommendation for the VP. Not "the model says X." The format is:

> *I recommend [specific action], because [model finding]. Before acting, we should validate [1–2 key assumptions]. The first step is [concrete next action].*

This is the section that determines whether your analysis gets adopted or ignored.

---

## Deliverables

### Deliverable 1: Jupyter Notebook

Your complete analysis covering all seven sections. Submitted via GitHub.

- All cells run top-to-bottom without errors (restart and run all before submitting)
- All sections completed — no bare `[TODO]` markers remaining
- Writing is professional and manager-ready throughout
- Notebook includes at least one visualization (model output, sensitivity chart, or time dimension chart) with a clear title and labeled axes
- GitHub repository is accessible and includes a short README with your name and a one-line description of your decision problem

### Deliverable 2: Presentation Slides (5–8 slides)

Your slides tell the story to the VP. They are not a printout of your notebook. Submitted as PDF or PowerPoint via GitHub alongside the notebook.

**Required slide content** (you may combine adjacent slides or add one optional slide, but stay within 8 total):

1. **The Decision** — what problem, what organization, why it matters to the VP
2. **The Model** — what you built, what the key decisions and constraints are (no code — use a clean diagram or table)
3. **The Recommendation** — what the model says to do, supported by one clear visual
4. **What Could Change This** — your top 2–3 sensitivity findings
5. **How It Plays Out Over Time** — the time dimension
6. **Where This Model Has Limits** — your nonlinear and assumption caveats, stated honestly
7. **What We Should Do** — your concrete recommendation, key caveat, and first step

**Slide standards:**
- Every slide has a clear headline (a claim, not a label — "Cost Spikes If Demand Rises 20%" not "Sensitivity Analysis")
- Every chart has a title and labeled axes
- No slide has more than 6 bullet points; no bullet is a full paragraph
- If a slide would take more than 2 minutes to explain, split it

---

## The Presentation

**Format:** 5–7 minutes of presentation + 2 minutes of Q&A, delivered via Zoom screen share
**Share:** Your slides only — not your notebook
**Audience:** A VP who knows the organization but has not seen your analysis

**Lead with the recommendation, not the method.** Decision-makers want to know what to do before they want to know how you figured it out. Open with the problem and your conclusion, then build the supporting case in the middle slides, then close with the recommendation and next step.

**Prepare for Q&A.** The VP (your instructor) and your classmates will ask questions. At minimum, be ready to defend:

- Why your model's assumptions are reasonable
- Which finding surprised you most
- What you would do differently with more time or data

**What "briefing a VP" means in practice:** Avoid jargon. Never say "my objective function" — say "what the model is trying to minimize." Never say "binary variable" — say "a yes/no decision." The goal is for a non-technical person to fully understand what you recommend and why.

**Peer engagement — Blackboard discussion.** A class discussion thread will be open during presentations. After each presenter finishes and before the next begins, you have 2 minutes to post a reply to the thread with two things: (1) the presenter's recommendation in one sentence, and (2) one question or pushback you would raise. Do this for every classmate. This is graded on completion and counts toward your presentation score — see the rubric.

---

## Choosing Your Domain

Pick a decision problem in your current job, a prior role, or an industry you are targeting. You must be able to answer these three questions before you begin:

1. Who makes this decision?
2. What are they trying to optimize?
3. What are the real constraints they are working within?

**Do not reuse any context from Assignments 1, 2, 3, 4, or the Midterm.** This project should represent new analytical work.

---

## Expectations: What to Check Before Submitting

**Notebook checklist:**
- Does your decision statement fit in one or two sentences? If you need a paragraph, the framing is too vague.
- Does your model include at least one integer or binary variable? A purely continuous model does not fully demonstrate Lesson 8.
- Did you run sensitivity on three parameters and identify the most critical one?
- Is your time section substantive? A single sentence does not satisfy the requirement.
- Did you identify a nonlinear relationship honestly? A generic statement ("diminishing returns exist in most problems") does not count.
- Is your final recommendation concrete and specific?

**Slides checklist:**
- Would you be comfortable presenting these slides to a real executive?
- Does every chart have a title and labeled axes?
- Does your opening slide communicate the decision and why it matters in under 30 seconds?
- Does your closing slide end with a clear action, not a vague conclusion?
- Have you rehearsed the 5–7 minute timing at least once?

---

## Resources

- [PuLP Documentation](https://coin-or.github.io/pulp/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- Course materials: Lessons 1–10
- All prior assignment notebooks and midterm feedback

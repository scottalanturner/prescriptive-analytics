# Week 11 — Decision-Making Under Uncertainty and Scenario Analysis

---

## Overview

For the past several weeks, every model we have built assumed the future was known. You were given demand numbers, cost figures, and capacity limits — and you solved for the best answer.

Real decisions don't work that way.

Companies planning factory capacity don't know what demand will look like in five years. Retailers ordering inventory don't know which products will take off. Finance teams setting budgets don't know where the economy will be in Q3. When the inputs to a decision are genuinely uncertain, a model that assumes certainty will give you a precise answer — but it may be precisely wrong.

This week you will read three papers that address this challenge from three different angles: a strategic framework for classifying uncertainty and choosing the right response, a technical overview of how decision makers structure choices when outcomes are unknown, and a practitioner perspective from a University of Richmond faculty member on how uncertainty undermines confidence in analysis — and what to do about it.

Together these readings cover all five core topics for this week:

- Deterministic vs. uncertain decision environments
- Scenario-based decision modeling
- Risk-aware decision objectives
- Comparing strategies across multiple futures
- Limitations of deterministic optimization

---

## Readings

---

### Reading 1 — Strategy Under Uncertainty

**Courtney, Kirkland, and Viguerie | McKinsey Quarterly | 2000**

🔗 [Read online — free, login required](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/strategy-under-uncertainty)

This is one of the most widely cited practitioner frameworks ever written on the topic of decision-making when the future is unclear. The authors — all McKinsey strategists — lay out four distinct levels of uncertainty and explain how the right analytical approach changes depending on which level you're in.

Level 1 is a clear enough future where standard forecasting and deterministic optimization work just fine. Level 2 involves a small number of distinct possible futures — the scenario territory. Level 3 involves a range of possible futures. Level 4 is true ambiguity where even the range is unclear. Each level calls for different tools and different ways of framing the decision.

**What to focus on:** How does this framework change the way you think about the optimization models you have already built? Most of the work we have done in this course has assumed Level 1 conditions. This paper will help you see where that assumption breaks down — and what to do instead.

---

### Reading 2 — Decision Making Under Uncertain and Risky Situations

**Taghavifard, Khalili Damghani, and Tavakkoli Moghaddam | Society of Actuaries | 2009**

🔗 [Download PDF — free](https://www.soa.org/globalassets/assets/files/resources/essays-monographs/2009-erm-symposium/mono-2009-m-as09-1-damghani.pdf)

This paper was written for professionals at the Society of Actuaries Enterprise Risk Management Symposium — practitioners who need to understand how to structure decisions when outcomes are uncertain. It covers the full landscape: what makes a decision problem deterministic versus uncertain versus risky, how to define decision criteria when you don't know which future will arrive, and how to compare strategies systematically across multiple possible outcomes.

This is the most comprehensive of the three readings and the one that maps most directly onto the technical concepts for this week. It is also the most detailed.

> ⚠️ **Important note on the math in this paper:** You will encounter decision tables, formulas, and notation — particularly in the sections covering decision criteria such as maximin, maximax, Laplace, and Hurwicz. **You are not expected to master these formulas or work through the calculations.** Your goal is to understand what problem each criterion is trying to solve. Ask yourself: *What kind of decision-maker does this criterion describe? Is it cautious? Optimistic? Balanced?* The concepts are what matter here. The math is background context.

**What to focus on:** The distinction between certainty, uncertainty, and risk (pages 1–8). The different decision criteria and what each one says about how a decision-maker values risk versus reward. Why "maximize expected value" is not always the right objective.

---

### Reading 3 — Is Risk Analysis a Source of Misinformation? The Undermining Effects of Uncertainty on Credibility

**Shital Thekdi and Terje Aven | SSRN | 2022**

🔗 [Access on SSRN — free with a free SSRN account](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4130891)

**Note:** Shital Thekdi is Associate Professor of Analytics and Operations at the Robins School of Business here at the University of Richmond. This paper represents research being done in our own department.

This reading approaches uncertainty from a different angle than the first two. Rather than asking *how do we build better models under uncertainty*, it asks: *what happens when an analyst presents uncertain results to a decision-maker?* When a model produces a range of outcomes instead of a single answer — when the recommendation comes with caveats — does that uncertainty make the analysis more honest, or does it make it less credible and therefore less useful?

This is a real tension that every analyst faces. Stakeholders want clear answers. Models under uncertainty produce ranges and probabilities. The paper explores how uncertainty in analysis affects trust, communication, and ultimately whether the analysis gets used at all.

**What to focus on:** The tension between analytical honesty and practical persuasiveness. Why communicating uncertainty is harder than computing it. How this connects to the "interpretation and communication" themes from earlier in the course — particularly the Optimization Tradecraft paper from Week 5.

---

## Assignment

Assignments for this week are posted in Blackboard.

- **Reading Questions** — Submit written responses in Blackboard
- **Discussion Post** — Post and reply to classmates in the Discussion Board

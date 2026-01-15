# Assignment 01: Conference Travel Decision Analysis

## Overview

This assignment helps you apply decision framing concepts from Lesson 2 to make informed travel decisions for a business conference. You'll identify decision variables, distinguish objectives from constraints, classify constraints as hard vs soft, recognize tradeoffs, and build a PuLP optimization model.

## Learning Objectives

- Identify decision variables vs inputs
- Distinguish objectives from constraints
- Classify constraints as hard vs soft
- Recognize tradeoffs between competing goals
- Build a PuLP model to demonstrate understanding

## Assignment Structure

The assignment is divided into two parts:

### Part 1: Base Assignment
- Decision statement
- Decision variables vs inputs
- Objectives vs constraints
- Hard vs soft constraints
- Tradeoff analysis
- PuLP model implementation

### Part 2: Stakeholder Considerations
- Add one consideration from the provided list
- Create one industry-specific consideration
- Update your model to incorporate these considerations
- Analyze how they affect your decision

## Getting Started

### Option 1: Open in Google Colab (Recommended)

Click the link below to open the assignment notebook directly in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Assignments/01ConferenceTravelDecisionAnalysis/assignment_template.ipynb)

**Direct Link:** [Open Assignment in Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Assignments/01ConferenceTravelDecisionAnalysis/assignment_template.ipynb)

### Option 2: Run Locally

1. Clone or download this repository
2. Navigate to `Assignments/01ConferenceTravelDecisionAnalysis/`
3. Ensure you have the required packages installed:
   ```bash
   pip install pulp pandas matplotlib
   ```
4. Open `assignment_template.ipynb` in Jupyter Notebook or JupyterLab
5. The data files (`lodging_options.csv` and `flight_options.csv`) are included in this folder

## Data Files

The assignment uses two data files that are automatically downloaded when running in Colab, or are available locally:

- `lodging_options.csv` - Contains lodging options (hotels and Airbnbs) with costs, ratings, distances, and other attributes
- `flight_options.csv` - Contains flight options from various East Coast cities to Las Vegas with costs, durations, and stops

## Assignment Scenario

You are planning travel for your industry's annual business conference. Management wants good networking coverage and is cost-conscious. They value quality but understand budget constraints.

**Key Constraints:**
- Conference duration: 3 nights
- Budget limit: $1,500 (total for all attendees)
- Team size: 2-4 people (you decide optimal number based on stakeholder priorities)

## Submission Requirements

1. Complete all TODO sections in the notebook
2. Ensure all cells run without errors
3. Submit your completed notebook via GitHub:
   - Create a new repository (or use your existing class repository)
   - Push your completed notebook to the repository
   - Include a README.md file with your name and any notes
4. Submit the GitHub repository link through the course submission system

## Resources

- [PuLP Documentation](https://coin-or.github.io/pulp/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- Lesson 2 course materials on decision framing

## Questions?

If you have questions about the assignment, please:
1. Check the course materials and lesson notes
2. Review the example problems from class
3. Post questions in the course discussion forum
4. Contact your instructor during office hours

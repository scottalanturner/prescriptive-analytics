# Lesson 1: Introduction to Prescriptive Analytics

Welcome to Lesson 1 of Prescriptive Analytics! This lesson introduces the fundamental concepts that form the foundation of prescriptive analytics.

## Learning Objectives

By the end of this lesson, you will understand:

- **The Analytics Continuum**: How descriptive, predictive, and prescriptive analytics build on each other
- **Tradeoffs**: Why you can't have everything and how to visualize tradeoffs in decision-making
- **Objectives and Constraints**: How these shape recommendations and why the same data can lead to different recommendations

## Core Concepts

### 1. Analytics Continuum
- **Descriptive Analytics**: "What happened?" - Understanding past performance
- **Predictive Analytics**: "What will happen?" - Forecasting future outcomes
- **Prescriptive Analytics**: "What should we do?" - Recommending actions

### 2. Tradeoffs
- Resources are always limited
- Improving one objective often requires sacrificing another
- The best decisions balance competing objectives

### 3. Objectives and Constraints
- **Objectives**: What you're trying to achieve (maximize profit, minimize cost, etc.)
- **Constraints**: Limits you must respect (budget limits, capacity limits, etc.)
- Models recommend based on what you tell them - change objectives or constraints, and recommendations change

## Notebooks

This lesson includes three interactive Jupyter notebooks. Each notebook is self-contained and includes extensive explanations, code examples, and visualizations.

### Notebook 1: Analytics Continuum
**File**: `01_Analytics_Continuum.ipynb`

This notebook demonstrates the three types of analytics using a retail store scenario. You'll see how:
- Descriptive analytics reveals patterns in historical data
- Predictive analytics forecasts future outcomes
- Prescriptive analytics recommends specific actions

**Key Learning**: Understanding how the three types of analytics build on each other.

[📓 Open in Jupyter](./01_Analytics_Continuum.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO/blob/main/Lesson01%20Introduction/01_Analytics_Continuum.ipynb)

> **Note**: To use the Google Colab links, replace `YOUR_USERNAME` and `YOUR_REPO` with your GitHub username and repository name. Alternatively, you can upload the notebook directly to Google Colab.

---

### Notebook 2: Visualizing Tradeoffs
**File**: `02_Visualizing_Tradeoffs.ipynb`

This notebook explores the fundamental concept of tradeoffs in decision-making. Using a budget allocation scenario, you'll learn:
- What tradeoffs are and why they're unavoidable
- How to visualize tradeoffs between competing objectives
- How to find the optimal balance when resources are limited

**Key Learning**: You cannot optimize everything simultaneously - you must make choices about what to prioritize.

[📓 Open in Jupyter](./02_Visualizing_Tradeoffs.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO/blob/main/Lesson01%20Introduction/02_Visualizing_Tradeoffs.ipynb)

---

### Notebook 3: Objectives and Constraints
**File**: `03_Objectives_and_Constraints.ipynb`

This notebook demonstrates how objectives and constraints shape recommendations. You'll see:
- How changing objectives (e.g., maximize revenue vs. maximize profit) changes recommendations
- How constraints eliminate options and change the best choice
- Why the same data can lead to different recommendations

**Key Learning**: Models recommend based on what you tell them - your objectives and constraints determine the recommendation.

[📓 Open in Jupyter](./03_Objectives_and_Constraints.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO/blob/main/Lesson01%20Introduction/03_Objectives_and_Constraints.ipynb)

---

## How to Use These Notebooks

### Option 1: Local Jupyter Environment
1. Ensure you have Jupyter installed: `pip install jupyter pandas numpy matplotlib`
2. Navigate to this directory
3. Launch Jupyter: `jupyter notebook` or `jupyter lab`
4. Open the notebook you want to explore

### Option 2: Google Colab
1. Click the "Open in Google Colab" link above each notebook
2. **Note**: You'll need to update the GitHub URL in the links above with your actual repository path
3. Alternatively, upload the notebook file directly to Google Colab

### Option 3: Direct Upload to Colab
1. Go to [Google Colab](https://colab.research.google.com/)
2. Click "File" → "Upload notebook"
3. Select the notebook file from your computer

## Prerequisites

- Basic familiarity with Python (variables, data types, basic operations)
- No advanced Python knowledge required - the notebooks are designed for beginners
- Understanding of basic business concepts (revenue, profit, cost)

## Technical Requirements

The notebooks use the following Python libraries:
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical operations
- `matplotlib` - Data visualization

All libraries are standard and available in Google Colab by default.

## Getting Help

- Each notebook is self-contained with extensive explanations
- Code is broken into small, understandable chunks
- Markdown cells provide context and explanations
- If you encounter issues, check that all cells are run in order

## Next Steps

After completing these notebooks, you'll be ready to:
- Understand the role of prescriptive analytics in decision-making
- Recognize tradeoffs in business decisions
- Understand how objectives and constraints shape recommendations
- Apply these concepts to real-world scenarios

---

**Remember**: Prescriptive analytics is about decision-first thinking. Models recommend, but humans decide and explain. These notebooks help you understand how models work so you can use them effectively.

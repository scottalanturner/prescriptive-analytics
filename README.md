# Prescriptive Analytics Course

Welcome to the Prescriptive Analytics course! This course introduces you to the principles and practices of prescriptive analytics—the branch of analytics that focuses on recommending actions to achieve desired outcomes.

## About This Course

Prescriptive analytics goes beyond describing what happened (descriptive) or predicting what will happen (predictive). It answers the question: **"What should we do?"**

This course covers:
- Decision-first thinking and how models recommend while humans decide
- The analytics continuum and how prescriptive analytics builds on descriptive and predictive analytics
- Objectives, constraints, and tradeoffs in decision-making
- How to structure problems for prescriptive analytics
- Methods and techniques for optimization and decision support
- Real-world applications and case studies

## Course Philosophy

**"Models recommend; humans decide and explain."**

Prescriptive analytics is a tool to support decision-making, not replace it. Throughout this course, you'll learn to:
- Structure decision problems clearly
- Define objectives and constraints explicitly
- Interpret and evaluate recommendations
- Explain decisions to stakeholders
- Recognize when models are appropriate and when they're not

## Lessons

### [Lesson 1: Introduction to Prescriptive Analytics](./Lesson01/)

**Overview**: This lesson introduces the fundamental concepts of prescriptive analytics through hands-on examples and interactive notebooks.

**Topics Covered**:
- The Analytics Continuum (Descriptive → Predictive → Prescriptive)
- Visualizing Tradeoffs in Decision-Making
- How Objectives and Constraints Shape Recommendations

**Notebooks**: 3 notebooks covering analytics continuum, tradeoffs, and objectives/constraints.

[📚 Go to Lesson 1 →](./Lesson01/)

---

### [Lesson 2: Modeling Fundamentals](./Lesson02/)

**Overview**: This lesson covers the fundamental distinctions and concepts needed to build effective prescriptive models.

**Topics Covered**:
- Decision Variables vs Inputs
- Objectives vs Constraints
- Hard vs Soft Constraints
- Tradeoffs, Heuristics, and Solution Quality

**Notebooks**: 6 notebooks covering modeling fundamentals.

[📚 Go to Lesson 2 →](./Lesson02/)

---

### [Lesson 3: Understanding Optimization](./Lesson03/)

**Overview**: This lesson deepens your understanding of what optimization actually does and how to interpret optimization results.

**Topics Covered**:
- What Optimization Is
- Feasible vs Infeasible Problems
- Optimal vs Acceptable Solutions
- Interpreting Results

**Notebooks**: 6 notebooks covering optimization concepts and result interpretation.

[📚 Go to Lesson 3 →](./Lesson03/)

---

### [Lesson 4: Parameters and Data Quality](./Lesson04/)

**Overview**: This lesson focuses on understanding parameters, their sources, and how data quality impacts optimization results.

**Topics Covered**:
- Parameters as Settings
- Historical Data vs Reality
- Forecast Uncertainty
- Data Quality Impact

**Notebooks**: 8 notebooks covering parameters, uncertainty, and data quality.

[📚 Go to Lesson 4 →](./Lesson04/)

---

### [Lesson 5: Validation and Sensitivity Analysis](./Lesson05/)

**Overview**: This lesson focuses on validating optimization solutions and understanding their sensitivity to assumptions and parameters.

**Topics Covered**:
- Sensitivity Analysis
- What-If Analysis
- Fragile vs Robust Decisions
- Comprehensive Validation

**Notebooks**: 7 notebooks covering validation techniques and sensitivity analysis.

[📚 Go to Lesson 5 →](./Lesson05/)

---

### [Lesson 6: Network Optimization](./Lesson06/)

**Overview**: This lesson introduces network optimization, a powerful approach for modeling systems with flows, connections, and capacity constraints.

**Topics Covered**:
- Networks as Nodes and Links
- Flow and Capacity
- Bottlenecks
- Supply Chain Networks

**Notebooks**: 7 notebooks covering network optimization concepts and applications.

[📚 Go to Lesson 6 →](./Lesson06/)

---

### [Lesson 7: Discrete and Integer Optimization](./Lesson07/)

**Overview**: This lesson explores discrete and integer optimization, where decisions must be whole numbers or come from discrete sets.

**Topics Covered**:
- Discrete vs Continuous Decisions
- Integer Constraints
- Feasibility Challenges
- Interpreting Integer Solutions

**Notebooks**: 7 notebooks covering discrete optimization concepts and challenges.

[📚 Go to Lesson 7 →](./Lesson07/)

---

### [Lesson 8: Penalties and Goal Programming](./Lesson08/)

**Overview**: This lesson explores how to handle multiple objectives and soft constraints using penalties and goal programming approaches.

**Topics Covered**:
- Penalties in Practice
- Goal Programming
- Stakeholder Conflicts
- Penalty Sensitivity

**Notebooks**: 6 notebooks covering penalties, goal programming, and multi-objective optimization.

[📚 Go to Lesson 8 →](./Lesson08/)

---

### [Lesson 9: Scheduling and Time-Based Optimization](./Lesson09/)

**Overview**: This lesson focuses on scheduling problems, where time constraints, dependencies, and sequencing are critical.

**Topics Covered**:
- Time Constraints and Dependencies
- Supply-Demand Matching
- Cost vs Service Tradeoffs
- Schedule Robustness

**Notebooks**: 8 notebooks covering scheduling concepts and time-based optimization.

[📚 Go to Lesson 9 →](./Lesson09/)

---

### [Lesson 10: Nonlinear Optimization](./Lesson10/)

**Overview**: This lesson introduces nonlinear optimization, where relationships between variables are not linear.

**Topics Covered**:
- Linear vs Nonlinear
- Diminishing Returns
- Interpreting Nonlinear Models
- When to Use Nonlinear Models

**Notebooks**: 4 notebooks covering nonlinear optimization concepts.

[📚 Go to Lesson 10 →](./Lesson10/)

---

### [Lesson 11: Simulation and Risk Analysis](./Lesson11/)

**Overview**: This lesson combines optimization with simulation to test solutions under uncertainty and assess risk.

**Topics Covered**:
- Simulation as Risk Testing
- Monte Carlo Methods
- Robust vs Fragile Solutions
- AI Assistance Validation

**Notebooks**: 10 notebooks covering simulation, risk analysis, and AI validation.

[📚 Go to Lesson 11 →](./Lesson11/)

---

## Assignments

### [Assignment 1: Conference Travel Decision Analysis](./Assignments/01ConferenceTravelDecisionAnalysis/)

**Overview**: Apply decision framing from Lesson 2 to a conference travel decision: decision variables, objectives vs constraints, hard vs soft constraints, tradeoffs, and a PuLP optimization model.

[📋 Go to Assignment 1 →](./Assignments/01ConferenceTravelDecisionAnalysis/)

---

### [Assignment 2: Resource Allocation Under Uncertainty](./Assignments/02ResourceAllocationSensitivity/)

**Overview**: Apply prescriptive analytics in your own field: choose a resource allocation problem, create a synthetic dataset, build an optimization model, run sensitivity analysis and validation, then respond to a stakeholder change of mind with an updated model and comparison.

[📋 Go to Assignment 2 →](./Assignments/02ResourceAllocationSensitivity/)

---

## Getting Started

1. **Prerequisites**: Basic familiarity with Python is helpful but not required. The notebooks are designed to be accessible to beginners. See [Lesson 1 README](./Lesson01/README.md) for detailed setup instructions.

2. **Setup**: 
   - You can work with the notebooks locally using Jupyter
   - Or use Google Colab (links provided in each lesson's README)

3. **Recommended Path**: 
   - Start with Lesson 1
   - Work through lessons sequentially
   - Each lesson builds on previous concepts
   - Complete the exercises and reflect on the concepts

## Course Materials

- **Notebooks**: Interactive Jupyter notebooks with code examples and explanations
- **Slides**: Presentation materials for each lesson
- **Source Documents**: Design specifications and curriculum planning documents

## How to Use This Repository

1. Navigate to the lesson you want to study
2. Read the lesson's README for overview and learning objectives
3. Open the notebooks (locally or in Google Colab)
4. Work through the examples and exercises
5. Review the slides for additional context

## Contributing

This is a course repository. If you're a student, focus on learning from the materials. If you're an instructor or contributor, please follow the established structure and conventions.

## License

This course material is for educational purposes.

---

**Remember**: Prescriptive analytics is about making better decisions. The tools and techniques you'll learn are means to an end—helping you and your organization make more informed, effective decisions.


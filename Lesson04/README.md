# Lesson 4: Parameters and Data Quality

Welcome to Lesson 4 of Prescriptive Analytics! This lesson focuses on understanding parameters, their sources, and how data quality impacts optimization results.

## Learning Objectives

By the end of this lesson, you will understand:

- **Parameters as Settings**: How parameters configure optimization models
- **Historical Data vs Reality**: Why past data may not reflect future conditions
- **Forecast Uncertainty Cascades**: How uncertainty compounds through models
- **Parameter Sensitivity**: How sensitive solutions are to parameter changes
- **Deterministic Optimism**: Why deterministic models can be overly optimistic
- **Averages Hide Variation**: How using averages can mask important variation
- **Data Quality Impact**: How data quality affects solution quality
- **Parameter Source Tracking**: The importance of tracking where parameters come from

## Core Concepts

### 1. Parameters as Settings
- Parameters configure how models behave
- Understanding parameters helps you control model behavior
- Parameters come from various sources with different levels of uncertainty

### 2. Historical Data vs Reality
- Historical data describes the past, not necessarily the future
- Conditions change, making historical patterns unreliable
- Models based on historical data assume patterns will continue

### 3. Forecast Uncertainty Cascades
- Uncertainty in inputs propagates through models
- Small uncertainties can compound into large solution variations
- Understanding uncertainty helps assess solution reliability

### 4. Parameter Sensitivity
- Solutions may be very sensitive to some parameters
- Small parameter changes can cause large solution changes
- Identifying sensitive parameters helps focus data collection efforts

### 5. Deterministic Optimism
- Deterministic models assume perfect information
- This can lead to overly optimistic solutions
- Reality includes uncertainty that deterministic models ignore

### 6. Averages Hide Variation
- Using average values ignores important variation
- Variation can significantly impact solution quality
- Understanding variation helps assess solution robustness

### 7. Data Quality Impact
- Poor data quality leads to poor solutions
- Garbage in, garbage out applies to optimization
- Investing in data quality improves solution quality

### 8. Parameter Source Tracking
- Knowing where parameters come from helps assess reliability
- Different sources have different levels of confidence
- Tracking sources enables better uncertainty management

## Notebooks

This lesson includes eight interactive Jupyter notebooks. Each notebook is self-contained and includes extensive explanations, code examples, and visualizations.

### Notebook 1: Parameters as Settings
**File**: `lesson04_concept01_parameters_as_settings.ipynb`

This notebook demonstrates how parameters configure optimization models. You'll learn:
- What parameters are and how they work
- How parameters control model behavior
- How to identify and understand key parameters

**Key Learning**: Parameters are settings that configure how models behave. Understanding parameters helps you control and interpret model results.

[📓 Open in Jupyter](./lesson04_concept01_parameters_as_settings.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson04/lesson04_concept01_parameters_as_settings.ipynb)

---

### Notebook 2: Historical Data vs Reality
**File**: `lesson04_concept02_historical_data_vs_reality.ipynb`

This notebook explores why historical data may not reflect future conditions. You'll see:
- How historical patterns may not continue
- Why conditions change over time
- How to assess whether historical data is relevant

**Key Learning**: Historical data describes the past, not necessarily the future. Models based on historical data assume patterns will continue, which may not be true.

[📓 Open in Jupyter](./lesson04_concept02_historical_data_vs_reality.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson04/lesson04_concept02_historical_data_vs_reality.ipynb)

---

### Notebook 3: Forecast Uncertainty Cascades
**File**: `lesson04_concept03_forecast_uncertainty_cascades.ipynb`

This notebook demonstrates how uncertainty propagates through models. You'll learn:
- How uncertainty in inputs affects outputs
- How small uncertainties can compound
- How to assess the impact of uncertainty

**Key Learning**: Uncertainty in inputs propagates through models. Small uncertainties can compound into large solution variations, affecting solution reliability.

[📓 Open in Jupyter](./lesson04_concept03_forecast_uncertainty_cascades.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson04/lesson04_concept03_forecast_uncertainty_cascades.ipynb)

---

### Notebook 4: Parameter Sensitivity
**File**: `lesson04_concept04_parameter_sensitivity.ipynb`

This notebook explores how sensitive solutions are to parameter changes. You'll see:
- Which parameters have the most impact on solutions
- How to identify sensitive parameters
- How sensitivity analysis helps focus data collection

**Key Learning**: Solutions may be very sensitive to some parameters. Identifying sensitive parameters helps focus data collection and uncertainty management efforts.

[📓 Open in Jupyter](./lesson04_concept04_parameter_sensitivity.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson04/lesson04_concept04_parameter_sensitivity.ipynb)

---

### Notebook 5: Deterministic Optimism
**File**: `lesson04_concept05_deterministic_optimism.ipynb`

This notebook examines why deterministic models can be overly optimistic. You'll learn:
- How deterministic models assume perfect information
- Why this leads to optimistic solutions
- How reality differs from deterministic assumptions

**Key Learning**: Deterministic models assume perfect information, which can lead to overly optimistic solutions. Reality includes uncertainty that deterministic models ignore.

[📓 Open in Jupyter](./lesson04_concept05_deterministic_optimism.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson04/lesson04_concept05_deterministic_optimism.ipynb)

---

### Notebook 6: Averages Hide Variation
**File**: `lesson04_concept06_averages_hide_variation.ipynb`

This notebook demonstrates how using averages can mask important variation. You'll see:
- How averages summarize but hide detail
- Why variation matters for solution quality
- How to account for variation in models

**Key Learning**: Using average values ignores important variation. Variation can significantly impact solution quality and robustness.

[📓 Open in Jupyter](./lesson04_concept06_averages_hide_variation.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson04/lesson04_concept06_averages_hide_variation.ipynb)

---

### Notebook 7: Data Quality Impact
**File**: `lesson04_concept07_data_quality_impact.ipynb`

This notebook explores how data quality affects solution quality. You'll learn:
- How poor data leads to poor solutions
- Why garbage in, garbage out applies to optimization
- How to assess and improve data quality

**Key Learning**: Poor data quality leads to poor solutions. Investing in data quality improves solution quality and reliability.

[📓 Open in Jupyter](./lesson04_concept07_data_quality_impact.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson04/lesson04_concept07_data_quality_impact.ipynb)

---

### Notebook 8: Parameter Source Tracking
**File**: `lesson04_concept08_parameter_source_tracking.ipynb`

This notebook demonstrates the importance of tracking where parameters come from. You'll see:
- Why source tracking matters
- How different sources have different reliability
- How to manage uncertainty through source tracking

**Key Learning**: Knowing where parameters come from helps assess reliability. Tracking sources enables better uncertainty management and solution validation.

[📓 Open in Jupyter](./lesson04_concept08_parameter_source_tracking.ipynb) | [🔗 Open in Google Colab](https://colab.research.google.com/github/scottalanturner/prescriptive-analytics/blob/main/Lesson04/lesson04_concept08_parameter_source_tracking.ipynb)

---


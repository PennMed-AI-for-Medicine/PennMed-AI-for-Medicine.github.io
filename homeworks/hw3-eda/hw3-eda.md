---
layout: default
title: Homework 3 - Exploratory Data Analysis & Clinical Data
active_tab: homework
release_date: 2026-02-11
due_date: 2026-02-25 23:59:00EST
classroom_link: https://classroom.github.com/a/XXXXXX
---

<!-- Check whether the assignment is ready to release -->
{% capture today %}{{site.time | date: '%s'}}{% endcapture %}
{% capture release_date %}{{page.release_date | date: '%s'}}{% endcapture %}
{% if release_date > today %}
<div class="alert alert-danger">
Warning: this assignment is not yet released. Check back on {{ page.release_date | date: '%B %-d, %Y' }}.
</div>
{% endif %}
<!-- End check -->

<div class="alert alert-info">
This assignment is due on {{ page.due_date | date: "%A, %B %-d, %Y" }} before {{ page.due_date | date: "%I:%M%p" }}.
</div>

<div class="alert alert-success" markdown="1">
**Get Started:**
1. [**Accept the assignment on GitHub Classroom**]({{ page.classroom_link }}) — You'll get your own private repository with starter code and data
2. Clone your repo and complete the exercises in `hw3_eda.py`
3. Commit regularly as you work (this is part of your grade!)
4. Push your completed work to GitHub before the deadline
</div>

---

## Learning Objectives

By completing this assignment, you will:

- Perform systematic exploratory data analysis on clinical tabular data
- Handle missing values appropriately for medical datasets
- Create meaningful visualizations of clinical variables
- Engineer features from raw clinical measurements
- Understand class imbalance and its implications for medical prediction

---

## Background

Before building any predictive model, you must understand your data. In clinical settings, this is especially critical because:

- **Missing data is rarely random** — A missing lab value might mean the test wasn't ordered (patient seemed healthy) or the result was lost (different implications!)
- **Outliers might be real** — That blood pressure of 250 might be a typo, or it might be a hypertensive crisis
- **Class imbalance is the norm** — Most patients don't have the disease you're predicting
- **Domain knowledge matters** — Knowing that HbA1c > 6.5 indicates diabetes is more valuable than any statistical test

This assignment uses the **Pima Indians Diabetes Dataset**, a classic clinical prediction dataset. Your task is to explore it thoroughly before any modeling begins.

---

## The Dataset

The dataset contains diagnostic measurements from female patients of Pima Indian heritage, used to predict diabetes onset.

| Feature | Description | Units |
|---------|-------------|-------|
| Pregnancies | Number of pregnancies | count |
| Glucose | Plasma glucose concentration (2hr OGTT) | mg/dL |
| BloodPressure | Diastolic blood pressure | mm Hg |
| SkinThickness | Triceps skin fold thickness | mm |
| Insulin | 2-hour serum insulin | μU/mL |
| BMI | Body mass index | kg/m² |
| DiabetesPedigreeFunction | Genetic risk score | score |
| Age | Age | years |
| Outcome | Diabetes diagnosis (1=yes, 0=no) | binary |

---

## Instructions

### Part 1: Data Loading & Initial Exploration (20 points)

**1.1 Load and Inspect (8 pts)**
- Load the dataset using pandas
- Display basic info: shape, dtypes, first/last rows
- Calculate summary statistics for all features

**1.2 Identify Data Quality Issues (12 pts)**
- Some features have 0 values that are biologically impossible (e.g., Glucose=0, BMI=0)
- Identify which features have this problem and how many rows are affected
- Discuss: Are these missing values encoded as 0, or data entry errors?

---

### Part 2: Missing Data Analysis (25 points)

**2.1 Visualize Missing Patterns (10 pts)**
- Treat biologically impossible zeros as missing values
- Create a visualization showing the pattern of missingness across features
- Are certain features more likely to be missing together?

**2.2 Compare Missing vs. Non-Missing (10 pts)**
- For patients with missing Insulin values vs. those without:
  - Compare the distribution of other features
  - Compare the outcome rate (diabetes prevalence)
- Is the data Missing Completely at Random (MCAR), Missing at Random (MAR), or Missing Not at Random (MNAR)?

**2.3 Imputation Strategy (5 pts)**
- Propose and implement an imputation strategy for the missing values
- Justify your choice (mean, median, model-based, or multiple imputation)

---

### Part 3: Visualization & Distributions (25 points)

**3.1 Univariate Distributions (10 pts)**

Create a figure showing the distribution of each feature:
- Use histograms or KDE plots
- Separate by outcome (diabetes vs. no diabetes)
- Which features show the clearest separation between classes?

**3.2 Correlation Analysis (8 pts)**
- Create a correlation heatmap
- Identify the features most correlated with the outcome
- Are any features highly correlated with each other (multicollinearity)?

**3.3 Clinical Visualizations (7 pts)**

Create at least two clinically meaningful visualizations:
- Example: BMI vs. Glucose colored by outcome
- Example: Age distribution by number of pregnancies
- Add appropriate titles, labels, and legends

---

### Part 4: Feature Engineering (20 points)

**4.1 Clinical Categories (8 pts)**

Create categorical features based on clinical thresholds:
- `glucose_category`: Normal (<100), Prediabetes (100-125), Diabetes (≥126)
- `bmi_category`: Underweight (<18.5), Normal (18.5-25), Overweight (25-30), Obese (≥30)
- `age_group`: Young (<30), Middle (30-50), Senior (≥50)

**4.2 Derived Features (7 pts)**

Create at least two new features that might be predictive:
- Example: `glucose_insulin_ratio` = Glucose / (Insulin + 1)
- Example: `age_bmi_interaction` = Age × BMI
- Justify why these features might be clinically meaningful

**4.3 Feature Summary (5 pts)**
- Create a summary table comparing feature statistics for diabetic vs. non-diabetic patients
- Calculate effect sizes (e.g., Cohen's d) for continuous features
- Which engineered features show the strongest association with outcome?

---

### Part 5: Class Imbalance Analysis (10 points)

**5.1 Quantify Imbalance (4 pts)**
- What is the ratio of positive to negative cases?
- Visualize the class distribution

**5.2 Implications for Modeling (6 pts)**

Answer these questions in code comments:
- If you built a model that always predicted "no diabetes," what would its accuracy be?
- Why is accuracy a misleading metric for this dataset?
- What metrics would be more appropriate? (Name at least 2)

---

## Submission via GitHub

1. **Complete your work** in `hw3_eda.py`
2. **Save your figures** to the `outputs/` directory
3. **Commit your changes** with meaningful messages
4. **Push to GitHub** before the deadline

### Deliverables

Your repository should contain:
- `hw3_eda.py` — Completed code with comments
- `outputs/` — Generated figures (PNG files)
- Clear commit history showing your progress

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| **Part 1: Data Loading & Initial Exploration** | **20** |
| 1.1 Load and inspect | 8 |
| 1.2 Identify data quality issues | 12 |
| **Part 2: Missing Data Analysis** | **25** |
| 2.1 Visualize missing patterns | 10 |
| 2.2 Compare missing vs non-missing | 10 |
| 2.3 Imputation strategy | 5 |
| **Part 3: Visualization & Distributions** | **25** |
| 3.1 Univariate distributions | 10 |
| 3.2 Correlation analysis | 8 |
| 3.3 Clinical visualizations | 7 |
| **Part 4: Feature Engineering** | **20** |
| 4.1 Clinical categories | 8 |
| 4.2 Derived features | 7 |
| 4.3 Feature summary | 5 |
| **Part 5: Class Imbalance** | **10** |
| 5.1 Quantify imbalance | 4 |
| 5.2 Implications for modeling | 6 |
| **Subtotal** | **100** |
| **Git Workflow** | |
| Multiple meaningful commits | -5 if missing |
| Clear commit messages | -5 if missing |

---

## Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Missing Data in Clinical Research (Sterne et al.)](https://www.bmj.com/content/338/bmj.b2393)
- [Pima Indians Diabetes Dataset on Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

---

## Tips

- **Start with simple summaries** — `df.describe()`, `df.info()`, `df.isnull().sum()`
- **Visualize before you analyze** — Plots often reveal issues that statistics miss
- **Think clinically** — Would a doctor find this feature meaningful?
- **Document your reasoning** — Comments explaining *why* you made choices are as important as the code
- **Commit after each part** — Don't wait until the end

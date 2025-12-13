---
layout: default
title: Homework 4 - Machine Learning for Clinical Prediction
active_tab: homework
release_date: 2026-02-25
due_date: 2026-03-11 23:59:00EST
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
2. Clone your repo and complete the exercises in `hw4_ml.py`
3. Commit regularly as you work (this is part of your grade!)
4. Push your completed work to GitHub before the deadline
</div>

---

## Learning Objectives

By completing this assignment, you will:

- Train and evaluate classification models for clinical prediction
- Understand evaluation metrics beyond accuracy (ROC, PR curves, calibration)
- Apply cross-validation and avoid data leakage
- Interpret models using feature importance and SHAP values
- Recognize when a model is (and isn't) clinically useful

---

## Background

Building a machine learning model is straightforward. Building one that's actually useful in clinical practice is hard. This assignment bridges that gap by focusing on the **evaluation** and **interpretation** aspects that determine whether a model could actually help patients.

You'll work with the Pima Indians Diabetes Dataset from HW3, but now your goal is to build and rigorously evaluate predictive models. The key insight: a model with 0.85 AUC might be useless, while one with 0.75 AUC might save lives. It depends on calibration, clinical context, and what decisions the model informs.

---

## The Dataset

Same dataset as HW3 — you should use your imputed data or start fresh:

| Feature | Description |
|---------|-------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration (2hr OGTT) |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | 2-hour serum insulin |
| BMI | Body mass index |
| DiabetesPedigreeFunction | Genetic risk score |
| Age | Age in years |
| **Outcome** | Diabetes diagnosis (1=yes, 0=no) — **target variable** |

---

## Instructions

### Part 1: Data Preparation & Train/Test Split (15 points)

**1.1 Load and Prepare Data (5 pts)**
- Load the diabetes dataset
- Handle missing values (zeros in Glucose, BMI, etc.) — you can use your approach from HW3
- Split into features (X) and target (y)

**1.2 Train/Test Split (10 pts)**
- Create a train/test split (80/20)
- Use stratification to maintain class balance
- **Important**: Document the class distribution in both sets
- Why is stratification important for imbalanced data?

---

### Part 2: Baseline Models (25 points)

**2.1 Logistic Regression (10 pts)**

Train a logistic regression model:
- Use default parameters first
- Report accuracy, precision, recall, F1 on the test set
- Print the confusion matrix
- Which features have the largest coefficients? What does this mean clinically?

**2.2 Random Forest (10 pts)**

Train a random forest classifier:
- Use default parameters first
- Report the same metrics as 2.1
- Extract and visualize feature importances
- Compare to logistic regression — which features matter most?

**2.3 Model Comparison (5 pts)**
- Create a table comparing the two models
- Which model would you choose and why?
- Is accuracy the right metric to compare them?

---

### Part 3: Evaluation Beyond Accuracy (25 points)

**3.1 ROC Curve Analysis (8 pts)**

For both models:
- Plot ROC curves on the same figure
- Calculate and display AUC for each
- Mark the point on each curve corresponding to the default threshold (0.5)
- What does the ROC curve tell you that accuracy doesn't?

**3.2 Precision-Recall Curves (8 pts)**

For both models:
- Plot Precision-Recall curves
- Calculate Average Precision (AP) for each
- Why are PR curves often more informative than ROC for medical prediction?

**3.3 Calibration Analysis (9 pts)**

For one model (your choice):
- Create a calibration plot (reliability diagram)
- Is your model well-calibrated?
- Why does calibration matter for clinical decision support?
- If poorly calibrated, what could you do to fix it?

---

### Part 4: Cross-Validation & Hyperparameter Tuning (20 points)

**4.1 K-Fold Cross-Validation (10 pts)**

Using the training data only:
- Implement 5-fold stratified cross-validation
- Report mean and std of AUC across folds
- Why do we use cross-validation instead of a single validation split?

**4.2 Hyperparameter Tuning (10 pts)**

For Random Forest:
- Use GridSearchCV or RandomizedSearchCV to tune:
  - `n_estimators`: [50, 100, 200]
  - `max_depth`: [3, 5, 10, None]
  - `min_samples_split`: [2, 5, 10]
- Report the best parameters
- Does tuning improve test set performance significantly?
- Warning: What's the risk of tuning on cross-validation and then expecting the same performance on truly new data?

---

### Part 5: Model Interpretability (15 points)

**5.1 SHAP Values (10 pts)**

Using your best model:
- Calculate SHAP values for the test set
- Create a SHAP summary plot (beeswarm)
- Create a SHAP bar plot (mean absolute SHAP values)
- Interpret: Which features drive predictions? In what direction?

**5.2 Individual Predictions (5 pts)**

Select two test patients:
- One correctly classified diabetic
- One false negative (missed diabetes)

For each:
- Show their feature values
- Create a SHAP waterfall plot
- Explain why the model made its prediction
- For the false negative: what went wrong?

---

### Part 6: Fairness Analysis (10 points - REQUIRED)

**6.1 Subgroup Performance (10 pts)**

The Pima dataset includes Age. Analyze whether your model performs equitably:

- Split the test set into age groups: Young (<30), Middle (30-50), Senior (>50)
- Calculate AUC, sensitivity, and specificity for each subgroup
- Create a table comparing performance across groups

| Age Group | N | AUC | Sensitivity | Specificity |
|-----------|---|-----|-------------|-------------|
| Young (<30) | | | | |
| Middle (30-50) | | | | |
| Senior (>50) | | | | |

Answer these questions:
- Does your model perform equally well across age groups?
- If there are disparities, what might explain them?
- How would you address this before deployment?

*Note: This dataset doesn't include race/ethnicity, but in real clinical AI, you must examine performance across demographic groups. The Obermeyer et al. paper (required reading) shows what happens when you don't.*

---

## Reflection Questions

Answer these in code comments or a markdown cell:

1. **Clinical Utility**: If this model were deployed, what threshold would you use? What's the tradeoff between missing diabetics (false negatives) and unnecessary follow-ups (false positives)?

2. **Fairness Deep Dive**: Based on your subgroup analysis, would you deploy this model as-is? What additional data would you want to collect?

3. **Limitations**: What are three reasons this model might not work well in a different hospital system?

---

## Submission via GitHub

1. **Complete your work** in `hw4_ml.py`
2. **Save your figures** to the `outputs/` directory
3. **Commit your changes** with meaningful messages
4. **Push to GitHub** before the deadline

### Deliverables

Your repository should contain:
- `hw4_ml.py` — Completed code with comments
- `outputs/` — Generated figures (PNG files)
- Clear commit history showing your progress

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| **Part 1: Data Preparation** | **15** |
| 1.1 Load and prepare data | 5 |
| 1.2 Train/test split with stratification | 10 |
| **Part 2: Baseline Models** | **25** |
| 2.1 Logistic regression | 10 |
| 2.2 Random forest | 10 |
| 2.3 Model comparison | 5 |
| **Part 3: Evaluation Beyond Accuracy** | **25** |
| 3.1 ROC curve analysis | 8 |
| 3.2 Precision-recall curves | 8 |
| 3.3 Calibration analysis | 9 |
| **Part 4: Cross-Validation & Tuning** | **20** |
| 4.1 K-fold cross-validation | 10 |
| 4.2 Hyperparameter tuning | 10 |
| **Part 5: Interpretability** | **15** |
| 5.1 SHAP values | 10 |
| 5.2 Individual predictions | 5 |
| **Part 6: Fairness Analysis** | **10** |
| 6.1 Subgroup performance | 10 |
| **Subtotal** | **110** |
| **Git Workflow** | |
| Multiple meaningful commits | -5 if missing |
| Clear commit messages | -5 if missing |

---

## Resources

- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [SHAP Documentation](https://shap.readthedocs.io/en/latest/)
- [An Introduction to Statistical Learning (ISLR)](https://www.statlearning.com/) — Chapters 2-4
- [Calibration Plots Explained](https://scikit-learn.org/stable/modules/calibration.html)
- [Decision Curve Analysis](https://www.mskcc.org/departments/epidemiology-biostatistics/biostatistics/decision-curve-analysis)

---

## Tips

- **Don't chase AUC** — A well-calibrated model with 0.75 AUC is often more useful than a poorly-calibrated one with 0.85
- **Interpret with domain knowledge** — If Glucose isn't a top feature, something might be wrong
- **Watch for data leakage** — Tune hyperparameters on training data only
- **SHAP is slow** — Use a subset of data if needed
- **Commit after each part** — Don't wait until the end

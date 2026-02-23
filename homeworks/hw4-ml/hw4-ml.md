---
layout: default
title: Homework 4 - Clinical ML Consultant
active_tab: homework
release_date: 2026-02-25
due_date: 2026-03-04 23:59:00EST
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
2. Clone your repo and work in `hw4_consultant.py` (code) and `memos/` (written deliverables)
3. This assignment is **~60% written analysis, ~40% code** — plan your time accordingly
4. Commit regularly as you work (this is part of your grade!)
5. Push your completed work to GitHub before the deadline
</div>

<div class="alert alert-warning" markdown="1">
**This assignment is different.** You are not following a recipe. You are playing the role of a consultant — you decide what to explore, which metrics matter, and what to recommend. There are traps in the data that you need to catch. Read carefully, think critically, and write clearly.
</div>

---

## Learning Objectives

By completing this assignment, you will:

- Audit a clinical dataset for data quality issues **before** modeling
- Identify data leakage and explain why it invalidates a model
- Build and evaluate classifiers using metrics appropriate to the clinical context
- Translate a clinical constraint into a quantitative threshold decision
- Critically evaluate a colleague's model for calibration and subgroup failures
- Write a deployment recommendation that synthesizes technical and clinical considerations

---

## Scenario

**You are an AI consultant** hired by Mercy Community Hospital, a mid-sized hospital serving a diverse patient population. Their Chief Medical Officer (CMO) wants to know: *can we use machine learning to screen for diabetes in our primary care clinics?*

The hospital has given you:

1. **A patient dataset** (`data/mercy_hospital_patients.csv`) — ~1,200 de-identified patients from their primary care clinics
2. **A colleague's model predictions** (`data/colleague_predictions.csv`) — Another consultant already built a model. The CMO wants your opinion on whether it's ready to deploy.
3. **The colleague's feature importance** (`data/colleague_feature_importance.csv`) — What their model relies on

Your job is to audit the data, build your own model, evaluate the colleague's work, and make a deployment recommendation. The CMO is not technical — your written memos need to be clear and honest about what ML can and cannot do here.

---

## The Dataset

`data/mercy_hospital_patients.csv` contains ~1,200 patients with the following features:

| Feature | Description |
|---------|-------------|
| `patient_id` | Unique identifier |
| `age` | Age in years |
| `sex` | Patient sex (M/F) |
| `bmi` | Body mass index |
| `systolic_bp` | Systolic blood pressure (mmHg) |
| `diastolic_bp` | Diastolic blood pressure (mmHg) |
| `fasting_glucose` | Fasting plasma glucose (mg/dL) |
| `total_cholesterol` | Total cholesterol (mg/dL) |
| `hdl_cholesterol` | HDL cholesterol (mg/dL) |
| `smoking_status` | Current / Former / Never |
| `physical_activity` | Low / Moderate / High |
| `num_office_visits` | Office visits in last 12 months |
| `family_history_diabetes` | Yes / No |
| `insurance_type` | Private / Medicare / Medicaid / Uninsured |
| `hba1c` | Hemoglobin A1c (%) |
| `metformin_prescribed` | Whether metformin is currently prescribed (Yes/No) |
| `diabetes_diagnosis` | **Target variable** (1 = diabetes, 0 = no diabetes) |

<div class="alert alert-danger" markdown="1">
**Not all of these features should be used as predictors.** Part of your job is to figure out which ones are appropriate. If you train a model on all columns blindly, you will get a very wrong answer.
</div>

---

## Deliverables

Your repository should contain:

| File | Contents |
|------|----------|
| `hw4_consultant.py` | All code (EDA, modeling, evaluation, peer review) |
| `outputs/` | Generated figures (PNG files) |
| `memos/phase1_data_audit.md` | Phase 1 written memo |
| `memos/phase3_threshold.md` | Phase 3 written memo |
| `memos/phase4_peer_review.md` | Phase 4 written memo |
| `memos/phase5_deployment.md` | Phase 5 deployment recommendation |

---

## Phase 1: Data Audit (20 points)

Before you touch a model, you need to understand the data. A responsible consultant doesn't start training until they've audited what they're working with.

### Code (8 pts)

Explore the dataset. At minimum:

- Examine feature distributions and class balance
- Compute a correlation matrix (pay attention to features that are suspiciously correlated with the target)
- Characterize missingness patterns — which features have missing values, and is the missingness random?
- Look at the relationship between key features and the target variable

You decide what to plot and what to compute. There is no checklist.

### Written: Data Audit Memo (12 pts)

Write a memo in `memos/phase1_data_audit.md` (minimum **300 words**) documenting your data quality findings **before any modeling**. Address at least three concerns you found in the data.

Your memo will be graded on what you catch:

| Finding | Points |
|---------|--------|
| Identify the HbA1c leakage problem and explain why it's leakage | 4 |
| Identify the metformin leakage problem and explain why it's leakage | 3 |
| Identify informative missingness or another valid data quality concern | 3 |
| Clear explanation of *why* each issue matters for modeling | 2 |

*Hint: Think about the causal relationship between each feature and the diagnosis. Which features could you actually measure **before** you know the outcome?*

---

## Phase 2: Model Development (25 points)

Now build your own model(s) using a **cleaned** version of the data — with leakage features removed and missingness handled appropriately.

### Code (20 pts)

- Build **at least two** different classifiers (your choice — logistic regression, random forest, gradient boosting, etc.)
- Use proper train/test splits with stratification
- Generate evaluation metrics and visualizations that you think are relevant for a diabetes screening task

This is open-ended. You choose which metrics to compute and which plots to generate. We're looking for evidence that you:

1. Actually removed the leakage features
2. Handled missing data thoughtfully (not just dropped all rows with NaNs)
3. Evaluated your models using metrics that make sense for screening
4. Compared your models meaningfully

### Written: Metric Justification (5 pts)

In a comment block or markdown cell in your code file, briefly explain (3-5 sentences): **Why did you choose these specific evaluation metrics?** What makes them appropriate for a diabetes screening task at a community hospital?

---

## Phase 3: Clinical Constraints (20 points)

The CMO tells you:

> *"We can't have more than 1 in 10 patients flagged as high-risk turning out to be healthy — our follow-up clinic is already overwhelmed."*

### Code (8 pts)

- Generate precision and sensitivity (recall) across a range of classification thresholds for your best model
- Identify the threshold that satisfies the CMO's constraint
- Produce a clear visualization of the tradeoff

### Written: Threshold Memo (12 pts)

Write a memo in `memos/phase3_threshold.md` addressing:

1. **Translation** (3 pts): What does the CMO's constraint mean in ML terms? Which metric does "1 in 10 flagged patients turning out to be healthy" correspond to? State the constraint precisely.

2. **Recommendation** (4 pts): What threshold do you recommend? What sensitivity (recall) do you achieve at that threshold? Show your work.

3. **Clinical Tradeoff** (5 pts): At your recommended threshold, how many diabetic patients will your model miss? Is this tradeoff clinically acceptable? What happens to the patients your model misses — are they harmed, or will they be caught through other means? Write as if you're explaining this to the CMO.

---

## Phase 4: Peer Review (20 points)

Your colleague already built a diabetes prediction model. The CMO is excited because it has an AUC of 0.93. Your job is to determine whether it's actually ready for deployment.

You have:
- `data/colleague_predictions.csv` — Contains `patient_id`, `true_label`, `predicted_probability`, `age`, `sex`
- `data/colleague_feature_importance.csv` — The features their model relies on most

### Code (5 pts)

- Load the colleague's predictions and reproduce their reported AUC
- Generate a calibration plot (reliability diagram) for their model
- Compute performance metrics stratified by age group (e.g., under 30 vs. 30+)

### Written: Peer Review Memo (15 pts)

Write a memo in `memos/phase4_peer_review.md` (minimum **400 words**). This is a professional peer review — be specific, cite numbers, and explain clinical implications.

| Finding | Points |
|---------|--------|
| Identify the calibration problem and explain what it means for patients | 5 |
| Identify the subgroup performance failure and explain who it harms | 5 |
| Final recommendation (deploy / fix / reject) with clear reasoning | 5 |

*Hint: A model can have a great AUC and still be dangerous. Check whether predicted probabilities match observed rates, and whether the model works equally well for all patient groups.*

---

## Phase 5: Deployment Recommendation (15 points)

### Written: Deployment Memo (15 pts)

Write a one-page memo in `memos/phase5_deployment.md` to the CMO recommending whether Mercy Community Hospital should deploy **your model** (not the colleague's) for diabetes screening.

This memo should synthesize everything you've learned across the assignment. Address:

| Component | Points |
|-----------|--------|
| Expected performance and honest limitations of your model | 5 |
| Fairness considerations — which patient groups need monitoring? What disparities did you observe or suspect? | 5 |
| What would need to be true before going live? (validation plan, monitoring strategy, failure modes) | 5 |

This is not a summary of Phase 2 results. We're looking for evidence that you've thought about what it means to put a model into clinical practice — the gap between "works on test data" and "safe to use on patients."

---

## Submission via GitHub

1. **Complete your code** in `hw4_consultant.py`
2. **Write your memos** in the `memos/` directory (Markdown format)
3. **Save your figures** to the `outputs/` directory
4. **Commit regularly** with meaningful messages — your commit history should show your thought process
5. **Push to GitHub** before the deadline

---

## Grading Rubric

| Component | Code | Written | Total |
|-----------|------|---------|-------|
| **Phase 1: Data Audit** | 8 | 12 | **20** |
| EDA and exploration | 8 | | |
| Audit memo (leakage, missingness, quality) | | 12 | |
| **Phase 2: Model Development** | 20 | 5 | **25** |
| Two classifiers on cleaned data | 20 | | |
| Metric justification | | 5 | |
| **Phase 3: Clinical Constraints** | 8 | 12 | **20** |
| Threshold analysis code and visualization | 8 | | |
| Threshold memo (translation, recommendation, tradeoff) | | 12 | |
| **Phase 4: Peer Review** | 5 | 15 | **20** |
| Reproduce AUC, calibration plot, subgroup analysis | 5 | | |
| Peer review memo | | 15 | |
| **Phase 5: Deployment Recommendation** | — | 15 | **15** |
| Deployment memo | | 15 | |
| **Subtotal** | **41** | **59** | **100** |
| **Git Workflow** | | | |
| Multiple meaningful commits | | | -5 if missing |
| Clear commit messages | | | -5 if missing |

---

## Resources

- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Calibration Plots Explained](https://scikit-learn.org/stable/modules/calibration.html)
- [An Introduction to Statistical Learning (ISLR)](https://www.statlearning.com/) — Chapters 2-4
- Obermeyer et al., ["Dissecting racial bias in an algorithm"](https://www.science.org/doi/10.1126/science.aax2342) — Science, 2019
- [Data Leakage in Machine Learning](https://machinelearningmastery.com/data-leakage-machine-learning/) — overview of common leakage patterns

---

## Tips

- **Read the data dictionary carefully** — Not every feature belongs in your model
- **Correlation with the target is not always a good thing** — Suspiciously high correlation should make you nervous, not excited
- **Write your memos for a non-technical reader** — The CMO is a physician, not a data scientist. Clear writing matters.
- **Don't chase AUC** — A well-calibrated model with honest limitations is worth more than a leaky model with 0.99 AUC
- **Commit after each phase** — Don't wait until the end
- **Budget time for writing** — The memos are worth more than the code

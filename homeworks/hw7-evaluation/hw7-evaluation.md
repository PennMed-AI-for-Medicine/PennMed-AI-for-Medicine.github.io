---
layout: default
title: Homework 7 - Model Evaluation & Explainability
active_tab: homework
release_date: 2026-04-15
due_date: 2026-04-22 23:59:00EST
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
1. [**Accept the assignment on GitHub Classroom**]({{ page.classroom_link }}) — You'll get your own private repository with starter code
2. Clone your repo and complete the exercises in `hw7_evaluation.py`
3. Push your completed work to GitHub before the deadline
</div>

<div class="alert alert-warning" markdown="1">
**Note:** This assignment builds on your work from HW4 (ML) and HW5 (Deep Learning). If you don't have working models from those assignments, starter models are provided in the repo.
</div>

---

## Learning Objectives

By completing this assignment, you will:

- Create and interpret calibration plots for clinical prediction models
- Apply decision curve analysis to assess clinical utility
- Generate and interpret SHAP explanations for tabular models
- Apply Grad-CAM visualizations to medical imaging models
- Critically evaluate when model explanations are trustworthy

---

## Background

A model with great AUC might still be clinically useless. This assignment goes beyond discrimination metrics to answer the questions clinicians actually care about:

- **"Can I trust the probability this model gives me?"** → Calibration
- **"At what risk threshold should I act?"** → Decision Curves
- **"Why did it make this prediction?"** → SHAP, Grad-CAM

These techniques bridge the gap between "my model has 0.85 AUC" and "this model is ready for clinical use." They're also essential components of the field guide you'll write for your final project.

---

## Scenario

You'll evaluate two models you've already built:

1. **Diabetes prediction model** from HW4 (tabular/ML)
2. **Medical image classifier** from HW5 (imaging/DL)

This reflects real-world practice: evaluation and explanation happen *after* you've built something, often by someone other than the original developer.

---

## Instructions

### Part 1: Calibration Analysis (30 points)

A well-calibrated model means: when it predicts 30% risk, about 30% of those patients actually have the outcome. This matters because clinicians interpret probabilities literally.

**1.1 Calibration Plots (10 pts)**

Using your HW4 diabetes prediction model:
- Create a reliability diagram (calibration plot) with 10 bins
- Add a histogram showing the distribution of predicted probabilities
- Include 95% confidence intervals on calibration curve

**1.2 Recalibration (10 pts)**

- Apply Platt scaling (logistic recalibration) to your model
- Apply isotonic regression as an alternative
- Create a comparison plot showing: original vs. Platt vs. isotonic calibration

**1.3 Calibration Metrics & Interpretation (10 pts)**

Calculate and report:
- Brier score (before and after recalibration)
- Expected Calibration Error (ECE)
- Maximum Calibration Error (MCE)

Write a short analysis (~150 words):
- Is the original model over-confident or under-confident?
- Which recalibration method works better and why?
- What would happen if a clinician used the uncalibrated probabilities for decision-making?

---

### Part 2: Decision Curve Analysis (25 points)

ROC curves tell you about discrimination. Decision curves tell you about **clinical utility**: does using this model lead to better decisions than simpler strategies?

**2.1 Build Decision Curves (10 pts)**

For your HW4 model:
- Create a decision curve showing net benefit across threshold probabilities (0% to 50%)
- Include reference lines for "treat all" and "treat none" strategies
- Add your model's curve with confidence bands (via bootstrapping)

**2.2 Clinical Threshold Analysis (15 pts)**

Assume the clinical context: patients predicted as high-risk will receive a preventive intervention (lifestyle counseling + more frequent monitoring).

Write a clinical interpretation (~200 words):
- At what threshold range does your model provide positive net benefit?
- Compare to "treat all patients with BMI > 30" as a simple clinical rule
- For a clinician who would intervene at 20% risk: is your model helpful?
- For what types of patients (threshold preferences) is the model NOT useful?

---

### Part 3: SHAP Explanations (25 points)

SHAP values explain individual predictions by attributing the prediction to each feature. But explanations can be misleading—your job is to interpret them critically.

**3.1 Global Feature Importance (10 pts)**

- Generate a SHAP summary plot (beeswarm) for your HW4 model
- Create a SHAP bar plot showing mean absolute SHAP values
- Identify the top 5 most influential features

Answer: Do these align with clinical knowledge about diabetes risk factors? Any surprises?

**3.2 Local Explanations (10 pts)**

Select 3 individual patients from your test set:
- One **true positive** (correctly identified as high risk)
- One **false positive** (incorrectly flagged as high risk)
- One **false negative** (missed—predicted low risk but developed diabetes)

For each patient:
- Generate a SHAP waterfall or force plot
- Identify which features drove the prediction
- Explain in 1-2 sentences why the model made this decision

**3.3 Critical Evaluation (5 pts)**

Answer briefly (~100 words):
- Are these explanations clinically sensible?
- Do any features seem like shortcuts or proxies (e.g., correlating with the outcome for non-causal reasons)?
- Would you trust these explanations when presenting to a clinician?

---

### Part 4: Grad-CAM for Image Models (20 points)

Saliency maps show "where the model looked" when making a prediction. Grad-CAM is one popular method—but saliency maps can be misleading if not validated.

**4.1 Generate Grad-CAM Visualizations (10 pts)**

Using your HW5 medical image classifier:
- Generate Grad-CAM heatmaps for 4 images:
  - 2 correct predictions (1 positive, 1 negative class)
  - 2 incorrect predictions (1 false positive, 1 false negative)
- Overlay heatmaps on the original images with appropriate transparency

**4.2 Sanity Check (5 pts)**

Implement the sanity check from [Adebayo et al. (2018)](https://arxiv.org/abs/1810.03292):
- Randomize the weights of your model's final layer
- Regenerate Grad-CAM for the same images
- Compare: does the saliency map change significantly?

If the saliency map looks similar with random weights, the explanation may not be trustworthy.

**4.3 Interpretation (5 pts)**

Answer briefly (~100 words):
- Is the model focusing on anatomically relevant regions?
- For the incorrect predictions, does the heatmap reveal why the model failed?
- Would you feel comfortable showing these visualizations to a radiologist?

---

## Deliverables

| File | Description |
|------|-------------|
| `hw7_evaluation.py` | Main code for all parts |
| `outputs/calibration_original.png` | Original model calibration plot |
| `outputs/calibration_comparison.png` | Before/after recalibration comparison |
| `outputs/decision_curve.png` | Decision curve analysis plot |
| `outputs/shap_summary.png` | SHAP beeswarm plot |
| `outputs/shap_local_*.png` | SHAP plots for 3 individual patients |
| `outputs/gradcam_*.png` | Grad-CAM visualizations (4+ images) |
| `outputs/gradcam_sanity.png` | Sanity check comparison |
| `analysis.md` | Written interpretations for Parts 1.3, 2.2, 3.3, 4.3 |

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| **Part 1: Calibration Analysis** | **30** |
| 1.1 Calibration plots | 10 |
| 1.2 Recalibration comparison | 10 |
| 1.3 Metrics & interpretation | 10 |
| **Part 2: Decision Curve Analysis** | **25** |
| 2.1 Decision curve plot | 10 |
| 2.2 Clinical threshold analysis | 15 |
| **Part 3: SHAP Explanations** | **25** |
| 3.1 Global feature importance | 10 |
| 3.2 Local explanations | 10 |
| 3.3 Critical evaluation | 5 |
| **Part 4: Grad-CAM** | **20** |
| 4.1 Grad-CAM visualizations | 10 |
| 4.2 Sanity check | 5 |
| 4.3 Interpretation | 5 |
| **Total** | **100** |

---

## Resources

**Calibration:**
- [Calibration: The Achilles Heel of Predictive Analytics (Van Calster et al.)](https://bmcmedicine.biomedcentral.com/articles/10.1186/s12916-019-1466-7)
- [scikit-learn calibration module](https://scikit-learn.org/stable/modules/calibration.html)

**Decision Curves:**
- [Decision Curve Analysis (Vickers lab)](https://www.mskcc.org/departments/epidemiology-biostatistics/biostatistics/decision-curve-analysis)
- [dcurves Python package](https://github.com/MSKCC-Epi-Bio/dcurves)

**SHAP:**
- [SHAP Documentation](https://shap.readthedocs.io/)
- [Interpretable ML Book - SHAP Chapter](https://christophm.github.io/interpretable-ml-book/shap.html)

**Grad-CAM:**
- [Grad-CAM Paper (Selvaraju et al.)](https://arxiv.org/abs/1610.02391)
- [Sanity Checks for Saliency Maps (Adebayo et al.)](https://arxiv.org/abs/1810.03292)
- [pytorch-grad-cam library](https://github.com/jacobgil/pytorch-grad-cam)

---

## Tips

- **Reuse your models**: This assignment is about evaluation, not building new models. Load your saved models from HW4/HW5.
- **Starter models provided**: If your previous models don't work, use the provided alternatives.
- **Think clinically**: A beautiful plot means nothing if you can't explain what it means for patient care.
- **Be skeptical of explanations**: Just because SHAP gives you numbers doesn't mean they're meaningful. That's why we include sanity checks.
- **This feeds your final project**: These evaluation techniques should appear in your field guide. Practice the interpretation skills here.
- **Written analysis matters**: The interpretation sections are where you demonstrate understanding. Don't rush them.

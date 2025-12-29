---
layout: default
title: Midterm Project
active_tab: homework
release_date: 2026-03-19
due_date: 2026-04-01 23:59:00EDT
---

<div class="alert alert-info">
This project is due on {{ page.due_date | date: "%A, %B %-d, %Y" }} before {{ page.due_date | date: "%I:%M%p" }}.
</div>

---

## Overview

The midterm project is your opportunity to apply what you've learned to a clinical AI problem end-to-end. Choose one of three tracks based on your interests and background. Each track produces the same deliverables: working code and a mini field guide.

**Deliverables:**
1. Working code (Jupyter notebook or Python script)
2. Mini field guide (2-3 pages)
3. Brief presentation (5-7 minutes)

---

## Project Tracks

Choose ONE of the following tracks:

### Track A: Medical Imaging

**Task:** Build a classification or segmentation model for medical images.

**Suggested Datasets:**
- [NIH ChestX-ray14](https://nihcc.app.box.com/v/ChestXray-NIHCC) — 112k chest X-rays, 14 disease labels
- [ISIC Skin Lesion](https://challenge.isic-archive.com/) — Dermoscopy images with lesion masks
- [APTOS Diabetic Retinopathy](https://www.kaggle.com/c/aptos2019-blindness-detection) — Retinal images, DR grading
- Any MONAI dataset from the [Model Zoo](https://monai.io/model-zoo.html)

**Minimum Requirements:**
- Train/val/test split with proper evaluation
- At least one baseline and one deep learning model
- Appropriate metrics (ROC/AUC for classification, Dice for segmentation)
- Visualization of predictions

---

### Track B: Clinical NLP

**Task:** Build a text classification or entity extraction model for clinical text.

**Suggested Datasets:**
- [MIMIC-III Clinical Notes](https://physionet.org/content/mimiciii/) — ICU notes (requires credentialing)
- [n2c2 Challenges](https://n2c2.dbmi.hms.harvard.edu/) — De-identified clinical text datasets
- [MedMentions](https://github.com/chanzuckerberg/MedMentions) — PubMed abstracts with entity annotations
- [PubMedQA](https://pubmedqa.github.io/) — Biomedical question answering

**Minimum Requirements:**
- Appropriate text preprocessing
- At least one baseline (e.g., TF-IDF + logistic regression) and one neural model
- Appropriate metrics (F1, precision/recall by class)
- Error analysis on misclassified examples

---

### Track C: Structured Clinical Data

**Task:** Build a risk prediction or outcome model using tabular clinical data.

**Suggested Datasets:**
- [MIMIC-III](https://physionet.org/content/mimiciii/) — ICU data (requires credentialing)
- [eICU](https://physionet.org/content/eicu-crd/) — Multi-center ICU data
- [Heart Disease UCI](https://archive.ics.uci.edu/ml/datasets/heart+disease) — Classic prediction task
- [Diabetes 130-US Hospitals](https://archive.ics.uci.edu/ml/datasets/diabetes+130-us+hospitals+for+years+1999-2008) — Readmission prediction

**Minimum Requirements:**
- Proper EDA and handling of missing data
- At least one baseline and one ML model (e.g., XGBoost, Random Forest)
- Appropriate metrics (AUC, calibration plot)
- Feature importance analysis (SHAP or similar)

---

### Custom Project (Requires Approval)

Have a different clinical AI project in mind? Propose it!

**To get approval:**
1. Email the instructor by **March 20** with:
   - Dataset description and access plan
   - Clinical problem and why it matters
   - Proposed approach
2. Wait for approval before starting

---

## Requirements

### Code (50 points)

| Component | Points |
|-----------|--------|
| Data loading and preprocessing | 10 |
| Model architecture (appropriate for task) | 10 |
| Training pipeline (loss, optimizer, logging) | 10 |
| Evaluation metrics (appropriate for task) | 10 |
| Code quality (readable, documented) | 10 |

### Mini Field Guide (35 points)

Write a 2-3 page document covering:

| Section | Points |
|---------|--------|
| **Problem Statement** — What clinical problem does this address? | 5 |
| **Data Description** — What data did you use? Limitations? | 5 |
| **Methods** — What approach did you take and why? | 10 |
| **Results** — Key performance metrics with interpretation | 10 |
| **Limitations & Next Steps** — What would you do differently? | 5 |

### Presentation (15 points)

5-7 minute presentation covering:
- The problem and why it matters
- Your approach
- Key results
- One thing you learned

Presentations will be during class on **April 1**.

---

## Submission

Submit via GitHub (link TBD):
1. `code/` — Your notebooks and/or scripts
2. `field_guide.pdf` — Your mini field guide
3. `slides.pdf` — Presentation slides
4. `README.md` — How to run your code

---

## Timeline

| Date | Milestone |
|------|-----------|
| Mar 18 | Project released, choose your track |
| Mar 20 | Deadline for custom project proposals |
| Mar 25 | Recommended: Data loaded, baseline running |
| Mar 31 | In-class work session |
| Apr 1 | **Presentations in class** |
| Apr 1 | **Code + Field Guide due by 11:59 PM** |

---

## Tips

- **Start with the data** — Make sure you can load and visualize before building models
- **Get a baseline working first** — A simple model that runs beats a complex model that doesn't
- **Document as you go** — Don't leave the field guide until the last minute
- **It's okay to fail** — If your model doesn't work well, analyze why. That's valuable!
- **Use what you learned** — HW2 (EDA), HW3 (DICOM), HW4 (ML), HW5 (deep learning) are all relevant

---

## Grading Rubric Summary

| Component | Points |
|-----------|--------|
| Code | 50 |
| Mini Field Guide | 35 |
| Presentation | 15 |
| **Total** | **100** |

---

## Resources

- [MONAI Tutorials](https://github.com/Project-MONAI/tutorials)
- [PyTorch Image Classification Tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)
- [Papers With Code - Medical Imaging](https://paperswithcode.com/area/medical)
- Office hours — Use them!

---
layout: default
title: Midterm Project
active_tab: homework
release_date: 2026-03-03
due_date: 2026-03-18 23:59:00EDT
---

<div class="alert alert-info">
This project is due on {{ page.due_date | date: "%A, %B %-d, %Y" }} before {{ page.due_date | date: "%I:%M%p" }}.
</div>

---

## Overview

The midterm project is your opportunity to apply what you've learned in Modules 1-4 to a clinical AI problem end-to-end. You will build a risk prediction or outcome model using structured clinical data, and write a mini field guide documenting your work.

**Deliverables:**
1. Working code (Jupyter notebook or Python script)
2. Mini field guide (2-3 pages)
3. Brief presentation (5-7 minutes)

---

## Project: Structured Clinical Data

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

### Custom Dataset (Requires Approval)

Have a different structured clinical dataset in mind? Propose it!

**To get approval:**
1. Email the instructor by **March 6** with:
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

Presentations will be during class on **Wednesday, March 18**.

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
| Mar 3 | Project released, teams assigned |
| Mar 6 | Deadline for custom dataset proposals |
| Mar 10 | Recommended: Data loaded, baseline running |
| Mar 11 | In-class work session |
| Mar 18 | **Presentations in class (Wednesday)** |
| Mar 18 | **Code + Field Guide due by 11:59 PM** |

---

## Tips

- **Start with the data** — Make sure you can load and visualize before building models
- **Get a baseline working first** — A simple model that runs beats a complex model that doesn't
- **Document as you go** — Don't leave the field guide until the last minute
- **It's okay to fail** — If your model doesn't work well, analyze why. That's valuable!
- **Use what you learned** — HW2 (EDA), HW3 (DICOM), and HW4 (ML) are all relevant

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

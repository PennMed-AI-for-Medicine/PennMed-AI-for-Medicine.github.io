---
layout: default
title: Midterm Project - Medical Imaging Case Study
active_tab: homework
release_date: 2026-03-19
due_date: 2026-04-01 23:59:00EDT
---

<div class="alert alert-info">
This project is due on {{ page.due_date | date: "%A, %B %-d, %Y" }} before {{ page.due_date | date: "%I:%M%p" }}.
</div>

---

## Overview

The midterm project is your first opportunity to apply deep learning to a medical imaging problem end-to-end. You'll work on a self-selected project from the approved options below, building on skills from Modules 1-5.

**Deliverables:**
1. Working code (Jupyter notebook or Python script)
2. Mini field guide (2-3 pages)
3. Brief presentation (5-7 minutes)

---

## Project Options

Choose ONE of the following tracks:

### Option A: Chest X-Ray Classification

**Task:** Build a classifier to detect one or more conditions from chest X-rays.

**Suggested Datasets:**
- [NIH ChestX-ray14](https://nihcc.app.box.com/v/ChestXray-NIHCC) — 112k images, 14 disease labels
- [CheXpert](https://stanfordmlgroup.github.io/competitions/chexpert/) — 224k images from Stanford
- [RSNA Pneumonia Detection](https://www.kaggle.com/c/rsna-pneumonia-detection-challenge) — Kaggle challenge data

**Minimum Requirements:**
- Binary or multi-label classification
- Train/val/test split with proper evaluation
- At least one baseline and one CNN model
- ROC curve and confusion matrix

---

### Option B: Medical Image Segmentation

**Task:** Segment anatomical structures or lesions from medical images.

**Suggested Datasets:**
- [ISIC Skin Lesion](https://challenge.isic-archive.com/) — Dermoscopy images with lesion masks
- [LiTS Liver Tumor](https://competitions.codalab.org/competitions/17094) — CT liver/tumor segmentation
- [DRIVE Retinal Vessels](https://drive.grand-challenge.org/) — Fundus images with vessel masks
- Any MONAI dataset from the [Model Zoo](https://monai.io/model-zoo.html)

**Minimum Requirements:**
- U-Net or similar architecture
- Dice score evaluation
- Visualization of predictions vs ground truth
- At least 3 example cases in your report

---

### Option C: Retinal Image Analysis

**Task:** Classify diabetic retinopathy severity or detect other retinal conditions.

**Suggested Datasets:**
- [APTOS 2019 Blindness Detection](https://www.kaggle.com/c/aptos2019-blindness-detection) — Kaggle DR classification
- [Messidor-2](https://www.adcis.net/en/third-party/messidor2/) — DR grading dataset
- [ODIR-5K](https://odir2019.grand-challenge.org/) — Multi-label ocular disease

**Minimum Requirements:**
- Handle class imbalance (DR severity is very imbalanced)
- Transfer learning from pretrained model
- Quadratic weighted kappa evaluation (standard for DR)
- Error analysis on misclassified cases

---

### Option D: Your Own Project (Requires Approval)

Have a different medical imaging project in mind? Propose it!

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
- **Use what you learned** — HW2 (DICOM), HW5 (deep learning) are directly relevant

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

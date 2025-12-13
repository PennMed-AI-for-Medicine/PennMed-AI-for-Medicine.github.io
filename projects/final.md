---
layout: default
title: Final Project - Technical Artifact + Field Guide
active_tab: homework
release_date: 2026-04-22
due_date: 2026-05-06 23:59:00EDT
---

<div class="alert alert-info">
This project is due on {{ page.due_date | date: "%A, %B %-d, %Y" }} before {{ page.due_date | date: "%I:%M%p" }}.
</div>

<div class="alert alert-warning" markdown="1">
**Final Presentations:** April 28-29 during class time. Sign up for a slot (link TBD).
</div>

---

## Overview

The final project is the capstone of this course. You'll build a complete clinical AI system and write a comprehensive field guide that could enable someone else to deploy and monitor it safely.

This project integrates everything you've learned:
- Medical data handling (imaging, text, or structured)
- Machine learning or deep learning modeling
- Evaluation with clinically meaningful metrics
- Governance, monitoring, and documentation

**Deliverables:**
1. Technical artifact (working model/pipeline)
2. Comprehensive field guide (6-10 pages)
3. Final presentation (15-20 minutes)

---

## Project Tracks

Choose ONE track. You may continue from your midterm project (different track) or start fresh.

### Track 1: Medical Imaging

Build an image classification, segmentation, or detection system.

**Example Projects:**
- Skin lesion classification with uncertainty quantification
- Organ segmentation from CT with automated QA
- Chest X-ray multi-label classification with explainability
- Retinal image screening with referral recommendations

**Must Include:**
- Deep learning model (CNN, U-Net, or similar)
- Transfer learning or appropriate training strategy
- Grad-CAM or other interpretability method
- Subgroup analysis (e.g., by image source, patient demographics if available)

---

### Track 2: Clinical NLP

Build a system that extracts, classifies, or summarizes clinical text.

**Example Projects:**
- Named entity extraction + UMLS linking pipeline
- Clinical note classification (e.g., identify high-risk patients)
- Discharge summary auto-generation/summarization
- Medication extraction and interaction checking

**Must Include:**
- Either traditional NLP (scispaCy, etc.) or LLM-based approach
- Comparison of at least two methods
- Evaluation on held-out test set
- Error analysis with clinical implications

---

### Track 3: Structured Data Prediction

Build a predictive model from tabular clinical data.

**Example Projects:**
- 30-day readmission prediction
- Sepsis early warning (like HW7 scenario, but with real model)
- Length of stay prediction
- Treatment response prediction

**Must Include:**
- Multiple model comparison (e.g., logistic regression vs. XGBoost vs. neural net)
- SHAP or similar interpretability
- Calibration analysis
- Fairness analysis across demographic groups

---

### Track 4: Custom Project (Requires Approval)

Have a different idea? Propose it!

**To get approval:**
1. Submit a 1-page proposal by **April 8** including:
   - Problem statement and clinical motivation
   - Data source and access plan
   - Proposed methods
   - How it relates to course themes
2. Meet with instructor to discuss

---

## The Field Guide (40% of grade)

The field guide is the heart of this project. It should be a document that a busy community clinic could use to decide whether to adopt your model and how to operate it safely.

### Required Sections

1. **Executive Summary** (0.5 page)
   - What does this tool do?
   - Who should use it and when?
   - Key performance metrics (1-2 sentences)

2. **Clinical Context** (1 page)
   - What problem does this solve?
   - Current standard of care
   - How would this tool change clinical workflow?

3. **Technical Description** (1-2 pages)
   - Data requirements
   - Model architecture (high-level)
   - Input/output specification
   - Computational requirements

4. **Performance Evaluation** (1-2 pages)
   - Metrics with confidence intervals
   - Subgroup performance (if applicable)
   - Comparison to baseline or alternative approaches
   - Known failure modes

5. **Governance Framework** (1-2 pages)
   - Acceptance testing protocol for new sites
   - Monitoring plan (what to track, thresholds, cadence)
   - Escalation protocol (who to contact, when to pause)
   - Human-in-the-loop requirements

6. **Limitations & Risks** (0.5-1 page)
   - Known limitations
   - Populations where performance may degrade
   - Potential for misuse
   - What this tool should NOT be used for

7. **Appendix** (as needed)
   - Detailed results tables
   - Additional visualizations
   - Technical implementation notes

---

## Technical Artifact (35% of grade)

Your code should be:
- **Reproducible** — Someone else can run it
- **Documented** — README explains how to use it
- **Organized** — Clear structure, not a single giant notebook

### Repository Structure

```
final-project/
├── README.md              # How to run everything
├── requirements.txt       # Dependencies
├── data/                  # Data or instructions to obtain it
│   └── README.md
├── src/                   # Source code
│   ├── data_loading.py
│   ├── model.py
│   ├── train.py
│   └── evaluate.py
├── notebooks/             # Exploration, visualization
│   └── analysis.ipynb
├── outputs/               # Results, figures
│   └── figures/
├── field_guide.pdf        # Your field guide
└── slides.pdf             # Presentation slides
```

---

## Presentation (25% of grade)

15-20 minute presentation + 5 minutes Q&A.

**Structure:**
1. **The Problem** (3 min) — What clinical problem? Why does it matter?
2. **The Data** (2 min) — What data? Key characteristics and limitations?
3. **The Approach** (4 min) — What did you build? Key technical decisions?
4. **Results** (4 min) — How well does it work? Honest assessment.
5. **Field Guide Highlights** (3 min) — Governance, monitoring, limitations
6. **Lessons Learned** (2 min) — What would you do differently?
7. **Q&A** (5 min)

Presentations are **April 28-29** during class.

---

## Grading Rubric

### Technical Artifact (35 points)

| Component | Points |
|-----------|--------|
| Data pipeline (loading, preprocessing, splits) | 7 |
| Model implementation (appropriate for task) | 8 |
| Training/evaluation code (runs, documented) | 7 |
| Results (metrics, visualizations) | 7 |
| Code quality (readable, organized, reproducible) | 6 |

### Field Guide (40 points)

| Section | Points |
|---------|--------|
| Executive summary | 4 |
| Clinical context | 6 |
| Technical description | 6 |
| Performance evaluation | 8 |
| Governance framework | 10 |
| Limitations & risks | 6 |

### Presentation (25 points)

| Component | Points |
|-----------|--------|
| Clarity and organization | 8 |
| Technical depth | 7 |
| Honest assessment of limitations | 5 |
| Q&A responses | 5 |

---

## Timeline

| Date | Milestone |
|------|-----------|
| Apr 1 | Project released, start planning |
| Apr 8 | Custom project proposals due |
| Apr 15 | Recommended: Data + baseline working |
| Apr 22 | Recommended: Main experiments complete |
| Apr 24 | Field guide draft recommended |
| Apr 28-29 | **Final Presentations** |
| May 6 | **Everything due by 11:59 PM** |

---

## FAQ

**Can I work in a team?**
Yes, teams of 2 are allowed. Teams of 2 are expected to do proportionally more work. Indicate contributions in your README.

**Can I use my own data from research?**
Yes, with approval. Make sure you can share enough for us to evaluate your work.

**What if my model doesn't work well?**
That's okay! Analyze why. A thoughtful analysis of failure is more valuable than inflated metrics.

**How much should the field guide assume about the reader?**
Assume the reader is a clinician with basic technical literacy — they know what "sensitivity" means but don't know PyTorch.

---

## Resources

- [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993)
- [Datasheets for Datasets](https://arxiv.org/abs/1803.09010)
- [CONSORT-AI Guidelines](https://www.nature.com/articles/s41591-020-1034-x)
- Your HW7 governance work — directly applicable!

---

## Tips

- **Start from HW7** — Your governance artifacts are a template for the field guide
- **The field guide is not an afterthought** — Budget significant time for it
- **Get feedback early** — Share drafts with classmates, come to office hours
- **Be honest about limitations** — We're grading your analysis, not your AUC
- **Practice your presentation** — 15 minutes goes fast

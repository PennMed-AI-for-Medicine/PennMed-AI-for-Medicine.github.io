---
layout: default
title: Homework 7 - Governance & Monitoring for Clinical AI
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
2. Clone your repo and complete the exercises in `hw7_governance.py`
3. Push your completed work to GitHub before the deadline
</div>

<div class="alert alert-warning" markdown="1">
**Note:** This is an intentionally lighter assignment to allow you to focus on your final project. It emphasizes thinking and writing over coding.
</div>

---

## Learning Objectives

By completing this assignment, you will:

- Design acceptance tests for a clinical AI model
- Implement basic monitoring and drift detection
- Create a governance checklist for AI deployment
- Think critically about what could go wrong in production

---

## Background

You've built models. Now what? The gap between a working model and a safely deployed clinical tool is enormous. This assignment focuses on the "boring" but critical work of governance:

- **Acceptance Testing**: How do you validate a model works at *your* institution?
- **Monitoring**: How do you know when performance degrades?
- **Governance**: Who is responsible? What are the rules?

This is the stuff that determines whether your model helps patients or harms them.

---

## Scenario

You're a data scientist at a community hospital. The hospital wants to deploy a **sepsis early warning model** that predicts which patients in the general ward are at risk of developing sepsis in the next 6 hours.

The model was developed at a large academic medical center and published with impressive results (AUC 0.89). Your job is to:
1. Design local validation before deployment
2. Set up monitoring for after deployment
3. Create governance documentation

---

## Instructions

### Part 1: Acceptance Testing Design (30 points)

Before deploying any external model, you need to validate it works at your institution.

**1.1 Define Your Test Cohort (10 pts)**

Design a validation study:
- What patient population will you test on?
- What time period?
- How will you identify "ground truth" sepsis cases?
- What's your minimum sample size and why?

Write this as a 1-paragraph protocol.

**1.2 Choose Evaluation Metrics (10 pts)**

Select 3-4 metrics that matter for this use case. For each:
- Why this metric?
- What threshold is acceptable?
- What would make you reject the model?

Consider: The model will generate alerts for nurses. False alarms cause alert fatigue. Missed sepsis cases can be fatal.

**1.3 Acceptance Criteria Document (10 pts)**

Create a formal acceptance criteria document with:
- Performance thresholds (with justification)
- Edge cases to test (e.g., post-surgical patients, pediatrics if applicable)
- Go/no-go decision criteria

---

### Part 2: Monitoring Implementation (35 points)

Once deployed, you need to know if the model is still working.

**2.1 Choose Monitoring Metrics (10 pts)**

Select 2-3 statistics to monitor continuously. For each:
- What does it measure?
- What's the expected baseline value?
- What change would trigger an alert?

Think about: input drift, prediction drift, outcome drift.

**2.2 Implement Drift Detection (15 pts)**

Write code that:
- Takes two distributions (reference and current)
- Calculates a drift statistic (e.g., PSI, KS test, chi-square)
- Returns whether drift is detected

Test your implementation with simulated data showing:
- No drift (distributions are similar)
- Drift detected (distributions differ)

**2.3 Monitoring Dashboard Sketch (10 pts)**

Create a simple visualization or sketch showing:
- Key metrics over time
- Alert thresholds
- Recent predictions summary

This can be a matplotlib figure or a hand-drawn sketch (photo) — the goal is to show what you'd want to see daily.

---

### Part 3: Governance Framework (35 points)

Documentation that nobody reads is useless. Create governance artifacts that busy clinicians might actually use.

**3.1 One-Page Model Card (15 pts)**

Create a model card (max 1 page) including:
- Model purpose and intended use
- Training data summary
- Performance metrics
- Known limitations
- Who to contact with questions

**3.2 Escalation Protocol (10 pts)**

Define what happens when things go wrong:
- Who gets notified if drift is detected?
- What's the threshold for pausing the model?
- Who makes the decision to turn it off?
- How do you communicate to clinical staff?

Write this as a simple flowchart or numbered steps.

**3.3 Review Cadence (10 pts)**

Propose a review schedule:
- How often do you review performance? (weekly? monthly?)
- What triggers an ad-hoc review?
- Who attends review meetings?
- What documentation is required?

---

## Deliverables

| File | Description |
|------|-------------|
| `hw7_governance.py` | Code for Part 2 (drift detection) |
| `acceptance_criteria.md` | Part 1.3 document |
| `model_card.md` | Part 3.1 one-page model card |
| `escalation_protocol.md` | Part 3.2 flowchart/steps |
| `outputs/` | Any figures (monitoring dashboard, etc.) |

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| **Part 1: Acceptance Testing** | **30** |
| 1.1 Test cohort design | 10 |
| 1.2 Evaluation metrics | 10 |
| 1.3 Acceptance criteria document | 10 |
| **Part 2: Monitoring** | **35** |
| 2.1 Monitoring metrics | 10 |
| 2.2 Drift detection implementation | 15 |
| 2.3 Dashboard sketch | 10 |
| **Part 3: Governance** | **35** |
| 3.1 Model card | 15 |
| 3.2 Escalation protocol | 10 |
| 3.3 Review cadence | 10 |
| **Total** | **100** |

---

## Resources

- [Model Cards for Model Reporting (Mitchell et al.)](https://arxiv.org/abs/1810.03993)
- [FDA Guidance on AI/ML Medical Devices](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices)
- [Hidden Technical Debt in ML Systems](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems)
- [Population Stability Index (PSI) Explanation](https://www.listendata.com/2015/05/population-stability-index.html)

---

## Tips

- **Think like a skeptic**: What could go wrong? What would a critic ask?
- **Be specific**: "Monitor performance" is vague. "Review weekly AUC on patients over 65" is actionable.
- **Keep it simple**: A governance plan nobody follows is worse than none at all
- **Consider your audience**: Nurses, IT staff, and executives need different information
- **This applies to your final project**: Use this assignment as practice for your field guide

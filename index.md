---
title: MPHY 6120 - Artificial Intelligence for Medicine - University of Pennsylvania
layout: default
active_tab: main_page
---

<div class="alert alert-warning" markdown="1">
**The Field Guide Mindset:** You will be asked to use AI tools that you did not design, do not fully understand, and do not have time to rigorously evaluate. This course teaches you to **build** those tools, **evaluate** them with discipline, and **write the field guide** someone else could use.
</div>

<div class="alert alert-success" markdown="1">
**Welcome to MPHY 6120: Artificial Intelligence for Medicine!** This course is designed for a broad audience including medical physicists, MD/PhDs, bioengineers, computer scientists, and translational researchers. Throughout the semester, you will learn to:

- Work with diverse medical data (images, clinical text, structured EHR data)
- Build and evaluate machine learning and deep learning models for clinical tasks
- Understand large language models and their applications in healthcare
- Design governance frameworks: acceptance tests, monitoring, and human-in-the-loop rules
- Communicate AI capabilities and limitations to non-technical clinicians
- Create "field guide" documentation for safe clinical AI deployment

The goal is to produce graduates who can both **build models** and **write the field guide** that tells a real clinic how to use them safely.
</div>

<div class="alert alert-info" markdown="1">
**Course Logistics - Spring 2026**

- **Course:** MPHY 6120 - Artificial Intelligence for Medicine
- **Schedule:** Tuesdays & Wednesdays, 1:45 - 3:15 PM
- **Classroom:** SCTR 8-146AB
- **Semester:** Spring 2026 (January 14 - April 29)
- **Expected enrollment:** ~25 students

We encourage in-person attendance for lab sessions. Contact the instructor if you cannot attend a specific day.
</div>

<div class="alert alert-success" markdown="1">
**Prerequisites:** Basic Python programming and familiarity with linear algebra and statistics. If you need a refresher, we recommend [Penn's free Introduction to Python Programming on Coursera](https://www.coursera.org/learn/python-programming-intro).
</div>

---

## Course Information

Course number
: MPHY 6120 – Artificial Intelligence for Medicine 

Instructor
: [Rafe McBeth, PhD](https://www.med.upenn.edu/apps/faculty/index.php/g20002680/c1744/p9544774)

Office
: 2-302 CMS  

Guest lectures
: TBD — Members of the Penn Medical Physics team, clinicians, or industry/regulatory experts as needed.

---

## Course Description

The fields of data science and artificial intelligence are transforming medicine. This course provides a **pragmatic field guide** for researchers and clinicians who want to meaningfully contribute to clinical AI applications.

We cover:
- **Technical foundations:** Python, PyTorch, medical imaging (DICOM, MONAI), clinical NLP
- **Core ML/DL methods:** Classification, segmentation, transformers, LLMs
- **The hard part:** Deployment, workflow integration, governance, and monitoring
- **The missing skill:** Turning models into governed, communicable systems

### Five Pillars of the Course

1. **Models vs. Systems** — Models are the easy part. Deployment, workflow, governance, and monitoring are the hard part.

2. **Metrics vs. Readiness** — A good ROC curve or Dice score is not the same as a tool ready for the clinic. Local validation, workflow fit, and oversight rules matter.

3. **Governance as Quantitative Discipline** — Governance is not bureaucracy. It is constraints (what must always be true), experiments (acceptance tests), and logs (traceability).

4. **Use Cases at Different Maturity Levels** — Students learn to place AI use cases on a maturity spectrum, from research to clinical deployment.

5. **Field Guide Mindset** — Always ask: "If I were a busy community clinician, what would I need to know to use this tool?"

---

## Course Format

We meet twice weekly for 90-minute sessions:
- **Lectures** (first ~45–60 minutes): Theoretical concepts, clinical AI case studies, best practices
- **Lab/Practical Time** (remaining ~30–45 minutes): Jupyter notebooks, coding exercises, project development

---

## Course Materials

**Primary Text:**
- *Little Book of Medical AI* (course companion, provided)

> **About the Little Book:** This is a living document being developed alongside the course. You'll receive draft chapters as we progress through modules. Your feedback and questions will shape the final version. Think of it as our collective field guide to the field—and a model for the field guides you'll write for your own projects.

**Code & Resources:**
- [Course GitHub Repository](https://github.com/PennMed-AI-for-Medicine)
- [Course Website](https://pennmed-ai-for-medicine.github.io/)

**Optional References:**
- *Machine and Deep Learning in Oncology, Medical Physics and Radiology* (2nd ed.) by Issam El Naqa et al., 2022
- *Think Python* (2nd ed.) by Allen Downey — [Free online](https://greenteapress.com/wp/think-python-2e/)
- *Python for Data Analysis* (3rd ed.) by Wes McKinney
- *The AI Revolution in Medicine* by Peter Lee, Carey Goldberg, and Isaac Kohane

---

## Grading

| Component | Weight | Description |
|-----------|--------|-------------|
| **Homework Assignments** | 50% | Coding tasks and short writing assignments |
| **Midterm Project** | 20% | Medical imaging case study + mini field guide |
| **Final Project** | 20% | Technical artifact + full field guide + presentation to Review Board |
| **Participation** | 10% | In-class discussions, peer feedback |

### Grade Scale

| Score | Grade |
|-------|-------|
| ≥ 97 | A+ |
| 93–97 | A |
| 90–93 | A− |
| 87–90 | B+ |
| 83–87 | B |
| 80–83 | B− |
| 75–80 | C+ |
| 70–75 | C |
| 65–70 | C− |
| 50–65 | D |
| < 50 | F |

---

## Project Deliverables

Projects have **two parts**:

### Part A: Technical Artifact
- Model, code, or pipeline for a clinical task
- Standard ML/DL evaluation metrics
- Code in GitHub repository

### Part B: Field Guide (3-5 pages)

A document for non-experts that could actually be handed to a busy clinician. This is graded separately from your technical work.

| Section | What to Include | Points |
|---------|-----------------|--------|
| **1. Tool Summary** | Plain-language description a non-technical clinician could understand in 2 minutes | 10 |
| **2. Intended Use** | Specific clinical context, patient population, workflow placement | 10 |
| **3. Performance Summary** | Key metrics, what they mean clinically, comparison to alternatives | 15 |
| **4. Limitations & Failure Modes** | When it breaks, edge cases, known biases | 15 |
| **5. Human Oversight Rules** | When to review, when to override, red flags to watch for | 15 |
| **6. Local Validation Plan** | How you would test this at a new site (cohort, metrics, thresholds) | 15 |
| **7. Monitoring Plan** | What to track, how often, who reviews, escalation criteria | 10 |
| **8. Patient Explanation** | One paragraph for informed consent / patient questions | 10 |

**Total: 100 points** (Field guide graded separately from technical artifact)

### Final Presentation: The Review Board

Final project presentations simulate a real clinical AI deployment review. A **Review Board** of senior clinical and technical leaders will attend—including clinical informaticists, department leadership, and industry experts. They will ask questions as if you were proposing to deploy your tool at their institution.

This is intentional: bridging technical depth with clinical context and leadership communication is the whole point. You're not just building a model; you're learning to advocate for its responsible deployment.

### Project Tracks

Students choose one of three tracks based on their background and interests. You select a track for your midterm project and can switch or continue for the final project.

**Track A: Medical Imaging**
- *Best for:* Students with image processing background, radiology/pathology interest
- *Example projects:* Chest X-ray classification, CT organ segmentation, histopathology analysis, retinal imaging
- *Key skills you'll develop:* DICOM/NIfTI handling, MONAI framework, CNNs, U-Net architectures

**Track B: Clinical NLP**
- *Best for:* Students with text/NLP background, documentation/EHR interest
- *Example projects:* Clinical notes extraction, radiology report analysis, LLM for documentation assistance
- *Key skills you'll develop:* Text preprocessing, embeddings, transformers, prompting strategies

**Track C: Structured Clinical Data**
- *Best for:* Students with statistics/epidemiology background, outcomes research interest
- *Example projects:* Risk prediction from EHR data, treatment response modeling, survival analysis
- *Key skills you'll develop:* Pandas, feature engineering, classical ML, tabular deep learning

---

## Submission & GitHub Workflow

All code assignments are submitted via **GitHub Classroom**:

1. Accept the assignment link (posted on Canvas and the homework page)
2. Clone your private repository
3. Complete the work, committing as you go
4. Push before the deadline

We use GitHub (not Gradescope) because version control is an essential skill for medical AI development. Your commit history shows your problem-solving process and distinguishes your work from AI-generated code. Grades are recorded in Canvas.

---

## AI Assistant Policy

We encourage the use of AI coding assistants (GitHub Copilot, ChatGPT, Claude) to enhance your learning. However:
- You are responsible for verifying correctness
- Your commit history should reflect your problem-solving process
- The goal is understanding, not just working code
- AI assistants are tools to accelerate learning, not replace it

---

## Office Hours

**Instructor:** TBD (will be announced first week of class)

**TA:** TBD

Office hours are drop-in; no appointment needed. For complex questions, email ahead so we can prepare.

---

Thank you for visiting the course page. We look forward to a dynamic semester exploring the latest developments in AI for medicine!

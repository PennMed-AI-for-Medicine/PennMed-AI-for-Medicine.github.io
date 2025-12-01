---
title: MPHY 6120 - Artificial Intelligence for Medicine - University of Pennsylvania
layout: default
img: class_logo2.png 
active_tab: main_page
---

<div class="alert alert-warning" markdown="1">
**The Field Guide Mindset:** You will be asked to use AI tools that you did not design, do not fully understand, and do not have time to rigorously evaluate. This course teaches you to **build** those tools, **evaluate** them with discipline, and **write the field guide** someone else could use.
</div>

<div style="background-color: #d4edda; color: #155724; border-color: #c3e6cb; padding: 15px; border: 1px solid transparent; border-radius: 4px;">
  <strong>Welcome to MPHY 6120: Artificial Intelligence for Medicine!</strong> This course is designed for a broad audience including medical physicists, MD/PhDs, bioengineers, computer scientists, and translational researchers. Throughout the semester, you will learn to:
  <ul>
    <li>Work with diverse medical data (images, clinical text, structured EHR data)</li>
    <li>Build and evaluate machine learning and deep learning models for clinical tasks</li>
    <li>Understand large language models and their applications in healthcare</li>
    <li>Design governance frameworks: acceptance tests, monitoring, and human-in-the-loop rules</li>
    <li>Communicate AI capabilities and limitations to non-technical clinicians</li>
    <li>Create "field guide" documentation for safe clinical AI deployment</li>
  </ul>

The goal is to produce graduates who can both <strong>build models</strong> and <strong>write the field guide</strong> that tells a real clinic how to use them safely.
</div>

<div class="alert alert-info" markdown="1">
**Course Logistics - Spring 2025**

- **Course:** MPHY 6120 - Artificial Intelligence for Medicine
- **Schedule:** Tuesdays & Wednesdays, 1:45 - 3:15 PM
- **Classroom:** SCTR 8-146AB
- **Semester:** Spring 2025 (January 21 - May 6)
- **Expected enrollment:** ~14 students

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
- *Little Book of Medical AI* (course companion, provided) — Your field guide to clinical AI

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
| **Final Project** | 20% | Technical artifact + full field guide (3-5 pages) |
| **Participation** | 10% | In-class discussions, peer feedback |

### Grade Scale

| Score | Grade | | Score | Grade |
|-------|-------|-|-------|-------|
| ≥ 97 | A+ | | 75–80 | C+ |
| 93–97 | A | | 70–75 | C |
| 90–93 | A− | | 65–70 | C− |
| 87–90 | B+ | | 50–65 | D |
| 83–87 | B | | < 50 | F |
| 80–83 | B− | | | |

---

## Project Deliverables

Projects have **two parts**:

### Part A: Technical Artifact
- Model, code, or pipeline for a clinical task
- Standard ML/DL evaluation metrics
- Code in GitHub repository

### Part B: Field Guide (3-5 pages)
A document for non-experts covering:
1. What this tool does (plain language)
2. Where it fits in the workflow (who, when, which patients)
3. Strengths (data-backed)
4. Limitations and failure modes
5. Safety rules (human review, prohibited uses)
6. Local validation summary
7. Monitoring plan (metrics, cadence, responsibility)
8. Patient explanation (one paragraph, lay language)

### Flexible Case Study Options

**Imaging Track:**
- Chest X-ray classification (pneumonia, COVID, cardiomegaly)
- CT organ/lesion segmentation (liver, kidney, lung nodules)
- Pathology/histology analysis
- Retinal imaging, mammography, or other approved tasks

**NLP Track:**
- Clinical notes extraction/classification
- Radiology report analysis
- LLM for documentation assistance
- Other approved clinical text tasks

---

## Office Hours

TBD — Schedule will be posted and announced via email.

---

## AI Assistant Policy

We encourage the use of AI coding assistants (GitHub Copilot, ChatGPT, Claude) to enhance your learning. However:
- You are responsible for verifying correctness
- Cite AI-assisted code where appropriate
- The goal is understanding, not just working code

---

Thank you for visiting the course page. We look forward to a dynamic semester exploring the latest developments in AI for medicine!

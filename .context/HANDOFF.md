# Session Handoff: Course Content Alignment

**Date:** 2025-12-26
**Project:** PennMed AI for Medicine Course (clinicalai.guide)
**Related repos:**
- Website: `PennMed-AI-for-Medicine.github.io` (this repo)
- Slides: `/Users/rafe/LocalGit/PennMed-AI-for-Medicine/slides`
- Textbook: `Little-Book-of-Medical-AI` (rafemcbeth.github.io/Little-Book-of-Medical-AI/)

---

## Session Summary

Major alignment effort to synchronize three interconnected course resources:
1. **Website** (scaffold) — The course structure students see
2. **Slides** (delivery) — In-class teaching materials
3. **Textbook** (depth) — Comprehensive reference, 19 chapters

### Philosophy Established
- **Field Guide mindset** is central — "Could a busy community clinic use this safely?"
- Textbook is broadest, course is scaffold, slides live in between
- 12 modules (0-11), 7 homeworks, midterm + final project
- NLP and LLMs kept as separate modules (historical context matters)

---

## What Was Done

### Website Changes (pushed to GitHub)
1. **Module 9** renamed: "Governance & Monitoring" → **"Model Evaluation & Explainability"**
   - Added lessons on calibration, decision curves, SHAP/LIME, saliency

2. **Module 10** renamed: "From Model to MVP" → **"Governance, Regulatory & Deployment"**
   - Added lessons on FDA pathways, SaMD, deployment, governance

3. **CLAUDE.md** created with course philosophy and content hierarchy

4. **Textbook cross-references** added to ALL modules (0-10)
   - Each module now links to relevant textbook chapters
   - Prefixed with 📖 for visibility

### Slides Changes (committed locally, no remote)
1. **Renumbered** all slides to match website (0-11)
2. **Moved to `supplemental/`:**
   - PyTorch Foundations (was Module 2)
   - Fairness & Bias (was Module 4)
   - Explainability details (was Module 8)
   - Deployment & MLOps (was Module 10)
   - Governance & Monitoring (was Module 11)

3. **Created stub slides** for:
   - Module 2: Medical Imaging Data (DICOM)
   - Module 4: Machine Learning Foundations
   - Module 6: Midterm Project
   - Module 8: Large Language Models

4. **Updated README.md** with new structure and supplemental guide

---

## Current State

### Website Modules (aligned)
| # | Title | Textbook Chapters |
|---|-------|------------------|
| 0 | Course Intro & Field Guide Mindset | Ch 1 |
| 1 | Python & Development Environment | Ch 2 |
| 2 | Medical Imaging Data | Ch 6 |
| 3 | Structured Clinical Data & EDA | Ch 3, 12 |
| 4 | Machine Learning Foundations | Ch 4, 18 |
| 5 | Deep Learning for Medical Imaging | Ch 5, 6 |
| 6 | Midterm Project | Ch 11 |
| 7 | Clinical Text & NLP | Ch 8, 12 |
| 8 | Large Language Models | Ch 9, 10 |
| 9 | Model Evaluation & Explainability | Ch 16 |
| 10 | Governance, Regulatory & Deployment | Ch 14, 19 |
| 11 | Final Projects | — |

### Slides Status
| Module | Status | Notes |
|--------|--------|-------|
| 0, 1, 3, 5, 7, 9, 10, 11 | ✅ Complete | Full slide decks |
| 2 | ✅ Complete (slim) | 23 slides, practical focus, textbook for depth |
| 4 | ✅ Complete | 41 slides, fairness woven throughout |
| 6 | 📝 Stub (minimal) | Work session, minimal slides needed |
| 8 | ✅ Complete | 39 slides, timeless concepts |
| supplemental/ | 📦 Extra | Content to integrate later |

---

## Pending / Next Steps

1. ~~**Develop stub slide content**~~ ✅ **DONE** — Modules 2, 4, 8 complete (see below)

2. **Integrate supplemental content** (optional, for deeper lectures)
   - Explainability details → Module 9
   - Deployment/Governance → Module 10

3. **Set up slides remote** — Currently no git remote configured

4. ~~**Review homework alignment**~~ ✅ **DONE** — HW7 rewritten (see below)

---

## Recent Changes (2025-12-26)

### Slides Modules 2, 4, 8 Developed

**Module 2 — Medical Imaging Data (23 slides)**
- Slim, practical: "enough to do HW and not be confused"
- DICOM basics, pydicom, window/level, MONAI
- Two-track pointer (core vs advanced/med phys)
- Deep dive → textbook appendix
- Philosophy: not a 90-min DICOM lecture for non-physics students

**Module 4 — ML Foundations (41 slides)**
- Opens with Obermeyer case (fairness hook)
- Fairness woven throughout, not bolted on
- Evaluation metrics that matter clinically (ROC, PR, calibration)
- Cross-validation, data leakage, temporal validation
- SHAP, fairness audit, calibration by group
- "Clinical utility > technical performance"

**Module 8 — LLMs in Medicine (39 slides)**
- Timeless concepts, not trends
- Transformers conceptually (attention intuition, not math)
- Prompting as transferable skill (zero/few-shot, chain-of-thought, RAG)
- Heavy emphasis on risks (8 slides on limitations)
- "When NOT to use LLMs" explicitly addressed
- Avoids: specific model versions, API tutorials, benchmarks

### HW7 Rewritten: Governance → Evaluation & Explainability

**Rationale:** Governance content is already embedded in midterm/final projects (field guide deliverables). Homework is better suited for technical, code-able skills.

**Old HW7:** "Governance & Monitoring for Clinical AI"
- Acceptance testing design
- Drift detection implementation
- Model cards, escalation protocols

**New HW7:** "Model Evaluation & Explainability"
- Part 1: Calibration analysis (plots, Platt scaling, Brier score)
- Part 2: Decision curve analysis (net benefit, clinical thresholds)
- Part 3: SHAP explanations (global + local, critical evaluation)
- Part 4: Grad-CAM for images (with sanity checks)

**Files changed:**
- `homeworks/hw7-governance/` → `homeworks/hw7-evaluation/`
- `hw7-governance.md` → `hw7-evaluation.md`

**Design principle:** Homework = technical skills, Projects = synthesis + governance thinking

---

## Key Decisions Made

| Decision | Rationale |
|----------|-----------|
| Keep Module 0 | Zero-indexing philosophy, "about to start an adventure" |
| NLP + LLMs separate | Historical context matters, NLP existed before LLMs |
| 7 homeworks | 12-week course with significant projects needs focus |
| Textbook broader than course | Students can go deeper; course is curated scaffold |
| Slides in supplemental/ | Don't delete good content; integrate later |

---

## Files Modified This Session

### Website (this repo)
- `_data/modules.yaml` — Module 9, 10 content; textbook references
- `CLAUDE.md` — Created (course philosophy)

### Slides repo
- `module_*_slides.py` — Renumbered and updated docstrings
- `supplemental/` — New directory with extra content
- `README.md` — Updated structure documentation
- `plans/` — Renumbered plan files

---

## Notes for Next Session

- Slides repo has no remote — changes are local only
- Website builds via GitHub Actions (no local Jekyll needed)
- Textbook at: https://rafemcbeth.github.io/Little-Book-of-Medical-AI/
- User prefers discussion before implementation on significant changes

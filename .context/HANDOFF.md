# Course Handoff: Current State

**Project:** MPHY 6120 - AI for Medicine (clinicalai.guide)
**Last updated:** 2025-12-28

**Related repos:**
- Website: `PennMed-AI-for-Medicine.github.io` — public
- Slides: `PennMed-AI-for-Medicine/slides` — private
- Textbook: `Little-Book-of-Medical-AI` (rafemcbeth.github.io/Little-Book-of-Medical-AI/)

See `CHANGELOG.md` for session-by-session history.

---

## Course Philosophy

- **Field Guide Mindset** — "Could a busy community clinic use this safely?"
- **Models vs Systems** — Building is easy, deployment is hard
- **Garbage In = Garbage Out** — Understand your data before modeling
- **Governance as Quantitative Discipline** — Constraints, experiments, logs

---

## Module Structure (12 modules, 0-indexed)

| # | Title | Homework | Textbook |
|---|-------|----------|----------|
| 0 | Course Intro & Field Guide Mindset | — | Ch 1 |
| 1 | Python & Development Environment | HW1 | Ch 2 |
| 2 | **Structured Clinical Data & EDA** | HW2 | Ch 3, 12 |
| 3 | **Medical Imaging Data** | HW3 | Ch 6 |
| 4 | Machine Learning Foundations | HW4 | Ch 4, 18 |
| 5 | Midterm Project (2 tracks: Imaging/Structured) | Midterm | Ch 11 |
| 6 | Deep Learning for Medical Imaging | HW5 | Ch 5, 6 |
| 7 | Clinical Text & NLP | HW6 | Ch 8, 12 |
| 8 | Large Language Models | (HW6 spans) | Ch 9, 10 |
| 9 | Model Evaluation & Explainability | HW7 | Ch 16 |
| 10 | Governance, Regulatory & Deployment | — | Ch 14, 19 |
| 11 | Final Projects | Final | — |

---

## Homework Schedule

| HW | Topic | Release | Due |
|----|-------|---------|-----|
| HW1 | Python Setup | Jan 21 | Jan 28 |
| HW2 | EDA & Clinical Data | Feb 4 | Feb 11 |
| HW3 | DICOM & Imaging | Feb 11 | Feb 25 |
| HW4 | ML for Clinical Prediction | Feb 25 | Mar 11 |
| HW5 | Deep Learning | Mar 18 | Mar 25 |
| HW6 | Clinical NLP & LLMs | Apr 1 | Apr 15 |
| HW7 | Evaluation & Explainability | Apr 15 | Apr 22 |

---

## Slides Status

| Module | Status | Notes |
|--------|--------|-------|
| 0, 1, 6, 7, 9, 10, 11 | ✅ Complete | Full slide decks |
| 2 | ✅ Complete | ~40 slides, EDA focus |
| 3 | ✅ Complete (slim) | ~23 slides, practical DICOM |
| 4 | ✅ Complete | ~48 slides, fairness woven in |
| 5 | 📝 Stub | Work session, minimal needed |
| 8 | ✅ Complete | ~42 slides, timeless LLM concepts |
| supplemental/ | 📦 Extra | Content to integrate later |

---

## Key Files

**Website:**
- `_data/modules.yaml` — Course structure (modules, lessons, readings)
- `_data/lectures.yaml` — Lecture schedule
- `homeworks/hw*-*/` — Homework specifications
- `projects/midterm.md` — Midterm project spec (2 tracks)
- `projects/final.md` — Final project spec
- `CLAUDE.md` — AI assistant instructions
- `LICENSE` — CC BY-NC-SA 4.0

**Slides:**
- `module_*_slides.py` — Slide generators (python-pptx)
- `template.py` — Shared slide templates
- `supplemental/` — Extra content for deeper lectures

---

## Textbook Alignment Check

When updating course content, verify textbook covers:
- [ ] EDA workflow and data quality (Module 2 now earlier)
- [ ] Missing data patterns (MAR/MCAR/MNAR)
- [ ] Calibration and decision curves (Module 9)
- [ ] External validation reality (5-15% drop)

---

## Pre-Launch TODOs

- [ ] **Hide unreleased homeworks** — Modify `_layouts/default.html` dropdown to filter by `release_date`. Currently shows all HWs for review purposes.
- [ ] Update GitHub Classroom links (currently placeholder `XXXXXX` for HW3-7)
- [ ] Finalize office hours in `index.md`
- [ ] Add guest lecture info

## Notes

- Website builds via GitHub Actions
- Slides repo is private (contains solutions context)
- User prefers discussion before significant changes
- License requires attribution for forks

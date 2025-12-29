# Session Changelog

Running log of significant changes made during AI-assisted development sessions.

---

## 2025-12-27

### Module Reorder: EDA Before DICOM

**Rationale:** "Garbage in = garbage out" — students should understand data exploration before tackling complex medical imaging formats. EDA skills transfer to all data types.

**Changes:**
- Module 2: Now **Structured Clinical Data & EDA** (was Module 3)
- Module 3: Now **Medical Imaging Data** (was Module 2)
- HW2: Now EDA homework (release Feb 4, due Feb 11)
- HW3: Now DICOM homework (release Feb 11, due Feb 25)

**Files changed:**
- `_data/modules.yaml` — Swapped module content
- `homeworks/hw2-eda/` — Renamed from hw3-eda, updated to HW2
- `homeworks/hw3-dicom/` — Renamed from hw2-dicom, updated to HW3
- `slides/module_2_slides.py` — Now EDA content
- `slides/module_3_slides.py` — Now DICOM content

### Textbook Reference Fixes

Verified all textbook URLs (16 links, all return 200). Fixed chapter-to-module mapping:

- **Module 2 (EDA):** Added Ch 3b (EDA for Clinical Data) as primary reading; Ch 3 (Stats) now optional
- **Module 3 (DICOM):** Added Appendix DICOM as primary reading; Ch 6 (CNNs) now optional preview

### Documentation Restructure

Split handoff documentation into two files:
- `HANDOFF.md` — Always-current state (modules, homework, slides status)
- `CHANGELOG.md` — Session-by-session history (this file)

### Other Changes
- Fixed mobile navbar padding (title flush against left edge)
- Added practical slides to Module 4 (missing data, class imbalance, external validation, decision curves, what-to-report checklist)
- Added practical slides to Module 8 (LLM evaluation, local vs cloud, cost considerations)
- Reviewed textbook EDA chapter (Ch 3b) — confirmed strong coverage of missing data, feature engineering, class imbalance; visualization is lighter but adequate

---

## 2025-12-26

### Initial Course Alignment

Major effort to synchronize website, slides, and textbook.

**Module Changes:**
- Module 9 renamed: "Governance & Monitoring" → "Model Evaluation & Explainability"
- Module 10 renamed: "From Model to MVP" → "Governance, Regulatory & Deployment"
- Added textbook cross-references to all modules

**HW7 Rewritten:**
- Old: "Governance & Monitoring" (acceptance testing, drift detection)
- New: "Model Evaluation & Explainability" (calibration, decision curves, SHAP, Grad-CAM)
- Rationale: Governance embedded in projects; homework better for technical skills

**Slides Work:**
- Set up private slides repo: `PennMed-AI-for-Medicine/slides`
- Created Module 2 (DICOM - slim), Module 4 (ML), Module 8 (LLMs)
- Moved old content to `supplemental/`

**Infrastructure:**
- Added CC BY-NC-SA 4.0 license to website
- Created CLAUDE.md with course philosophy
- Added textbook link to front page

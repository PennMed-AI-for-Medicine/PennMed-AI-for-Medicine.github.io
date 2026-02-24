# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the course website for **MPHY 6120 - Artificial Intelligence for Medicine** at the University of Pennsylvania. It's a Jekyll-based static site deployed to **clinicalai.guide** via GitHub Pages.

### Course Philosophy
The course centers on the **Field Guide mindset**: teaching students to build AI that a busy community clinic could use safely. Key themes:
- Models vs Systems (deployment is the hard part)
- Research → Implementation bridge
- Governance as quantitative discipline

### Content Hierarchy
Three interconnected resources exist:
1. **Textbook** (`Little-Book-of-Medical-AI`) — Broadest knowledge, 19 chapters, reference material
2. **Course Website** (this repo) — Scaffold, 12 modules (0-11), the "what we're teaching"
3. **Slides** (`/slides/` repo) — Delivery, lives between textbook and class

### Module Structure (12 modules)
- **0**: Course Introduction & Field Guide Mindset
- **1-4**: Skills building (Python, EDA, Imaging, ML)
- **5**: Midterm Project
- **6**: Deep Learning for Medical Imaging
- **7-8**: NLP & LLMs (kept separate for historical context)
- **9**: Model Evaluation & Explainability
- **10**: Governance, Regulatory & Deployment
- **11**: Final Projects

## Build Commands

```bash
# Install dependencies
bundle install

# Serve locally with auto-reload (http://localhost:4000)
bundle exec jekyll serve

# Build static site to _site/
bundle exec jekyll build
```

## Architecture

### Data-Driven Content
Course content is defined in YAML files under `_data/`:
- `modules.yaml` - Complete course structure (12 modules with lessons, readings, descriptions)
- `lectures.yaml` - Lecture details
- `staff.yaml` - Instructor/TA information
- `exams.yaml` - Exam schedule
- `university_calendar.yaml` - Academic calendar dates

Jekyll Liquid templates iterate over these data structures to generate pages dynamically.

### Key Files
- `_config.yml` - Jekyll configuration (theme: jekyll-theme-midnight, timezone: America/New_York)
- `_layouts/default.html` - Main page template (Bootstrap 3.3.5, responsive)
- `assets/css/class.css` - Course-specific styling (dark theme overrides)

### Content Pages
- `index.md` - Course homepage
- `modules.md` - Lists all course modules (renders from `_data/modules.yaml`)
- `schedule.md` - Calendar-based schedule (generated dynamically)
- `staff.md` - Staff directory with flip-card animations
- `resources.md` - Curated external links

### Assignments
- `homeworks/hw1-python-setup/` through `homeworks/hw7-governance/` - Weekly homework specs
- `projects/midterm.md` and `projects/final.md` - Major project specifications

Each homework has its own directory with an `hw.md` file containing learning objectives, instructions, grading rubrics, and GitHub Classroom links.

## Common Tasks

**Adding/editing a module**: Edit `_data/modules.yaml` - each module has `module_number`, `start_date`, `end_date`, `title`, `description`, `lessons[]`, and `readings[]`

**Adding a homework**: Create `homeworks/hwN-topic/hw.md` following the existing format

**Updating schedule**: Schedule page auto-generates from YAML data files

**Styling changes**: Modify `assets/css/class.css` for course-specific styles

## Technical Notes

- Uses `jekyll-theme-midnight` (dark theme)
- MathJax enabled for LaTeX equations in markdown
- Front matter `active_tab` controls navigation highlighting
- The `_archive/` directory contains previous semester materials (excluded from build)
- Media files (.mov, .mp4) are gitignored

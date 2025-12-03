---
layout: default
title: MPHY 6120 Homework 1 - Python & Environment Setup
active_tab: homework
release_date: 2025-01-28
due_date: 2025-02-04 23:59:00EST
materials:
    - 
        name: Starter Notebook
        url: hw1-starter.ipynb
submission_link: https://www.gradescope.com/
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
This assignment is due on {{ page.due_date | date: "%A, %B %-d, %Y" }} before {{ page.due_date | date: "%I:%M%p %Z" }}.
</div>

{% if page.materials %}
<div class="alert alert-success">
<b>Materials:</b>
<ul>
{% for material in page.materials %}
<li><a href="{{ material.url }}">{{ material.name }}</a></li>
{% endfor %}
</ul>
</div>
{% endif %}

## Learning Objectives

By completing this assignment, you will:
- Set up your Python development environment using `uv`
- Verify PyTorch installation and GPU access (if available)
- Practice basic Python skills needed for the course
- Submit your first assignment via Gradescope

## Instructions

### Part 1: Environment Setup (30 points)

1. Install `uv` package manager
2. Create a virtual environment for the course
3. Install required packages: `torch`, `numpy`, `pandas`, `matplotlib`
4. Verify your installation by running the starter notebook

### Part 2: Python Skills Review (40 points)

Complete the exercises in the starter notebook covering:
- NumPy array operations
- Pandas DataFrames
- Basic plotting with matplotlib

### Part 3: PyTorch Basics (30 points)

- Create a simple tensor
- Perform basic tensor operations
- Check if CUDA is available (if you have a GPU)

## Submission

Submit your completed notebook to [Gradescope]({{ page.submission_link }}).

## Grading

| Component | Points |
|-----------|--------|
| Environment setup verified | 30 |
| Python exercises | 40 |
| PyTorch basics | 30 |
| **Total** | **100** |



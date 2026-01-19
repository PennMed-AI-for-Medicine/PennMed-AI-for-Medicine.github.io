---
layout: default
title: Homework 1 - Python & Environment Setup
active_tab: homework
release_date: 2026-01-21
due_date: 2026-01-28 23:59:00EST
classroom_link: https://classroom.github.com/a/wYc9Dgh8
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
2. Clone your repo to your local machine
3. Complete the exercises in `hw1_exercises.py`
4. Commit and push your work to GitHub before the deadline
</div>

---

## Learning Objectives

By completing this assignment, you will:

- Set up VS Code with GitHub Copilot as your AI pair programming environment
- Configure your Python development environment using `uv`
- Verify PyTorch installation and GPU access (if available)
- Practice basic Python skills needed for the course
- Learn the Git workflow used throughout this course

---

## Instructions

### Part 1: Environment Setup (25 points)

#### 1.1 Install VS Code and GitHub Copilot (9 points)

We'll use Visual Studio Code as our IDE with GitHub Copilot as your AI pair programmer. This mirrors how many professional developers work today.

**Step 1: Install VS Code**

Download and install [Visual Studio Code](https://code.visualstudio.com/) for your operating system.

**Step 2: Get GitHub Education Benefits**

As a student, you get free access to GitHub Copilot and other developer tools:

1. Go to [GitHub Education](https://education.github.com/pack)
2. Click "Get your pack" and verify your student status with your Penn email
3. Once approved, Copilot will be free on your GitHub account

**Step 3: Install VS Code Extensions**

Open VS Code and install these extensions (Ctrl/Cmd + Shift + X):

1. **Python** (by Microsoft) — Python language support
2. **GitHub Copilot** — AI pair programming assistant
3. **Jupyter** — Notebook support

**Step 4: Sign into GitHub Copilot**

1. Click the Copilot icon in the VS Code sidebar
2. Sign in with your GitHub account (the one with Education benefits)
3. Verify Copilot is working by typing a comment like `# function to calculate BMI` and see if it suggests code

**Deliverable:** Screenshot showing VS Code with the Python and GitHub Copilot extensions installed and Copilot active.

> **A note on AI pair programming:** Copilot is a tool to accelerate your work, not replace your learning. Use it to get unstuck, explore syntax, and see alternative approaches—but make sure you understand every line of code you submit. Your commit history should reflect *your* problem-solving process.

#### 1.2 Install uv Package Manager (8 points)

[uv](https://github.com/astral-sh/uv) is a fast Python package and environment manager that we'll use throughout the course. It's written in Rust and is significantly faster than pip—it handles both virtual environment creation and package installation in one tool.

Install it by following the instructions for your operating system:

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify the installation by running:
```bash
uv --version
```

**Deliverable:** Screenshot showing `uv --version` output.

#### 1.3 Create a Virtual Environment (4 points)

Create a dedicated virtual environment for this course:

```bash
# Create a new directory for the course
mkdir mphy6120
cd mphy6120

# Initialize a new project with uv
uv init

# Create virtual environment with Python 3.11
uv venv --python 3.11
```

Activate the virtual environment:

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```powershell
.venv\Scripts\activate
```

**Deliverable:** Screenshot showing your activated virtual environment (your prompt should show `(.venv)` or similar).

#### 1.4 Install Required Packages (4 points)

Install the core packages we'll use throughout the course:

```bash
uv pip install torch numpy pandas matplotlib jupyter ipykernel
```

**Note:** If you have an NVIDIA GPU and want CUDA support, follow the [PyTorch installation guide](https://pytorch.org/get-started/locally/) for your specific setup.

Verify your installation by starting Python and running:

```python
import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print(f"PyTorch version: {torch.__version__}")
print(f"NumPy version: {np.__version__}")
print(f"Pandas version: {pd.__version__}")
print("All packages imported successfully!")
```

**Deliverable:** Screenshot showing successful package imports with version numbers.

---

### Part 2: Python Skills Review (40 points)

Complete the following exercises in `hw1_exercises.py` from your cloned repository. The file contains function stubs—replace the `None` values with your implementations.

#### 2.1 NumPy Array Operations (15 points)

1. **Array Creation (3 pts):** Create a 1D NumPy array containing the integers 1 through 10.

2. **Random Matrix (3 pts):** Create a 3x3 matrix of random values between 0 and 1 using `np.random.rand()`.

3. **Statistics (3 pts):** For your random matrix, compute and print the mean, standard deviation, min, and max.

4. **Reshaping (3 pts):** Create a 1D array of 12 elements and reshape it into a 3x4 matrix.

5. **Slicing (3 pts):** From your 3x3 random matrix, extract a 2x2 submatrix from the top-left corner.

#### 2.2 Pandas DataFrames (15 points)

1. **Create DataFrame (3 pts):** Create a DataFrame with columns `patient_id`, `age`, `heart_rate`, and `diagnosis` with at least 10 rows of sample data.

2. **Add Column (3 pts):** Add a new column `age_group` that categorizes patients as "young" (< 40), "middle" (40-65), or "senior" (> 65).

3. **Filter (3 pts):** Filter the DataFrame to show only patients with heart rate > 80.

4. **GroupBy (3 pts):** Group by `diagnosis` and compute the mean age and heart rate for each group.

5. **Missing Data (3 pts):** Introduce some `NaN` values into your DataFrame, then demonstrate using `fillna()` or `dropna()`.

#### 2.3 Matplotlib Visualization (10 points)

Create the following visualizations with proper labels, titles, and legends:

1. **Line Plot (2.5 pts):** Plot $y = x^2$ for $x \in [0, 10]$.

2. **Scatter Plot (2.5 pts):** Create a scatter plot of random (x, y) data with at least 50 points.

3. **Histogram (2.5 pts):** Generate 1000 samples from a normal distribution and plot a histogram.

4. **Bar Chart (2.5 pts):** Create a bar chart showing the count of patients per diagnosis from your DataFrame.

---

### Part 3: PyTorch Basics (25 points)

Continue working in `hw1_exercises.py` for these exercises.

#### 3.1 Tensor Creation (10 points)

1. **From List (2 pts):** Create a 2D tensor from a nested Python list.

2. **Special Tensors (4 pts):** Create tensors using:
   - `torch.zeros(3, 4)`
   - `torch.ones(2, 3)`
   - `torch.rand(3, 3)`
   - `torch.arange(0, 10, 2)`

3. **Tensor Properties (4 pts):** For each tensor you created, print its `dtype`, `shape`, and `device`.

#### 3.2 Tensor Operations (10 points)

1. **Element-wise (3 pts):** Create two 3x3 random tensors and perform element-wise addition, multiplication, and exponentiation.

2. **Matrix Operations (4 pts):** Perform matrix multiplication (`@` or `torch.matmul`) and transpose.

3. **NumPy Conversion (3 pts):** Convert a PyTorch tensor to a NumPy array and back. Demonstrate that changes to one affect the other (shared memory).

#### 3.3 GPU/CUDA Check (10 points)

Write code that:

1. **Check Availability (4 pts):** Check if CUDA is available and print the result.

2. **GPU Info (3 pts):** If CUDA is available, print the GPU device name. If not, print a message saying CPU will be used.

3. **Device Transfer (3 pts):** Create a tensor and move it to the available device (GPU if available, otherwise CPU). Print the tensor's device.

```python
# Example structure
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")

x = torch.rand(3, 3).to(device)
print(f"Tensor device: {x.device}")
```

---

## Submission via GitHub

All submissions for this course are done through GitHub. This mirrors real-world software development workflows and helps you build essential version control skills.

### How to Submit

1. **Complete your work** in `hw1_exercises.py` (replace `None` values with your code)
2. **Commit your changes** with meaningful commit messages:
   ```bash
   git add hw1_exercises.py
   git commit -m "Complete NumPy exercises 2.1.1-2.1.5"
   ```
3. **Push to GitHub** before the deadline:
   ```bash
   git push
   ```

### Commit Expectations

Good commit habits are part of your grade. We expect:

- **Multiple commits** showing your progress (not just one giant commit at the end)
- **Meaningful commit messages** that describe what you did (e.g., "Add patient DataFrame with age groups" not "stuff")
- **Working code** in your final commit (we grade the last commit before the deadline)

### Example Good Commit History
```
a]b3f2d1 Complete Part 3: PyTorch CUDA check
8c4e5f6 Add tensor operations and NumPy conversion
2d1a9b7 Complete Part 2: matplotlib visualizations
f7e8c3a Add pandas DataFrame exercises
9a2b4c5 Complete NumPy array operations
1e6d8f2 Verify environment setup - all packages installed
```

### Why Git Matters

In the era of AI-assisted coding, your commit history tells the story of *your* work:
- It shows your problem-solving process
- It distinguishes your contributions from AI-generated code
- It's a skill every employer expects

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| **Part 1: Environment Setup** | **25** |
| 1.1 VS Code + GitHub Copilot configured | 9 |
| 1.2 uv installation verified | 8 |
| 1.3 Virtual environment created | 4 |
| 1.4 Packages installed correctly | 4 |
| **Part 2: Python Skills** | **40** |
| 2.1 NumPy exercises | 15 |
| 2.2 Pandas exercises | 15 |
| 2.3 Matplotlib visualizations | 10 |
| **Part 3: PyTorch Basics** | **25** |
| 3.1 Tensor creation | 8 |
| 3.2 Tensor operations | 9 |
| 3.3 GPU/CUDA check | 8 |
| **Git Workflow** | **10** |
| Multiple meaningful commits | 5 |
| Clear commit messages | 5 |
| **Total** | **100** |

---

## Resources

- [Git Handbook](https://guides.github.com/introduction/git-handbook/) — If you're new to Git
- [uv Documentation](https://docs.astral.sh/uv/)
- [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [Pandas Getting Started](https://pandas.pydata.org/docs/getting_started/index.html)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)

---

## Tips

- **Start early!** Environment setup can sometimes have unexpected issues. GitHub Education verification can take 1-2 days.
- **Commit often** — Don't wait until you're done to make your first commit.
- **Use the course GitHub Discussions** or office hours if you get stuck.
- **If you don't have a GPU**, that's completely fine—all coursework can be done on CPU.
- **Use Copilot wisely** — Let it help you learn syntax and explore approaches, but understand every line you submit.

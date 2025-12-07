---
layout: default
title: Homework 1 - Python Environment & Basics
active_tab: homework
due_date: 2025-02-04 23:59:00 EST
---

# Homework 1: Python Environment & Basics
**Due: {{ page.due_date | date: "%A, %B %-d, %Y at %I:%M %p" }}**

---

## Learning Objectives

By completing this assignment, you will:

- Set up your Python development environment using `uv`
- Verify PyTorch installation and GPU access (if available)
- Practice basic Python skills needed for the course
- Submit your first assignment via Gradescope

---

## Instructions

### Part 1: Environment Setup (30 points)

#### 1.1 Install uv Package Manager (10 points)

[uv](https://github.com/astral-sh/uv) is a fast Python package manager that we'll use throughout the course. Install it by following the instructions for your operating system:

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify the installation:
```bash
uv --version
```

#### 1.2 Create a Virtual Environment (10 points)

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

#### 1.3 Install Required Packages (10 points)

Install the core packages we'll use throughout the course:

```bash
uv pip install torch numpy pandas matplotlib jupyter ipykernel
```

**Note:** If you have an NVIDIA GPU and want CUDA support, follow the [PyTorch installation guide](https://pytorch.org/get-started/locally/) for your specific setup.

Verify your installation by running Python and checking imports:

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

---

### Part 2: Python Skills Review (40 points)

Complete the following exercises in a Jupyter notebook named `hw1_python_skills.ipynb`.

#### 2.1 NumPy Array Operations (15 points)

1. Create a 1D NumPy array containing the integers 1 through 10
2. Create a 3x3 matrix of random values between 0 and 1
3. Compute the mean, standard deviation, min, and max of your random matrix
4. Reshape a 1D array of 12 elements into a 3x4 matrix
5. Demonstrate array slicing: extract a 2x2 submatrix from your 3x3 matrix

#### 2.2 Pandas DataFrames (15 points)

1. Create a DataFrame with at least 3 columns and 10 rows of sample data (e.g., patient_id, age, diagnosis)
2. Add a new column based on calculations from existing columns
3. Filter the DataFrame based on a condition
4. Group data by one column and compute summary statistics
5. Handle missing values: introduce some NaN values and demonstrate `fillna()` or `dropna()`

#### 2.3 Basic Plotting with Matplotlib (10 points)

Create the following visualizations:

1. A line plot showing a simple mathematical function (e.g., $y = x^2$)
2. A scatter plot of random data with appropriate labels and title
3. A histogram of normally distributed random data
4. A bar chart comparing categorical data

Include proper labels, titles, and legends where appropriate.

---

### Part 3: PyTorch Basics (30 points)

Complete the following exercises in the same notebook or a new one named `hw1_pytorch_basics.ipynb`.

#### 3.1 Create and Manipulate Tensors (10 points)

1. Create tensors using different methods:
   - From a Python list
   - Using `torch.zeros()`, `torch.ones()`, `torch.rand()`
   - Using `torch.arange()` and `torch.linspace()`

2. Check tensor properties: `dtype`, `shape`, `device`

#### 3.2 Basic Tensor Operations (10 points)

1. Perform element-wise operations: addition, multiplication, exponentiation
2. Perform matrix operations: matrix multiplication, transpose
3. Demonstrate broadcasting with tensors of different shapes
4. Convert between NumPy arrays and PyTorch tensors

#### 3.3 GPU/CUDA Check (10 points)

Write code that:

1. Checks if CUDA is available on your system
2. If available, moves a tensor to GPU and back to CPU
3. Reports GPU device name and memory (if available)
4. Handles the case gracefully when no GPU is present

Example structure:
```python
import torch

# Check CUDA availability
cuda_available = torch.cuda.is_available()
print(f"CUDA available: {cuda_available}")

if cuda_available:
    print(f"GPU Device: {torch.cuda.get_device_name(0)}")
    # Move tensor to GPU
    x = torch.rand(3, 3)
    x_gpu = x.to('cuda')
    print(f"Tensor on GPU: {x_gpu.device}")
else:
    print("Running on CPU only - this is fine for most coursework!")
```

---

## Submission Instructions

1. **Create a PDF report** containing:
   - Screenshot of your terminal showing successful package installation
   - All code cells and their outputs from your Jupyter notebook(s)
   - Brief written answers explaining what each code block does

2. **Submit to Gradescope:**
   - Upload your PDF report
   - Upload your `.ipynb` notebook file(s)

3. **Naming convention:**
   - `hw1_lastname_firstname.pdf`
   - `hw1_python_skills.ipynb`
   - `hw1_pytorch_basics.ipynb`

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| **Part 1: Environment Setup** | **30** |
| uv installation verified | 10 |
| Virtual environment created | 10 |
| Packages installed correctly | 10 |
| **Part 2: Python Skills** | **40** |
| NumPy exercises complete | 15 |
| Pandas exercises complete | 15 |
| Matplotlib visualizations | 10 |
| **Part 3: PyTorch Basics** | **30** |
| Tensor creation & properties | 10 |
| Tensor operations | 10 |
| GPU/CUDA check | 10 |
| **Total** | **100** |

---

## Resources

- [uv Documentation](https://docs.astral.sh/uv/)
- [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [Pandas Getting Started](https://pandas.pydata.org/docs/getting_started/index.html)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Penn's Python Course on Coursera](https://www.coursera.org/learn/python-programming-intro)

---

## Tips

- Start early! Environment setup can sometimes have unexpected issues.
- Use the course GitHub Discussions or office hours if you get stuck.
- Document any errors you encounter and how you resolved them.
- If you don't have a GPU, that's completely fine - all coursework can be done on CPU.

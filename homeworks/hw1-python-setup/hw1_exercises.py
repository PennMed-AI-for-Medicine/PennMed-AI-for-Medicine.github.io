"""
MPHY 6120 - Homework 1: Python & Environment Setup
Due: January 28, 2026 at 11:59 PM EST

This is an alternative to the Jupyter notebook for students who prefer
working with .py files. Complete the exercises by replacing the `None`
values with your code.

Run with: python hw1_exercises.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch


def part1_environment_check():
    """Part 1: Environment Verification (30 points)"""
    print("=" * 60)
    print("Part 1: Environment Verification")
    print("=" * 60)

    import sys
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print(f"\nPyTorch version: {torch.__version__}")
    print(f"NumPy version: {np.__version__}")
    print(f"Pandas version: {pd.__version__}")
    print("\n✓ All packages imported successfully!")
    print()


# =============================================================================
# Part 2: Python Skills Review (40 points)
# =============================================================================

def exercise_2_1_numpy():
    """2.1 NumPy Array Operations (15 points)"""
    print("=" * 60)
    print("Exercise 2.1: NumPy Array Operations")
    print("=" * 60)

    # 2.1.1 (3 pts): Create a 1D array containing integers 1 through 10
    # YOUR CODE HERE
    arr_1d = None
    print(f"2.1.1 - 1D Array: {arr_1d}")

    # 2.1.2 (3 pts): Create a 3x3 matrix of random values between 0 and 1
    np.random.seed(42)
    # YOUR CODE HERE
    random_matrix = None
    print(f"\n2.1.2 - Random 3x3 Matrix:\n{random_matrix}")

    # 2.1.3 (3 pts): Compute mean, std, min, max of the random matrix
    # YOUR CODE HERE
    matrix_mean = None
    matrix_std = None
    matrix_min = None
    matrix_max = None
    print(f"\n2.1.3 - Statistics:")
    print(f"  Mean: {matrix_mean}")
    print(f"  Std:  {matrix_std}")
    print(f"  Min:  {matrix_min}")
    print(f"  Max:  {matrix_max}")

    # 2.1.4 (3 pts): Create a 1D array of 12 elements and reshape to 3x4
    # YOUR CODE HERE
    arr_12 = None
    reshaped = None
    print(f"\n2.1.4 - Reshaped (3x4):\n{reshaped}")

    # 2.1.5 (3 pts): Extract 2x2 submatrix from top-left corner
    # YOUR CODE HERE
    submatrix = None
    print(f"\n2.1.5 - 2x2 Submatrix (top-left):\n{submatrix}")
    print()

    return random_matrix  # Return for use in later exercises


def exercise_2_2_pandas():
    """2.2 Pandas DataFrames (15 points)"""
    print("=" * 60)
    print("Exercise 2.2: Pandas DataFrames")
    print("=" * 60)

    # 2.2.1 (3 pts): Create a DataFrame with patient data
    # Columns: patient_id, age, heart_rate, diagnosis
    # At least 10 rows, use diagnoses like: 'healthy', 'hypertension', 'arrhythmia'
    # YOUR CODE HERE
    df = None
    print("2.2.1 - Patient DataFrame:")
    print(df)

    # 2.2.2 (3 pts): Add 'age_group' column
    # "young": age < 40, "middle": 40 <= age <= 65, "senior": age > 65
    # YOUR CODE HERE

    print("\n2.2.2 - With age_group column:")
    print(df[['patient_id', 'age', 'age_group']] if df is not None else None)

    # 2.2.3 (3 pts): Filter patients with heart_rate > 80
    # YOUR CODE HERE
    high_hr_patients = None
    print("\n2.2.3 - Patients with heart rate > 80:")
    print(high_hr_patients)

    # 2.2.4 (3 pts): Group by diagnosis and compute mean age and heart_rate
    # YOUR CODE HERE
    grouped_stats = None
    print("\n2.2.4 - Statistics by diagnosis:")
    print(grouped_stats)

    # 2.2.5 (3 pts): Handle missing data
    # YOUR CODE HERE
    if df is not None:
        df_with_nan = df.copy()
        # Introduce NaN values
        # Then demonstrate fillna() or dropna()
        df_cleaned = None
        print("\n2.2.5 - After handling missing data:")
        print(df_cleaned)
    print()

    return df


def exercise_2_3_matplotlib(df):
    """2.3 Matplotlib Visualization (10 points)"""
    print("=" * 60)
    print("Exercise 2.3: Matplotlib Visualization")
    print("=" * 60)

    # Create a figure with 2x2 subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # 2.3.1 (2.5 pts): Line plot of y = x² for x ∈ [0, 10]
    ax1 = axes[0, 0]
    # YOUR CODE HERE
    # x = ...
    # y = ...
    # ax1.plot(x, y)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y = x²')
    ax1.set_title('2.3.1: Quadratic Function')
    ax1.grid(True, alpha=0.3)

    # 2.3.2 (2.5 pts): Scatter plot of random data (50+ points)
    ax2 = axes[0, 1]
    np.random.seed(42)
    # YOUR CODE HERE
    # x = ...
    # y = ...
    # ax2.scatter(x, y)
    ax2.set_xlabel('X values')
    ax2.set_ylabel('Y values')
    ax2.set_title('2.3.2: Random Scatter Plot')

    # 2.3.3 (2.5 pts): Histogram of normally distributed data (1000 samples)
    ax3 = axes[1, 0]
    np.random.seed(42)
    # YOUR CODE HERE
    # data = ...
    # ax3.hist(data, bins=30)
    ax3.set_xlabel('Value')
    ax3.set_ylabel('Frequency')
    ax3.set_title('2.3.3: Normal Distribution Histogram')

    # 2.3.4 (2.5 pts): Bar chart of patients per diagnosis
    ax4 = axes[1, 1]
    if df is not None:
        # YOUR CODE HERE
        # diagnosis_counts = df['diagnosis'].value_counts()
        # ax4.bar(diagnosis_counts.index, diagnosis_counts.values)
        pass
    ax4.set_xlabel('Diagnosis')
    ax4.set_ylabel('Number of Patients')
    ax4.set_title('2.3.4: Patient Count by Diagnosis')

    plt.tight_layout()
    plt.savefig('hw1_plots.png', dpi=150)
    print("Plots saved to hw1_plots.png")
    plt.show()
    print()


# =============================================================================
# Part 3: PyTorch Basics (30 points)
# =============================================================================

def exercise_3_1_tensors():
    """3.1 Tensor Creation (10 points)"""
    print("=" * 60)
    print("Exercise 3.1: Tensor Creation")
    print("=" * 60)

    # 3.1.1 (2 pts): Create a 2D tensor from a nested Python list
    # YOUR CODE HERE
    tensor_from_list = None
    print(f"3.1.1 - Tensor from list:\n{tensor_from_list}")

    # 3.1.2 (4 pts): Create special tensors
    # YOUR CODE HERE
    zeros_tensor = None      # 3x4 tensor of zeros
    ones_tensor = None       # 2x3 tensor of ones
    rand_tensor = None       # 3x3 tensor of random values
    arange_tensor = None     # tensor with values 0, 2, 4, 6, 8

    print(f"\n3.1.2 - Special tensors:")
    print(f"Zeros (3x4):\n{zeros_tensor}")
    print(f"\nOnes (2x3):\n{ones_tensor}")
    print(f"\nRandom (3x3):\n{rand_tensor}")
    print(f"\nArange (0, 10, step=2):\n{arange_tensor}")

    # 3.1.3 (4 pts): Print tensor properties
    print("\n3.1.3 - Tensor properties:")
    tensors = {
        'zeros_tensor': zeros_tensor,
        'ones_tensor': ones_tensor,
        'rand_tensor': rand_tensor,
        'arange_tensor': arange_tensor
    }
    for name, tensor in tensors.items():
        if tensor is not None:
            # YOUR CODE HERE
            # Print dtype, shape, device for each tensor
            pass
    print()


def exercise_3_2_operations():
    """3.2 Tensor Operations (10 points)"""
    print("=" * 60)
    print("Exercise 3.2: Tensor Operations")
    print("=" * 60)

    # 3.2.1 (3 pts): Element-wise operations
    torch.manual_seed(42)
    # YOUR CODE HERE
    a = None  # 3x3 random tensor
    b = None  # 3x3 random tensor
    addition = None       # a + b
    multiplication = None # a * b
    power = None          # a ** 2

    print("3.2.1 - Element-wise operations:")
    print(f"a + b:\n{addition}")
    print(f"\na * b:\n{multiplication}")
    print(f"\na ** 2:\n{power}")

    # 3.2.2 (4 pts): Matrix operations
    torch.manual_seed(42)
    # YOUR CODE HERE
    m1 = None  # 2x3 matrix
    m2 = None  # 3x2 matrix
    mat_mul = None        # m1 @ m2
    m1_transposed = None  # m1.T

    print("\n3.2.2 - Matrix operations:")
    print(f"m1 @ m2:\n{mat_mul}")
    print(f"\nm1 transposed:\n{m1_transposed}")

    # 3.2.3 (3 pts): NumPy conversion and shared memory
    print("\n3.2.3 - NumPy conversion:")
    torch_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
    # YOUR CODE HERE
    numpy_array = None  # Convert to NumPy

    if numpy_array is not None:
        numpy_array[0] = 100.0
        print(f"After modifying NumPy array[0] = 100:")
        print(f"NumPy array: {numpy_array}")
        print(f"PyTorch tensor: {torch_tensor}")
        print(f"Shared memory: {numpy_array[0] == torch_tensor[0].item()}")
    print()


def exercise_3_3_cuda():
    """3.3 GPU/CUDA Check (10 points)"""
    print("=" * 60)
    print("Exercise 3.3: GPU/CUDA Check")
    print("=" * 60)

    # 3.3.1 (4 pts): Check CUDA availability
    # YOUR CODE HERE
    cuda_available = None
    print(f"3.3.1 - CUDA available: {cuda_available}")

    # 3.3.2 (3 pts): Get GPU information (if available)
    print("\n3.3.2 - GPU information:")
    if torch.cuda.is_available():
        # YOUR CODE HERE
        # Print GPU device name
        pass
    else:
        print("CUDA is not available. Using CPU.")
        print("This is fine for all coursework!")

    # 3.3.3 (3 pts): Move tensor to device
    print("\n3.3.3 - Move tensor to device:")
    # YOUR CODE HERE
    device = None  # Create device object

    if device is not None:
        x = torch.rand(3, 3)
        x_on_device = None  # Move to device
        print(f"Using device: {device}")
        print(f"Tensor device: {x_on_device.device if x_on_device is not None else 'N/A'}")
    print()


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("MPHY 6120 - Homework 1: Python & Environment Setup")
    print("=" * 60 + "\n")

    # Part 1
    part1_environment_check()

    # Part 2
    random_matrix = exercise_2_1_numpy()
    df = exercise_2_2_pandas()
    exercise_2_3_matplotlib(df)

    # Part 3
    exercise_3_1_tensors()
    exercise_3_2_operations()
    exercise_3_3_cuda()

    print("=" * 60)
    print("Homework 1 Complete!")
    print("=" * 60)

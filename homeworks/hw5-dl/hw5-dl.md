---
layout: default
title: Homework 5 - Deep Learning for Medical Image Classification
active_tab: homework
release_date: 2026-03-18
due_date: 2026-03-25 23:59:00EST
classroom_link: https://classroom.github.com/a/XXXXXX
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
1. [**Accept the assignment on GitHub Classroom**]({{ page.classroom_link }}) — You'll get your own private repository with starter code and data
2. Clone your repo and complete the exercises in `hw5_dl.py`
3. Commit regularly as you work (this is part of your grade!)
4. Push your completed work to GitHub before the deadline
</div>

<div class="alert alert-warning" markdown="1">
**GPU Access:** This assignment involves training neural networks. While the models are small enough to train on CPU, GPU access will make training significantly faster. See the Resources section for GPU options.
</div>

---

## Learning Objectives

By completing this assignment, you will:

- Build and train a CNN for medical image classification using PyTorch
- Apply transfer learning from pretrained models
- Implement data augmentation for medical images
- Evaluate model performance with appropriate metrics
- Visualize what neural networks learn (filters, activations, Grad-CAM)

---

## Background

Deep learning has revolutionized medical image analysis. CNNs can now detect diabetic retinopathy, classify skin lesions, and identify lung nodules with expert-level performance. But building these models requires understanding both the deep learning fundamentals and the unique challenges of medical imaging.

In this assignment, you'll classify chest X-rays using the MedMNIST dataset — a standardized collection designed for educational purposes. You'll start with a simple CNN, then apply transfer learning, and finally interpret what your model has learned.

---

## The Dataset

We'll use **PneumoniaMNIST** from the MedMNIST collection:
- **Task**: Binary classification (Normal vs Pneumonia)
- **Images**: 5,856 chest X-ray images (28×28 grayscale)
- **Split**: 4,708 train / 524 val / 624 test
- **Source**: Derived from the Chest X-Ray Images (Pneumonia) dataset

The images are intentionally small (28×28) to enable fast training without GPUs while still teaching core concepts.

| Class | Label | Count (Train) |
|-------|-------|---------------|
| Normal | 0 | ~1,214 |
| Pneumonia | 1 | ~3,494 |

**Note**: The dataset is imbalanced (~75% pneumonia). Keep this in mind for evaluation!

---

## Instructions

### Part 1: Data Loading & Exploration (15 points)

**1.1 Load the Dataset (5 pts)**
- Use the `medmnist` package to load PneumoniaMNIST
- Create PyTorch DataLoaders for train, validation, and test sets
- Use appropriate batch sizes (e.g., 64 or 128)

**1.2 Visualize the Data (5 pts)**
- Display a grid of sample images from each class
- Show the class distribution (bar plot)
- Discuss: How might class imbalance affect training?

**1.3 Data Augmentation (5 pts)**
- Implement data augmentation for the training set:
  - Random horizontal flip
  - Random rotation (±10 degrees)
  - Random brightness/contrast adjustment
- Show examples of augmented images
- Why is augmentation important for medical imaging?

---

### Part 2: Build a Simple CNN (25 points)

**2.1 Define the Architecture (10 pts)**

Build a CNN from scratch with:
- 2-3 convolutional layers with ReLU activation
- Max pooling after each conv layer
- 1-2 fully connected layers
- Appropriate output layer for binary classification

Document your architecture choices.

**2.2 Training Loop (10 pts)**

Implement a training loop that:
- Uses Binary Cross Entropy loss (or CrossEntropyLoss)
- Uses Adam optimizer
- Tracks training and validation loss/accuracy per epoch
- Implements early stopping based on validation loss

**2.3 Training Curves (5 pts)**
- Plot training vs validation loss over epochs
- Plot training vs validation accuracy over epochs
- Is your model overfitting? How can you tell?

---

### Part 3: Transfer Learning (25 points)

**3.1 Load Pretrained Model (8 pts)**

Use a pretrained model (e.g., ResNet18) and adapt it for our task:
- Load pretrained weights (ImageNet)
- Modify the first conv layer to accept 1-channel input (grayscale)
- Replace the final layer for binary classification
- Discuss: Why might ImageNet pretrained weights help for medical images?

**3.2 Fine-Tuning Strategy (8 pts)**

Implement fine-tuning:
- First: Freeze all layers except the final classifier, train for a few epochs
- Then: Unfreeze and train the full model with a lower learning rate
- Compare this approach to training from scratch

**3.3 Compare Models (9 pts)**

Create a comparison table:

| Model | Test Accuracy | Test AUC | Precision | Recall | F1 |
|-------|--------------|----------|-----------|--------|-----|
| Simple CNN | | | | | |
| ResNet18 (from scratch) | | | | | |
| ResNet18 (pretrained) | | | | | |

Which model performs best? Why?

---

### Part 4: Model Evaluation (20 points)

**4.1 Confusion Matrix & Metrics (8 pts)**

For your best model:
- Display the confusion matrix on the test set
- Calculate and report: Accuracy, Precision, Recall, F1, AUC
- Given the clinical context (pneumonia detection), which metric matters most?

**4.2 ROC and PR Curves (6 pts)**
- Plot the ROC curve with AUC
- Plot the Precision-Recall curve with AP
- Mark the operating point for different threshold choices

**4.3 Error Analysis (6 pts)**
- Display examples of:
  - True Positives (correctly identified pneumonia)
  - True Negatives (correctly identified normal)
  - False Positives (normal misclassified as pneumonia)
  - False Negatives (pneumonia misclassified as normal)
- Can you identify patterns in the errors?

---

### Part 5: Model Interpretability (15 points)

**5.1 Visualize Filters (5 pts)**
- Display the learned filters from the first convolutional layer
- What patterns do these filters detect?

**5.2 Grad-CAM Visualization (10 pts)**

Implement Grad-CAM to visualize what the model focuses on:
- Select 4-6 test images (mix of correct and incorrect predictions)
- Generate Grad-CAM heatmaps
- Overlay heatmaps on original images
- Discuss: Is the model looking at clinically relevant regions?

---

## Reflection Questions

Answer these in code comments:

1. **Clinical Deployment**: If this model were deployed for pneumonia screening, what threshold would you choose? What are the consequences of false positives vs false negatives?

2. **Limitations**: What are three limitations of using MedMNIST (28×28 images) compared to real clinical chest X-rays?

3. **Next Steps**: What would you do differently if you had access to full-resolution chest X-rays and a GPU cluster?

---

## Submission via GitHub

1. **Complete your work** in `hw5_dl.py`
2. **Save your figures** to the `outputs/` directory
3. **Commit your changes** with meaningful messages
4. **Push to GitHub** before the deadline

### Deliverables

Your repository should contain:
- `hw5_dl.py` — Completed code with comments
- `outputs/` — Generated figures (PNG files)
- Clear commit history showing your progress

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| **Part 1: Data Loading & Exploration** | **15** |
| 1.1 Load dataset | 5 |
| 1.2 Visualize data | 5 |
| 1.3 Data augmentation | 5 |
| **Part 2: Simple CNN** | **25** |
| 2.1 Define architecture | 10 |
| 2.2 Training loop | 10 |
| 2.3 Training curves | 5 |
| **Part 3: Transfer Learning** | **25** |
| 3.1 Load pretrained model | 8 |
| 3.2 Fine-tuning strategy | 8 |
| 3.3 Compare models | 9 |
| **Part 4: Model Evaluation** | **20** |
| 4.1 Confusion matrix & metrics | 8 |
| 4.2 ROC and PR curves | 6 |
| 4.3 Error analysis | 6 |
| **Part 5: Interpretability** | **15** |
| 5.1 Visualize filters | 5 |
| 5.2 Grad-CAM | 10 |
| **Subtotal** | **100** |
| **Git Workflow** | |
| Multiple meaningful commits | -5 if missing |
| Clear commit messages | -5 if missing |

---

## Resources

### GPU Access Options
- **Google Colab** (free): Limited GPU time, good for experimentation
- **Penn HPC** (if available): Check with your department
- **Local GPU**: If you have one

### Documentation
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [MedMNIST Documentation](https://medmnist.com/)
- [Grad-CAM Paper](https://arxiv.org/abs/1610.02391)
- [Transfer Learning Tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)

---

## Tips

- **Start simple**: Get the basic CNN working before transfer learning
- **Monitor for overfitting**: Use validation loss, not just accuracy
- **Class imbalance**: Consider class weights or oversampling
- **Grad-CAM can be tricky**: Use existing implementations (e.g., `pytorch-grad-cam`)
- **Commit often**: After each part works
- **CPU is fine**: MedMNIST is designed to be trainable without GPUs

---
layout: default
title: Homework 3 - DICOM & Medical Imaging Fundamentals
active_tab: homework
release_date: 2026-02-11
due_date: 2026-02-25 23:59:00EST
classroom_link: https://classroom.github.com/a/iNGrBf7m
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
1. [**Accept the assignment on GitHub Classroom**]({{ page.classroom_link }}) — You'll get your own private repository with starter code and sample DICOM data
2. Clone your repo and complete the exercises in `hw3_dicom.py`
3. Commit regularly as you work (this is part of your grade!)
4. Push your completed work to GitHub before the deadline
</div>

<div class="alert alert-warning" markdown="1">
**Two-Track Structure:** This assignment has a **Core Track** (Parts 1-3) that everyone completes, and an **Advanced Track** (Part 4) for students who want to dive deeper into radiation therapy data. The Advanced Track is optional but can earn you extra credit.
</div>

---

## Learning Objectives

By completing this assignment, you will:

- Understand the DICOM file format and its importance in medical imaging
- Read and extract metadata from DICOM files using pydicom
- Visualize medical images with proper window/level settings
- Work with DICOM coordinate systems and spatial relationships
- **(Advanced)** Handle radiation therapy DICOM objects (RT Structure, RT Dose)

---

## Background

DICOM (Digital Imaging and Communications in Medicine) is the universal standard for medical imaging. Every CT scan, MRI, X-ray, and most other medical images you'll encounter in clinical AI are stored as DICOM files.

Understanding DICOM is essential because:
- **The metadata is often more valuable than the pixels** — patient info, acquisition parameters, spatial coordinates
- **Coordinate systems matter** — a model trained on one scanner may fail on another if you ignore geometry
- **Window/level affects what you see** — the same CT data looks completely different for lung vs. bone vs. soft tissue

---

## Instructions

### Part 1: DICOM Basics (30 points)

**1.1 Reading DICOM Files (10 pts)**

Load a CT DICOM file and extract key metadata:
- Patient ID, Study Date, Modality
- Image dimensions (Rows, Columns)
- Pixel spacing and Slice thickness
- Print a summary of the DICOM header

**1.2 Understanding DICOM Tags (10 pts)**

DICOM uses a tag system (Group, Element) to organize data. For the provided CT file:
- Look up 5 DICOM tags using the [DICOM Standard Browser](https://dicom.innolitics.com/)
- Explain what each tag represents and why it matters for AI applications
- Document your findings in the code comments

**1.3 Pixel Data Access (10 pts)**

Extract and examine the pixel array:
- Get the pixel array from the DICOM file
- Print its shape, dtype, min, max values
- Explain the difference between stored values and Hounsfield Units (HU)
- Apply the rescale slope and intercept to convert to HU

---

### Part 2: Visualization & Window/Level (30 points)

**2.1 Basic Visualization (10 pts)**

Display a CT slice using matplotlib:
- Show the image with a grayscale colormap
- Add a colorbar showing HU values
- Add appropriate title and axis labels

**2.2 Window/Level for Different Tissues (15 pts)**

The same CT data looks completely different depending on window/level settings. Create a figure showing the **same slice** with four different window/level presets:

| Preset | Window Width (W) | Window Level (L) | Use Case |
|--------|------------------|------------------|----------|
| Lung | 1500 | -600 | Lung parenchyma, airways |
| Soft Tissue | 400 | 40 | Abdomen, organs |
| Bone | 2000 | 400 | Skeletal structures |
| Brain | 80 | 40 | Brain parenchyma |

Display all four in a 2x2 subplot figure.

**2.3 Custom Window/Level Function (5 pts)**

Write a reusable function `apply_window_level(image, window, level)` that:
- Takes a HU image and window/level parameters
- Returns a normalized image (0-255) suitable for display
- Handles clipping appropriately

---

### Part 3: DICOM Geometry & Coordinates (25 points)

**3.1 Image Position and Orientation (10 pts)**

For medical imaging AI, understanding spatial relationships is critical. Extract and explain:
- `ImagePositionPatient` — Where is the top-left pixel in 3D space?
- `ImageOrientationPatient` — How is the image oriented?
- What coordinate system does DICOM use (LPS vs RAS)?

**3.2 Loading a CT Series (15 pts)**

A CT scan consists of many slices. Write code to:
- Load all DICOM files from a directory
- Sort them by slice location (hint: `SliceLocation` or `ImagePositionPatient[2]`)
- Stack them into a 3D numpy array
- Print the resulting volume dimensions and voxel spacing (dx, dy, dz)

---

### Part 4: Advanced Track — Radiation Therapy DICOM (25 points EXTRA CREDIT)

<div class="alert alert-info" markdown="1">
**Optional:** This section is for students who want to explore radiation therapy data. It covers RT Structure Sets, RT Dose, and DVH calculation. Complete Parts 1-3 first!
</div>

**4.1 RT Structure Set Basics (8 pts)**

RT Structure Sets (RTSTRUCT) contain contoured regions of interest (ROIs) like organs and tumors.

- Load the provided RT Structure file
- List all structure names and their ROI numbers
- Extract the contour data for one structure (e.g., "PTV" or "Bladder")
- Explain the format of contour data (how are the points stored?)

**4.2 RT Dose Visualization (8 pts)**

RT Dose files contain 3D dose distributions from radiation treatment planning.

- Load the RT Dose file
- Extract the dose grid and its spatial information
- Display a dose colorwash overlaid on a CT slice
- Use an appropriate colormap (e.g., `jet` or `hot`) with transparency

**4.3 DVH Calculation (9 pts)**

A Dose-Volume Histogram (DVH) is a fundamental tool in radiation oncology, showing what percentage of a structure receives at least a given dose.

- Using the RT Structure contours and RT Dose grid
- Calculate the DVH for one structure
- Plot the cumulative DVH (Volume % vs Dose in Gy)
- Report D95 (dose covering 95% of the volume) and V20 (volume receiving ≥20 Gy)

---

## Submission via GitHub

1. **Complete your work** in `hw3_dicom.py`
2. **Commit your changes** with meaningful messages:
   ```bash
   git add hw3_dicom.py
   git commit -m "Complete Part 2: window/level visualization"
   ```
3. **Push to GitHub** before the deadline:
   ```bash
   git push
   ```

### Commit Expectations

- **Multiple commits** showing your progress
- **Meaningful commit messages** describing what you did
- **Working code** in your final commit

---

## Grading Rubric

### Core Track (Required)

| Component | Points |
|-----------|--------|
| **Part 1: DICOM Basics** | **30** |
| 1.1 Reading DICOM files | 10 |
| 1.2 Understanding DICOM tags | 10 |
| 1.3 Pixel data access | 10 |
| **Part 2: Visualization** | **30** |
| 2.1 Basic visualization | 10 |
| 2.2 Window/level presets | 15 |
| 2.3 Custom W/L function | 5 |
| **Part 3: Geometry** | **25** |
| 3.1 Position and orientation | 10 |
| 3.2 Loading CT series | 15 |
| **Git Workflow** | **15** |
| Multiple meaningful commits | 8 |
| Clear commit messages | 7 |
| **Core Total** | **100** |

### Advanced Track (Extra Credit)

| Component | Points |
|-----------|--------|
| 4.1 RT Structure basics | 8 |
| 4.2 RT Dose visualization | 8 |
| 4.3 DVH calculation | 9 |
| **Advanced Total** | **+25** |

---

## Resources

- [DICOM Standard Browser](https://dicom.innolitics.com/) — Look up any DICOM tag
- [pydicom Documentation](https://pydicom.github.io/pydicom/stable/)
- [Radiopaedia: Windowing (CT)](https://radiopaedia.org/articles/windowing-ct) — Window/level explanation
- [DICOM Coordinate System](https://nipy.org/nibabel/dicom/dicom_orientation.html) — LPS coordinate system

---

## Tips

- **Start with Part 1** — Make sure you can read files before trying to visualize
- **Use the DICOM browser** — When you see an unfamiliar tag, look it up!
- **Window/level is just contrast adjustment** — Don't overthink it
- **The Advanced Track is genuinely hard** — Only attempt after completing Parts 1-3
- **Commit early and often** — Don't wait until you're done

---

## Sample Data

Your repository includes sample DICOM data in the `data/` directory:
- `data/ct/` — A small CT series (10-15 slices)
- `data/rt/` — RT Structure and RT Dose files (for Advanced Track)

This data is de-identified and safe to use for educational purposes.

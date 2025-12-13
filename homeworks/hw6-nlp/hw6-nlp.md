---
layout: default
title: Homework 6 - Clinical NLP & Large Language Models
active_tab: homework
release_date: 2026-04-01
due_date: 2026-04-15 23:59:00EST
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
1. [**Accept the assignment on GitHub Classroom**]({{ page.classroom_link }}) — You'll get your own private repository with starter code
2. Clone your repo and complete the exercises in `hw6_nlp.py`
3. Commit regularly as you work (this is part of your grade!)
4. Push your completed work to GitHub before the deadline
</div>

<div class="alert alert-warning" markdown="1">
**LLM Options:** Part 3 requires access to a large language model. You have several options:
- **Ollama + Llama 3** (free, local) — Recommended for most students
- **Course Azure credits** — Limited credits available; request access via Canvas
- **OpenAI API** — If you prefer; ~$2-5 for this assignment

See the Resources section for setup instructions.
</div>

---

## Learning Objectives

By completing this assignment, you will:

- Process and analyze clinical text using NLP techniques
- Extract medical entities using scispaCy and clinical NLP tools
- Understand word embeddings and their applications in medicine
- Use large language models for clinical NLP tasks
- Evaluate LLM outputs for accuracy and safety

---

## Background

Clinical notes contain rich information that's often inaccessible to traditional analysis. A radiology report might say "no evidence of acute cardiopulmonary process" — a human understands this means the lungs and heart look fine, but extracting that meaning computationally is challenging.

This assignment covers the NLP pipeline from traditional techniques to modern LLMs:
- **Part 1**: Text preprocessing and traditional NLP
- **Part 2**: Medical entity extraction with scispaCy
- **Part 3**: Prompting LLMs for clinical tasks
- **Part 4**: Evaluating LLM outputs for clinical safety

---

## The Data

We'll use **synthetic clinical notes** designed to mimic real discharge summaries without containing actual patient information. The notes include:
- Chief complaint and history of present illness
- Medications and allergies
- Assessment and plan sections

---

## Instructions

### Part 1: Text Preprocessing & Traditional NLP (20 points)

**1.1 Text Preprocessing (8 pts)**

Clinical text is messy. Implement preprocessing steps:
- Tokenization (handle medical abbreviations)
- Sentence segmentation
- Lowercasing (when appropriate)
- Handling of clinical-specific patterns (e.g., "pt" → "patient", "hx" → "history")

Compare your preprocessed output to the raw text.

**1.2 TF-IDF Analysis (7 pts)**

Using a collection of clinical notes:
- Build a TF-IDF representation
- Identify the most distinctive terms for different note types (if applicable)
- Discuss: Why might TF-IDF miss clinically important information?

**1.3 Text Classification Baseline (5 pts)**

Build a simple text classifier using TF-IDF + Logistic Regression:
- Classify notes by a relevant category (e.g., presence of specific condition)
- Report accuracy, precision, recall
- This is your baseline for comparison with LLM approaches

---

### Part 2: Medical Entity Extraction (25 points)

**2.1 Setup scispaCy (5 pts)**

Install and configure scispaCy with a clinical model:
```bash
pip install scispacy
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_core_sci_md-0.5.1.tar.gz
```

Load the model and process a sample clinical note.

**2.2 Named Entity Recognition (10 pts)**

Extract medical entities from clinical notes:
- Diseases/conditions
- Medications
- Procedures
- Anatomical locations

Visualize the extracted entities (displacy or custom visualization).

**2.3 UMLS Linking (10 pts)**

Link extracted entities to UMLS concepts:
- Use scispaCy's UMLS entity linker
- For each entity, display the top UMLS matches with CUI codes
- Discuss: Why is concept normalization important for clinical NLP?

---

### Part 3: LLM Prompting for Clinical Tasks (30 points)

**3.1 Zero-Shot Extraction (10 pts)**

Use an LLM (GPT-4 or similar) to extract structured information:

```python
prompt = """
Extract the following from this clinical note:
- Chief Complaint
- Medications (list)
- Allergies
- Primary Diagnosis

Clinical Note:
{note_text}

Return as JSON.
"""
```

Compare LLM extraction to scispaCy results. Which is more accurate?

**3.2 Clinical Summarization (10 pts)**

Prompt the LLM to generate:
- A brief summary suitable for patient handoff
- A list of action items for the care team

Evaluate the summaries for:
- Accuracy (does it capture key information?)
- Completeness (did it miss anything important?)
- Hallucination (did it add information not in the note?)

**3.3 Few-Shot Learning (10 pts)**

Compare zero-shot vs few-shot prompting:
- Provide 2-3 examples before the task
- Does few-shot improve extraction accuracy?
- Test on a held-out set of notes

Document your prompt engineering process.

---

### Part 4: LLM Evaluation & Safety (25 points)

**4.1 Hallucination Detection (10 pts)**

LLMs can "hallucinate" — generate plausible but incorrect information. This is especially dangerous in clinical settings.

Design tests to detect hallucinations:
- Create notes with specific facts
- Ask the LLM to extract/summarize
- Check if the output contains information not present in the input

Report your hallucination rate.

**4.2 Comparison Evaluation (8 pts)**

For a set of clinical notes, compare:

| Method | Accuracy | Completeness | Time | Cost |
|--------|----------|--------------|------|------|
| scispaCy | | | | Free |
| GPT-3.5 | | | | ~$0.002/note |
| GPT-4 | | | | ~$0.03/note |

When would you use each approach?

**4.3 Clinical Safety Analysis (7 pts)**

Analyze the failure modes of LLM-based extraction:
- What types of errors are most common?
- Which errors would be most dangerous clinically?
- How would you design guardrails for a production system?

---

## Reflection Questions

Answer these in code comments:

1. **Deployment**: Would you trust an LLM to extract medication lists for a clinical decision support system? What safeguards would you require?

2. **Cost-Benefit**: Given the cost and accuracy tradeoffs, when does using GPT-4 make sense vs. traditional NLP?

3. **Future Directions**: How might clinical NLP change in the next 5 years? What will still require human review?

---

## Submission via GitHub

1. **Complete your work** in `hw6_nlp.py`
2. **Save your outputs** to the `outputs/` directory
3. **Commit your changes** with meaningful messages
4. **Push to GitHub** before the deadline

**Important**: Do NOT commit your API keys! Use environment variables.

### Deliverables

Your repository should contain:
- `hw6_nlp.py` — Completed code with comments
- `outputs/` — Generated outputs and visualizations
- Clear commit history showing your progress

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| **Part 1: Traditional NLP** | **20** |
| 1.1 Text preprocessing | 8 |
| 1.2 TF-IDF analysis | 7 |
| 1.3 Text classification baseline | 5 |
| **Part 2: Medical Entity Extraction** | **25** |
| 2.1 Setup scispaCy | 5 |
| 2.2 Named entity recognition | 10 |
| 2.3 UMLS linking | 10 |
| **Part 3: LLM Prompting** | **30** |
| 3.1 Zero-shot extraction | 10 |
| 3.2 Clinical summarization | 10 |
| 3.3 Few-shot learning | 10 |
| **Part 4: Evaluation & Safety** | **25** |
| 4.1 Hallucination detection | 10 |
| 4.2 Comparison evaluation | 8 |
| 4.3 Clinical safety analysis | 7 |
| **Subtotal** | **100** |
| **Git Workflow** | |
| Multiple meaningful commits | -5 if missing |
| Clear commit messages | -5 if missing |

---

## Resources

### LLM Access Options

**Option 1: Ollama + Llama 3 (Recommended — Free)**

Run models locally on your laptop. Works great for this assignment.

```bash
# Install Ollama (macOS)
brew install ollama

# Or download from https://ollama.ai

# Pull Llama 3 (8B model, ~4GB)
ollama pull llama3

# Run it
ollama run llama3
```

In Python:
```python
import requests

def query_ollama(prompt, model="llama3"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False}
    )
    return response.json()["response"]
```

**Option 2: Course Azure Credits**

Limited credits available for GPT-4 access. Request via Canvas assignment. Use sparingly — these are shared resources.

**Option 3: OpenAI API**

If you prefer commercial API: [platform.openai.com](https://platform.openai.com/)
- Cost estimate: ~$2-5 for this assignment
- GPT-3.5 is much cheaper than GPT-4; use 3.5 for development

### Documentation
- [Ollama](https://ollama.ai/) — Local LLM runner
- [scispaCy](https://allenai.github.io/scispacy/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [UMLS Metathesaurus](https://www.nlm.nih.gov/research/umls/index.html)

### Papers
- [scispaCy: Fast and Robust Models for Biomedical NLP](https://arxiv.org/abs/1902.07669)
- [Large Language Models in Medicine](https://www.nature.com/articles/s41586-023-06291-2)

---

## Tips

- **Start with scispaCy** — Get entity extraction working before moving to LLMs
- **Cache API responses** — Don't re-call the API unnecessarily (saves money and time)
- **Use environment variables** — Never hardcode API keys
- **Be specific in prompts** — Vague prompts get vague results
- **Document your prompts** — Prompt engineering is part of the assignment
- **Commit often** — After each part works

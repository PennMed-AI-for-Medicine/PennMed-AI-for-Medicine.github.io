---
layout: default
title: Homework 6 - Clinical NLP & Large Language Models
active_tab: homework
release_date: 2026-04-01
due_date: 2026-04-21 23:59:00EST
classroom_link: https://classroom.github.com/a/LY_5FPlh
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
**LLM Access (Part 3-4):** You'll need access to at least two language models.

**Recommended: OpenRouter (free, no GPU needed)**
1. Create a free account at [openrouter.ai](https://openrouter.ai)
2. Generate an API key at [openrouter.ai/keys](https://openrouter.ai/keys)
3. Use the free-tier models (same setup as the in-class LLM Arena lab)

**Alternative: Ollama (local)**
If you set up Ollama during the lab, that works too. See [Resources](#resources) below.
</div>

---

## Learning Objectives

By completing this assignment, you will:

- Process clinical text using traditional NLP techniques
- Extract medical entities and detect negation
- Use LLMs programmatically for clinical NLP tasks
- Compare traditional NLP vs. LLM approaches on the same tasks
- Evaluate LLM outputs for hallucination and clinical safety

---

## Background

This assignment puts two generations of NLP side by side. You'll build a traditional pipeline (preprocessing, TF-IDF, entity extraction) and an LLM-powered pipeline, then run them on the **same clinical notes** and compare.

The punchline isn't "LLMs are better" — it's more nuanced than that. Traditional tools are deterministic, fast, and free. LLMs are flexible but hallucinate, cost money, and need guardrails. Understanding when to use each is a core clinical AI skill.

**This builds on the Module 8 Lab (LLM Arena):** In class you explored model capabilities interactively. Here you'll build evaluation pipelines programmatically.

---

## The Data

The starter repo includes **20 synthetic discharge summaries** (`data/notes.json`) with ground-truth annotations:
- Diagnoses, medications, allergies, and procedures for each note
- A classification label (complex discharge vs. routine)
- Notes vary in complexity, abbreviation density, and negation patterns

These notes mimic real clinical text without containing actual patient information.

---

## Instructions

### Part 1: Traditional Clinical NLP (20 points)

**1.1 Text Preprocessing (8 pts)**

Clinical text is messy. Implement a `preprocess_note(text)` function that handles:
- Abbreviation expansion (e.g., "pt" → "patient", "SOB" → "shortness of breath")
- Section segmentation (split into SUBJECTIVE, OBJECTIVE, ASSESSMENT, PLAN)
- Sentence tokenization that handles clinical patterns (e.g., "q4-6h", "2.5mg")

Run your preprocessor on 3 sample notes and show before/after output.

**1.2 TF-IDF Classification (12 pts)**

Build a classifier to identify **complex discharges** (patients needing extra follow-up):
- Create TF-IDF features from the preprocessed notes
- Train a Logistic Regression classifier
- Report accuracy, precision, recall, and F1 using leave-one-out cross-validation
- Print the top 5 words most predictive of each class

This is your **baseline** — you'll compare LLM performance against it in Part 4.

---

### Part 2: Medical Entity Extraction (20 points)

**2.1 Named Entity Recognition with scispaCy (10 pts)**

Extract medical entities from the clinical notes:

```python
# Setup (run once)
# uv add scispacy
# uv run python -m pip install \
#   https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_md-0.5.4.tar.gz
```

For each note, extract:
- Diseases/conditions
- Medications (name, dose if present)
- Procedures

Compare extracted entities to the ground-truth annotations. Report precision and recall for medication extraction specifically.

**If scispaCy installation fails** (e.g., network issues), implement a rule-based extractor using regex patterns for medications (drug name + dose + route + frequency) and report its precision/recall instead. Document what you tried.

**2.2 Negation Detection (10 pts)**

Negation changes everything: "no pneumonia" is the opposite of "pneumonia."

Implement a `detect_negation(sentence, entity)` function that returns `PRESENT`, `ABSENT`, or `UNCERTAIN` using prefix/suffix cue words (similar to what we built in the NLP walkthrough notebook).

Test on these cases and at least 5 of your own:
```
"No evidence of pneumonia"           → pneumonia: ABSENT
"Patient has diabetes"               → diabetes: PRESENT
"Ruled out PE"                       → PE: UNCERTAIN
"Patient denies chest pain"          → chest pain: ABSENT
"History of stroke, now resolved"    → stroke: ???  (discuss)
```

Discuss: Where does this simple approach fail? What would you need for production use?

---

### Part 3: LLM-Powered Clinical NLP (30 points)

Use the OpenRouter API (or Ollama) to access LLMs programmatically. The starter code includes a `query_llm()` helper function.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

def query_llm(prompt, system_prompt="", model="meta-llama/llama-3.2-3b-instruct:free"):
    """Query an LLM via OpenRouter. Returns the response text."""
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model=model, messages=messages, temperature=0.3, max_tokens=1024
    )
    return response.choices[0].message.content
```

**Important:** Never hardcode your API key. Use an environment variable:
```bash
export OPENROUTER_API_KEY="sk-or-..."
```

**3.1 Zero-Shot Information Extraction (10 pts)**

Write a prompt that extracts structured information from a clinical note:
- Chief complaint
- Medications (as a list with name, dose, route, frequency)
- Allergies
- Primary diagnosis

Return results as JSON. Test on at least 5 notes from the dataset.

For each note, verify the extracted data against ground truth. Report:
- How many medications were correctly extracted?
- Were any medications hallucinated (present in output but not in note)?
- Did the model return valid JSON every time?

**3.2 Prompt Engineering (10 pts)**

Take your extraction prompt from 3.1 and improve it systematically:

1. **Baseline** — your original zero-shot prompt
2. **Structured** — add explicit output format instructions and a system prompt
3. **Few-shot** — add 2 example note/extraction pairs before the target note

Run all three versions on the same 5 notes. Create a comparison table:

| Note | Version | Medications Found | Correct | Hallucinated | Valid JSON |
|------|---------|-------------------|---------|--------------|------------|
| 1    | Baseline | ... | ... | ... | ... |
| 1    | Structured | ... | ... | ... | ... |
| 1    | Few-shot | ... | ... | ... | ... |

Which version performed best? Did any version eliminate hallucinations entirely?

**3.3 Clinical Summarization (10 pts)**

Write a prompt that generates a **3-sentence handoff summary** for each note — the kind a night physician would read to take over care.

Generate summaries for 5 notes, then evaluate each summary on three criteria:
- **Accurate** — every claim in the summary is supported by the note (yes/no + explain)
- **Complete** — critical information is not missing (yes/no + what's missing)
- **Safe** — no hallucinated medications, doses, or diagnoses (yes/no + what's wrong)

This is manual evaluation — read the note, read the summary, and judge. Include your evaluations as code comments or a results table.

---

### Part 4: Head-to-Head Evaluation (30 points)

This is the capstone: put traditional NLP and LLMs on the same task and compare rigorously.

**4.1 Medication Extraction: scispaCy vs LLM (12 pts)**

Run **both** your scispaCy pipeline (Part 2.1) and your best LLM prompt (Part 3.2) on the same 10 notes. Extract medications from each.

Create a comparison table:

| Method | Precision | Recall | F1 | Avg Time/Note | Cost/Note | Hallucinations |
|--------|-----------|--------|----|---------------|-----------|----------------|
| scispaCy | | | | | Free | N/A |
| LLM (3B) | | | | | Free tier | |
| LLM (12B) | | | | | Free tier | |

If you have access to a larger model (via Ollama or paid API), add a row for it.

**4.2 Hallucination Stress Test (10 pts)**

Design 5 "trap" notes that test specific hallucination risks:
1. A note that mentions a drug was **discontinued** — does the LLM still list it as active?
2. A note with **no allergies documented** — does the LLM invent any?
3. A note mentioning a family member's condition — does the LLM attribute it to the patient?
4. A note with an **unusual but real** drug name — does the LLM change it to something more common?
5. A trap of your own design

For each trap, run your LLM prompt and document whether it fell for the trap.

Report your **hallucination rate**: out of all the traps across all notes, what fraction produced hallucinated content?

**4.3 Deployment Recommendation (8 pts)**

Write a brief analysis (~250 words) answering:

1. Your hospital wants to auto-extract medication lists from discharge notes to populate the patient portal. Which approach would you recommend (scispaCy, small LLM, large LLM, or hybrid) and why?

2. What specific failure modes would you test for before deployment?

3. What human oversight would you require?

Frame this as a recommendation to a non-technical hospital administrator — clear, specific, and honest about limitations.

---

## Deliverables

Your repository should contain:

| File | Description |
|------|-------------|
| `hw6_nlp.py` | All code with clear comments |
| `outputs/classification_results.txt` | Part 1.2 metrics and top features |
| `outputs/extraction_comparison.txt` | Part 3.2 prompt comparison table |
| `outputs/head_to_head.txt` | Part 4.1 comparison table |
| `outputs/hallucination_results.txt` | Part 4.2 trap results |

Written analyses (Parts 2.2 discussion, 3.3 evaluations, 4.3 recommendation) can be in code comments or a separate `analysis.md`.

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| **Part 1: Traditional NLP** | **20** |
| 1.1 Text preprocessing | 8 |
| 1.2 TF-IDF classification + metrics | 12 |
| **Part 2: Entity Extraction** | **20** |
| 2.1 scispaCy NER + accuracy | 10 |
| 2.2 Negation detection + discussion | 10 |
| **Part 3: LLM Clinical Tasks** | **30** |
| 3.1 Zero-shot extraction + verification | 10 |
| 3.2 Prompt engineering comparison | 10 |
| 3.3 Summarization + manual evaluation | 10 |
| **Part 4: Head-to-Head Evaluation** | **30** |
| 4.1 scispaCy vs LLM comparison | 12 |
| 4.2 Hallucination stress test | 10 |
| 4.3 Deployment recommendation | 8 |
| **Subtotal** | **100** |
| **Git Workflow** | |
| Multiple meaningful commits | -5 if missing |
| API key committed to repo | -10 |

---

## Resources {#resources}

### LLM Access

**Option 1: OpenRouter (Recommended)**

Free account, free models, no GPU needed.

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

# Free models to try:
# "meta-llama/llama-3.2-3b-instruct:free"  (small, fast)
# "google/gemma-3-12b-it:free"             (medium, better quality)
```

**Option 2: Ollama (Local)**

If you installed Ollama during the Module 8 lab:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
# Use whatever models you pulled: "llama3.2", "gemma3:4b", etc.
```

Both options use the same `openai` Python library — just different `base_url`.

### NLP Tools
- [scispaCy documentation](https://allenai.github.io/scispacy/)
- [scikit-learn TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)

### Papers
- [scispaCy: Fast and Robust Models for Biomedical NLP](https://arxiv.org/abs/1902.07669)
- [Benefits, Limits, and Risks of GPT-4 as an AI Chatbot for Medicine](https://www.nejm.org/doi/full/10.1056/NEJMsr2214184)

---

## Tips

- **Start with Parts 1-2** — traditional NLP has no API dependencies
- **Cache LLM responses** — save results to a file so you don't re-call the API while debugging
- **Set your API key as an environment variable**, not in your code: `export OPENROUTER_API_KEY="sk-or-..."`
- **The deployment recommendation (4.3) matters** — this is where you demonstrate clinical AI thinking, not just coding. Write it like a memo, not a homework answer.
- **Commit after each part** — don't save it all for the end

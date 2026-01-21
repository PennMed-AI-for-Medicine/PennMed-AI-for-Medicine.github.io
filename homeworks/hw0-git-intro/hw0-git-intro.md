---
layout: default
title: Homework 0 - Git & GitHub Practice
active_tab: homework
release_date: 2026-01-20
due_date: 2026-01-21 23:59:00EST
classroom_link: https://classroom.github.com/a/re50haE3
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

<div class="alert alert-warning" markdown="1">
**This is an ungraded practice assignment.** The goal is to make sure you can complete the basic Git workflow before HW1.
</div>

<div class="alert alert-success" markdown="1">
**Quick Start:**
1. Complete the [one-time setup](#one-time-setup-do-this-first) below
2. [Accept the assignment on GitHub Classroom]({{ page.classroom_link }})
3. Clone, edit, commit, push — done!
</div>

---

## Learning Objectives

By completing this assignment, you will:

- Set up a course folder on your computer
- Clone a repository from GitHub
- Edit files and commit your changes
- Push your work back to GitHub

This is the **core workflow** you'll use for every homework assignment this semester.

---

## Prerequisites

Before starting, make sure you have:

1. **A GitHub account** — [Sign up here](https://github.com/signup) if you don't have one
2. **Git installed** — See [installation instructions](#installing-git) below
3. **VS Code installed** — [Download here](https://code.visualstudio.com/)

---

## One-Time Setup (Do This First)

### 1. Create a course folder

Create a folder on your computer where you'll keep all your work for this course.

**Mac (Terminal):**
```bash
mkdir ~/MPHY6120
```

**Windows (Command Prompt or PowerShell):**
```bash
mkdir %USERPROFILE%\MPHY6120
```

Or just create a folder called `MPHY6120` in your home directory using Finder/File Explorer.

### 2. Learn to navigate to your folder

You'll need to open a terminal and navigate to your course folder. Practice this now:

**Mac (Terminal):**
```bash
cd ~/MPHY6120
```

**Windows (Command Prompt):**
```bash
cd %USERPROFILE%\MPHY6120
```

**Windows (PowerShell):**
```bash
cd ~\MPHY6120
```

**Tip:** You can also open a terminal directly in VS Code (View → Terminal), but you'll still need to navigate to your course folder.

### 3. Set up the VS Code terminal command

This lets you open VS Code from the command line by typing `code .`

1. Open VS Code
2. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows)
3. Type "shell command"
4. Select **"Shell Command: Install 'code' command in PATH"**
5. Restart your terminal

Test it by typing `code .` in your terminal — VS Code should open.

---

## The Assignment

### Step 1: Accept the assignment

[**Click here to accept the assignment on GitHub Classroom**]({{ page.classroom_link }})

This creates your own private repository. After accepting, you'll see a page with your repository URL.

### Step 2: Clone your repository

Open your terminal, navigate to your course folder, and clone:

```bash
cd ~/MPHY6120
git clone https://github.com/PennMed-AI-for-Medicine/hw0-git-intro-YOUR-USERNAME.git
cd hw0-git-intro-YOUR-USERNAME
```

Replace `YOUR-USERNAME` with your actual GitHub username (or just copy the URL from GitHub).

### Step 3: Open in VS Code

```bash
code .
```

Or open VS Code manually: File → Open Folder → select your `hw0-git-intro-YOUR-USERNAME` folder.

### Step 4: Edit the files

In VS Code, open and edit these two files:

1. **`students.md`** — Add yourself to the student roster following the format shown
2. **`exercises/reflection.md`** — Answer the questions about your background and goals

**Save both files** when you're done (Cmd+S / Ctrl+S).

### Step 5: Commit and push your changes

Go back to your terminal (or use the VS Code terminal) and run:

```bash
git status
git add students.md exercises/reflection.md
git commit -m "Add [Your Name] to roster and complete reflection"
git push
```

**What these commands do:**
- `git status` — Shows what files you changed
- `git add` — Stages files to be included in your commit
- `git commit -m "..."` — Saves your changes with a description
- `git push` — Uploads your commit to GitHub

---

## How Do I Know I'm Done?

1. Go to your repository on GitHub (refresh the page)
2. You should see your commit message at the top
3. Click on `students.md` and `exercises/reflection.md` to verify your changes are there

If you see your changes on GitHub, **you're done!**

---

## Troubleshooting

### "command not found: git"

Git isn't installed. See [Installing Git](#installing-git) below.

### "git push asks for username/password"

You need to set up authentication. The easiest way:
1. Install [GitHub CLI](https://cli.github.com/)
2. Run `gh auth login` and follow the prompts

### "git push says 'rejected' or 'failed'"

Run `git pull` first, then try `git push` again.

### "I don't see my changes on GitHub"

Make sure you ran all three commands: `git add`, `git commit`, AND `git push`. Check with `git status` — it should say "nothing to commit, working tree clean" and "Your branch is up to date".

### "The terminal says 'not a git repository'"

You're not in the right folder. Make sure you `cd` into your cloned repository folder.

---

## Installing Git

**Mac:**
Open Terminal and type `git --version`. If Git isn't installed, you'll be prompted to install it, or you can install via [Homebrew](https://brew.sh/): `brew install git`

**Windows:**
Download and install from [git-scm.com](https://git-scm.com/download/win). Use the default options during installation.

After installing, restart your terminal and verify with `git --version`.

---

## What About Branches and Pull Requests?

You may have heard about "branches" and "pull requests" — we'll introduce those concepts starting with HW1. For now, focus on mastering the basics: **clone → edit → commit → push**.

---

## Resources

- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Oh Shit, Git!?!](https://ohshitgit.com/) — For when things go wrong
- [GitHub CLI](https://cli.github.com/) — Makes authentication easier

---

## Questions?

Post on Ed Discussion with the `git` tag, or come to office hours.

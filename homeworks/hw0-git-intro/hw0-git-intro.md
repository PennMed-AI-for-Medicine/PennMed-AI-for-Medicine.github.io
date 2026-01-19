---
layout: default
title: Homework 0 - Git & GitHub Practice
active_tab: homework
release_date: 2026-01-20
due_date: 2026-01-20 23:59:00EST
classroom_link: TBD
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
**This is an ungraded in-class exercise.** We'll do this together on Day 1. If you can't complete this workflow in one class session, come to office hours immediately—you'll need this skill for every assignment.
</div>

<div class="alert alert-success" markdown="1">
**Get Started:**
1. [**Accept the assignment on GitHub Classroom**]({{ page.classroom_link }}) — You'll get your own private repository
2. Clone your repo to your local machine
3. Create a branch, make changes, commit, push, and open a pull request
</div>

---

## Learning Objectives

By completing this assignment, you will practice:

- Cloning a repository from GitHub
- Creating and switching branches
- Making commits with meaningful messages
- Pushing to a remote repository
- Creating a pull request

This is the **exact workflow** you'll use for every homework assignment this semester.

---

## Why Git Matters

In the era of AI-assisted coding, your **commit history tells the story of your work**:

- It shows your problem-solving process
- It distinguishes your contributions from AI-generated code
- It's a skill every employer expects

Good commit habits will also make your life easier when you need to undo mistakes or understand what you changed.

---

## Instructions

### Step 1: Clone Your Repository

After accepting the assignment on GitHub Classroom, clone your repo:

```bash
git clone <your-repo-url>
cd hw0-git-intro-<your-username>
```

### Step 2: Create a Branch

**Never work directly on `main`!** Always create a feature branch:

```bash
git checkout -b add-my-info
```

Verify you're on your branch:

```bash
git branch
```

You should see:
```
  main
* add-my-info
```

### Step 3: Complete the Tasks

#### Task 1: Add Yourself to the Roster

Open `students.md` and add your information following the format shown.

#### Task 2: Answer Reflection Questions

Open `exercises/reflection.md` and answer the questions about your background and goals for this course.

### Step 4: Commit Your Changes

```bash
# See what you changed
git status

# Stage your changes
git add students.md exercises/reflection.md

# Commit with a descriptive message
git commit -m "Add [Your Name] to roster and complete reflection"
```

**Good commit messages:**
- Start with a verb (Add, Fix, Update, Remove)
- Describe WHAT changed, not HOW
- Keep it under 50 characters

### Step 5: Push to GitHub

```bash
git push -u origin add-my-info
```

### Step 6: Create a Pull Request

1. Go to your repository on GitHub
2. Click "Compare & pull request"
3. Add a title and brief description
4. Click "Create pull request"

**Leave the PR open** — don't merge it. The instructors will review it.

---

## Troubleshooting

### "I made changes on main by accident"

```bash
# Create a new branch with your changes
git checkout -b add-my-info
# Your changes come with you!
```

### "I need to undo my last commit"

```bash
# Undo commit but keep changes
git reset --soft HEAD~1
```

### "I'm getting merge conflicts"

Don't panic! Post on Ed Discussion or come to office hours.

---

## Submission Checklist

Your submission is complete when:

- [ ] You've added yourself to `students.md`
- [ ] You've completed `exercises/reflection.md`
- [ ] You've pushed your branch to GitHub
- [ ] You've created a pull request (leave it open for review)

---

## Resources

- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Oh Shit, Git!?!](https://ohshitgit.com/) — For when things go wrong
- [📖 Textbook: Chapter 2 — Programming Fundamentals](https://rafemcbeth.github.io/Little-Book-of-Medical-AI/chapters/02-programming.html)

---

## Questions?

Post on Ed Discussion with the `git` tag, or come to office hours.

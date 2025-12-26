# .context/

This directory contains context files for AI assistant handoffs between sessions.

## Files

- **HANDOFF.md** — Current/recent session summary, decisions, and next steps
- **DECISIONS.md** — Running log of key architectural decisions (optional)
- **STATUS.md** — Current project status snapshot (optional)

## Purpose

These files help maintain continuity when working with AI assistants like Claude Code. They capture:

1. What was done and why
2. Current state of the project
3. Pending work and next steps
4. Key decisions and their rationale

## Usage

At the start of a new session, the AI assistant can read `HANDOFF.md` to quickly understand context. At the end of a session, update it with progress.

## Git Tracking

This directory can be:
- **Tracked** — Useful for team collaboration and history
- **Gitignored** — If you prefer private working notes

Currently: *Not gitignored* (your choice to add to `.gitignore`)

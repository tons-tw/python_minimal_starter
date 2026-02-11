---
name: git-commit
description: Create a git commit based on staged files
whenToUse: When the user asks to commit, save changes, or create a git commit
---

## Steps

1. Run these git commands to gather context:
   - `git status` — check staged files
   - `git diff --staged` — see what will be committed
   - `git branch --show-current` — current branch
   - `git log --oneline -10` — recent commit style

2. If nothing is staged, stop and tell the user.

3. Based on **staged files only**, create a git commit.

## Rules

1. **Conventional Commits** ([spec](https://www.conventionalcommits.org/en/v1.0.0/)):

   ```txt
   <type>(<scope>): <description>

   [body]
   ```

   - Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `data`
   - Add `!` for breaking changes: `feat!: remove old API`

2. **Good Commit Message** ([guide](https://chris.beams.io/posts/git-commit/)):
   - Subject: max 50 chars, no period, imperative mood ("add" not "added"), lowercase after type
   - Body (if needed): explain **what** and **why**, not how. Prefer bullet points.

3. **Simple English**: Short, common words. No idioms. Easy for non-native speakers to read.

4. **No AI Attribution**: No Claude badge, signature, `Co-Authored-By`, or `Generated with` lines.

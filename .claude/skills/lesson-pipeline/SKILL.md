---
name: lesson-pipeline
description: >
  Weekly lesson production pipeline for ISYS 320U Prescriptive Analytics.
  Use this skill whenever Scott asks to "run the lesson pipeline", "create lesson materials",
  "process lesson XX", "build this week's lesson", "generate lesson deliverables", or any
  similar request to produce the full set of course materials for a lesson. This is the
  primary skill for turning a raw lesson slide markdown file into all weekly deliverables:
  restructured slides, narratives PDF, image prompts + generated images, bullets-only markdown,
  enriched Jupyter notebooks, and a Blackboard quiz. Always use this skill when lesson
  materials or lesson production is mentioned.
---

# ISYS 320U: Lesson Production Pipeline

This skill automates the full weekly lesson production process. It implements the workflow in `Source Docs/LESSON_WORKFLOW_PIPELINE.md` with the following configuration choices for this course:

- **No PowerPoint (.pptx)** — bullets-only markdown is the final deliverable for slides
- **Full image generation** — runs `image_gen/main.py` after writing the prompts file
- **Human checkpoint** — pauses after slide restructuring for your review before generating all derived files
- **Quiz location** — saves to `04 Quizzes/lessonXX_quiz.txt` (not inside `Slides/`)

---

## Step 0: Identify the Lesson

If the user hasn't specified a lesson number, ask: *"Which lesson number are we processing this week? (e.g., 09)"*

Pad single digits with a leading zero: `09`, `10`, `11`. Use `XX` as the placeholder throughout.

**Repository root** (all relative paths below start here):
```
<mounted-folder>/prescriptive-analytics/
```
Where `<mounted-folder>` is the user's selected folder, e.g.:
`/sessions/.../mnt/ISYS 320U Prescriptive Analytics/`

The `04 Quizzes/` folder is one level up from the repository root:
```
<mounted-folder>/04 Quizzes/
```

---

## Phase 1: Restructure the Slides

**Input:** `Slides/lessonXX.md`
**Output:** `Slides/lessonXX_revised.md`

**Read these files first before writing anything:**
1. `Source Docs/syllabus_schedule.txt` — find the Week XX entry; these bullet points are the **primary learning objectives** and must all be explicitly covered
2. `Source Docs/master_lesson_blueprint.txt` — find the Week XX entry; use Core Concepts and Concepts Reinforced as supplementary depth, but not as a substitute for the syllabus objectives
3. `Slides/GENERIC_RESTRUCTURE_PLAN.md` — full restructuring rules
4. The two most recent prior `Slides/lessonYY_revised.md` files — for redundancy checking
5. `Source Docs/LESSON_WORKFLOW_PIPELINE.md` Steps 1–2 — for detailed guidance

**Key rules (see GENERIC_RESTRUCTURE_PLAN.md for full detail):**

- **Target:** 45–55 slides. Preserve slide count — do not aggressively reduce.
- **Syllabus first:** Every bullet in the `syllabus_schedule.txt` entry for Week XX must be explicitly covered with dedicated slide content. The master blueprint adds depth and detail but does not replace syllabus objectives.
- **Section structure:** Section heading slide → content slides → activity slide(s) → next section heading. Never collect all activities at the end.
- **Slide format:**
  ```markdown
  ## Slide N: Title

  **Slide Bullets:**
  - Top-level bullet
      - Sub-bullet (2–4 per top-level bullet)
  - Top-level bullet
      - Sub-bullet (2–4 per top-level bullet)
  - Top-level bullet
      - Sub-bullet (2–4 per top-level bullet)

  *[Why This Matters]* Single insight synthesizing the key takeaway for this entire slide — ONE per slide, placed after all bullets, not after individual bullets

  **Real-World Example:**
  - 1–5 bullets (prefer: auto dealership, credit union, unclaimed property, baseball/sports analytics, IT security)

  ---
  ```
- **Mini Demo / Stylus Walkthrough sections are NOT included in the revised file.** Do not copy Mini Demo content from the source into `lessonXX_revised.md`. Image prompts (Branch B) will be created directly from the revised slide bullets.
- **Activity slides:** `## Slide N: Activity: [Name]` — include only `**Slide Bullets:**` with the activity prompts. No `**Discussion:**` section. No `*[Why This Matters]*` on activity slides.
- **Key Takeaways slide:** No `*[Why This Matters]*` on the final Key Takeaways slide.
- **Section heading slides:** No bullets, no `*[Why This Matters]*` — title and `---` only.
- **Remove:** Look-ahead slides, time references in activities
- **Do NOT modify** `Slides/lessonXX.md` — always write to `_revised.md`
- Number all slides sequentially, no gaps

**Validate before proceeding:**
1. Count `## Slide` headers — must be 45–55
2. Every syllabus objective for Week XX is explicitly covered
3. Every blueprint Core Concept for Week XX is present
4. No redundancy with prior lessons (check last 5–6 slides especially)
5. Activities are at the end of their sections, not bunched at end of deck
6. Slides numbered sequentially with no gaps
7. No Mini Demo sections present anywhere in the file
8. Each content slide has exactly ONE `*[Why This Matters]*` statement after all bullets
9. No activity slide has a `**Discussion:**` section
10. **Real-world example audit:** Read all Real-World Example and Applied Example bullets across the entire file. Confirm no industry, organization, or scenario appears more than twice total. Replace any third+ occurrence with a different industry before submitting for review

---

## ⏸️ CHECKPOINT — Wait for Review

After Phase 1 completes:

1. Tell the user: *"Phase 1 complete. `Slides/lessonXX_revised.md` has been created with [N] slides covering [brief list of main sections]. Please review it and let me know when to proceed — or flag any changes you want first."*
2. Provide a direct link to the file.
3. **Do not start Phase 2 until the user explicitly says to proceed.**

---

## Phase 2: Parallel Deliverables

Once the user approves, launch Branches A, B, C, D, and E simultaneously as parallel subagents. Each branch is independent.

---

### Branch A — Narratives + PDF

**Input:** `Slides/lessonXX_revised.md`
**Outputs:** `Slides/lessonXX_narratives.md`, `Slides/lessonXX_narratives.pdf`

**Narratives markdown:**
- The revised file already has no Mini Demo sections — use it as-is for the narratives
- Keep everything exactly as-is: document title, `## Slide N: Title`, `---` dividers, `**Slide Bullets:**`, `*[Why This Matters]*`, `**Real-World Example:**`
- Do not rewrite, summarize, or rephrase any content

**Narratives PDF:**
- Use the script `Source Docs/generate_narratives_pdf.py` to produce the PDF — **do not use pandoc or any other converter**
- Edit the `md_path` and `out_path` variables at the bottom of the script to point to `Slides/lessonXX_narratives.md` and `Slides/lessonXX_narratives.pdf`, set `num_slides=999`, then run it:
  ```bash
  cd <repository-root>
  python3 "Source Docs/generate_narratives_pdf.py"
  ```
- This script uses reportlab and renders: `•` top-level bullets, `–` indented sub-bullets, italic blue *[Why This Matters]* lines, bold section labels, and thin HR dividers between slides
- Do NOT use the `pdf` skill or pandoc — they do not render markdown bullets correctly

---

### Branch B — Image Prompts + Image Generation

**Input:** `Slides/lessonXX_revised.md`
**Outputs:** `Slides/lessonXX_image-prompts.md`, then images + PDF via script

**Writing image prompts:**

The revised file has no Mini Demo sections. Instead, write one image prompt for each **content slide** (not section heading slides, activity slides, or the Key Takeaways slide). Derive the prompt from the slide's top-level bullets — the prompt should visualize the slide's core teaching concept.

```markdown
### Slide N: [Exact slide title]

**Prompt:** "[Single paragraph image prompt]"
```

Skip: section heading slides (title only), activity slides, Key Takeaways slide.

**Prompt style rules:**
- Open with: `"A simple hand-drawn whiteboard-style diagram.`
- Close with: `White background. Black lines and text only. No shading, no gradients, no decorative elements. Minimal detail — focus on the key concept only."`
- Lead with the **teaching concept** — what insight should a student take away?
- Show the minimum elements needed; avoid extra nodes, rows, or arrows
- For comparisons (e.g., feasible vs infeasible): two clearly labeled sides
- For before/after: two states with a dividing line and labels
- No tables with more than 3 rows or 3 columns
- Use `"Clear, readable labels."` when text labels matter

**Good prompt example:**
```
"A simple hand-drawn whiteboard-style diagram. Heading at top: 'Discrete vs Continuous'.
Two columns: left labeled 'Continuous' with 'Any value (e.g. 3.7)' below;
right labeled 'Discrete' with 'Whole numbers only (e.g. 3 or 4)' below.
A large X through '3.7' under the Discrete column.
Key message: 'You cannot hire 3.7 people' written below both columns.
White background. Black lines and text only. No shading, no gradients. Clear, readable labels."
```

**Running image generation:**

After saving `Slides/lessonXX_image-prompts.md`:

1. Update `image_gen/config.json`:
   ```json
   {
     "input_file": "Slides/lessonXX_image-prompts.md",
     "output_folder": "image_gen_outputs",
     "output_folder_name": "lessonXX",
     "pdf": "lessonXX_pictures.pdf"
   }
   ```
2. Confirm `image_gen/.env` contains `GOOGLE_AI_STUDIO_API_KEY`
3. Run from the repository root: `python image_gen/main.py`
4. Output PDF: `image_gen_outputs/lessonXX/lessonXX_pictures.pdf`

---

### Branch C — Bullets-Only Markdown

**Input:** `Slides/lessonXX_revised.md`
**Output:** `Slides/lessonXX_bullets_only.md`

**Format rules:**
- Slide title only — no `## Slide N:` prefix
- Use `•` for bullets (not `-`)
- Separate slides with `---`
- No section labels (`Slide Bullets:`, `Real-World Example:`, `Discussion:`)

| Slide type | What to include |
|---|---|
| Content slides | Title + top-level bullets from **Slide Bullets:** only (no sub-bullets, no narratives) |
| Activity slides | Title + all **Slide Bullets:** bullets + all **Discussion:** bullets |
| Section heading slides | Title only + `---` |

**Do NOT create a PowerPoint (.pptx).** Bullets markdown is the final deliverable.

---

### Branch D — Enrich and Validate Jupyter Notebooks

**Location:** `LessonXX/` folder
**Files:** All `lessonXX_conceptNN_*.ipynb` files

**Goal:** Make notebooks feel like a guided conversation with a patient instructor — not a code dump. Students have no Python background and are learning optimization concepts for the first time.

**Quality bar:** Read `Lesson08/lesson08_concept01_introduction_to_logical_constraints.ipynb` before starting. Every markdown cell in that notebook is the minimum standard for this work.

---

**Every code cell must be preceded by a rich markdown cell.** "Rich" means all of the following, not just one:

1. **A heading** that names the step (e.g., `## Step 2: Import Libraries`)
2. **Purpose paragraph** (2–3 sentences): What concept does this step demonstrate? Why does it matter to a student learning this topic? Connect it to the lesson's bigger idea — don't just describe mechanics.
3. **What the code does** (1–2 sentences): What inputs go in, what does it produce? Plain English — no jargon, no variable names.
4. **What to look for in the output** (specific, not vague): Tell students exactly what a correct result looks like and what would indicate a problem. For constraint violations: say what the violation means in plain English. For solver results: explain what "Optimal" means — "the solver found the best possible solution given the rules you gave it." For charts: say what pattern or comparison to focus on.

**Special rules by cell type:**

- **Install cells** (`%pip install ...`): Explain *why* these packages are needed — what does pulp do? pandas? Don't just say "install packages." Add: "What to look for: you should see 'Requirement already satisfied' if already installed, or installation messages otherwise. No action needed either way."
- **Import cells** (`import pandas...`): Explain what each library does in one sentence each. Add: "What to look for: no output is expected. If you see an error, a package may not be installed."
- **Data setup cells**: Explain *why* the specific values were chosen (not just what they are). If using costs of $1,000 and $1,500, explain what those represent and why they make the comparison useful for teaching the concept.
- **Empty or near-empty markdown cells**: A markdown cell with only a heading is not acceptable. Treat it the same as a missing markdown cell — write the full explanation.

**After every key result cell, check whether interpretation is needed:**
- If a result shows a constraint violation: does the preceding markdown explain what that violation means in plain English?
- If a result shows "Optimal" or solver status: is there a sentence explaining what that means?
- If a result produces numbers: is there context telling the student whether this is expected, surprising, or concerning?
- If a result is a chart: does the preceding markdown say what pattern to look for?

**Notebook-level requirements:**
- **Opening cell**: Rich intro explaining what this notebook demonstrates, why it matters to a student, and what they will be able to do after completing it. 3–5 sentences minimum.
- **Key Concepts cell**: Define every term used in the notebook before it appears in code. Plain English — no formulas.
- **Scenario cell**: Set up the business problem clearly. Who is making what decision? What are the constraints? What are the options?
- **Final cell**: Must be a markdown conclusion — not a code cell. Summarize: what did the student just see? What are the 3–4 key takeaways? How does this connect back to the lesson's larger theme?

**What "plain English" means here:**
- No: "We initialize the LP relaxation with the objective function coefficients"
- Yes: "We're telling the solver what we want to minimize (total cost) and what the rules are (at least one shift must be open)"
- No: "The coefficient of variation measures distributional spread"
- Yes: "This number tells us how unevenly the work is distributed — 0 means perfectly equal, higher numbers mean bigger gaps between the most and least burdened employees"

---

**Validation — run and check all notebooks:**

```bash
cd <repository-root>/LessonXX
jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=120 lessonXX_concept*.ipynb
```

Run one at a time if a notebook takes long. After each:
- All cells execute without error (fix any that don't — common causes: missing imports, deprecated function calls, wrong file paths)
- Numerical outputs make intuitive sense
- Charts have: title, labeled axes, legible text at reasonable font size
- No fractional values where integers are expected (e.g., "hire 3.7 people")
- Solver status explained in plain English in the adjacent markdown
- Final cell is a markdown conclusion, not a code cell

**Common issues to fix proactively:**
- Bare headings with no explanation — the most common failure; fix all of them
- Empty markdown cells (`<cell_type>markdown</cell_type>` with no content) — fill these
- Charts with no title or axis labels — add `ax.set_title(...)`, `ax.set_xlabel(...)`, `ax.set_ylabel(...)`
- "What to look for" that just says "see the results" — make it specific to what the output actually shows
- Missing conclusion cell — add one if the last cell is a code cell

---

### Branch E — Blackboard Quiz

**Output:** `<mounted-folder>/04 Quizzes/lessonXX_quiz.txt`

Note: this saves to `04 Quizzes/` in the parent folder, **not** inside `Slides/`.

**Purpose:** 10-question multiple-choice quiz for Blackboard. Low-stakes (15 minutes). Goal is concept reinforcement, not trivia.

**Source material rules:**
- Draw only from top-level slide bullets in `Slides/lessonXX_bullets_only.md` (or the `**Slide Bullets:**` top-level items in the revised file)
- Do NOT use activity slides, Mini Demo content, narratives, or image prompts as source
- Spread questions across the lesson's major concept sections — no clustering on one topic
- Do not reference "the lecture," "today's class," or slide numbers

**Question quality:**
- 10 questions, 4 answer choices each, exactly one correct answer
- Difficulty: undergraduate, paid-attention level — not trivial, not tricky
- Distractors must be plausible (no obviously absurd wrong answers)
- Prefer "why" and "what happens when" over pure recall
- Do not test definitions in isolation

**⚠️ Correct answer position MUST be randomized:**
Distribute the correct answer across positions A, B, C, and D throughout the 10 questions. Do not put the correct answer in the same position for more than 2–3 consecutive questions. A reasonable target: 2–3 questions with correct answer in each of the four positions.

**Blackboard format** — tab-separated, one question per line, no header row:
```
MC[TAB]Question text[TAB]Answer A text[TAB]correct[TAB]Answer B text[TAB]incorrect[TAB]Answer C text[TAB]incorrect[TAB]Answer D text[TAB]incorrect
```

Example line:
```
MC	Why can't you hire 3.7 people?	People are discrete units and cannot be split	correct	Optimization models only allow integers	incorrect	Labor laws prohibit fractional hiring	incorrect	Fractions increase model complexity	incorrect
```

Save as: `<mounted-folder>/04 Quizzes/lessonXX_quiz.txt`

---

## Phase 2 Completion Report

When all branches finish, summarize for the user:

- Links to all files created successfully
- Slide count in the revised file
- Number of image prompts generated and whether the image script ran cleanly
- Which notebooks had issues (if any) and what was fixed
- Confirmation that the quiz has randomized correct-answer positions

---

## Quick Reference: Output Files

| File | Location |
|---|---|
| `lessonXX_revised.md` | `Slides/` |
| `lessonXX_narratives.md` | `Slides/` |
| `lessonXX_narratives.pdf` | `Slides/` |
| `lessonXX_image-prompts.md` | `Slides/` |
| `lessonXX_pictures.pdf` | `image_gen_outputs/lessonXX/` |
| `lessonXX_bullets_only.md` | `Slides/` |
| `LessonXX/*.ipynb` (enriched) | `LessonXX/` |
| `lessonXX_quiz.txt` | `../04 Quizzes/` |

All `Slides/` paths are relative to the repository root (`prescriptive-analytics/`).
The quiz path is relative to the mounted folder root.

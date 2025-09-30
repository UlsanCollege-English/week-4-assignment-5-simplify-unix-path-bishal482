[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hznd-ymU)
# HW5 — Simplify Unix Path (Stack)

## Story
You’re building tooling around server logs that store messy absolute paths like `/a//b/./c/../d/`. You need to normalize them so automation stops tripping over weird segments.

## Task (Technical)
Implement `simplify_path(path: str) -> str`:
- Input is an **absolute** path (starts with `/`).
- Segments are split by `/` and may include:
  - `.`  (current dir) → ignore
  - `..` (parent) → pop one directory if possible
  - empty segments (from `//`) → ignore
- Output must be a canonical absolute path with **single slashes** and **no trailing slash**, except root `/`.

**Approach:** use a **stack** of directory names.

## Hints
1) Iterate segments; push normal names.
2) On `..`, `pop` if the stack isn’t empty; ignore otherwise (stay at root).
3) Join with `'/'` and prefix with `'/'`.

## Run tests locally
```bash
python -m pytest -q
```

## Submission

Push to GitHub Classroom

Commit → push → check Actions.

## Common problems
- Producing an empty string instead of / for the root.

- Treating relative paths (not required here).
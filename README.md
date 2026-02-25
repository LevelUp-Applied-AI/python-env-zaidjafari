[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/rZxQuJoV)
# AI.SPIRE Pre-Work — Python Toolchain

This repository is your workspace for Pre-Work Days 3–5.

| Day | PR | Topic |
|-----|-----|-------|
| 3 | PR-2 | Python venv Bootstrap + Sanity Script |
| 4 | PR-3 | Notebook vs Script: Same Output Two Ways |
| 5 | PR-4 | Compute & Debug Evidence Pack |

## Setup

Install Python 3.11 from [python.org](https://python.org), then:

bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
# source .venv/Scripts/activate  # Windows (Git Bash)
python -m pip install --upgrade pip
python -m pip install -r requirements-prework.txt


## Submitting PRs

1. Create a branch named for the PR task (e.g., pr-02-python-env)
2. Complete the work
3. Push the branch and open a PR from your branch to main
4. Submit the PR URL in TalentLMS
## When to use each

* **Jupyter Notebook:** I would choose a notebook when I am exploring a dataset and the next step depends on what I just saw, as it allows for interactive cell execution and immediate visual feedback. It is also perfect for building reports where code, charts, and narrative text must appear together.
* **Python Script:** I would choose a script for production environments where code needs to run in a deterministic, top-to-bottom manner, such as in a cron job or a CI/CD pipeline. Scripts are preferred when I need full testing support (like pytest) or a clean Git history without noisy JSON diffs.

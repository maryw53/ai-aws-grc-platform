---
name: FedRAMP SSP Setup
description: Install the frdocx-to-froscal-ssp Python pipeline and verify its dependencies. Idempotent.
---

# /fedramp-ssp:setup

Prepares the SSP DOCX→OSCAL pipeline. Clones `ethanolivertroy/frdocx-to-froscal-ssp`, installs its Python requirements into a dedicated virtualenv, and records the install path.

## How to run

```bash
bash plugins/fedramp-ssp/scripts/setup.sh [--python=<python3-executable>]
```

## What it does

1. Detect Python ≥ 3.10. `--python=/opt/homebrew/bin/python3.12` overrides.
2. Clone/update `ethanolivertroy/frdocx-to-froscal-ssp` into `~/.local/share/claude-grc/tools/frdocx-to-froscal-ssp`.
3. Create a virtualenv at `<tool-dir>/.venv` and `pip install -r requirements.txt` (primarily `python-docx`).
4. Verify that the entry-point script runs (`python cli.py --help` or equivalent).
5. Warn (not fail) if Java 17 isn't available — it's only needed for optional oscal-cli validation inside the pipeline; the `/oscal:validate` command from this toolkit can fill that role.
6. Write config:

   ```yaml
   version: 1
   source: fedramp-ssp
   source_version: "0.1.0"
   python: "/opt/homebrew/bin/python3.12"
   venv: "~/.local/share/claude-grc/tools/frdocx-to-froscal-ssp/.venv"
   tool_dir: "~/.local/share/claude-grc/tools/frdocx-to-froscal-ssp"
   oscal_version: "1.2.0"
   ```

## Typical output

```
fedramp-ssp:setup ✓
  python:      /opt/homebrew/bin/python3.12 (3.12.5)
  tool dir:    ~/.local/share/claude-grc/tools/frdocx-to-froscal-ssp
  venv:        ready (python-docx installed)
  java:        OpenJDK 17.0.11 (optional, available)
  config:      ~/.config/claude-grc/connectors/fedramp-ssp.yaml

Next:
  /fedramp-ssp:convert --ssp-docx=<path> --appendix-a-docx=<path>
```

## Failure modes

- **Python < 3.10**: exit 2. Install a newer Python or pass `--python=<path>`.
- **Network unreachable for git clone / pip**: exit 2.
- **Java missing**: *warn only*; the pipeline still produces OSCAL. Use `/oscal:validate` downstream instead of the tool's bundled validation step.

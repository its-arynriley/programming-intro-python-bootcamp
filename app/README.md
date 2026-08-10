# Track Career Analyzer App

This folder contains Track Career Analyzer, the app built during the bootcamp.

The app started as a terminal Python program and now includes a pandas-powered Streamlit browser app.

> [!NOTE]
> Early phases use only `app.py`. The Streamlit file is created later in Phase 08.

## App Growth

```mermaid
flowchart LR
    terminal["app.py terminal app"] --> csv["CSV-backed app"]
    csv --> pandas["pandas analysis"]
    pandas --> streamlit["streamlit_app.py browser app"]
```

## Run The Starter App

```bash
cd app
python3 app.py
```

## Install App Dependencies

Starting in Phase 07, use a local virtual environment before installing pandas and Streamlit:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run The Streamlit App

This file exists after Phase 08:

```bash
cd app
streamlit run streamlit_app.py
```

Fallback:

```bash
cd app
python3 -m streamlit run streamlit_app.py
```

## Data

Sample data lives in `data/sample_results.csv`.

The student's working data file is `data/results.csv`.

Before sharing or deploying, check this file for private information and replace anything that should not be public.

## App Link

Deployment status: Not deployed yet. The app can be run locally with Streamlit.

## Sharing Status

This app is ready for local sharing. Deployment can happen after the data file and repository are reviewed one more time for public readiness.

## Final Demo

Use the repository-level final demo checklist:

```text
../docs/final-demo-checklist.md
```

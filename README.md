# EDA Snacks

This project provides a starter structure for exploratory data analysis on snack datasets.

## Folder structure

- `data/raw/` — raw CSV files
- `data/processed/` — cleaned and transformed output data
- `notebooks/` — Jupyter notebooks for analysis
- `src/eda_snacks/` — reusable Python modules
- `tests/` — automated tests
- `docs/` — notes and documentation
- `scripts/` — runnable analysis scripts
- `outputs/figures/` — generated charts
- `outputs/reports/` — markdown or summary reports

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python -m src.eda_snacks
```

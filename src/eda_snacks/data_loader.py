from pathlib import Path

import pandas as pd


def load_csv(file_path: str | Path) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    path = Path(file_path)
    return pd.read_csv(path)


def list_data_files(directory: str | Path):
    """Return all CSV files in a given directory."""
    directory = Path(directory)
    if not directory.exists():
        return []
    return sorted(directory.glob("*.csv"))

from pathlib import Path

from .config import PROCESSED_DATA_DIR, RAW_DATA_DIR
from .data_loader import list_data_files, load_csv
from .preprocess import clean_column_names, fill_missing_values


def run_pipeline(raw_dir: str | Path = RAW_DATA_DIR, output_dir: str | Path = PROCESSED_DATA_DIR):
    """Process all CSV files in a raw data directory."""
    raw_path = Path(raw_dir)
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    processed_files = []
    for csv_file in list_data_files(raw_path):
        df = load_csv(csv_file)
        df = clean_column_names(df)
        df = fill_missing_values(df)
        target = out_path / f"processed_{csv_file.name}"
        df.to_csv(target, index=False)
        processed_files.append(target)

    return processed_files

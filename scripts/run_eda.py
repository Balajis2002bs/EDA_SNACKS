from pathlib import Path

from src.eda_snacks.config import RAW_DATA_DIR
from src.eda_snacks.pipeline import run_pipeline


def main():
    csv_files = sorted(Path(RAW_DATA_DIR).glob("*.csv"))
    print(f"Found {len(csv_files)} CSV file(s) in {RAW_DATA_DIR}")
    outputs = run_pipeline(RAW_DATA_DIR)
    print(f"Processed {len(outputs)} file(s)")


if __name__ == "__main__":
    main()

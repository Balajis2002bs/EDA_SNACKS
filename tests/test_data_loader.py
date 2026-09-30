from pathlib import Path

from src.eda_snacks.data_loader import list_data_files


def test_list_data_files_returns_csvs():
    data_dir = Path("data/raw")
    files = list_data_files(data_dir)
    assert all(file.suffix.lower() == ".csv" for file in files)

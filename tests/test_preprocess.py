import pandas as pd

from src.eda_snacks.preprocess import clean_column_names


def test_clean_column_names_handles_spaces():
    df = pd.DataFrame({"Snack Name": ["Chips"], "Unit Price": [10]})
    cleaned = clean_column_names(df)
    assert list(cleaned.columns) == ["snack_name", "unit_price"]

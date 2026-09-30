import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize column names to lowercase snake_case."""
    df = df.copy()
    df.columns = [str(col).strip().lower().replace(" ", "_") for col in df.columns]
    return df


def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill numeric missing values with median."""
    df = df.copy()
    for col in df.select_dtypes(include=["number"]).columns:
        df[col] = df[col].fillna(df[col].median())
    return df

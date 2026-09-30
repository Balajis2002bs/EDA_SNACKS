import pandas as pd


def describe_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Return general dataset statistics."""
    return df.describe(include="all").T


def missing_value_summary(df: pd.DataFrame) -> pd.Series:
    """Return missing-value counts per column."""
    return df.isna().sum()

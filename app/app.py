from pathlib import Path

import pandas as pd
import streamlit as st

from src.eda_snacks.data_loader import list_data_files, load_csv
from src.eda_snacks.preprocess import clean_column_names, fill_missing_values

st.set_page_config(page_title="EDA Snacks Dashboard", layout="wide")
st.title("EDA Snacks Dashboard")

raw_dir = Path("data/raw")
raw_dir.mkdir(parents=True, exist_ok=True)

csv_files = list_data_files(raw_dir)

if not csv_files:
    st.info("No CSV files found in data/raw. Add your dataset to begin.")
    st.stop()

selected_file = st.selectbox("Choose a dataset", [f.name for f in csv_files])
file_path = raw_dir / selected_file

df = load_csv(file_path)
cleaned_df = fill_missing_values(clean_column_names(df))

st.subheader("Dataset preview")
st.dataframe(cleaned_df.head(10), use_container_width=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Rows", len(cleaned_df))
with col2:
    st.metric("Columns", len(cleaned_df.columns))
with col3:
    st.metric("Missing values", int(cleaned_df.isna().sum().sum()))

st.subheader("Summary statistics")
st.dataframe(cleaned_df.describe(include="all").T, use_container_width=True)

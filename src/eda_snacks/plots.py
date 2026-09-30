import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns


def plot_distribution(df, column_name: str, bins: int = 20):
    """Plot the distribution of a numeric column."""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df[column_name], bins=bins, kde=True, ax=ax)
    ax.set_title(f"Distribution of {column_name}")
    fig.tight_layout()
    return fig

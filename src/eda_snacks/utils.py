from pathlib import Path


def ensure_directory(path):
    """Create a directory if it does not already exist."""
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory

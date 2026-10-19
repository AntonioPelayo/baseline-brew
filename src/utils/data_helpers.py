import os
import pandas as pd


def _read_csv(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"Could not load {path}: {e}")
        return pd.DataFrame()


def load_beans_dataframe() -> pd.DataFrame:
    """Load coffee bean purchases. Path can be overridden via COFFEE_BEANS_CSV."""
    return _read_csv(os.getenv('COFFEE_BEANS_CSV', 'data/coffee_beans.csv'))


def load_roasters_dataframe() -> pd.DataFrame:
    """Load roaster locations. Path can be overridden via COFFEE_ROASTERS_CSV."""
    return _read_csv(os.getenv('COFFEE_ROASTERS_CSV', 'data/coffee_roasters.csv'))


__all__ = [
    'load_beans_dataframe',
    'load_roasters_dataframe',
]

import numpy as np
import pandas as pd


def read_spaces_separated_csv_file(file_path: str) -> pd.DataFrame:
    """
    Read a CSV file separated by one or more spaces into a pandas DataFrame.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - pd.DataFrame: A DataFrame containing the data from the CSV file.

    Raises:
    - ValueError: If file_path is None or an empty string.
    - FileNotFoundError: If the file specified by file_path is not found.
    - pd.errors.EmptyDataError: If the specified file is empty.
    """

    if file_path is None:
        raise ValueError("File path cannot be None.")

    if file_path is None:
        raise ValueError("File path cannot be empty.")

    # Use pandas.read_csv with sep="\s+" to handle spaces as separators
    return pd.read_csv(file_path, sep="\s+") # noqa


def load_numpy_array_from_text(file_path: str, skip_rows: int = 0) -> np.ndarray:
    """
    Load data from a text file into a NumPy array, skipping a specified number of rows.

    Parameters:
    - file_path (str): The path to the text file.
    - skip_rows (int, optional): The number of rows to skip from the beginning of the file (default is 0).

    Returns:
    - np.ndarray: A NumPy array containing the loaded data.

    Raises:
    - ValueError: If file_path is None or an empty string.
    - ValueError: If skip_rows is less than 0.
    - FileNotFoundError: If the file specified by file_path is not found.
    """
    # Check if file_path is None or an empty string
    if file_path is None:
        raise ValueError("File path cannot be None.")

    if file_path == "":
        raise ValueError("File path cannot be empty.")

    # Check if skip_rows is less than 0
    if skip_rows < 0:
        raise ValueError("Number of rows to skip must be greater than or equal to 0.")

    # Use numpy.loadtxt to load data from the file
    return np.loadtxt(file_path, skiprows=skip_rows)

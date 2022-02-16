import numpy as np
import pandas as pd

from dataclasses import dataclass

class Sample:
    def __init__(self, fp: str):
        self.fp = fp
        self.csv = pd.read_csv(fp)
        self.df = pd.DataFrame()

@dataclass
class Data:
    ''' Stores the Input and Output Data Frames '''
    odf: None # Output DataFrame
    idf: None # Input DataFrame

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    def display(self, title='Output DataFrame', df='odf'):
        print(f'==== {title} ====\n\n{self[df]}\n')

def show(df: pd.DataFrame, msg='DataFrame'):
    ''' Displays the contents of a DataFrame in a block format '''
    print(msg)
    print('=' * len(msg))
    print(df)
    print('=' * len(msg) + '\n')

def catslice(idf: pd.DataFrame, odf: pd.DataFrame, cols: list[str] = None) -> pd.DataFrame:
    ''' Concatenates slices of data from a DataFrame

    If no columns are given, then the two DataFrames are concatenated together.

    Returns
    -------
    pd.DataFrame
        The DataFrame with the copied columns
    '''
    if cols is None:
        return pd.concat([idf, odf])
    else:
        for col in cols:
            odf[col] = idf[col].copy()
        return odf

# def expand(data: pd.DataFrame, col: str, val) -> pd.DataFrame:
    # ''' Expands a single value into a DataFrame '''
    # # default_values = np.repeat(np.arange(nvalues), ncolumns).reshape(nvalues, ncolumns)
    # col_len = data.shape[0]
    # array   = np.full(col_len, val)
    # arraydf = pd.DataFrame(array)
    # return()

def expand(nvalues, ncolumns) -> np.ndarray:
    ''' Expands values into Numpy Arrays '''
    array = np.repeat(np.arange(nvalues), ncolumns).reshape(nvalues, ncolumns)
    return array

def export(df: pd.DataFrame, dest: str, cols: list = None):
    ''' Exports a csv file of the Data Frame to a destination

    Parameters
    ----------
    df : pd.DataFrame
        A Pandas DataFrame
    dest : str
        File path to the output csv file
    cols : list
        A list of columns to copy over from df

    Returns
    -------
    None
    '''
    output: pd.DataFrame = df if cols is None else df[cols] # Split behavior into splice method
    show(output) # Side effect
    output.to_csv(dest, index=False)

# Numpy Arrays
def colavg(data: pd.DataFrame, col='avg') -> np.ndarray:
    masses = data[col].to_numpy()
    return np.average(masses)

def stdev(df: pd.DataFrame, col: str) -> np.ndarray:
    ''' Returns the standard deviation of the input Data Frame

    Parameters
    ----------
    data : Data
        A Data dataclass
    col : str
        The column to calculate stdev on

    Returns
    -------
    np.ndarray
        Returns a Numpy Array filled with the standard deviation
        from the input DataFrame
    '''
    return(np.std(df.to_numpy()))

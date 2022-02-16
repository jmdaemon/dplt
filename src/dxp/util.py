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

def expand(nvalues, ncolumns) -> np.ndarray:
    ''' Expands values into Numpy Arrays '''
    array = np.repeat(np.arange(nvalues), ncolumns).reshape(nvalues, ncolumns)
    return array

def slice(df: pd.DataFrame, cols: list[str]):
    ''' Return a slice of the DataFrame's columns '''
    return df[cols]

# Numpy Arrays
def colavg(df: pd.DataFrame, col='avg') -> np.ndarray:
    ''' Return the average of an entire column '''
    values = df[col].to_numpy()
    return np.average(values)

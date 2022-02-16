import numpy as np
import pandas as pd

class Sample:
    def __init__(self, fp: str, df: pd.DataFrame):
        self.fp = fp
        self.df = df

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

def colavg(df: pd.DataFrame, col='avg') -> np.ndarray:
    ''' Return the average of an entire column '''
    values = df[col].to_numpy()
    return np.average(values)

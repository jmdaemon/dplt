import numpy as np
import pandas as pd

from dataclasses import dataclass

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


# Pandas DataFrames

## Displaying
def head(data: Data):
    ''' Displays the head of both the input and output Data Frames '''
    print(f'==== Output DataFrame ====\n\n{data.odf.head()}\n')
    print(f'==== Input DataFrame ====\n\n{data.idf.head()}\n')

def display(df: pd.DataFrame, title='DataFrame'):
    ''' Displays the contents of a Pandas DataFrame '''
    print(f'==== {title} ====\n\n{df}\n')

## Helper Functions
def shape(df: pd.DataFrame):
    ''' Returns the shape of a DataFrame'''
    shape = df.shape[0]
    return shape

def copy(data: Data, cols: list[str] = None) -> Data:
    ''' Copies all the data from cols in data.idf to data.odf

    Parameters
    ----------
    cols : list[str]
        List of columns to copy

    Returns
    -------
    Data
        The Data dataclass
    '''
    cols = data.idf.columns.tolist() if cols is None else None
    for col in cols:
        data.odf[col] = data.idf[col].copy()
    return data

def merge(data: pd.DataFrame, arr: np.ndarray, col: str) -> pd.DataFrame:
    ''' Merges a Numpy Array into a Pandas DataFrame

    Parameters
    ----------
    data : Data
        Data dataclass object
    arr : np.ndarray
        Numpy Array to copy from
    col : str
        Sets the destination column of the copied data in the
        Pandas DataFrame

    Returns
    -------
    pd.DataFrame
        The resulting DataFrame with the new merged values
    '''
    data[col] = pd.DataFrame(arr)
    return data

# Type mismatch
def expand(data: Data, val, col: str) -> pd.DataFrame:
    array = np.full(data.idf.shape[0], val)
    return(merge(data, array, col))

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
    display(output) # Side effect
    output.to_csv(dest, index=False)

# Numpy Arrays
def avg(data: Data, col='avg') -> np.ndarray:
    masses = data.idf[col].to_numpy()
    return np.average(masses)

def stdev(data: Data, col: str) -> np.ndarray:
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
    return(np.std(data.idf[col].to_numpy()))

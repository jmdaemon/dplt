import dxp.calc as pc
import numpy as np
import pandas as pd

# Displaying
def head(data: pd.DataFrame, inputs: pd.DataFrame):
    print(f'==== Output DataFrame ====\n\n{data.head()}\n')
    print(f'==== Input DataFrame ====\n\n{inputs.head()}\n')

def display(df: pd.DataFrame, title='Output DataFrame', *args, **kwargs):
    print(f'==== {title} ====\n')
    print(f'{df}\n')

# For DataFrames
def shape(df: pd.DataFrame):
    shape = df.shape[0]
    return shape

def copy(data: pd.DataFrame, inputs: pd.DataFrame, cols: list[str]):
    for col in cols:
        data[col] = inputs[col].copy()
    return data

def clone(data: pd.DataFrame, inputs: pd.DataFrame):
    cols = inputs.columns.tolist()
    for col in cols:
        data[col] = inputs[col].copy()
    return data

def merge(data: pd.DataFrame, arr: np.ndarray, col: str):
    data[col] = pd.DataFrame(arr)
    return data

def expand(data: pd.DataFrame, inputs: pd.DataFrame, val, col):
    array = np.full(inputs.shape[0], val)
    return(merge(data, array, col))

def export(df, dest, cols):
    output: pd.DataFrame
    if len(cols) == 1:
        output = df
    else:
        output = df[cols]
    display(output)
    output.to_csv(dest, index=False)

# Array Calculations
def avg(data: pd.DataFrame, inputs: pd.DataFrame, col='avg'):
    masses = inputs[col].to_numpy()
    return np.average(masses)

def stdev(data, inputs, col='stdev'):
    return(np.std(inputs[col].to_numpy()))

def err(data: pd.DataFrame, inputs: pd.DataFrame, sigmas: np.ndarray, length: int, col='davg'):
    v_cdt       = np.vectorize(pc.errorf)
    deltas      = v_cdt(sigmas, length)
    data[col]   = pd.DataFrame(deltas)
    return data, deltas

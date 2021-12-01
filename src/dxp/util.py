import dxp.calc as pc
import numpy as np
import pandas as pd

import to_precision as tp
def signif(x, p=2):
    x = np.asarray(x)
    to_sf = np.vectorize(tp.std_notation)
    return to_sf(x, p)

# Displaying
def head(data: pd.DataFrame, inputs: pd.DataFrame):
    print(f'==== Output DataFrame ====\n\n{data.head()}\n')
    print(f'==== Input DataFrame ====\n\n{inputs.head()}\n')

def shape(df: pd.DataFrame):
    shape = df.shape[0]
    return shape

def display(df: pd.DataFrame, title='Output DataFrame', *args, **kwargs):
    print(f'==== {title} ====\n')
    print(f'{df}\n')

# Populate
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

def avg(data: pd.DataFrame, inputs: pd.DataFrame, col='avg'):
    masses = inputs[col].to_numpy()
    return np.average(masses)

def stdev(data, inputs, col='stdev'):
    return(np.std(inputs[col].to_numpy()))

def err(data: pd.DataFrame, inputs: pd.DataFrame, sigmas: np.ndarray, length: int, col='davg'):
    v_cdt           = np.vectorize(pc.errorf)
    deltas      = v_cdt(sigmas, length)
    data[col] = pd.DataFrame(deltas)
    return data, deltas

# Export
def export_data(df: pd.DataFrame, dest):
    output_data = df
    display(output_data)
    output_data.to_csv(dest, index=False)

def export_graph(df, cols: list[str], dest):
    output_graph = df[cols]
    display(output_graph)
    output_graph.to_csv(dest, index=False)

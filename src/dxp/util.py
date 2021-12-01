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

def avg(data: pd.DataFrame, inputs: pd.DataFrame, shape, idxs: list[str], col='avg'):
    values = []
    for idx in idxs:
        values.append(inputs[idx])

    flat_values = []
    for val in values:
        flat_values.append(val.values.flatten())

    ar_data = np.empty(shape=shape)

    i = 0
    for values_list in zip(*flat_values):
        ar_data[i] = pc.average(values_list)
        i += 1

    data[col] = pd.DataFrame(ar_data)
    return data, ar_data, flat_values

def sd(data: pd.DataFrame, inputs: pd.DataFrame,
       shape, ar_data: np.ndarray, fvals: list, col='s.d'):
    ar_sd: np.ndarray = np.empty(shape)

    i = 0
    for values_list in zip(*fvals):
        ar_sd[i] = pc.std_dev(values_list)
        i += 1

    data[col] = pd.DataFrame(ar_sd)
    return data, ar_sd

def err(data: pd.DataFrame, inputs: pd.DataFrame, sigmas: np.ndarray, length: int, col='davg'):
    v_cdt           = np.vectorize(pc.errorf)
    deltas      = v_cdt(sigmas, length)
    data[col] = pd.DataFrame(deltas)
    return data, deltas

def calc_T(tbar: float):
    return tbar / 10

def pop_T(data: pd.DataFrame, inputs: pd.DataFrame,
          ar_t_bar: np.ndarray):
    np.vectorize(calc_T)(ar_t_bar)
    ar_T = np.vectorize(calc_T)(ar_t_bar)
    data['T'] = pd.DataFrame(ar_T)
    display(data, title='Period Populated')
    return data, ar_T

def pop_dT(data: pd.DataFrame, inputs: pd.DataFrame,
           ar_delta_t: np.ndarray):
    np.vectorize(calc_T)(ar_delta_t)
    ar_dT = np.vectorize(calc_T)(ar_delta_t)
    data['dT'] = pd.DataFrame(ar_dT)
    display(data, title='Error in Period Populated')
    return data, ar_dT

# Export
def export_data(df: pd.DataFrame, dest):
    output_data = df
    display(output_data)
    output_data.to_csv(dest, index=False)

def export_graph(df, cols: list[str], dest):
    output_graph = df[cols]
    display(output_graph)
    output_graph.to_csv(dest, index=False)

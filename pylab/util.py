import pylab.calc as pc
import numpy as np
import pandas as pd

import to_precision as tp
def signif(x, p=2):
    x = np.asarray(x)
    to_sf = np.vectorize(tp.std_notation)
    return to_sf(x, p)

# Displaying
def head(data: pd.DataFrame, inputs: pd.DataFrame):
    print('==== Output DataFrame ====\n')
    print(data.head())
    print('==== Input DataFrame ====\n')
    print(inputs.head())
    print('\n')

def display(df: pd.DataFrame, title='Output DataFrame', *args, **kwargs):
    print(f'==== {title} ====\n')
    print(f'{df}\n')

# Populate
def copy(data: pd.DataFrame, inputs: pd.DataFrame, cols: list[str]):
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

def populate(data: pd.DataFrame, inputs: pd.DataFrame,
             output_csv: str, graph_csv: str):
    # ==== Copying ====
    cols = ['L', 'dL', 't1', 't2', 't3', 't4', 't5']
    data = copy(data, inputs, cols)

    # ==== Calculations ====

    display(data)
    ids = ['t1', 't2', 't3', 't4', 't5']
    shape = inputs['t1'].shape
    length = 5

    # Populate
    data, avgs, fvals = avg(data, inputs, shape, ids)
    display(data, title='Average Acceleration')
    data, sigmas = sd(data, inputs, shape, avgs, fvals)
    display(data, title='Standard Deviation')
    data, sigmas = err(data, inputs, sigmas, length, 'dabar')
    display(data, title='Error in Acceleration')

    # Significant Figures
    df = data.apply(signif)
    display(df)

    # Export
    print(output_csv, graph_csv)
    export_data(df, output_csv)

def output(csv_input: str,
           output_csv: str,
           graph_csv: str,
           *args, **kwargs):
    '''
    output takes in some input.csv filename, reads the file
    '''

    columns = ['L', 'dL', 't1', 't2', 't3', 't4', 't5']
    inputs  = pd.read_csv(csv_input)
    data    = pd.DataFrame(columns=columns, index=inputs.index)
    display(data    , title='Output DataFrame')
    display(inputs  , title='Input DataFrame')
    populate(data, inputs, output_csv, graph_csv)

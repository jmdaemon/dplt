from util import *

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

from dxp.util import pd, display
import importlib.util

def output(fp: str, csv_input: str, output_csv: str, graph_csv: str,
           *args, **kwargs):
    '''
    Reads values from a csv file and outputs a
    csv file with additional calculated data and columns.

    Parameters
        fp          - path to current lab directory
        csv_input   - path to lab data in csv format
        output_csv  - Name/Destination of populated csv data
        graph_csv   - Name/Destination of the output csv graph
    '''

    inputs  = pd.read_csv(csv_input)
    columns = inputs.columns.tolist()
    data    = pd.DataFrame(columns=columns, index=inputs.index)
    display(data    , title='Output DataFrame')
    display(inputs  , title='Input DataFrame')

    def module_from_file(module_name, file_path):
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    pop = module_from_file("pop", f'{fp}/pop.py')
    pop.populate(data, inputs, output_csv, graph_csv)

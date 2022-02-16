import dxp.util as du
import pandas as pd
import numpy as np

def setupdf():
    d = {'col1': [1, 2], 'col2': [3, 4]}
    return pd.DataFrame(data=d)

def test_show(capsys):
    df = setupdf()
    du.show(df)
    captured = capsys.readouterr()
    assert(captured is not None), 'Should output contents of DataFrame'

def test_catslice():
    idf = setupdf()
    odf = pd.DataFrame()
    sliceidf = pd.DataFrame(idf['col1'])
    assert (du.catslice(idf, odf, ['col1']).equals(sliceidf)), 'Should concat slices of DataFrame'

def test_colavg():
    df = setupdf()
    assert(du.colavg(df, 'col1') == 1.5), 'Should calculate the average of a DataFrame column'

def test_expand():
    actual = du.expand(1, 2)
    expect = np.ndarray([1,1])
    assert (actual.all() == expect.all()), 'Should expand values to an array'

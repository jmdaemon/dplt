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
    assert(captured is not None), 'Should output contents of dataframe'

def test_copy():
    idf = setupdf()
    odf = pd.DataFrame()
    sliceidf = pd.DataFrame(idf['col1'])
    assert (du.copy(idf, odf, ['col1']).equals(sliceidf)), 'Should copy slices of dataframe'

def test_merge():
    idf = setupdf()
    data = np.array([3, 4])
    # odf = pd.DataFrame(data={'col1': [3, 4]})
    outputdf = du.merge(idf, data, 'col1')
    expect = pd.DataFrame(data={'col1': [1,2,3,4]})
    assert(outputdf.equals(expect)), 'Should merge values from numpy array'

def test_stdev():
    df = setupdf()
    print(df['col1']) # Debug statement
    actual = du.stdev(df, 'col1')
    expect = 0.5
    assert np.isclose(actual, expect,
                      rtol=1e-05, atol=1e-08, equal_nan=False
                      ), 'Should calculate standard deviation of dataframe'

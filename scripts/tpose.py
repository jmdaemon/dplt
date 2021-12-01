#!/usr/bin/python

import pandas as pd
import argparse
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)
parser = argparse.ArgumentParser(description='Output transposed csv files')
parser.add_argument('input'     , type=str, help='Specify csv file to transpose')
parser.add_argument('--h'       , action='store_true', help='Specify csv file to transpose')
parser.add_argument('--saveas'  , type=str, help='Specify csv file to transpose')
args = parser.parse_args()

csv_input   = args.input
has_header  = args.h
saveas      = args.saveas

# csv_string  = pd.read_csv(csv_input, header=None).T.dropna().astype(int).to_csv(header=False, index=False)
# output      = csv_string.strip()
# print(f'{output}')

finput = csv_input if csv_input else 'scripts/phys/Data.csv'
# finput = 'scripts/phys/Data.csv'
# finput = 'Input.csv'
# finput = 'TPose.csv'

csv: pd.DataFrame
if has_header:
    # use skiprows if you want to skip headers
    csv = pd.read_csv(finput, skiprows=1)
else:
    csv = pd.read_csv(finput, header=None)

df_csv = pd.DataFrame(data=csv)
transposed_csv = df_csv.T

if (saveas is None):
    # print(transposed_csv)
    # transposed_csv.to_csv(saveas, index=False)
    # print(transposed_csv.to_csv(header=None, index=False).strip('\n').split('\n'))
    print(transposed_csv.to_csv(header=None, index=False))
else:
    transposed_csv.to_csv(saveas, index=False)

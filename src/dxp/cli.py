#!/usr/bin/python

import argparse
import wora.dynmod
import pandas as pd
import dxp.util as du

def main():
    parser = argparse.ArgumentParser(description='Executable file for Labs')
    parser.add_argument('input' , type=str, help='Sets the inputs csv file')
    parser.add_argument('-o'    , required=False, type=str,
                        help='Set the output file [Default: out.csv]')

    args = parser.parse_args()

    # Set inputs, default output file to 'out.csv'
    fp  = args.input
    out = args.csv if args.csv else 'out.csv'

    # Wrap data in dictionary
    inputs  = du.Sample(fp, pd.read_csv(fp))
    outputs = du.Sample(out, pd.DataFrame())
    data = {
        'input': inputs,
        'output': outputs
    }

    # Hand execution off to pop.py file
    pop = wora.dynmod.module_from_file("pop", f'{fp}/pop.py')
    pop.pop(data)

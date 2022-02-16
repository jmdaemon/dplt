#!/usr/bin/python

import argparse
import wora.dynmod
import pandas as pd
import dxp.util as du

def main():
    parser = argparse.ArgumentParser(description='Executable file for Labs')
    parser.add_argument('input' , type=str, help='Sets the inputs csv file')
    parser.add_argument('-d'    , required=False, type=str, help='''Sets the working directory
                        for the pop.py file [Default: ./]''')
    parser.add_argument('-o'    , required=False, type=str,
                        help='Set the output file [Default: out.csv]')

    args = parser.parse_args()

    # Get user input and set defaults
    fp  = args.input
    wd  = args.d if args.d else '.'
    out = args.csv if args.csv else 'out.csv'

    # Wrap data in dictionary
    inputs  = du.Sample(fp, pd.read_csv(fp))
    outputs = du.Sample(out, pd.DataFrame())
    data = {
        'input': inputs,
        'output': outputs
    }

    # Hand execution off to pop.py file
    pop = wora.dynmod.module_from_file("pop", f'{wd}/pop.py')
    pop.pop(data)

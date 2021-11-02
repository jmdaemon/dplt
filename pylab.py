#!/usr/bin/python

import argparse
import pylab.util

parser = argparse.ArgumentParser(description='Executable file for Labs')
parser.add_argument('input'     , type=str, help='File path to some input.csv')
parser.add_argument('--csv'     , required=False, type=str, help='Change output filename of lab data [Default: Data.csv]')
parser.add_argument('--graph'   , required=False, type=str, help='Change output filename of graph data [Default: Graph.csv]')

args = parser.parse_args()

input_csv   = args.input
output_csv  = args.csv
graph_csv   = args.graph

input_csv = input_csv if input_csv else 'Data.csv'
graph_csv = graph_csv if graph_csv else 'Graph.csv'
pylab.util.output(input_csv, output_csv, graph_csv)

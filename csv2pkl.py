#!/usr/bin/env python3
#
# based on /t00b-shadi-unzip s3 files.ipynb
# Author: Shadi Akiki
# Organization: Pi campus, School of AI, Class of 2019 q2
#
# Installation: pip3 install pandas tables
# Usage: python csv2pkl.py example.csv example.pkl

import sys

if len(sys.argv)!=3:
    raise Exception("Wrong usage. Should be:  python csv2pkl.py example.csv example.pkl")

fn_in = sys.argv[1]
fn_out = sys.argv[2]

import pandas as pd

df=pd.read_csv(fn_in)
df.to_pickle(fn_out)

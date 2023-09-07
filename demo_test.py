# coding: utf8
""" 
@ File: demo_test.py
@ Editor: PyCharm
@ Author: Ace (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-08-22
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import os


def test():
    import pandas as pd

    hdf5_path = r'JupyterData/AI/temp/data/stock_data/day/day_eps_ttm.h5'
    s = pd.read_hdf(hdf5_path)

    return 0


if __name__ == '__main__':
    print(test())

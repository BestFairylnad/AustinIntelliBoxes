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

if __name__ == '__main__':
    for environ in os.environ.items():
        print(environ)

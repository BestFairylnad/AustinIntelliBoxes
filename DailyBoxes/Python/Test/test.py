# coding: utf8
""" 
@ File: test.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China)
@ HomePage: https://github.com/AustinFairyland
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-09-17
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')


class TestClass:

    # def __str__(self):
    #     return '类'

    def __repr__(self):
        return self.s()
    
    def s(self):
        print('s')


if __name__ == '__main__':
    print(TestClass())

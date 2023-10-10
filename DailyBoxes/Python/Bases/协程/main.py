# coding: utf8
""" 
@File: main.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2023-10-10
"""

import os
import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import asyncio

from coroutine import test

if __name__ == '__main__':
    try:
        print(asyncio.run(test()))
    except Exception as error:
        print(error)

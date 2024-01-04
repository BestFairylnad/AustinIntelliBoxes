# coding: utf8
""" 
@File: public.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-03
"""
from __future__ import annotations

import os
import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import time
import random


class MethodDecorators:
    
    def __init__(self, annotation):
        self.__annotation = annotation
        
    def __call__(self, function, *args, **kwargs):
        def wrapper(*args, **kwargs):
            print("Start Running {}".format(self.__annotation))
            try:
                print(1)
            except Exception as error:
                print(error)
        
        return wrapper
    


if __name__ == '__main__':
    print(1)

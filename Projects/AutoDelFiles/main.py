# coding: utf8
""" 
@File: main.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/2 22:38
"""

from util import del_file
import sys

if __name__ == '__main__':
    try:
        stats = sys.argv[1]
        if stats == 'del':
            del_file(enable=True)
    except IndexError:
        del_file()

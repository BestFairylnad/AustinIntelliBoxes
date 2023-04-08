# coding: utf8
""" 
@File: setup.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/2 20:29
"""

from distutils.core import setup
from Cython.Build import cythonize

if __name__ == '__main__':
    print('start')
    setup(ext_modules=cythonize(['util/del_files.py', 'util/initialize.py']))


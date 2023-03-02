# coding: utf8
""" 
@File: test.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/2 20:29
"""

import py_compile

if __name__ == '__main__':
    # py_compile.compile('main.py', 'main.pyc', optimize=2)
    # py_compile.compile('util/__init__.py', 'util/del_files.pyc', optimize=2)
    py_compile.compile('util/del_files.py', 'util/del_files.pyc', optimize=2)
    py_compile.compile('util/initialize.py', 'util/initialize.pyc', optimize=2)

# coding: utf8
""" 
@File: __init__.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/2 19:56
"""

from .del_files import DelFiles


def del_file(enable=False): DelFiles().filter(enable)

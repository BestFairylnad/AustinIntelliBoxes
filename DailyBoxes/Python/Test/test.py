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
warnings.filterwarnings("ignore")
from operator import itemgetter


class TestClass:
    def __repr__(self):
        return self.s()

    def s(self):
        print("s")

    def test001(self):
        return True

    def test002(self):
        s = (
            {"id": 1, "name": "状态", "value": "", "status": True},
            {"id": 2, "name": "修改密码", "value": "", "status": True},
            {"id": 3, "name": "编辑", "value": "", "status": True},
            {"id": 4, "name": "删除", "value": "", "status": True},
        )


if __name__ == "__main__":
    print(TestClass().test002())

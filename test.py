# coding: utf8
""" 
@ File: test.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-08-22
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import os
from datetime import datetime
from fake_useragent import UserAgent
import re
from Bio import Entrez
from Bio import Medline
from datetime import timedelta

from subprocess import call
import pkg_resources


def test():
    return True


def pip_update_all():
    packages = [dist.project_name for dist in pkg_resources.working_set]
    for dist in packages:
        str_s = 'pip install --no-cache-dir --upgrade {}'.format(dist)
        try:
            print(str_s)
            # call(str_s, shell=True)
        except Exception as error:
            print(error)
            break

    return True


if __name__ == '__main__':
    print(test())
    print(pip_update_all())

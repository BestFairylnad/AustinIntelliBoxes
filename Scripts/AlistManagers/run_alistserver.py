# coding: utf8
""" 
@ File: run_alistserver.py
@ Editor: PyCharm
@ Author: Ace (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-08-21
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')


import subprocess


subprocess.run(r'alist.exe server', shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
exit()

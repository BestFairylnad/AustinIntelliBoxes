# coding: utf8
""" 
@File: main.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China)
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2023-09-26
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

from PIL import Image
import os


def png2ico(png_filepath):
    ico_size = (64, 64)

    png_path, png_ext = os.path.splitext(png_filepath)
    img = Image.open(png_filepath).resize(ico_size)
    try:
        ico_filepath = ''.join('{}{}'.format(png_path, '.ico'))
        img.save(ico_filepath)
    except Exception as error:
        print(error)


if __name__ == '__main__':
    png2ico(r'E:\Developments\Projects\AustinIntelliBoxes\Scripts\png2ico\导航.png')

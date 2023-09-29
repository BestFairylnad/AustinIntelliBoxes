# coding: utf8
""" 
@File: img_compression.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2023-09-29
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

from PIL import Image


def compression(input_file, output_file):
    img = Image.open(input_file)
    with open(output_file, 'wb') as file:
        img.save(file, quality=30)

    return output_file


if __name__ == '__main__':
    compression(input_file='austinheader.jpg', output_file='output/austinheader.jpg')

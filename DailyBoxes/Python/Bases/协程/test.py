# coding: utf8
""" 
@File: test.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2023-10-10
"""

import os
import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from common import download_images
from coroutine import main
import asyncio

if __name__ == '__main__':
    # url_list = [
    #     'https://cdn.pixabay.com/photo/2023/09/29/07/52/mountains-8283189_1280.jpg',
    #     'https://cdn.pixabay.com/photo/2023/10/06/17/08/ai-generated-8298734_1280.jpg',
    #     'https://th.bing.com/th/id/OIG.o5N4j0tRaL5ZTSDpMxg0?pid=ImgGn'
    # ]
    # for url in url_list:
    #     download_images(url)
    
    # asyncio.run(main())
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    

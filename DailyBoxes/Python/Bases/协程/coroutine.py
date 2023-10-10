# coding: utf8
""" 
@File: coroutine.py
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


import aiohttp
from uuid import uuid4


async def test():
    work_path = os.getcwd()
    return work_path


async def fetch(session: aiohttp.ClientSession, url: str):
    print('发送请求: {}'.format(url))
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        image_name = uuid4().__str__() + '.png'
        with open(image_name, 'wb') as file:
            file.write(content)


async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'https://cdn.pixabay.com/photo/2023/09/29/07/52/mountains-8283189_1280.jpg',
            'https://cdn.pixabay.com/photo/2023/10/06/17/08/ai-generated-8298734_1280.jpg',
            'https://th.bing.com/th/id/OIG.o5N4j0tRaL5ZTSDpMxg0?pid=ImgGn'
        ]
        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]
        
        await asyncio.wait(tasks)

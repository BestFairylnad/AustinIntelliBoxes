# coding: utf8
"""
@ File: demo01.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China) https://fairy.host
@ HomePage: https://github.com/AustinFairyland
@ OS: Linux Ubuntu 22.04.4 Kernel 6.2.0-36-generic
@ CreatedTime: 2023/11/27
"""
from __future__ import annotations

import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class Dog:
    def __init__(self, species, nick, long, weight):
        self.species = species
        self.nick = nick
        self.long = long
        self.weight = weight

    def eat(self):
        print("{}吃了狗粮".format(self.nick))
        self.weight += 1


if __name__ == "__main__":
    dog = Dog("泰迪", "小黑子", 20, 10)
    for _ in range(5):
        dog.eat()
    print(dog.weight)

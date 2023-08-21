# coding: utf8
""" 
@ File: passwordgenerator.py
@ Editor: PyCharm
@ Author: Ace (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-08-20
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import random


class PasswdRules:
    """ 密码规则"""

    def __init__(self, count):
        """
        初始化
        :param count: 密码长度
        """
        self.__count = count

    def __get_common_char(self) -> str:
        """
        密码字符串
        :return: 密码字符串
        """

        def get_special_char():
            """
            特殊字符串
            :return: 特殊字符串
            """
            count = random.randint(1, 3)
            return count, random.choices('!@$%^&*()_+~', k=count)

        special_char_count, special_char = get_special_char()
        common_chat = random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=(self.__count - special_char_count))
        result = []
        result.extend(special_char + common_chat)
        random.shuffle(result)

        return ''.join(result)

    def get_passwd(self) -> str:
        """
        获取密码
        :return: 
        """
        return self.__get_common_char()


if __name__ == '__main__':
    passwd_count = 12
    if passwd_count < 8: passwd_count = 8
    instantiation_passwd_rules = PasswdRules(count=passwd_count)
    print(instantiation_passwd_rules.get_passwd())

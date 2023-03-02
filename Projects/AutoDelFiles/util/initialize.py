# coding: utf8
""" 
@File: initialize.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/2 20:22
"""

import os
import configparser
from loguru import logger
import platform


class Initizlize:

    def __init__(self):
        self.abspath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if os.path.isfile(os.path.join(self.abspath, 'application.ini')):
            self.config_file = os.path.join(self.abspath, 'application.ini')
        else:
            if os.path.isfile(os.path.join(os.path.dirname(self.abspath), 'application.ini')):
                self.config_file = os.path.join(os.path.dirname(self.abspath), 'application.ini')
            else:
                raise logger.error('Failed to read the configuration file, please try again...')
        if platform.system() == 'Windows':
            self.delimiter = '\\'
        elif platform.system() == 'Linux':
            self.delimiter = '/'
        else:
            raise logger.error('Unrecognized operating system...')

    def get_config(self, section) -> dict:
        con = configparser.ConfigParser()
        try:
            con.read(self.config_file, encoding='utf-8')
            sections = con.items(section)
            if dict(sections) == {}:
                raise logger.error('Exception in configuration file. Please check configuration...')
            return dict(sections)
        except Exception as error:
            raise logger.error(error)

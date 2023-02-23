# coding: utf8
""" 
@File: Public.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/2/21 14:24
"""

import os
import platform

class PublicTools:
    """Publice tools"""
    
    def __init__(self):
        pass
    
    def project_path(self):
        """
        project path
        :return: project abs path
        """
        return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    def config_path(self):
        """
        config path
        :return: config abs path
        """
        return os.path.join(self.project_path(), 'Configuration')
    
    def package_path(self):
        """
        install path
        :return: install abs path
        """
        return os.path.join(self.project_path(), 'Packages')
    
    def run_os(self) -> str:
        """
        judgment OS
        :return: str: win or unix
        """
        if platform.system().lower() == 'windows':
            return 'win'
        elif platform.system().lower() == 'linux':
            return 'unix'


# coding: utf8
""" 
@File: Deployments.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/2/21 20:02
"""

from Src.Utils.BuildRunEnvironment import BuildRunEnvironmentTools
from loguru import logger


class Deploy:
    """ Deploy Java (JDK, JRE)"""

    def __init__(self):
        self.__build = BuildRunEnvironmentTools()
    
    def __deploy(self, win, unix):
        """
        Deploy the Java environment
        :return: jdk_home
        """
        if self.__build.public_tools.run_os() == 'win':
            return win
        elif self.__build.public_tools.run_os() == 'unix':
            return unix
        logger.warning()
        
    def java_(self):
        path_package = self.__build.config.get('PackagePath')['java']
        path_install = self.__build.config.get('InstallPath')['java']
        logger.debug('Java package path: {}'.format(path_package))
        logger.debug('Java install path: {}'.format(path_install))
        self.__deploy(
            win=self.__build.deploy_java_win(path_package=path_package, path_install=path_install),
            unix=self.__build.deploy_java_unix(path_package=path_package, path_install=path_install)
        )
        
    def mysql_(self):
        path_package = self.__build.config.get('PackagePath')['mysql']
        path_install = self.__build.config.get('InstallPath')['mysql']
        logger.debug('Java package path: {}'.format(path_package))
        logger.debug('Java install path: {}'.format(path_install))
        self.__deploy(
            win=self.__build.deploy_mysql_win(path_package=path_package, path_install=path_install),
            unix=self.__build.deploy_mysql_unix(path_package=path_package, path_install=path_install)
        )

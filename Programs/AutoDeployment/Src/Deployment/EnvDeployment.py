# coding: utf8
""" 
@File: EnvDeployment.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/2/21 20:02
"""

from Src.Utils.BuildEnvironment import BuildEnvironmentTools
from loguru import logger


class EnvDeployment(BuildEnvironmentTools):

    def __init__(self):
        super().__init__()
        
    def deploy_java(self):
        """
        部署java
        :return: jdk_home
        """
        path_java_package = self.config.get('PackagePath')['java']
        path_java_install = self.config.get('InstallPath')['java']
        logger.debug('Java package path: {}'.format(path_java_package))
        logger.debug('Java install path: {}'.format(path_java_install))
        if self.public_tools.run_os() == 'win':
            return self.deploy_java_win(path_package=path_java_package, path_install=path_java_install)
        elif self.public_tools.run_os() == 'unix':
            return self.deploy_java_unix(path_package=path_java_package, path_install=path_java_install)
        logger.warning()

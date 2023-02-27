# coding: utf8
""" 
@File: test.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/2/21 14:34
"""

from Src.Deployment.EnvDeployment import EnvDeployment
from loguru import logger
from Src.Utils.Public import PublicTools
import os


if __name__ == '__main__':
    public_tools = PublicTools()
    if os.path.isdir(os.path.join(public_tools.project_path(), 'logs')):
        if os.path.isfile(os.path.join(public_tools.project_path(), 'logs/text.log')):
            os.remove(os.path.join(public_tools.project_path(), 'logs/text.log'))
            logger.add(os.path.join(public_tools.project_path(), 'logs/text.log'), rotation='5MB', encoding='utf8')
        else:
            logger.add(os.path.join(public_tools.project_path(), 'logs/text.log'), rotation='5MB', encoding='utf8')
    else:
        os.mkdir(os.path.join(public_tools.project_path(), 'logs'))
        logger.add(os.path.join(public_tools.project_path(), 'logs/text.log'), rotation='5MB', encoding='utf8')
    env_deployment = EnvDeployment()
    # java
    env_deployment.deploy_java()



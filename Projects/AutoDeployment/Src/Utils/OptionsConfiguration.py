# coding: utf8
""" 
@File: OptionsConfiguration.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/2/21 14:24
"""

import os
import yaml
from Src.Utils.Public import PublicTools
from loguru import logger


class OptionsconfigurationTools:
    """Options config tool class"""

    def __init__(self):
        self.__public_tools = PublicTools()
        self.path_yaml_config = os.path.join(self.__public_tools.config_path(), 'GlobalConfig.yaml')

    def get_yaml(self) -> dict:
        """
        Get yaml file config
        :return: dict: config details
        """
        with open(file=self.path_yaml_config) as yaml_file:
            yaml_config = yaml.load(yaml_file.read(), Loader=yaml.FullLoader)
        yaml_file.close()
        return yaml_config
    
    def write_yaml(self, yaml_config, mode):
        """
        Write yaml file config
        :param yaml_config: new config
        :param mode: Writeing from 'w' or 'a+'
        :return: 
        """
        try:
            with open(file=self.path_yaml_config, mode=mode, encoding='utf-8') as yaml_file:
                yaml.dump(data=yaml_config, stream=yaml_file, allow_unicode=True)
            logger.success('{}'.format('Writing yaml configuration succeeded.'))
        except Exception as error:
            logger.error('{}'.format(error))





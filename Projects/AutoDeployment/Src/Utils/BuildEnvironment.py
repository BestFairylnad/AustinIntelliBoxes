# coding: utf8
""" 
@File: BuildEnvironmentTools.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/2/21 14:19
"""

import platform
from loguru import logger
from Src.Utils.OptionsConfiguration import OptionsconfigurationTools
import zipfile
from tqdm import tqdm
from Src.Utils.Public import PublicTools
import os
import subprocess
import tarfile
import shutil


class BuildEnvironmentTools:
    """Building Environment tool class"""

    def __init__(self):
        self.public_tools = PublicTools()
        self.options_configuration = OptionsconfigurationTools()
        if self.public_tools.run_os() == 'win':
            self.config: dict = self.options_configuration.get_yaml().get('BuildEnvironments')['win']
        elif self.public_tools.run_os() == 'unix':
            self.config: dict = self.options_configuration.get_yaml().get('BuildEnvironments')['unix']
        logger.debug('OS info: OS: {}, name: {}, version: {}, machine: {}'.format(
            platform.uname().system,
            platform.uname().node,
            platform.uname().release,
            platform.uname().machine
        ))
        logger.debug('configuration files: {}'.format(self.options_configuration.path_yaml_config))

    def deploy_java_win(self, path_package, path_install):
        """
        win: deploy java
        :param path_package: java install package path
        :param path_install: java install path
        :return: java install path
        """

        def run_command(cmd):
            """
            run cmd
            :param cmd: win: cmd
            :return: 1 or 0
            """
            try:
                path_add = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                logger.info('{}'.format(cmd))
                path_add.wait()
                return 1
            except Exception as error:
                logger.error('{}'.format(error))
                return 0

        try:
            file_java_zip = zipfile.ZipFile(path_package)
            for zip_file in tqdm(file_java_zip.namelist(), desc='Unzipping java package...'):
                file_java_zip.extract(member=zip_file, path=path_install)
            JDK_HOME = os.path.join(path_install, r'jdk\bin')
            run_command(r'setx JAVA_HOME {} /m'.format(JDK_HOME))
            logger.success('Install java package successfully.')
            if self.options_configuration.get_yaml().get('RunEnvironment') is not None:
                new_config: dict = self.options_configuration.get_yaml()
                temp_config: dict = self.options_configuration.get_yaml().get('RunEnvironment')
                temp_config.update(win={'java': os.path.join(JDK_HOME, 'java.exe')})
                new_config['RunEnvironment'] = temp_config
                self.options_configuration.write_yaml(yaml_config=new_config, mode='w')
            else:
                config_dict = {
                    'RunEnvironment': {
                        'win': {
                            'java': os.path.join(JDK_HOME, 'java.exe')
                        }
                    }
                }
                self.options_configuration.write_yaml(yaml_config=config_dict, mode='a+')
            return JDK_HOME
        except Exception as error:
            logger.error('{}'.format(error))
            logger.error('Failed to install java.')
            return 0

    def deploy_java_unix(self, path_package, path_install):
        """
        unix: deploy java
        :param path_package: java install package path
        :param path_install: java install path
        :return: java install path
        """
        if os.path.isdir(path_install):
            shutil.rmtree(path_install, ignore_errors=True)
        try:
            file_java_zip = tarfile.open(name=path_package, mode='r')
            for zip_file in tqdm(file_java_zip.getmembers()):
                file_java_zip.extract(member=zip_file, path=path_install)
            file_java_zip.close()
            JAVA_HOME = os.path.join(path_install, r'jdk1.8.0_202')
            JDK_HOME = os.path.join(JAVA_HOME, r'bin')
            with open(file='{}/.bash_profile'.format(os.environ['HOME']), mode='a+') as user_profile:
                user_profile.write('export JAVA_HOME={}\n'.format(JAVA_HOME))
                user_profile.write('export PATH=$JAVA_HOME/bin:$PATH\n')
            user_profile.close()
            if os.system('source {}/.bash_profile'.format(os.environ['HOME'])) == 0:
                logger.success('Adding user environment variables succeeded.')
            else:
                logger.warning('Failed to add user environment variable.')
            logger.success('Install java package successfully.')
            if self.options_configuration.get_yaml().get('RunEnvironment') is not None:
                new_config: dict = self.options_configuration.get_yaml()
                temp_config: dict = self.options_configuration.get_yaml().get('RunEnvironment')
                temp_config.update(unix={'java': os.path.join(JDK_HOME, 'java')})
                new_config['RunEnvironment'] = temp_config
                self.options_configuration.write_yaml(yaml_config=new_config, mode='w')
            else:
                config_dict = {
                    'RunEnvironment': {
                        'unix': {
                            'java': os.path.join(JDK_HOME, 'java')
                        }
                    }
                }
                self.options_configuration.write_yaml(yaml_config=config_dict, mode='a+')
        except Exception as error:
            logger.error('{}'.format(error))
            logger.error('Failed to install java')
            return 0

    def deploy_mysql_win(self, path_package, path_install):
        """
        win: deploy mysql
        :param path_package: mysql package path
        :param path_install: mysql install path
        :return: 
        """
        try:
            file_mysql_zip = zipfile.ZipFile(path_package)
            for zip_file in tqdm(file_mysql_zip.namelist(), desc='Unzip mysql package...'):
                file_mysql_zip.extract(member=zip_file, path=path_install)
        except Exception as error:
            logger.error('{}'.format(error))
            logger.error('Failed to install MySQL')
            


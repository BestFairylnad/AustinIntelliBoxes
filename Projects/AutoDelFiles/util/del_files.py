# coding: utf8
""" 
@File: del_files.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@OS: Windows 11 Professional Workstation 22H2
@Environment: Python3.9 (FairyAdministrator)
@CreatedTime: 2023/3/2 20:00
"""

from .initialize import Initizlize
import shutil
import os
from loguru import logger
import glob
from tqdm import tqdm
from datetime import datetime


class DelFiles(Initizlize):

    def __init__(self):
        super().__init__()

    def delete(self, everything):
        if os.path.isdir(everything):
            try:
                shutil.rmtree(everything)
                logger.info('{} deleted successfully.'.format(everything))
            except Exception as error:
                logger.error(error)
        else:
            try:
                os.remove(everything)
                logger.info('{} deleted successfully.'.format(everything))
            except FileNotFoundError:
                logger.warning('The parent directory of file has been deleted.')
            except Exception as error:
                logger.error(error)

    def filter(self, delect=False):
        timeout_day = self.get_config('service').get('modify_timeout_day')
        file_ext_list = [ext.strip() for ext in self.get_config('service').get('file_ext').split(';')]
        try:
            timeout_day = int(timeout_day)
        except ValueError or TypeError:
            raise logger.error('Configuration file "timeout_day" parameter error')
        try:
            files_path: str = self.get_config(section='service').get('file_path')
        except Exception as error:
            logger.error(error)
        for file_path in files_path.split(';'):
            for file in glob.glob('{}{}**'.format(file_path.strip(), self.delimiter), recursive=True):
                try:
                    if file == '{}{}'.format(file_path.strip(), self.delimiter):
                        pass
                    else:
                        modified_time = os.path.getmtime(file)
                        time_difference = datetime.now() - datetime.fromtimestamp(modified_time)
                        if time_difference.days > timeout_day:
                            file_name, file_ext = os.path.splitext(file)
                            if file_ext in file_ext_list or '.*' in file_ext_list:
                                logger.info('Matching file to {}'.format(file))
                                if delect is True:
                                    self.delete(file)
                except FileNotFoundError:
                    logger.warning(file)
                    logger.warning('The parent directory of file has been deleted.')
    print('Done...')

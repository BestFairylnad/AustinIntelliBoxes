# coding: utf8
""" 
@ File: merge_logs.py
@ Editor: PyCharm
@ Author: Ace (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-04-18
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

from glob import glob
import platform


def merge(folder_path: str, output_path: str, extension: str = None, file_coding: str = 'utf8') -> ...:
    separate: str
    if platform.system() == 'Windows':
        separate = '\\'
    elif platform.system() == 'Linux':
        separate = '/'
    else:
        sys.exit()
    if extension is None:
        extension = '**'
    else:
        extension = '*.{}'.format(extension)
    folder_path_glob: str
    if folder_path.endswith(separate):
        folder_path_glob = '{}**{}{}'.format(folder_path, separate, extension)
    else:
        folder_path_glob = '{}{}**{}{}'.format(folder_path, separate, separate, extension)
    glob_file_name = glob(folder_path_glob, recursive=True)
    with open(output_path, 'w', encoding=file_coding) as output_file:
        for file_path in glob_file_name:
            print(file_path)
            with open(file_path, 'r', encoding=file_coding) as file:
                print(file.read())
                output_file.write(file.read())
    return ...


def main():
    # gpt
    merge(
        folder_path=r'D:\Developments\Github\AceProfessional\AceRepositories\Projects\DataProcessing\AnalyseLogs\RunnetGPT\data\ChatGPT',
        output_path=r'D:\Developments\Github\AceProfessional\AceRepositories\Projects\DataProcessing\AnalyseLogs\RunnetGPT\data\ChatGPT\gpt.log',
        extension='log',
        file_coding='gbk'
    )
    # Nginx
    merge(
        folder_path=r'D:\Developments\Github\AceProfessional\AceRepositories\Projects\DataProcessing\AnalyseLogs\RunnetGPT\data\Nginx',
        output_path=r'D:\Developments\Github\AceProfessional\AceRepositories\Projects\DataProcessing\AnalyseLogs\RunnetGPT\data\Nginx\nginx.log',
        extension='log'
    )
    pass


if __name__ == '__main__':
    main()

# coding: utf8
""" 
@ File: downloadfiles.py
@ Editor: PyCharm
@ Author: Ace (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-08-21
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import requests
from tqdm import tqdm


class DownloadFiles:
    """ 下载文件"""

    def __init__(self, url: str):
        """
        初始化
        :param url: 下载地址 
        """
        self.__url = url
        if url.find('/') == -1:
            print('url错误')
            sys.exit(1)
        else:
            self.__file_name = url.split('/')[-1]

    def __downloadfiles(self):
        res = requests.get(url=self.__url, stream=True)
        total_length = int(res.headers.get('content-length'))
        with open(self.__file_name, mode='wb') as files:
            for file_data in tqdm(res.iter_content(chunk_size=1024), desc=self.__file_name, total=int(total_length / 1024)):
                if file_data:
                    files.write(file_data)
            files.close()

    def download(self):
        return self.__downloadfiles()


if __name__ == '__main__':
    # url = 'https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe'
    url = '1'
    instantiation_download_files = DownloadFiles(url=url)
    instantiation_download_files.download()

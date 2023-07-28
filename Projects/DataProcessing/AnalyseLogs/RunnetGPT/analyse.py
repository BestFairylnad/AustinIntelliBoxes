# coding: utf8
""" 
@ File: analyse.py
@ Editor: PyCharm
@ Author: Ace (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-04-08
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

from collections import Counter
import pandas
from tqdm import tqdm
from loguru import logger
import os
import sys
import re

@logger.catch()
def statistics_ip(nginx_log_file_path, output_file_path=''):
    ip_list = []
    try:
        with open(file=nginx_log_file_path, mode='r', encoding='utf8') as nginx_logs:
            for line in tqdm(nginx_logs.readlines()):
                ip = line.split(' ')[0]
                if not ip.startswith('11.') or ip == '11.1.1.1' or ip == '127.0.0.1':
                    continue
                ip_list.append(ip)
        nginx_logs.close()
        result = sorted(Counter(ip_list).items(), key=lambda x: x[1], reverse=True)
        data_format = pandas.DataFrame(result, columns=['IP', 'Count'])
        data_format.to_excel(excel_writer=os.path.join(output_file_path, 'statistics_ip.xlsx'), index=False, sheet_name='IP')
        logger.info('IP统计完成...')
        return True
    except Exception as error:
        logger.error('IP统计失败...')
        logger.exception(error)
        return False


def statistics_tokens(tokens_log_file_path):
    init_tokens_number = 0
    try:
        with open(file=tokens_log_file_path, mode='r', encoding='utf8') as tokens_logs:
            for line in tqdm(tokens_logs.readlines()):
                line: str
                if '传输完毕' not in line:
                    continue
                match = re.search(pattern=r'\[([\d\s,]+)\]', string=line)
                if match:
                    tokens_number_list = map(int, match.group(1).split(','))
                    for tokens_number in tokens_number_list:
                        init_tokens_number += tokens_number
        tokens_logs.close()
        logger.info('tokens统计完成..., 共计tokens: {}'.format(init_tokens_number))
        return True
    except Exception as error:
        logger.error('tokens统计失败...')
        logger.exception(error)


def main():
    output = 'output'
    if not os.path.exists(output):
        os.makedirs(output)
    statistics_ip(nginx_log_file_path='data/Nginx/20230410/access.log', output_file_path=output)
    statistics_tokens(tokens_log_file_path='data/ChatGPT/20230408/stdout.log')
    return True


if __name__ == '__main__':
    print(main())

# coding: utf8
""" 
@ File: 股票K线图绘制.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-09-08
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
from datetime import datetime
from mplfinance.original_flavor import candlestick_ochl
import seaborn as sns
from matplotlib.pylab import date2num
import pandas as pd
import numpy as np


def stock_k_line_chart_plott():
    read_data = pd.read_csv('./股票数据_修改日期.csv')

    def date_to_num(dates):
        datetime_list = []
        for date in dates:
            date_time = datetime.strptime(date, '%Y-%m-%d')
            num_date = date2num(date_time)
            datetime_list.append(num_date)

        return datetime_list

    data_array = read_data.values
    data_array[:, 1] = date_to_num(data_array[:, 1])
    quote = np.column_stack((data_array[:, 1:6][:, :2], data_array[:, 1:6][:, 4:], data_array[:, 1:6][:, 2:4]))
    
    cut_data = quote[:20, :]

    plt.rcParams['font.sans-serif'] = ['SimHei']
    fig, axes = plt.subplots(figsize=(15, 5))
    candlestick_ochl(axes, cut_data, width=0.6, colorup='r', colordown='g', alpha=1.0)
    plt.title('K线图', fontsize=25)
    plt.grid(True)
    axes.xaxis_date()
    plt.savefig('./1.png')
    # plt.show()
    # plt.close()

    print('Done')

    return


if __name__ == '__main__':
    sns.set()
    print(stock_k_line_chart_plott())

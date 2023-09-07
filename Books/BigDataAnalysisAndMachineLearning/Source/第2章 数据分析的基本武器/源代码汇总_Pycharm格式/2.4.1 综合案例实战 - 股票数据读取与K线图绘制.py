# # 2.4 综合案例实战 - 股票数据读取与K线图绘制
# # 2.4.1 初步尝试 - 股票数据读取与可视化
# 1.股票数据库：Tushare库的安装与使用
# !pip install tushare
import tushare as ts
df = ts.get_k_data('000002', start='2009-01-01', end='2019-01-01')
df.head()

df.to_excel('股价数据.xlsx', index=False)

# 2.绘制股价走势图
df.set_index('date', inplace=True)
df.head()

df['close'].plot()

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
df['close'].plot(title='万科股价走势图')

# **补充知识点：直接使用Matplotlib库画图的注意点**
# 通过Tushare库获取股价数据
import tushare as ts
df = ts.get_k_data('000002', start='2009-01-01', end='2019-01-01')
from datetime import datetime
df['date'] = df['date'].apply(lambda x:datetime.strptime(x,'%Y-%m-%d'))
import matplotlib.pyplot as plt
plt.plot(df['date'], df['close'])
plt.show()

# # 2.4.2 综合实战 - 股票K线图绘制
# **1.股票K线图基本知识**
MA5 = (Close1 + Close2 + Close3 + Close4 + Close5)/5
# **2.绘制股票K线图**

# (1) 安装绘制K线图的相关库：mpl_finance库
# !pip install https://github.com/matplotlib/mpl_finance/archive/master.zip

# (2) 引入绘图相关库
import tushare as ts
import matplotlib.pyplot as plt
import mpl_finance as mpf
import seaborn as sns
sns.set()


# (3) 通过Tushare库获取股票基本数据
df = ts.get_k_data('000002','2019-06-01', '2019-09-30')
df.head()

from matplotlib.pylab import date2num
import datetime
def date_to_num(dates):
    num_time = []
    for date in dates:
        date_time = datetime.datetime.strptime(date,'%Y-%m-%d')
        num_date = date2num(date_time)
        num_time.append(num_date)
    return num_time
df_arr = df.values
df_arr[:,0] = date_to_num(df_arr[:,0])
print(df_arr[0:5])

# (5) 绘制K线图
fig, ax = plt.subplots(figsize=(15,6))
mpf.candlestick_ochl(ax, df_arr, width=0.6, colorup='r', colordown='g', alpha=1.0)
plt.grid(True)
ax.xaxis_date()

# (6) 绘制K线图及均线图
df['MA5'] = df['close'].rolling(5).mean()
df['MA10'] = df['close'].rolling(10).mean()
df.head(15)

plt.rcParams['font.sans-serif'] = ['SimHei']
fig, ax = plt.subplots(figsize=(15,6))
mpf.candlestick_ochl(ax, df_arr, width=0.6, colorup='r', colordown='g', alpha=1.0)
plt.plot(df_arr[:,0], df['MA5'])
plt.plot(df_arr[:,0], df['MA10'])
plt.grid(True)
plt.title('万科A')
plt.xlabel('日期')
plt.ylabel('价格')
ax.xaxis_date ()

# (7) 绘制股票K线图、均线图、成交量柱状图
fig, axes = plt.subplots(2, 1, sharex=True, figsize=(15,8))
ax1, ax2 = axes.flatten()
mpf.candlestick_ochl(ax1, df_arr, width=0.6, colorup = 'r', colordown = 'g', alpha=1.0)
ax1.plot(df_arr[:,0], df['MA5'])
ax1.plot(df_arr[:,0], df['MA10'])
ax1.set_title('万科A')
ax1.set_ylabel('价格')
ax1.grid(True)
ax1.xaxis_date()
ax2.bar(df_arr[:,0], df_arr[:,5])
ax2.set_xlabel('日期')
ax2.set_ylabel('成交量')
ax2.grid(True)
ax2.xaxis_date()
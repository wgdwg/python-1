'''
使用matplotlib绘制折线图
author：WangGuodong
time：2022-07-14
'''

from matplotlib import pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
x = range(2,26,2)
y1 =  [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
y2 = [10, 11, 13.5, 14, 14.5, 17, 19, 21, 20, 17, 14, 11]
plt.plot(x,y1,marker='o',label='室外温度')
plt.plot(x,y2,marker='*',label='室内温度')
plt.xticks(range(min(x),max(x)+2,2))
plt.yticks(range(5,max(y1,)))
plt.xlabel('时间：(hours)')
plt.ylabel('温度：(℃)')
plt.legend() #图例生效代码
plt.show()#图片显示代码

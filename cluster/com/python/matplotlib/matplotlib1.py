'''
使用matplotlib绘制折线图
author：WangGuodong
time：2022-07-14
'''

from matplotlib import pyplot as plt
import matplotlib
matplotlib.rc('font', family='YouYuan')
x = ['西红柿首富', '战狼2', '红海行动', '泰囧','美人鱼']
y = [15, 52, 16, 10, 33]

plt.bar(range(len(x)), y, width=0.6, color='blue')
#设置x轴
plt.xticks(range(len(x)), x)
plt.xlabel('Movie name')
plt.ylabel('Movie box office')
plt.show()



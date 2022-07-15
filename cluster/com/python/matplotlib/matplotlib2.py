'''
使用matplotlib绘制条形图
author：WangGuodong
time：2022-07-14
'''

from matplotlib import pyplot as plt
import matplotlib
matplotlib.rc('font', family='YouYuan')
x = ['西红柿首富', '战狼2', '红海行动', '泰囧','美人鱼']
y = [15, 52, 16, 10, 33]

plt.barh(range(len(x)), y, height=0.5, color='orange')
#设置x轴
plt.yticks(range(len(x)), x)
plt.xlabel('Movie box office')
plt.ylabel('Movie name')
plt.show()
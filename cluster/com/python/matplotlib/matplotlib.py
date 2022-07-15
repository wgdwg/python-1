'''
python数据可视化之matplotlib
可以考虑使用matplotlib绘制各种图形
常用的就是绘制散点图,折线图，条形图等
author：WangGuodong
time：2022-07-14
'''

from matplotlib import pyplot as plt
import matplotlib
matplotlib.rc('font', family='YouYuan')

y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
x_3 = range(1,32)

plt.scatter(x_3, y_3,color='r')
#调整x轴的刻度
x_label = ['March {}'.format(i) for i in x_3]
plt.xticks(x_3[::3], x_label[::3],rotation=45)

plt.xlabel('time：(month)')
plt.ylabel('temperature:(℃)')
plt.show()


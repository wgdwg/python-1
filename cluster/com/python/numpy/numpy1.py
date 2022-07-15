'''
numpy是python进行数值数据处理的库
作为科学计算的库，重在大型的数值计算，多维矩阵执行数值运算
Author：WangGuodong
time:2022-07-14
'''

import numpy as np
import random
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rc('font', family='YouYuan')
#生成ndarray类型的列表
#使用np.array()方法生成列表
t = np.array([1,2,3])
print(t, type(t))
t1 = np.array(range(10)) #生成0~9的列表
print(t1, type(t1))
t2 = np.arange(10) #生成0~9的列表
print(t2, type(t2))
t3 = np.arange(4,10,2) #生成步长为2的列表
print(t3, type(t3))
print("*" * 100)

#numpy中的数据类型
t4 = np.array(range(1,4),dtype=float)
print(t4, t4.dtype)
t5 = np.array([1,0,0,1,0],dtype=bool)
print(t5, type(t5))
t6 = t4.astype(int)
print(t6, t6.dtype)
t7 = np.array([random.randint(1,10) for i in range(10)])
t8 = np.array(list(random.random() for i in range(10)))
print(t7, t7.dtype)
print(t8, t8.dtype)
print(np.round(t8,2)) #保留两位有效数字
print('*' * 100)

#矩阵维度的修改
x1 = np.array(range(12))
print(x1.shape) #打印矩阵的维度信息
print(x1.reshape(3,4)) #修改矩阵的维度信息
x2 = np.arange(12)
x2 = x2.reshape(3,4)
x3 = x2.reshape(x2.shape[0]*x2.shape[1],) #转换成一维
print(x3)

#numpy读取本地数据和索引
file_path = './ratings.csv'
file1 = np.loadtxt(file_path,delimiter=',',dtype=float,skiprows=1)
file2 = np.loadtxt(file_path,delimiter=',',dtype=float,skiprows=1,unpack=True) #将数据的列变成行
print(file1)
print('*' * 100)
print(file2)
#矩阵的转置
t2 = np.arange(24).reshape(4,6)
print(t2)
print(t2.T)#转置
print('*' * 100)
#对矩阵中的元素进行修改
print(t2[2,:]) #去除第3行
print(t2[2:]) #取出第3行及之后的所有行
print(t2[[1,3]]) #取出不连续的多行
print(t2[:,[1,3]]) #取出不连续的多列
print(t2[1,2]) #取出某个元素的值
print(np.where(t2<10,0,10)) #小于10，赋值0，反之，赋值10
print(t2[t2>=10]) #找出矩阵中大于等于10的元素
print(t2.clip(10,18)) #小于10的替换为10，大于18的替换为18
print('*' * 100)
#数据的拼接
y1 = np.array([[1,2,3],[4,5,6]])
y2 = np.array([[0,1,2],[3,4,5]])
print(y1)
print(y2)
print('*' * 100)
print(np.vstack([y1, y2])) #竖直拼接
print('*' * 100)
print(np.hstack([y1,y2])) #水平拼接
print('*' * 100)
y1[[0,1],:] = y1[[1,0],:] #第一行和第二行互换
print(y1)
print('*' * 100)
y2[:,[0,1]] = y2[:,[1,0]] #第一列和第二列交换
print(y2)

#将两个数据集融合到一起，保留原始数据信息
us_path = "./US_video_data_numbers.csv"
gb_path = "./GB_video_data_numbers.csv"
#加载国家数据
us_data = np.loadtxt(us_path,delimiter=',',dtype=int)
gb_data = np.loadtxt(gb_path,delimiter=',',dtype=int)
#构造一个全为0和全为1的数组
zeros_data = np.zeros((us_data.shape[0],1)).astype(int)
ones_data = np.ones((gb_data.shape[0],1)).astype(int)
us_data = np.hstack((us_data, zeros_data))
gb_data = np.hstack((gb_data, ones_data))
final_data = np.vstack((us_data,gb_data))
print(final_data)
print('*' * 100)

#特殊矩阵的创建
z1 = np.zeros((2,3)).astype(int) #2行3列的0矩阵
z2 = np.ones((3,2)).astype(int) #3行2列的1矩阵
z3 = np.eye(4).astype(int) #四阶的单位矩阵
print(z1)
print(z2)
print(z3)
print(np.argmax(z3,axis=0)) #每一列最大值的位置
print(np.argmax(z3,axis=1)) #每一行最大值的位置
print(np.argmin(z3,axis=0)) #每一列最最小值的位置
print(np.random.randint(10,20,(3,4))) #生成3行4列的10~20的随机整数
#numpy基本运算
f1 = np.arange(12).reshape(3,4).astype(float)
print(f1)
print(np.sum(f1,axis=0)) #按列求和
print(np.sum(f1, axis=1)) #按行求和
print(np.mean(f1,axis=0)) #按列求均值
print(np.median(f1,axis=0)) #按列求中值
print(np.max(f1)) #求矩阵最大值
print(np.min(f1)) #求矩阵最小值
print(np.max(f1,axis=0)) #按列求最大值
print(np.ptp(f1)) #求极值
print(f1.std()) #求标准差
print('*' * 100)

#根据数据的最后一列评论数量绘制直方图
us1_path = "./US_video_data_numbers.csv"
#加载国家数据
us1_data = np.loadtxt(us1_path,delimiter=',',dtype=int)
comments = us1_data[:,-1]
comments = comments[comments<5000]
d = 50
bin_num = (comments.max() - comments.min()) // d
plt.hist(comments, bin_num)
plt.xlabel('评论数量')
plt.ylabel('组数')
plt.show()

#根据评论数和喜欢数绘制散点图，观察二者之间的关系
uk1_path = './GB_video_data_numbers.csv' ;
uk1_data = np.loadtxt(uk1_path,delimiter=',',dtype=int)
uk1_data = uk1_data[uk1_data[:,1]<50000]
t_uk_comments = uk1_data[:,-1]
t_uk_like = uk1_data[:,1]
plt.scatter(t_uk_like,t_uk_comments,color ='r')
plt.xlabel('喜欢数')
plt.ylabel('评论数')
plt.show()



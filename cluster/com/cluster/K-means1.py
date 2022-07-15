#对于无监督学习，有两个重要应用，一个是聚类，一个是降维
'''
K-means聚类的主要步骤：
1)选取K个初始的质心，作为初始的类别，及确定K个初始类别
2）计算每一个样本点距离质心的距离，找到样本点距离最近的质心，将样本点划分为该质心所对应的类别
3）根据当前划分的类别情况，计算并更新K个类别对应的质心
4）直到质心不再发生变换或者达到迭代上限为止
'''

import numpy as np
from matplotlib import pyplot as plt

#从sklearn中直接生成聚类数据
from sklearn.datasets._samples_generator import make_blobs


#加载数据,x是100行2列的数据列表,y是100个数据的列表
x, y = make_blobs(n_samples=100,centers=6,random_state=1234,cluster_std=0.6)
#x的第一列作为x轴，x的第二列作为y轴，绘制散点图
plt.scatter(x[:,0],x[:,1],c=y)
plt.show()


#引入距离函数，默认为欧式距离
from scipy.spatial.distance import cdist

centroids = []
print(np.array(centroids,np.float64))
#算法实现部分
class K_means(object):
    #初始化聚类数目为K=6，确定迭代上限300与初始质心
    def __init__(self, n_clusters=6,max_iter=300,centroids=[]):
        self.n_clusters = n_clusters ;
        self.max_iter = max_iter ;
        self.centroids = np.array(centroids, np.float64) ;
        print(np.array(centroids,np.float64))
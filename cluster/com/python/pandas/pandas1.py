'''
python中的numpy库可以处理数值型数据，但是还是不够的，
因为我们所要考虑不仅仅有数值型数据，还有字符串、时间序列等
因此我们需要使用pandas进行处理相应数据
author:WangGuodong
time:2022-07-15
'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import  matplotlib
matplotlib.rc('font', family='YouYuan')

#pandas中常用的数据类型：Series一维带标签的数组，DataFrame二维Series容器
t1 = pd.Series([1,3,4,2,6,5]) #不指定编号，默认从0开始编号
print(t1, type(t1))
print('*' * 100)

#pandas生成一维带标签的数组，并设置标签
t2 = pd.Series([1,2,5,4,6,3], index=list('abcdef'))
print(t2, type(t2))
print('*' * 100)

#pandas通过字典的方式创建数组
temp_dict = {'name' : 'Wang', 'age' : 24, 'tel' : '10086'}
t3 = pd.Series(temp_dict)
print(t3)
print(t3[0]) #找到对应位置的值
#通过键找到值
print(t3['name'])
print(t3.get('name'))
#找到键和键的长度
print(t3.index, len(t3.index))
#找到值
print(t3.values)
#找到对应的元素
print(t3[0:3], t3[[0,2]])

#使用pandas读取外部文件，对于一维使用Series，对于二维使用DataFrame
p = pd.read_csv('./ratings.csv') #直接从当前目录下读取全部文件内容，不需要跳过第一行
print(p)
#DataFrame对象是二维的，既有行索引，又有列索引
t4 = pd.DataFrame(np.arange(12).reshape(3,4)) #默认索引
t5 = pd.DataFrame(np.arange(12).reshape(3,4),index=list('xyz'),columns=list('abcd')) #指定索引
print(t4)
print(t5)
print('*' * 100)
#pandas按照字典的方式创建DataFrame数组
d = {'name' : ['Tang', 'Miao'], 'age' : [25, 23], 'Tel' : ['10086', '10087']}
print(pd.DataFrame(d)) #指定的键默认为列标
print('*' * 100)
d2 = [{'name':'Tang', 'age' : 25, 'Tel' : '10086'}, {'name' : 'miao', 'Tel':'10087'}, {'age' : '22', 'Tel':'10089'}]
print(pd.DataFrame(d2))
print('*' * 100)

#行索引
print(t5.index)
#列索引
print(t5.columns)
print(t5.values) #值
print(t5.shape) #形状
print(t5.head(1)) #显示第一行
print(t5.tail(1)) #显示最后一行
print(t5.info()) #显示关键信息
print(t5.describe()) #显示数字相关信息

'''
对于包含大量名字的数据，我们想知道哪些名字的使用次数比较高，
我们需要进行排序处理，当然我们也可以进行取行和取列操作
'''
df = pd.read_csv('./dogNames2.csv')
#按照动物名字的使用次数进行降序排序
#print(df.head(1))
df = df.sort_values(by='Count_AnimalName',ascending=False)
#取使用次数最高的前20个
print(df[:20])
print(df[:20]['Row_Labels']) #只取名字列
#df.loc通过标签索引行数据
t6 = pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list('wxyz'))
print(t6)
print(t6.loc['a']['z']) #索引对应行列数据
print(t6.loc[:]['w']) #取w列
print(t6.loc['a'][:]) #取a行
print(t6.loc[['a','c']]) #取多行

#df.iloc通过位置索引数据
print(t6.iloc[1])

#需要进行多条件筛选的时候，需要使用布尔索引
dfs = pd.read_csv('./dogNames2.csv')
df1 = dfs[(dfs['Count_AnimalName']>=800) & (dfs['Count_AnimalName']<=1000)]
df2 = dfs[(dfs['Count_AnimalName']>=800) | (dfs['Count_AnimalName']<=1000)]
print(df1)
print('*' * 100)
print(df2)
print('*' * 100)
#找到使用次数大于700且字符串长度大于4的狗的名字
print(dfs[(dfs['Count_AnimalName']>700)& (dfs['Row_Labels'].str.len()>4)])
print('*' * 100)

ts = np.arange(24).reshape(4,6).astype(float)
ts[[0,0,3],[0,5,2]] = np.nan
t8 = pd.DataFrame(ts,index=list('abcd'),columns=list('uvwxyz'))
print(t8)
print('*' * 100)
print(pd.isnull(t8))
print(pd.notnull(t8))
print('*' * 100)
print(t8.dropna(axis=0,how='any')) #删除当前存在nan的行
print(t8.dropna(axis=0,how='all')) #删除当前行中都为nan的行
print(t8.dropna(axis=1,how='any')) #删除当前列存在nan的列
print('*' * 100)
print(t8.fillna(888)) #nan的位置填充888
print('*' * 100)
print(t8.fillna(t8.mean()))#nan的位置填充均值
t8[t8==0] = np.nan  #认为0为缺失值的时候可以赋值nan

#统计方法和字符串离散化
df = pd.read_csv('./IMDB-Movie-Data.csv')
print(df)
print(df.head(1))
print(df.info())
print(df['Rating'].mean()) #获取所有评分的均值
#获取导演的人数,两种方法
print(len(set(df['Director'].tolist())))
print(len(df['Director'].unique()))
#获取演员的人数
temp_actors_list = df['Actors'].str.split(',').tolist()
print(temp_actors_list)
#需要将二维的列表转换成为一维的列表
actors_list = [i for j in temp_actors_list for i in j]
print(len(set(actors_list)))
print('*' * 100)
#电影时长的最大值，最小值，中值等
max_runtime = df['Runtime (Minutes)'].max()
min_runtime = df['Runtime (Minutes)'].min()
median_runtime = df['Runtime (Minutes)'].median()
mean_runtime = df['Runtime (Minutes)'].mean()
print(max_runtime,min_runtime,median_runtime,mean_runtime)
#最大电影时长和最小电影时长的电影对应的索引
max_runtime_index = df['Runtime (Minutes)'].argmax()
min_runtime_index = df['Runtime (Minutes)'].argmin()
print(max_runtime_index,min_runtime_index)
print('*' * 100)

#若知道电影数据，现在想对电影数据的评分、播放时长分别可视化处理
df = pd.read_csv('./IMDB-Movie-Data.csv')
run_data = df['Runtime (Minutes)'].values

max_run = run_data.max()
min_run = run_data.min()
bin_num = (max_run - min_run) // 5

plt.hist(run_data,bin_num)
plt.xticks(range(min_run,max_run+5,5))
plt.xlabel('播放时长')
plt.ylabel('组数')
plt.show()

rating_data = df['Rating'].values
max_rating = rating_data.max()
min_rating = rating_data.min()

plt.hist(rating_data,20)
plt.xlabel('评分')
plt.ylabel('组数')
plt.show()

#数据的合并和分组聚合
#如果给出一组电影数据，我们想知道电影的分类情况
df = pd.read_csv('./IMDB-Movie-Data.csv')
print(df['Genre'].head(3))

#找出分类的二维列表并转换成一维
temp_genre_list = df['Genre'].str.split(',').tolist()
genre_list = list(set([i for j in temp_genre_list for i in j]))

#构造一个全0的数组，然后每个电影出现该分类，则标记1，最后按列求和，即得到每个分类堆的数目
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)
for i in range(df.shape[0]):
    zeros_df.loc[i,temp_genre_list[i]] = 1 ; #分类出现则标记为1
genre_df = zeros_df.sum(axis=0) #按列求和
print(genre_df)

x = genre_df.index
y = genre_df.values
plt.figure(figsize=(14,8))
plt.bar(range(len(x)),y)
plt.xticks(range(len(x)),x,rotation=45)

plt.xlabel('电影类别')
plt.ylabel('类别数量')
plt.show()
print('*' * 100)

#下面我们一起看一下数据的合并join和merge的使用
df1 = pd.DataFrame(np.ones((2,4)),index=list('AB'),columns=list('abcd'))
df2 = pd.DataFrame(np.zeros((3,3)),index=list('ABC'), columns=list('xyz'))
print(df1)
print("*" * 100)
print(df2)
print('*' * 100)
print(df1.join(df2)) #按左边的,右边多余的行删除
print('*' * 100)
print(df2.join(df1))#按左边，右边缺少的行用NAN值填充
print('*' * 100)
df3 = pd.DataFrame(np.arange(9).reshape(3,3), columns=list('fax'))
print(df3)
print('*' * 100)

#关于pandas中索引和复合索引的问题
df = pd.read_csv('./starbucks_store_worldwide.csv')
group1 = df[["Brand"]].groupby(by=[df['Country'],df['State/Province']]).count()
print(group1.index)

#使用matplotlib可视化店铺总数排名前10的国家
data1 = df.groupby(by=df['Country']).count()['Brand'].sort_values(ascending=False)[:10]
print(data1)
x = data1.index
y = data1.values
plt.figure(figsize=(16,8),dpi=80)
plt.bar(x,y,color='orange')
plt.xlabel('国家名称')
plt.ylabel('店铺总数')
plt.show()

#使用matplotlib可视化中国每个城市的店铺数目
df = pd.read_csv('./starbucks_store_worldwide.csv')
df = df[df['Country']=='CN']
data2 = df.groupby(by=df['City']).count()['Brand'].sort_values(ascending=False)[:25]
x = data2.index
y = data2.values
plt.figure(figsize=(16,8),dpi=80)
plt.bar(x,y)
plt.xlabel('城市名称')
plt.ylabel('店铺总数')
plt.show()

'''
现在有全球排名靠前的10000本书的数据
可视化不同年份书的数量和评分情况
'''
df = pd.read_csv('./books.csv')
data3 = df[pd.notnull(df["original_publication_year"])]
group3 = data3.groupby(by=df["original_publication_year"]).count()['title']
x = group3.index
y = group3.values
plt.figure(figsize=(16,8), dpi=80)
plt.plot(range(len(x)),y)
plt.xticks(list(range(len(x)))[::10],x[::10].astype(int),rotation=45)
plt.xlabel('年份')
plt.ylabel('书的数量')
plt.show()

#不同年份评分均值
group4 = data3['average_rating'].groupby(by=data3["original_publication_year"]).mean()
x = group4.index
y = group4.values
plt.figure(figsize=(16,8), dpi=80)
plt.plot(range(len(x)),y,color='red')
plt.xticks(list(range(len(x)))[::10],x[::10].astype(int),rotation=45)
plt.xlabel('年份')
plt.ylabel('平均评分')
plt.show()
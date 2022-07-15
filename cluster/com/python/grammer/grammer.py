'''
author：WangGuodong
time：2022-07-14
任务：复习python语法
'''

#1.数据类型
x = 3 + 4j #复数
a = 10 #整型
b = 14.3 #浮点型
c = 'hello world'#字符串类型
d = False #bool型
c = [1, 2, 3] #列表类型list
d = (1, 2, 3) #元组类型tuple
e = {1, 2, 3} #集合类型set
f = {'name':'wang', 'age':18} #字典类型dict
print(type(c), type(d), type(e), type(f))
print(type(x))

#2.格式化输出
name = 'wang'
age = 24
weight = '60'
id = '0692'
print('我的名字叫%s' %name)
print('我的年龄%d' %age)
print('我的名字叫%s,我的年龄%s岁,我的体重是%skg,我的学号是%s' %(name, age, weight, id))

#3.常用的转义字符
print('hello\n' 'python') #换行
print('hello\t' 'python') #制表符，一个tab键的距离
#print默认的结束字符是换行，结束的字符也可以是其它的
print('hello', end='\t')
print('python', end='\n')
print('hello', end='  ')

#4.输入和输出
password = input('请输入你的密码：')
print(password)
print(type(password))

#5.数据类型的转换
number = input('请输入一个大于10，小于20的数字：')
print(number)
print(type(number), type(int(number)), type(float(number))) #分别转换成整型和浮点型
print(type(list(number)), type(tuple(number)), type(str(number)))#转换成列表、元组、字符串类型


#6.运算符：基本运算符、复合赋值运算符、逻辑运算符
x1 = 5
y1 = 2
print(x1+y1, x1-y1, x1*y1, x1/y1, x1//y1) #加、减、乘、除、整除
print(x1%y1, x1**y1) #取余和指数次方
x1 //= y1 #整除并赋值
print(x1)
x1 **= y1 #幂次方并赋值
print(x1)
x2 = True
y2 = False
print(x2 and y2 , x2 or y2, not x2, not y2)

#7.条件语句
if True:
    print('正确！')
else:
    print('错误！')

ages = 22
if ages >= 18:
    print('恭喜您已经成年了！！！')
elif ages >= 1 and ages <= 17:
    print('不好意思,你尚未成年！！！')
else:
    print('你的输入错误，请重新输入，谢谢！！！')

#8.循环语句
#range的用法，range是左闭右开的区间
s = range(10) #默认从0开始，步长为1
print(s)
print(list(s)) #转换成列表的形式，步长为1，即0~9
print(list(range(1,10))) #1~9，步长为1
print(list(range(1,10,2))) #1~9，步长为2
print(list(range(10,0,-1))) #从10开始，步长为-1，从10到1
print(10 in s) #判断10是否在序列中
print(10 not in s)
#while循环,从1加到100
sum = 0
s0 = 1
while s0 <= 100:
    sum += s0
    s0 += 1
print(sum)
#for --- in 循环的使用
for item in 'python' : #一次读取python中的每个单词
    print(item, end = ' ')
for i in range(1,11):
    print(i, end=' ') #产生1~10的整数序列
print()
for _ in range(1,10):
    print('好好科研,好好努力,大厂offer拿到手软！！！')
sum1 = 0
for i in range(0,101):
    sum1 += i
print(sum1)
lis = [1,2,3,4,5,6]
for j in range(0,len(lis)):
    print(lis[j], end=' ')
print()

#9.列表的使用
lst = [1, 2, 'hello', 4.5]
for i in range(0, len(lst)): #打印lst列表中的元素
    print(lst[i])
print(lst.index('hello')) #根据列表元素查找索引
print(lst[-1]) #最后一个元素，逆向索引
print(lst[0]) #第一个元素,正向索引
#切片的方式获取列表中的多个元素
print(lst[0:len(lst):1]) #三个位置的元素分别为起始位置，结束位置，步长
print(lst[0:len(lst):2])
#注意，如果省略起始位置，则默认从头开始,省略步长，则默认步长为1，省略结束位置,则默认最后一个元素的位置
#另外,如果步长出现负数，则默认从后往前遍历
#列表元素的判断及遍历
print(1 in lst)
print(1 not in lst)
for k in lst:
    print(k, end=' ')
print()
#向列表中添加元素
lst.append('learning') #在列表末尾追加一个元素
lst1 = [2,3,4]
lst.extend(lst1) #在列表后追加多个元素
lst.insert(0,100) #在第一个位置插入元素100
print(lst)
lst2 = ['java', 'c', 'Matlab']
lst[1:1:1] = lst2 #在设定的位置插入列表
print(lst)
#删除列表中的元素
lst3 = [1,2,3,4,5,6,7,8,'hello']
lst3.remove('hello') #将指定元素从列表删除
print(lst3)
lst3.pop(0) #删除指定索引的元素
print(lst3)
lst3.clear()
print(lst3) #清空列表元素
del lst3 #删除列表
#print(lst3)
#修改列表元素的值
lst4 = [1,2,3,'hello',4]
lst4[0] = 100 #将第一个元素的值修改为100
print(lst4)
lst4[1:5] = [200, 300, 400, 500]#修改第二个元素到最后一个元素的值
print(lst4)
#对列表元素进行排序
lst5 = [1,4,3,2,6,5]
lst5.sort() #默认升序排序
print(lst5)
lst5.sort(reverse=True) #降序排序
print(lst5)
lst10 = [1,2,3,4,5,5,5,6]
lst11 = [1,2,3,4,6,6,6,5]
print(len(lst10)) #列表的长度
print(max(lst10)) #列表的最大元素
print(min(lst10)) #列表的最小元素
print(lst10.count(5)) #统计元素5在列表中出现的次数


#10.字典的操作
scores = {'唐乃乔': 99, '缪鹏':100, '谭祖万': 67}
print(scores)
print(type(scores))
print(scores['唐乃乔'])
print(scores.get('唐乃乔'))
print('谭祖万' in scores) #判断谭祖万是否在scores集合中
del scores['唐乃乔'] #删除键值对
print(scores)
scores['唐乃乔'] = 97 #新增键值对
print(scores)
scores['唐乃乔'] = 88 #修改已有键值对
print(scores)
keys = scores.keys() #获取字典的所有键
print(list(keys))
values = scores.values()#获取字典的所有值
print(list(values))
#遍历字典，获取键值对
for item in scores:
    print(item, scores.get(item))
scores.clear() #清空字典中的元素
print(scores)


#11.元组的基本操作,用的很少
t = ('java', 'C', 'python')
print(t)
for i in t:
    print(i, end=' ')
print()


#12.集合的操作
s1 = {1,1,1,2,3,4,4,5,8,7,9,0} #集合自动去重和排序
print(s1)
s2 = set(range(0,11)) #set方式创建集合
print(s2)
s3 = set([1,4,3,3]) #列表转换成集合,自动排序和去重
print(s3)
print(1 in s3, 1 not in s3) #判断元素是否在集合s3中
s3.add(5) #集合中添加元素
print(s3)
s3.update({6,7,8}) #集合中添加多个元素
print(s3)
#分别删除集合中的元素8个元素7
s3.remove(8)
s3.discard(7)
print(s3)
s3.pop() #删除集合中的第一个元素
print(s3)
s3.clear() #清空集合中的元素
print(s3)


#12.字符串的基本操作
s = 'hello World'
print(s.swapcase()) #大写变小写，小写变大写
print(s.find('l')) #查找l第一次出现的位置
print(s.rfind('l')) #查找l最后一次出现的位置
print(s.upper()) #字符串转大写
print(s.lower()) #字符串转小写
print(s.title()) #首字母变大写
print(s.capitalize())#首字母变大写
#字符串的拆分操作
s2 = 'java | c| python'
s3 = s2.split(sep='|') #从左侧拆分
print(s3)
s4 = s2.split(sep='|') #从右侧拆分
print(s4)
s5 = s2.split(sep='|', maxsplit=1) #指定拆分次数为1次
print(s5)
#常用的字符串判断方法如下
print(s2.isalnum()) #字符串是否由字母和数字组成
print(s2.isnumeric()) #字符串是否全由数字组成
print(s2.isalpha()) #字符串是否全由字母组成
print(s2.isidentifier()) #判断字符串是否是合法的标识符
#字符串的替换与合并
s11 = 'hello python python python'
s12 = s11.replace('python', 'java')
print(s12)
print(s11.replace('python','java', 2)) #指定替换次数为2次
#字符串的拼接
print('-'.join(s11)) #档额字符的拼接
s13 = ['java', 'c', 'python']
print('-'.join(s13)) #字符串列表的拼接
s14 = 'hello'


#13.函数的定义和使用
def cal1(a,b): #带返回值的函数
    return a + b

def cal2(num):
    odd = []
    even = []
    for i in num:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return odd, even

def cal3(a, b): #无返回值的函数
    print(a**b)

ls = [1,2,3,4,5,6,7,8]
print(cal2(ls))
print(cal1(4,5))
cal3(2,3)





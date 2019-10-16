#基于python的软件生态系统  ecosystem : Scipy
'''
官网：scipy.org
六大核心包：
NumPy、SciPy library、Matplotlib、IPython、Sympy、pandas
SciPy中的数据结构：
ndarray(N维数组)
Series(变长数组)
DataFrame(数据框)
'''

#NumPy
import numpy as np 
from scipy import linalg

aArray = np.ones((3,4))
print(aArray)
arr=np.array([[1,2],[3,4]])
print(linalg.det(arr))#计算行列式


a1=np.arange(1,5,dtype=np.float64)
a2=np.power(a1,2)
a2.sum()
a3=np.arange(4)

aArray=np.array([(1,2,3),(4,5,6)])
#[[1,2,3][4,5,6]]
aArray[0]
#[1 2 3]
aArray[0:2]
aArray[:,[0,1]]
aArray[1,[0,1]]

for row in aArray:
    print(row)



#ndarray基本概念
'''
维度（dimensions）称为轴（axis），轴的个数称为秩（rank）
基本属性：
ndarray.ndim 秩
ndarray.shape 维度
ndarray.size 元素总个数
ndarray.dtype 元素类型
ndarray.itemsize 元素字节大小
'''
#ndarray的创建
aArray=np.array([1,2,3])
bArray=np.array([(1,2,3),(4,5,6)])
np.arange(1,2,0.5)
np.random.random((2,2))
np.linspace(1,2,10,endpoint=False)
np.ones([2,3])
np.zeros((2,2))
#九九乘法表
np.fromfunction(lambda i,j: (i+1)*(j+1),(9,9))

###
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
x[1,2]

x[0]#选择第一行

x[:,[0,2]]#选择第1、3列
x[:,::3]

x[::2]#选择第1、3行

x[::-1]
x[:,::-1]
x[::-2]
###

#ndarray操作
aArray=np.array([(1,2,3),(4,5,6)])
aArray.shape#维度2*3
aArray.reshape(3,2)#aArray不变
aArray.resize(3,2)#aArray变

x=np.arange(1,17).reshape(4,4)
x.reshape(2,-1)#转化为2行n列
x.reshape(-1,1)

#vstack在垂直方向拼接
aArray=np.array([1,3,7])
bArray=np.array([3,5,8])
np.hstack((aArray,bArray))
np.vstack((aArray,bArray))

#numpy数组特性--广播
a=np.array([1,2,3])
b=np.array([[1,2,3],[4,5,6]])
c=a+b

#ndarray的运算
'''
sum     mean平均值
std标准差     var方差
min     max
argmin  argmax 返回索引
cumsum  cumprod
'''
aArray=np.array([(1,2,3),(4,5,6)])
aArray.sum()
aArray.sum(axis=0)#按列求和
aArray.sum(axis=1)#按行求和

#ndarray的专门应用--线性代数
'''
dot 矩阵内积
linalg.det 行列式
linalg.inv 逆矩阵
linalg.solve 多元一次方程求根
linalg.eig 求特征值和特征向量
'''

#ndarray的ufunc函数(universal function)
'''
ufunc是一种能对数组的每一个元素进行操作的函数
add all any arange 
'''
import time
import math

x= np.arange(0,100,0.01)
t_m1=time.process_time()
for i,t  in enumerate(x):
    x[i]=math.pow((math.sin(t)),2)
t_m2=time.process_time()

y=np.arange(0,100,0.01)
t_n1=time.process_time()
y=np.power(np.sin(y),2)
t_n2=time.process_time()

print('Running time of math:',t_m2-t_m1)
print('Running time of math:',t_n2-t_n1)



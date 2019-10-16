import numpy as np 

x=np.ones((10,10))
print(x)
x[1:-1,1:-1]=0
print(x)
x=np.full((10,10),1)
print(x)
x=np.full((10,10),np.pi)
print(x)
x=np.array([[1,2,3],[4,5,6]],dtype=np.float64)
print(x)
x=np.full_like(x,4)
print(x)
#创建单位数组
print(np.identity(10))
print(np.eye(8))
print(np.eye(8,k=1))
print(np.eye(8,k=-2))

#采样
print(np.random.normal(0,5,100))
print(np.random.uniform(-5,5,100))
#对于一个二维数组怎样可以从中有放回和无放回采样k行数据
a=np.random.rand(3,5)
mask=np.random.choice(np.arange(a.shape[0]),2,replace=True)
print(a[mask])

#数组的bool索引
x=np.arange(1,101)
print(x<=50)
print(x[x<=50])
print(x[(x>50)&(x%2==0)])
x[x%2==0]=-1
print(x)
print(np.where(x%2==0,-1,x))

scores=np.array([[98,76,87],[76,88,91]])
score_mean=scores.mean(axis=1,keepdims=True)
print(score_mean)
print(scores-score_mean)

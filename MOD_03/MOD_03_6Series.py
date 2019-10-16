#变长字典series
'''
类似于一维数组的对象，由数据和索引组成
'''
import pandas as pd
import numpy as np
#自带索引0 1 2...
aSer=pd.Series([1,2.0,'a'])
#自定义Series的index
bSer=pd.Series(['apple','peach','lemon'],index=[1,2,3])
print(bSer.index)
print(bSer.values)

#Series的基本运算
aSer=pd.Series([3,5,7],index=['a','b','c'])
print(aSer['b'])
#所有values*2
bSer=aSer*2
#计算自然对数的n次方
cSer=np.exp(aSer)

#Series的数据对齐 对于不存在的索引返回NaN(Not a Number 表示未定义或不可表示的值)
data={'AXP':'86.40','CSCO':'122.64','BA':'99.44'}
sindex=['AXP','CSCO','BA','AAPL']
aSer=pd.Series(data,index=sindex)
print(aSer)
print(pd.isnull(aSer))
data1={'AXP':'86.40','CSCO':'122.64','CVX':'23.78'}
bSer=pd.Series(data1)
print(aSer+bSer)
#在运算中自动对齐不同索引的数据
data={'AXP':86.40,'CSCO':122.64,'BA':99.44}
aSer=pd.Series(data,index=sindex)
print(aSer)
data1={'AXP':86.40,'CSCO':122.64,'CVX':23.78}
bSer=pd.Series(data1)
print(aSer+bSer)
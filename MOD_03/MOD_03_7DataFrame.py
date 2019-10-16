#Series对应的是一维序列，而DataFram对应的是二维表结构，是一种表格型的数据结构，可以看成是共享同一个index的Series集合
#创建DataFrame#
import pandas as pd
import numpy as np
#1
data={'name':['wangdachui','linling','niuyun'],'pay':[4000,5000,6000]}
frame=pd.DataFrame(data)
print(frame)
#2 注意创建DataFrame方法把我们的工资值转化为了字符串
data=np.array([('wangdachui',4000),('linling',5000),('niuyun',6000)])
frame=pd.DataFrame(data,index=range(1,4),columns=['name','pay'])
print(frame)
print(frame.index)
print(frame.columns)
print(frame.values)

#DataFrame基本操作#
#获取DataFrame对象的列和行可获得Series
print(frame['name'])
print(frame.pay)
print(frame.iloc[:2,1])
#DataFrame对象的修改和删除
frame['name']='admin'
print(frame)
#删除列
#del frame['pay']
#print(frame)

#Dataframe的统计功能# 
#找DataFrame对象成员的最低工资
print(frame.pay.min())
#高工资人群 用矢量运算的方式解决问题而非for循环
print(frame[frame.pay>='5000'])
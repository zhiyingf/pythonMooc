#input print 
'''
print(对象1,对象2,...,对象n,sep='',end='\n')
sep表示输出对象之间的分隔符，
end表示print()函数输出完成后自动换行
'''

#输入任务：
'''
1、如何输入获得两个字符串
2、如何输入获得两个整数
3、如何输入后获得一个元素均为数值型的列表
'''
x,y=input('Input:').split()#split()参数默认是空白字符（空格、换行符等）

x1,y1=eval(input('Input:'))

lst=list(eval(input('Input:')))


#输出任务：
'''
1、如何在输出数据中加入一个非空白分隔符
2、如何换行输出所有数据
3、如何将循环输出的所有数据放在同一列表
'''
x,y=4,5
print(x,y,sep=',')

print(x)
print(y)

for i in range(1,5):
    print(i,end=' ')


#利用列表解析
list1=['12','12.2','678']
list2=[eval(item) for item in list1]
#使用map
#list2=list(map(eval,list1))转换成数值型
#list(map(str,list2))转换成字符串


#函数式编程
'''
基本函数：
map(函数,列表)返回的是map对象
reduce(函数,列表)  
filter(函数,列表)
算子(operator):
lambda
'''
list3=[3,2,5,8,1]
list(map(lambda x: x*2,list3))

list4=[1,2,3,4,5,6]
list(filter(lambda x: x%2==0,list4))

from functools import reduce
list5=[1,2,3,4,5]
reduce(lambda x,y: x+y,list5)


list6=['qewqe','qdqdw']
'abc'.upper()#upper('abc')错误
list(map(lambda word: word.upper(),list6))

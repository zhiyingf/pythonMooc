
def addMe2Me(x):
    'apply operation + to argument.'
    return (x+x)
#x=int(input('Please input a number'))
#print(addMe2Me(x))

#传递函数
def self(f,y):
    print(f(y))
#self(addMe2Me,2.2)


#匿名函数：lambda函数
def my_add(x,y):return x+y

lambda x,y : x+y

my_add=lambda x,y:x+y

r=lambda x: x+x
#print(r(5))




#素数判断
from math import sqrt
def isprime(x):
    k=int(sqrt(x))
    j=2
    while j<=k:
        if x%j==0:
            print('{} is not a prime.'.format(x))
            break
        j+=1
    else:
        print('{:d} is a prime.'.format(x))
    
#x=int(input('Please input a number:'))
#isprime(x)

#默认参数
def f(x=True):
    ''' whether x is correct word or not '''
    if x:
        print('x is a correct word.')
    print('OK')
#默认参数一般需要放在参数列表的最后
def f1(x,y=True):
    ''' x and y both correct words or not.'''
    if y:
        print(x,'and y both correct.')
    print(x,'is OK')

#位置参数，即位置很重要  关键字参数
def f2(x,y):
    ''' x and y both correct words or not.'''
    if y:
        print(x,'and y both correct.')
    print(x,'is OK')

#f(False)
#f1(5)
#f2(68,False)
#f2(y=False,x=68)使用关键字参数
''' 
关键字参数是让调用者通过使用参数名区分参数。允许改变参数列表中的参数顺序
'''
#f2(y=False ,86)一旦使用了关键字参数，就把整个关键字参数表打乱
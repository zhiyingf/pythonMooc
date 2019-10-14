#tuple不可变，无sort方法  x=2,
'''
元组用于：
在映射内容中用作键使用
函数的特殊类型参数
作为函数的返回值
'''
def foo(args1,args2='world'):
    print(args1,args2)
foo('Hello,')
foo('Hello,',args2='Python!')
foo(args2='Apple!',args1='Hello,')

def foo1(args1,*args):
    print(args1)
    print(args)
foo1('Hello','Wang','Lin','fu')

def foo2():
    return 1,2,3
print(foo2())
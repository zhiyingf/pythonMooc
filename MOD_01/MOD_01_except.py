'''
try:
    num1=int(input('Enter the first number:'))
    num2=int(input('Enter the second number:'))
    print(num1/num2)
except ValueError as err:#err 错误原因名
    print('Please input a digit!')
    print(err)
'''
#except:捕捉所有异常 空的except子句和as



#多个except子句和一个except块捕捉所有异常
'''
try:
    num1=int(input('Enter the first number:'))
    num2=int(input('Enter the second number:'))
    print(num1/num2)
except ValueError as err:#err 错误原因名
    print('Please input a digit!')
    print(err)
except ZeroDivisionError as err:
    print('The second number cannot be zero!')
    print(err)
'''



#else子句
'''
try:
    num1=int(input('Enter the first number:'))
    num2=int(input('Enter the second number:'))
    print(num1/num2)
except ValueError as err:#err 错误原因名
    print('Please input a digit!')
    print(err)
else:
    print('Aha , everything is OK.') 
'''

#异常处理 多次输入 循环
'''
while True:
    try:
        num1=int(input('Enter the first number:')) 
        num2=int(input('Enter the second number:'))
        print(num1/num2)
        break
    except ValueError:
        print('Please input a digit!')
    except ZeroDivisionError:
        print('The second number cannot be zero!')
        '''


#finally子句
'''
def finallyTest():
    try:
        x=int(input('Enter the first number:'))
        y=int(input('Enter the second number:'))
        print(x/y)
        return 1
    except Exception as err:
        print(err)
        return 0
    finally:
        print('It is a finally clause.')

result=finallyTest()
print(result)
'''

#上下文管理器（Context Manager）和with语句
'''
利用try-finally结构来进行文件的异常处理和关闭，利用finally子句来进行文件的关闭，希望不管文件是不是正常打开都对文件进行关闭
'''
'''
try:
    f=open('D:\\pythonstudy\\workdir\\fzy.txt')
    for line in f:
        print(line,end=' ')
except IOError:
    print('Cannot open the file!')
finally:
    f.close()
'''

'''
但是假设文件都不能正常打开，那f变量其实并没有获得值，所以程序执行仍然会发生异常
python提供了上下文管理器：定义和控制代码块执行前的准备动作以及执行后的收尾动作
'''
with open(r'D:\pythonstudy\workdir\fzy.txt') as f:
    for line in f:
        print(line,end=' ')

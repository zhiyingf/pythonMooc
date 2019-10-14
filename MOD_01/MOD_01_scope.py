#改变全局变量的值
a=3
def f(x):
    global a #要明确告诉函数a是全局变量
    print(a)
    a=5
    print(a+x)

f(8)
print(a)
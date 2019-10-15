#寻找n以内的亲密数对。
'''
对于两个不同的整数A和B，如果整数A的全部因子（包括1，不包括A本身）之和等于B；且整数B的全部因子（包括1，不包括B本身）之和等于A，则将A和B称为亲密数。自定义函数fac(x)计算x包括1但不包括本身的所有因子和并返回。从键盘输入整数n，调用fac()函数寻找n以内的亲密数并输出。注意每个亲密数对只输出一次，小的在前大的在后，例如220-284。
'''
import math
def fac(n):
    ans=1
    for i in range(2,n):
        if n%i==0:
            ans+=i
    return ans
def main():
    xInput=int(input())
    for i in range(1,xInput):
        x=fac(i)
        if x<i and i==fac(x):
            print('{}-{}'.format(x,i))

if __name__ == "__main__":
    main()
#非递归
def fib(n):
    a,b=0,1
    count=1
    while count<n:
        a,b=b,a+b
        count+=1
    print(a)

#递归
def fib1(n):
    if n==0 or n==1:
        return n
    else :
        return fib1(n-1)+fib1(n-2)

#汉诺塔问题
def hanoi(a,b,c,n):
    if n==1:
        print(a,'->',c)
    else :
        hanoi(a,c,b,n-1)
        print(a,'->',c)
        hanoi(b,a,c,n-1)



#hanoi('a','b','c',3)


#n=int(input('Input a number:'))
#fib(n)
#随机数游戏
'''
from random import randint
x = randint(0,300)
for count in range(0,5):
    print('Please input a number :')
    digit = int(input())
    if x==digit :
        print('bingo')
    elif x>digit:
        print('Too small, try once again.')
    elif x<digit:
        print('Too large, try once again.')
'''

#输出2-100之间的素数
'''
from math import sqrt
#使用while循环
j=2
while j<=100:
    i=2
    k=sqrt(j)
    while i<=k:
        if j%i==0:
            break
        i=i+1
    if i>k:
        print(j,end=' ')
    j+=1
#使用for循环
for i in range(2,101):
    k=int(sqrt(i))
    flag=True
    for j in range(2,k+1):
        if i%j==0:
            flag=False
            break
    if flag:
        print(i,end=" ")
'''

#continue语句
'''
sumA=0
i=1
while i<=5:
    sumA+=i
    if i==3:
        i+=1
        continue
        #break
    print('i={},sum={}'.format(i,sumA))    
    i+=1
'''

#随机数游戏 filename : guessnum3.py
'''
from random import randint
x=randint(0,300)
go = 'y'
while go=='y':
    digit=int(input('Please input a number between 0~300:'))
    if digit==x:
        print('Bingo!')
        break
    elif digit>x:
        print('Too large , please try again.')
    else:
        print('Too small , please try again.')
    go=input('Input y if you want to continue.')
else:
    print('Goodbye!')    

'''

#循环中的else语句 prime.py
'''
from math import sqrt
num=int(input('Please enter a number:'))
j=2
while j<=int(sqrt(num)):
    if num%j==0:
        print('{:d} is not a prime.'.format(num))
        break
    j+=1
else:
    print('{:d} is a prime.'.format(num))
'''


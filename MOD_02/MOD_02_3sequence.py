#序列:字符串''、列表list[]、元组tuple{} 
'''
索引：0 ----> n-1，-n <---- -1
切片[begin,end,offset(切片)]
序列类型转换内建函数：
list(),str(),tuple()
len(),sorted(),max(),min(),sum(),zip(),reversed(),
enumerate(),
'''
'''
week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print(week[1],'\n',week[-2],'\n',week[1:4],'\n',week[:6],'\n',week[::-1])
print('apple'*3)
print('pine'+' apple')
'BA' in ('BA','122.64','The Boeing Company')
p1=list('Hello world!')
print(p1)
p2=tuple('Hello,world!')
print(p2)
'''

#将字符串'Hello,world!?'中的'World'替换成'Python!???'，并计算其中包含的标点符号的个数(,.?!)
aStr='Hello,World!?'
bStr=aStr[:7]+'Python!???'
count=0
for ch in bStr[:]:
    if ch in ',.?!':
        count+=1
print(count)
#%+格式运算符
#format_string % (arguments_to_convert)
print('There are %d punctuation marks.'%(count))
#替换后面的参数的占位符：{参数序号：格式说明符(格式限定符b二进制,o八进制,x十六进制,c字符,d十进制整数,f浮点数,e指数记法,+m.nf,<左对齐,0>5d右对齐 用0填充左边 宽度为5,^居中对齐,{{}}输出一个{})}
#format_string.format(argument_to_convert)
print('There are {0:d} punctuation marks.'.format(count))
age,height=21,1.758
print('Age:{0:0>5d},Height:{1:5.2f}'.format(age,height))
print('Age:{0:<5d},Height:{1:5.2f}'.format(age,height))

#用format函数格式化字符串
'''
字符串默认的对齐方式：左对齐
整数：右对齐
'''
cCode=['Axp','BA','CAT','CSCO','CVX']
cPrice=['78.51','184.76','96.39','33.71','106.09']
for i in range(5):
    print('{:<8d}{:8s}{:8s}'.format(i,cCode[i],cPrice[i]))


#判断回文串
'''
sStr='acdhdca'
if sStr==''.join(reversed(sStr)):
    print('yes')
else:
    print('No')
'''

import operator
sStr='acdhdca'
if operator.eq(sStr,''.join(reversed(sStr)))==1:
    print('yes')
else:
    print('No')


#字符串的运用
song='Blowing in the wind'
song.find('the')
song.find('the',8,12)#-1表示没找到
song.lower()
song.split(' ')#字符串截断
song.replace('the','that')#字符串替换
#用指定字符串连接列表
alist=['hello','world']
' '.join(alist)
#encode编码
y='你好'
z=y.encode('utf-8')#z是一个字节包
z.decode()

#
aStr='What do you think this saying "No pain,No gain."?'
'''
lindex=aStr.index('\"',0,len(aStr))
rindex=aStr.rindex('\"',0,len(aStr))
tempStr=aStr[lindex+1:rindex]
'''
tempStr=aStr.split('\"')[1]
if tempStr.istitle():
    print('it is title format.')
else:
    print('it is not title format.')
print(tempStr.title())
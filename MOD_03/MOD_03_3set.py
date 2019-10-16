#set
'''
可变集合set
不可变集合frozenset

数学符号  python符号
∈        in
不属于    not in
=         ==
≠         !=
真包含     <
包含       <=
被真包含    >
被包含     >=

交∩          &
并∪          |
差 - 或 \      -
异或        ^

运算符可复合
&=  |=  -=  ^=
'''
names=['w','w','n']
namesSet=set(names)
s1=set('hello')
namesFro=frozenset(names)
s2=frozenset('hello')
'h' in s1
#True

aSet=set('sunrise')
bSet=set('sunset')
print(aSet & bSet)
print(aSet | bSet)
print(aSet - bSet)
print(aSet ^ bSet)
print(aSet -=set('sun'))

#集合的内建函数
aSet.issubset(bSet)#判断aSet是不是bSet的子集

'''
s1.discard(x)x不在s1中时返回none
s1.remove(x)x不在s1中时发生异常keyError
'''

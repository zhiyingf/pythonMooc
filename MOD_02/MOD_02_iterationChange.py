#可变可迭代对象修改问题
'''
python中可变可迭代对象一边迭代一边修改会出现问题，remove insert对迭代器的迭代产生影响
'''
lst=[1,2,4,3,5]
for x in lst[:]:#lst的浅拷贝：lst[:]
    if x%2==0:
        lst.remove(x)
print(lst)

#不可变迭代器,不会修改原始迭代器中的元素
s="beautiful"
for ch in s:
    if ch in "aeion":
        s=s.replace(ch,'')
print(s)

#浅拷贝与深拷贝：关系到是否会修改原始对象或原始对象中的部分元素
x=[1,2,3]
y=x
y[0]=4
print(x)#x改变，说明x,y都是对同一块内存空间的引用

#为避免以上问题，可以创建对象的拷贝
z=x[:]#把x的浅拷贝赋给z
z[0]=8
print(x)#x没有改变

x=[1,2,[3,4]]
y=x.copy()#x浅拷贝 
y[0],y[2][0]=9,9
print(y)
print(x)#x的一级元素没有改变，二级元素改变。
'''
说明：让一级元素有了自己独立的内存空间，二级元素仍然指向了被拷贝对象的二级元素的内存区域
即：浅拷贝只复制了父对象，就是一级元素，而不复制内部子对象
想要实现既复制父对象又复制内部子对象使用深拷贝
python默认的方式是浅拷贝
'''
import copy
z=copy.deepcopy(x)
z[0],z[2][0]=8,8
print(z)
print(x)

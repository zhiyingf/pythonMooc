'''
import collections
import copy
s = "我/是/一个/测试/句子/，/大家/赶快/来/统计/我/吧/，/大家/赶快/来/统计/我/吧/，/大家/赶快/来/统计/我/吧/，/重要/事情/说/三遍/！/"
s_list = s.split('/') 
# 为避免迭代时修改迭代对象本身，创建一个列表的深拷贝，也可用浅拷贝s_list_backup = s_list[:]
s_list_backup = s_list[:]
[s_list.remove(item) for item in s_list_backup if item in '，。！”“']
t=collections.Counter(s_list)
print(type(t))
print(t)
'''
#字典元素的增加、删除、更新、查询
'''
元素增加：d['b']=2、d.update({'b': 2,'c':3})、d.update(b=2,c=3)
元素删除：d.pop('b')  pop(),()里为需要删除的key值；  del x['b']
元素查询：
    1、d['b'] 如果键值（key）'b'不存在就会出现keyError错误（报错）
    2、d.get('b')如果键值（key）'b'不存在返回None，否则返回value
'''
def countfeq(s):
    ans={}
    slist=s.split(' ')
    slistClean=slist[:]
    for item in slistClean:
        if item[len(item)-1] in ',.':
            slist.remove(item)
            slist.append(item[0:len(item)-1])
    for item in slist:
        if ans.get(item)==None:
            ans[item]=1
        else:
            ans[item]+=1
    return ans
def main():
    s = "Not clumsy person in this world, only lazy people, only people can not hold out until the last."
    ans=countfeq(s.lower())
    #print(ans)
    s1=input()
    if ans.get(s1)==None:
        print(0)
    else:
        print(ans[s1])
    



if __name__ == "__main__":
    main()
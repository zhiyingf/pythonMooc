#dict:key-value
'''
创建字典：
1、aInfo={'w':1,'N':2}
2、bInfo=dict([('w',1),('N':2)])
3、cInfo=dict([['W',1],['N':2]])
4、dInfo=dict(w=1,N=2)
5、keys=['w','N'];values=[1,2]
   eInfo=dict(zip(keys,values))

6、将所有员工工资默认设置为3000
aDict={}.fromkeys(('w','N'),3000)  ['w','N']也可以，只要是序列就可以
     sorted(aDict)=?  返回一个list:['N','w']

字典更新、添加：
aInfo['w']=300
字典键值查询：
'w' in aInfo  =True 或者  False
aInfo.get(key) =values 或者 None
字典删除：
del aInfo['w']
aInfo.pop(key)
aInfo.clear()

字典常用方法：
hash('Wn')用于判断某一个对象是不是可哈希的，一般我们可以理解为是不是不可变的
          可哈希会出现哈希值，列表不可哈希

aInfo.keys()返回key列表
aInfo.values()

for k,v in aInfo.items():
    print(k,v)

字典更新（添加、更改）：
aInfo={'w':1,'N':2}
bInfo={'w':2,'m':4}
aInfo.update(bInfo)

setdefault()
'''

#字典相关使用小案例：
'''
1、json格式：JavaScript Object notation  js对象标记，一种轻量级的数据交换方式
x={"name":"Niuyun","address":{"city":"Beijing","street":"chaoyang road"}}
print(x['address']['street'])

import json
json_str=json.dumps(x)将x转换成json编码字符串
json.loads(json_str)还原
.json文件

搜索引擎关键字查询
百度
http://www.baidu.com/s?wd=%s
谷歌
http://www.googlestable.com/search/?q=%us

Bing
中国：http://cn.bing.com/search?q=%us
美国：http://www.bing.com/search?q=%us

'''
import requests
def func0():
    kw={'q':'Python dict'}
    r= requests.get('http://cn.bing.com/search',params=kw)
    print(r.url)
    #http://cn.bing.com/search?q=Python+dict
    print(r.text)

#可变长关键字参数
'''
python中的参数形式：
位置或关键字参数
仅位置参数
可变长位置参数 *argst
可变长关键字参数 **argst
（参数可以设置为默认值）
'''
def func1(args1,*argst,**argsd):
    print(args1)
    print(argst)
    print(argsd)
    
    
func1('hello,','Wangdachui','Niuyun','linling',a1=1,a2=2,a3=3)
#hello,
#('Wangdachui','Niuyun','linling')
#{'a1':1,'a2':2,'a3':3}
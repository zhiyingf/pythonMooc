#例一   中英文词频统计
#英文词频统计
import random

def englishCounter(sr):
    poemList=sr.split()
    pDict={}
    for item in poemList:
        if item[-1] in ',.!?\'"':
            item=item[:-1]
        '''
        if item not in pDict:
            pDict[item]=1
        else:
            pDict[item]+=1
        '''
        pDict[item]=pDict.get(item,0)+1
    return pDict

#例二  file.txt文件统计
def func(stuList):
    d={}
    for item in stuList:
        r=item.split('_')
        a,b=r[0],r[1].strip()#strip去掉尾部换行符
        if a not in d:
            d[a]=[b]
        else:
            d[a]+=[b]
    '''
    在字典中
    基于key排序：sorted(d.items(),key=lambda d: d[0])
    基于value排序：sorted(d.items(),key=lambda d: d[1])
    基于value后基于key排序：sorted(d.items(),key=lambda d: (d[1],d[0]))
    基于value值的个数排序(少到多)：sorted(d.items(),key=lambda d: len(d[1]))
    基于value值的个数排序(多到少)：sorted(d.items(),key=lambda d: len(d[1]),reverse=True)
    '''
    lst=sorted(d.items(),key=lambda d: len(d[1]),reverse=True)
    #print(d)
    #print(lst)
    return lst
def counter():
    try:
        with open(r'D:\pythonstudy\用python玩转数据（MOOC）\MOD_03\file.txt')as f:
            stuList=f.readlines()
    except FileNotFoundError:
        print('the file does not exist!')
    else:
        result=func(stuList)
        for item in result:
            print(item[0],'->',item[1])

#例三？？
def func1(data):
    clsNo=random.choice(list(data.keys()))#基于字典的键key随机产生班级号
    stuNo=random.randint(1,data[clsNo])#
    return "{} {:02}".format(clsNo,stuNo)
def setClass():
    data={'A001':32,'A002':47,'B001':39,'B002':42}
    result=set()#创建空集合
    while len(result)<10:
        result.add(func1(data))
    print(result)


def main():
    #print(englishCounter(input()))
    #counter()
    setClass()

if __name__ == "__main__":
    main()
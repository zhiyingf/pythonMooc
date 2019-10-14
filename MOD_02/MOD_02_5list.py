#list方法：
'''
append(),copy(),count(),extend(),index()
insert(),pop(),remove(),reverse(),sort()
'''
jScores=[9,9,8.5,10,7,8,8,9,8,10]
aScore=9
jScores.sort()
jScores.pop()
jScores.pop(0)
jScores.append(aScore)
aveScore=sum(jScores)/len(jScores)
print(aveScore)

#enumerate把列表list逐项加序号0：Monday  1:Tuesday  ....
week=['Monday','Tuesday','Wednesday','Thursday','Friday']
weekend=['Saturday','Sunday']
week.extend(weekend)
for i,j in enumerate(week):
    print(i+1,j)

#
numList=[3,11,5,8,16,1]
fruitList=['apple','banana','pear','lemon','avocado']
numList.sort(reverse=True)
fruitList.sort(key=len)
print(numList)
print(fruitList)

#列表解析
'''
[expression for expr in sequence1
            for expr2 in sequence2
            ......
            for exprN in sequenceN
            if condition]
'''
[x for x in range(10)]
[x**2 for x in range(10)]
[x**2 for x in range(10) if x**2<50]
[(x+1,y+1)for x in range(2) for y in range(2)]


#
def clean_list(lst):
    cleaned_list=[]
    for item in lst:
        for c in item:
            if c.isalpha()!=True:
                item=item.replace(c,'')
        cleaned_list.append(item)
    return cleaned_list
coffee_list=['32Latte','_American30','/34Cappuccino','Mocha35']
cleaned_list=clean_list(coffee_list)
for k,v in zip(range(1,len(cleaned_list)+1),cleaned_list):
    print(k,v)
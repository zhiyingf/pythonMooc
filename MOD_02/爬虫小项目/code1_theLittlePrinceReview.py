'''
https://book.douban.com/subject/1084336/comments/  只有20条短评
https://book.douban.com/subject/1084336/comments/hot?p=1
'''
'''
新加文件写入功能：将获取到的数据写入本地工作区间
'''
import requests,re,os,shutil
from bs4 import BeautifulSoup

#获取一个网页中的短评和评分
def getAll(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'lxml')
    comments=soup.find_all('div','comment')
    return comments
    
def main():
    #改变当前的工作目录，路径为D:\pythonstudy\用python玩转数据（MOOC）\MOD_02\爬虫小项目
    os.chdir(r'D:\pythonstudy\用python玩转数据（MOOC）\MOD_02\爬虫小项目')
    if os.path.exists('./output'):
        shutil.rmtree('./output')#rmtree递归的删除目录
    os.mkdir('./output')#mkdir用于创建目录

    if os.path.exists('output/theLittlePrinceReview.txt'):
        os.remove('output/theLittlePrinceReview.txt')
    else:
        open('output/theLittlePrinceReview.txt','w')

    commentAll=[]

    for i in range(1,4):
        url='https://book.douban.com/subject/1084336/comments/hot?p={}'.format(str(i))
        commentAll.extend(getAll(url))
    #print(len(commentAll))
    commentAll=commentAll[0:50]
    comments=[]
    stars=[]
    pattern_s=re.compile('<span class="user-stars allstar(.*) rating"')
    sum=0
    for x,y in enumerate(commentAll):
        short=y.p.span.string
        comments.extend(short)
        p=re.findall(pattern_s,str(y))
        stars.extend(p)
        if p==[]:
            s1='用户{}：\n短评：{}\n评分为：无\n\n'.format(x+1,short)
        else:
            s1='用户{}：\n短评：{}\n评分为：{}\n\n'.format(x+1,short,p[0])
        with open('output/theLittlePrinceReview.txt','a',encoding='utf-8')as f:
            f.writelines(s1)
        
    for i in stars:
        sum+=int(i)
    ave=sum//len(stars)
    s1="平均评分为:{:.0f}\n".format(ave)
    with open('output/theLittlePrinceReview.txt','a',encoding='utf-8') as f:
        f.writelines(s1)

if __name__ == "__main__":
    main()








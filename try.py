#深入了解BeautifulSoup
from bs4 import BeautifulSoup
import lxml
import requests

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup=BeautifulSoup(html,'lxml')
#print(soup.prettify())#soup.prettify()  #打印 soup 对象的内容，格式化输出
print(soup.title)
print(soup.head)
print(type(soup))
print(type(soup.title))
print(type(soup.find_all('p','title')))
print(soup.find_all('p','title'))

def getAll(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'lxml')
    Comments=soup.find_all('div','commend')
    print(Comments)
    return compile
    
# shortAll=[]

for i in range(1,4):
    url='https://book.douban.com/subject/1084336/comments/hot?p={}'.format(str(i))
    short=getAll(url)
    # shortAll.extend(short)




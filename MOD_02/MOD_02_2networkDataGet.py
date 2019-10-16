#网络数据获取（爬取）：抓取网页，解析网页内容
'''
抓取：c----s  request respond 解析
urllib内建模块 --urllib.request
Requests第三方库 中小型网络爬虫开发
Scrapy框架 大型

解析
BeautifulSoup库
re模块

第三方库：抓取+解析


豆瓣爬虫协议查看：https://www.douban.com/robots.txt

url get发送请求，然后获得一个Response对象，这个对象包含Request请求信息和服务器response响应信息,
request会自动解码来自服务器的信息：网页格式json格式（r.json()）、二进制格式(r.content())
r.text(),r.encoding(utf-8)
'''
'''
import requests
r=requests.get('https://book.douban.com/subject/3218539/')
#r.status_code
#r.text
'''
#获取的是二进制，保存数据
'''
import os
import requests
import shutil
os.chdir(r'd:\pythonstudy\workdir')
if os.path.exists('../output'):
    shutil.rmtree('../output')
os.mkdir('../output')
r=requests.get('https://www.baidu.com/img/bd_logo1.png')
with open('../output/baidu.png','wb')as fp:
    fp.write(r.content)
'''

#为了反爬
'''
为了反爬，有些网站会对Headers的User-Agent进行检测，需将headers信息传递给get函数的headers参数，
例如知乎，直接访问会返回400，加上headers参数后可正确返回：
re = requests.get('https://www.zhihu.com')
re.status_code

# headers可从http测试网站https://httpbin.org或浏览器的“开发者工具”获得
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11"}
re = requests.get('https://www.zhihu.com', headers = headers)
re.status_code

'''



#BeautifulSoup解析抓取的网页
'''
HTML选择解析器---lxml
'''
'''
from bs4 import BeautifulSoup
ma='<p class="title"><b>The Little Prince</b></p>'
soup=BeautifulSoup(ma,"lxml")
#BeautifulSoup对象有四种：tag(html中的标签),NavigableString(Tag中的字符串),BeautifulSoup,Comment(子类)
print(soup.p)
print(type(soup.p))
tag=soup.p
print(tag.name)
print(tag.attrs)
print(tag['class'])
print(tag.string)
print(type(tag.string))
print(soup.find_all('b'))#find_all查找对象中b标签中的内容
'''

#爬取小王子短评，并写入文件
'''
import os
import requests
from bs4 import BeautifulSoup
os.chdir('d:/pythonstudy/workdir')
print(os.getcwd())
r=requests.get('https://book.douban.com/subject/1084336/comments/')
soup=BeautifulSoup(r.text,'lxml')
pattern=soup.find_all('span','short')
i=0
with open('小王子短评.txt','w')as f:
    for item in pattern:
        i+=1
        f.writelines(str(i)+item.string+'\n')
'''


#获取豆瓣评分
'''
这种比较细节内容的获取比较适合于正则表达式来处理
正则表达式通常用来检索替换符合某个规则或者模块的文本
<span class="comment-info">
    <a href="https://www.douban.com/people/sweetmm/">黛安Diane</a>
        <span class="user-stars allstar50 rating" title="力荐"></span>
            <span>2009-12-22</span>
</span>

[0-9]  .  *  

{.*}
把字符串编译成pattern实例，执行速度更快
'''

import requests
from bs4 import BeautifulSoup
import re
s=0
r=requests.get('https://book.douban.com/subject/1084336/comments/hot?p={}'.format(str(1)))
soup=BeautifulSoup(r.text,'lxml')
print(type(r.text))
pattern=soup.find_all('span','short')
# for item in pattern:
#     print(item.string)
pattern_s=re.compile('<span class="user-stars allstar(.*) rating"')
p=re.findall(pattern_s,r.text)
print(p)
for star in p:
    s+=int(star)
    #print(s)
print(s)

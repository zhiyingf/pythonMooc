'''
<figcaption><a>....</a></figcaption>
<td>(.*?)</td>\s+<td class="table-td-bold">(.*?)</td>\s+<td class="table-td-rightborder">(.*?)</td>
'''
import re
import requests
from bs4 import BeautifulSoup
r=requests.get('http://www.volleyball.world/en/vnl/2018/women/results-and-ranking/round1')
soup=BeautifulSoup(r.text,'lxml')
tames_fig=soup.find_all('figcaption')
pattern_s=re.compile('<td>(.*?)</td>\s+<td class="table-td-bold">(.*?)</td>\s+<td class="table-td-rightborder">(.*?)</td>')
p=re.findall(pattern_s,r.text)

all=[]
for x,y in enumerate(tames_fig):
    tame=y.a.string
    all.append([tame,p[x]])
    print(x+1,'TAEM:{},MATCHE:{}'.format(tame,p[x]))
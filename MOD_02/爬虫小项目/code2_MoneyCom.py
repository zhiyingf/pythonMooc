'''
<td class="wsod_firstCol"><a href="/quote/quote.html?symb=MMM" class="wsod_symbol">MMM</a>&nbsp;<span title="3M">3M</span></td>
<td class="wsod_aRight"><span stream="last_202757" class="wsod_stream">158.10</span></td>

<td class="wsod_firstCol"><a href="/quote/quote.html?symb=AXP" class="wsod_symbol">AXP</a>&nbsp;<span title="American Express">American Express</span></td>
<td class="wsod_aRight"><span stream="last_55991" class="wsod_stream">116.40</span></td>
'''
import unicodedata,re,requests,os,shutil
from bs4 import BeautifulSoup
def main():

    os.chdir(r'D:\pythonstudy\用python玩转数据（MOOC）\MOD_02\爬虫小项目')
    if os.path.exists('./output')==False:
        os.mkdir('./output')#mkdir用于创建目录

    if os.path.exists('output/moneyCom.txt'):
        os.remove('output/moneyCom.txt')
    else:
        open('output/moneyCom.txt','w')


    r=requests.get('https://money.cnn.com/data/dow30/')
    soup=BeautifulSoup(r.text,'lxml')
    codeCom=soup.find_all('td','wsod_firstCol')
    price=soup.find_all('span','wsod_stream')
    all=[]
    for x,y in enumerate(codeCom):
        code=y.a.string
        com=y.span.string
        pri=price[x*3].string
        all.append([code,com,pri])
        s1='{:0>2d} 代码：{}，公司名称：{}，成交价：{}\n'.format(x+1,code,com,pri)
        with open('output/moneyCom.txt','a+') as f:
            f.writelines(s1)

if __name__ == "__main__":
    main()
    
#print(all)


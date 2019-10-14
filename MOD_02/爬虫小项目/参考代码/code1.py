# -*- coding: utf-8 -*-
"""
Comments parsing
@author: Dazhuang
"""
import requests, re, time
from bs4 import BeautifulSoup
count = 0
i = 0
s, count_s, count_del = 0, 0, 0
lst_stars = []
while count < 50:
    try:
        r = requests.get('https://book.douban.com/subject/bookid/comments/hot?p=' + str(i+1))
    except Exception as err:
        print(err)
        break
    soup = BeautifulSoup(r.text, 'lxml')
    comments = soup.find_all('span', 'short')
    pattern = re.compile('<span class="user-stars allstar(.*?) rating"')
    # Other way: we can use a whole regular expression to pattern comments and rangking stars
    p = re.findall(pattern, r.text)
    for item in comments:
        count += 1
        if count > 50:
        # count the number of comments more than 50 of the page
            count_del += 1
        else:
            print(count, item.string)
    for star in p:
        lst_stars.append(int(star))
        time.sleep(5) # delay request from douban's robots.txt
        i += 1
    for star in lst_stars[:-count_del]: # calculate the rating star of 50 comments
        s += int(star)
if count >= 50:
    print(s // (len(lst_stars)-count_del))
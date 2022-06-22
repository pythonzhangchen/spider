# -*- coding: utf-8 -*-
# @Time : 2022/6/15 18:29 
# @Author : chen.zhang 
# @File : spilder-moive-1.py
import requests
from bs4 import BeautifulSoup

# url = 'https://www.1905.com/pinglun/'
#
# res = requests.get(url=url)
# res.encoding = 'utf-8'
# print(res.text)
with open('moive.html', 'r', encoding='utf-8') as r:
    content = r.read()

soup = BeautifulSoup(content, 'lxml')
# info = soup.find_all(name='div', attrs={'class': 'comment-list'})[0].find_all('li')
info = soup.select('.comment-list>ul li')

for li in info:
    print('*' * 100)
    title = li.select('li>a')[0].attrs['title']
    detail_page_link = li.select('li>a')[0].attrs['href']
    img = li.select('li>a>img')[0].attrs['src']
    abstract_text = li.select('li>.list-txt>.txt-abstract')[0].text

    print(title, detail_page_link, img, abstract_text)
    print('#' * 100)


url = 'https://www.1905.com/coll/newslist/pingluninfo_2.json'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

param = {
    't': '1655290800',
    'callback': 'successgetall',
}

res = requests.get(url=url, params=param, headers=header).text.split('(')[1].split(')')[0]
# res.encoding = 'utf-8'
# print(eval(res))
for x in eval(res)['info']:
    # print(x)
    print(x['title'], x['description'], x['thumb'], x['url'], sep=' ## ')

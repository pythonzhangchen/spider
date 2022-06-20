# -*- coding: utf-8 -*-
# @Time : 2022/6/13 17:12 
# @Author : chen.zhang 
# @File : basicSKill_lxml.py
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as r:
    content = r.read()

soup = BeautifulSoup(content, 'lxml')

## 指明道姓
res_1 = soup.find_all(name='a')
print(res_1)
for x in res_1:
    print(x.text,'***********', x.attrs['href'])

## 叠加提取】
res_2 = soup.find_all(name='div', attrs={'class': 'others'})
print(res_2)
final_2 = res_2[0].find_all(name='a')
print(final_2)
for x in final_2:
    print(x.text,'***********', x.attrs['href'])

##路径法则
res_3 = soup.select('#_others>ul>li>a')
print(res_3)

## 路径法则 跳级路径
res_4 = soup.select('#_others>ul a')
print(res_4)

## 路径法则 锁定属性的标签可以出现在路径的任何位置
res_5 = soup.select('html .others>ul a')
print(res_5)

## 路径法则 锁定属性的标签可以出现在路径的任何位置
res_6 = soup.select('html div>ul a')
print(res_6)
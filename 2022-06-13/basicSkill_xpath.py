# -*- coding: utf-8 -*-
# @Time : 2022/6/13 17:30 
# @Author : chen.zhang 
# @File : basicSkill_xpath.py
from lxml import etree

with open('index.html','r',encoding='utf-8') as r:
    content= r.read()

tree = etree.HTML(content)

# 案例一
res_1 = tree.xpath('/html/head/title')
print(res_1)
print(res_1[0].text)

# 案例二 基于属性定位
res_2 = tree.xpath('/html/body/div[@class="others"]')
print(res_2)

# 案例三 获取元素后数字定位
res_3 = tree.xpath('/html/body/div[@class="others"]/ul/li')
print(res_3)
# 那么何如继续按照这个逻辑向下找呢？ 因为li里还有 a   a是我们的终极目标
for li in res_3:
    a_res=li.xpath('./a/@href')
    print(a_res)

# 案例四 跳级式定位 即从某个标签开始向下看 所有层级满足条件
res_5 = tree.xpath('/html//div[@class="others"]//a')
print(res_5)
for x in res_5:
    print(x.text)
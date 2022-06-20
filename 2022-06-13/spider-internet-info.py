# -*- coding: utf-8 -*-
# @Time : 2022/6/13 17:55 
# @Author : chen.zhang 
# @File : spider-internet-info.py
import requests
import re
from bs4 import BeautifulSoup
from lxml import etree

# 互联网数据咨询

url = 'http://www.199it.com/archives/category/service/cloud-computing'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                  'Safari/537.36 '
}

res = requests.get(url=url, headers=header)
res.encoding = 'utf-8'
# print(res.text)
#
# TODO 正则
patt = '<div class="post-img"><div itemprop="image" itemscope="" itemtype=".*?" class="post-thumb"><a href="(.*?)" title="(.*?)"><img itemprop="url" src="(.*?)" class="attachment-post-thumbnail wp-post-image" alt=".*?"></a> <meta itemprop="width" content="228"><meta itemprop="height" content="152"></div></div>'
res1 = re.findall(pattern=patt, string=res.text, flags=re.S)
print(res1)
# for x in res1:
#     print(x[0], x[1], x[2])

# TODO bs4+lxml
soup = BeautifulSoup(markup=res.text,features='lxml')
res_2 =soup.find_all(name='article', attrs={'class':'newsplus'})
for x in res_2:
    # print(x.find_all(name='a'))
    print(x.find_all(name='a')[0].attrs['href'])
    print(x.find_all(name='a')[0].attrs['title'])
    print(x.find_all(name='img')[0].attrs['src'])

# TODO etree+xpath

tree = etree.HTML(res.text)

res_3_titles_links = tree.xpath('//*[@id="content"]/article//div[@itemprop="image"]/a')
print(res_3_titles_links)
for x in res_3_titles_links:
    title = x.xpath('@title')
    links = x.xpath('@href')
    srcs = x.xpath('./img/@src')
    print(title,links,srcs)
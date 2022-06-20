# -*- coding: utf-8 -*-
# @Time : 2022/6/14 16:04 
# @Author : chen.zhang 
# @File : spilder-security-info.py
import requests
from bs4 import BeautifulSoup
from lxml import etree
import re

url = 'http://www.csrc.gov.cn/chongqing/c104815/c3446627/content.shtml'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                  'Safari/537.36 '
}
res = requests.get(url=url, headers=header)
res.encoding = 'utf-8'

# print(res.text)
# TODO 正则
patt ='<tr height=".*?" style=".*?">(.*?)</tr>'
patt_1 ='<td style="padding-top:1px;padding-left:1px;padding-right:1px;color:#000000;font-size:12.0pt;font-weight:400;font-style:normal;text-decoration:none;font-family:DengXian;border:none;text-align:general;vertical-align:bottom;white-space:nowrap.*?">(.*?)</td>'
list = []
res_1= re.findall(pattern=patt,string=res.text,flags=re.S)
# print(res_1)
# print(len(res_1))
for x in range(len(res_1)-1):
    res_2=re.findall(pattern=patt_1,string=res_1[x+1],flags=re.S)
    list.append(tuple(res_2))
for x in list:
   print(x)

# TODO bs4 lxml
soup =BeautifulSoup(markup=res.text,features='lxml')
res_2 = soup.select('.detail-news>table tr')
# print(res_2)
# for index,x in enumerate(res_2):
#     # print(index,'*************',x)
#     lower_level = x.select('td')
#     print(lower_level)
for x in res_2[1:len(res_2)]:   # 注意这里得列表提取长度
    print('*****************')
    td_level=x.select('td')
    stock_id = td_level[0].text
    stock_code = td_level[1].text
    stock_title = td_level[2].text
    stock_company = td_level[3].text
    stock_addr = td_level[4].text
    stock_z_company = td_level[5].text
    stock_date = td_level[6].text
    print(stock_id,stock_code,stock_title,stock_company,stock_addr,stock_z_company,stock_date)

# TODO etree+xpath

tree = etree.HTML(res.text)
res_3 = tree.xpath("//*[@class='detail-news']/table/tbody/tr")
for x in res_3[1:len(res_3)]:
    td = x.xpath('./td')
    stock_id = td[0].text
    stock_code = td[1].text
    stock_title = td[2].text
    stock_company = td[3].text
    stock_addr = td[4].text
    stock_z_company = td[5].text
    stock_date = td[6].text
    print(stock_id, stock_code, stock_title, stock_company, stock_addr, stock_z_company, stock_date)
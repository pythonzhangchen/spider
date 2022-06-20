# -*- coding: utf-8 -*-
# @Time : 2022/6/6 17:21 
# @Author : chen.zhang 
# @File : L1_get.py
import requests

url = 'https://www.baidu.com/s?wd=万门大学&rsv_spt=1&rsv_iqid=0xb8b92cfc00116697&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8' \
      '&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=21&rsv_sug1=14&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=4373' \
      '&rsv_sug4=676686'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                  'Safari/537.36'}

res = requests.get(url=url, headers=header)

res.encoding = 'utf-8'

print(res.text)

with open('aaa.html', 'a', encoding='utf-8') as add:
    add.write(res.text)

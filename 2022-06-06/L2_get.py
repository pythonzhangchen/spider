# -*- coding: utf-8 -*-
# @Time : 2022/6/8 16:14 
# @Author : chen.zhang 
# @File : L2_get.py
import requests

# 头条案例

url = 'https://www.toutiao.com/api/search/content/'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                   'Safari/537.36 '
}

params = {
    'aid': 24,
    'app_name': 'web_search',
    'affset': '100',
    'format': 'json',
    'keyward': '泰山',
    'autoload': 'true',
    'count': '20',
    'en_ac': '1',
    'cur_tab': '1',
    'form': 'seach_tab',
    'pd': 'synthesis',
    'timestamp': '1608479020632'
}

res=requests.get(url=url,params=params,headers=header)
# print(res.text)

for x in res.json()['log_pb']:
    print(x)

# -*- coding: utf-8 -*-
# @Time : 2022/6/6 18:19 
# @Author : chen.zhang 
# @File : L1_get.py
import requests

url = 'https://www.baidu.com/s'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                  'Safari/537.36'}
params = {
    'wd': '万门大学',
    'rsv_sug1': '10',
    'rsv_sug7': '101',
}
res = requests.get(url=url, headers=header, params=params)

res.encoding = 'utf-8'

print(res.text)

with open('index.html', 'a', encoding='utf-8') as add:
    add.write(res.text)

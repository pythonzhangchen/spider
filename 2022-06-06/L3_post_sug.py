# -*- coding: utf-8 -*-
# @Time : 2022/6/8 17:36 
# @Author : chen.zhang 
# @File : L3_post_stu.py
import requests

#  百度翻译
url = 'https://fanyi.baidu.com/sug'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                  'Safari/537.36 '
}

data = {
    'kw': 'good'
}

res = requests.put(url=url, headers=header, data=data).json()
# print(res)

for x in res['data']:
    print(x)

# 搜狗翻译

url = 'https://fanyi.sogou.com/reventondc/suggV3'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                  'Safari/537.36 '
}

data = {
    'from': 'auto',
    'to': 'en',
    'client': 'web',
    'text': '中国',
    'uuid': '982bbe24-8bb4-4755-a2c9-d81a32c1ea58',
    'pid': 'sogou-dict-vr',
    'addSugg': 'on',
}

res = requests.put(url=url, data=data, headers=header).json()
print(res)
#
# for x in res.json()['sugg']:
#     print(x)

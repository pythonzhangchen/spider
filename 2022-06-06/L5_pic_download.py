# -*- coding: utf-8 -*-
# @Time : 2022/6/10 18:08 
# @Author : chen.zhang 
# @File : L5_pic_download.py
import requests

url = 'https://image.baidu.com/search/acjson'

header = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'image.baidu.com',
    'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDIsNiwxLDQsNSw4LDcsOQ%3D%3D&word=%E8%BE%B9%E5%A2%83%E7%89%A7%E7%BE%8A%E7%8A%AC',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

params = {
    'tn': 'resultjson_com',
    'logid': '8209532581992279463',
    'ipn': 'rj',
    'ct': '201326592',
    'is': '',
    'fp': 'result',
    'fr': '',
    'word': '边境牧羊犬',
    'queryWord': '边境牧羊犬',
    'cl': '2',
    'lm': '-1',
    'ie': 'utf-8',
    'oe': 'utf-8',
    'adpicid': '',
    'st': '',
    'z': '',
    'ic': '',
    'hd': '',
    'latest': '',
    'copyright': '',
    's': '',
    'se': '',
    'tab': '',
    'width': '',
    'height': '',
    'face': '',
    'istype': '',
    'qc': '',
    'nc': '1',
    'expermode': '',
    'nojc': '',
    'isAsync': '',
    'pn': '90',
    'rn': '20',
    'gsm': '5a',
}

res = requests.get(url=url, params=params, headers=header)
for x in res.json()['data']:
    if len(x) == 0:
        pass
    else:
        print(x['thumbURL'])
        img = requests.get(url=x['thumbURL']).content   #content  以二进制返回
        filename = x['thumbURL'].split('/')[-1].split('?')[0]
        with open('images/%s' % filename+'.jpg', 'wb') as w:
            w.write(img)

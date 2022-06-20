# -*- coding: utf-8 -*-
# @Time : 2022/6/10 16:27 
# @Author : chen.zhang 
# @File : L4_post_login.py
import requests

# url = 'http://www.ppcam.con/admin/login/'
#
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
#                   'Safari/537.36 ',
#     'Cookie': 'csrftoken=Yd8BbmTZ0OaOJMRPqa48aCiKfxquB8dAtlPCQ1hFsRr0ZAoFkNG5s16Nh6xy76XY'
# }
#
# data = {
#     'username': 'zhangchen',
#     'password': '123456',
#     'csrfmiddlewaretoken': 'CC6EgnpXZ1ayMosI7DSHS4UgryBN6ipQ7KNFV2NDr4rK2cZy1guEatIjt7SRCg9e',
#     'next': '/admin/',
# }

# 测试登录是否成功
# res = requests.post(url=url, data=data, headers=header)
# res.encoding='utf-8'
# print(res.text)

# 后台内部单独访问
# url = 'http://www.ppcam.cn/admin/PowerApp/photos/'
# res = requests.get(url=url)
# print('@@@@@@@@@@' * 10)
# print(res.text)


# session 联合登录
url = 'http://www.ppcam.con/admin/login/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                  'Safari/537.36 ',
    'Cookie': 'csrftoken=Yd8BbmTZ0OaOJMRPqa48aCiKfxquB8dAtlPCQ1hFsRr0ZAoFkNG5s16Nh6xy76XY'
}

data = {
    'username': 'zhangchen',
    'password': '123456',
    'csrfmiddlewaretoken': 'CC6EgnpXZ1ayMosI7DSHS4UgryBN6ipQ7KNFV2NDr4rK2cZy1guEatIjt7SRCg9e',
    'next': '/admin/',
}

sess = requests.Session()

res =sess.post(url=url,headers=header,data=data)
print(res.text)

url = 'http://www.ppcam.con/admin/PowerAPP/setupsd/'
res1 = sess.get(url=url)
print(res1.text)
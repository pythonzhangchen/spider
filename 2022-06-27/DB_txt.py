# -*- coding: utf-8 -*-
# @Time : 2022/6/27 15:52 
# @Author : chen.zhang 
# @File : DB_txt.py

infomation = [
    ['mike4', 40, 'wanmen'],
    ['mike2', 20, 'wanmen'],
    ['mike1', '30', ''],
]

# with open('1.txt', 'a', encoding='utf-8') as add:
#     for x in infomation:
#         add.write(str(x) + '\n')


with open('1.txt','r',encoding='utf-8') as r:
    for i in r.readlines():
        print(eval(i))
        print(type(eval(i)))
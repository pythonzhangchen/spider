# -*- coding: utf-8 -*-
# @Time : 2022/6/13 16:35 
# @Author : chen.zhang 
# @File : basicSkill_re.py
import re

with open('index.html', 'r', encoding='utf-8') as r:
    content = r.read()

# 方式1 课程名字 li标签的a标签
patt1 = r'<li><a.*?href=".*?">(.*?)</a></li>'
res1 = re.findall(pattern=patt1, string=content, flags=re.S)
print(res1)

# 方式2 p标签中的课程名字  双正则搭配 使用
# **第一级
patt2 = r'<div class="general">(.*?)</div>'
res2 = re.findall(pattern=patt2, string=content, flags=re.S)
print(res2)
# **第二级
patt2_1 = '<p>(.*?)</p>'
res2_1 = re.findall(pattern=patt2_1, string=res2[0], flags=re.S)
print(res2_1)


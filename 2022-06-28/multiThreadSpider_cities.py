# -*- coding: utf-8 -*-
# @Time : 2022/7/18 18:23 
# @Author : chen.zhang 
# @File : multiThreadSpider_cities.py
import requests
from lxml import etree
import sqlite3

conn = sqlite3.connect('cities.db')
c = conn.cursor()

# c.execute('''CREATE TABLE
# CITIES (city_name,city_links)
# ''')
#
# conn.commit()

res =requests.get('https://cq.fang.ke.com/loupan/pg1/')
tree = etree.HTML(res.text)
city = tree.xpath('/html/body/div[2]/div[3]//a')  #  //  不按照级别a标签全部要
total_city = []
for x in city:
    total_city.append([x.text,x.xpath('@href')[0].split('//')[-1]])

print(total_city)

c.executemany("INSERT INTO cities VALUES (?,?)",total_city)
conn.commit()
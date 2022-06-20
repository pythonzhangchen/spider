# -*- coding: utf-8 -*-
# @Time : 2022/6/2 14:38 
# @Author : chen.zhang 
# @File : git_city_distance.py
import pymysql

db = pymysql.connect(host="localhost", user="root", password="123456", database="ZZBase", port="3306", charset="utf8")
cursor = db.cursor()

cityA = input('请输入第一个城市')
cityB = input('请输入第二个城市')
sql = "SELECT * FROM cities WHERE CityA like '%%%%%%s%%%%%' and CityB like '%%%%%%s%%%%%'" % (str(cityA), str(cityB))

cursor.execute(sql)
res = cursor.fetchone()

print(res)

db.close()


# -*- coding: utf-8 -*-
# @Time : 2022/6/27 17:38 
# @Author : chen.zhang 
# @File : DB_sqlite3.py
import sqlite3

conn = sqlite3.connect('my_data.db')

c = conn.cursor()

# 创建表
c.execute('''CREATE TABLE info
                (name,age,school)''')
conn.commit()

c.execute('ALTER TABLE info ADD date')
conn.commit()

infomation = [
    ['mike4',40,'wanmen'],
    ['mike4',20,'wanmen'],
    ['mike4',"30",''],
    ['mike4',"45",'wanmen123123123'],
]
c.executemany('INSERT INTO info VALUES (?,?,?)', infomation)
conn.commit()

# 单数据添加
name = 'hike'
age = 50
school = 'wanmendaxue'
c.execute('INSERT INTO info VALUES ("%s","%s","%s")'%(name,age,school))
conn.commit()

# 数据查询

for row in c.execute('SELECT * FROM info'):
    print(row)

# 待条件查询
for row in c.execute('SELECT * FROM info WHERE age>"30"'):
    print(row)

# -*- coding: utf-8 -*-
# @Time : 2022/7/18 16:58 
# @Author : chen.zhang 
# @File : multiThreadSpider_stage_1.py
from threading import Thread

import requests
from bs4 import BeautifulSoup
import time


# 图下载
def photo_download(link):
    img = requests.get(link).content
    with open('images/%s' % link.split('/')[-1], 'wb') as w:
        w.write(img)


def total_page_check():
    res = requests.get(url='https://cq.fang.ke.com/loupan/pg1/')
    soup = BeautifulSoup(res.txt, 'lxml')
    total = soup.select('.page-box')[0].attrs['data-total-count']

    # 判断为整数
    total_info = int(total) / 10
    if str(total_info).split('.')[-1] == '0':
        total_page = int(total) / 10
    else:
        total_page = int(total) / 10 + 1
    print('总数据量', total)
    return int(total_page)


# 任务分配机制
def task_distribution_policy(total):
    a = total[0:int(len(total)) / 2]
    b = total[int(len(total)) / 2:]
    return a, b


# 总任务量
def task_distribution_deploy():
    total_pages = total_page_check()
    total_task = []
    for page in range(total_pages):
        total_task.append('https://cq.fang.ke.com/loupan/pg%s/' % str(page + 1))
    print(total_task)
    print(len(total_task))
    return total_task  # 返回全部任务列表-所有需要访问的地址


# 线程具体任务
def spider(urls):
    global pages_total
    for url in urls:
        print('@link>>>>>', url)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        main_data_list = []
        main_target = soup.select('.resblock-list')
        for x in main_target:
            temp_list = []

            temp_list.append(current_city)

            estate = x.select('.name')[0].text
            temp_list.append(estate)

            price = x.select('.number')[0].text
            temp_list.append(price)

            address = x.select('.resblock-location')[0].text
            temp_list.append(address)

            condition = x.select('.resblock-name span')[0].text
            temp_list.append(condition)

            type = x.select('.resblock-name span')[1].text
            temp_list.append(type)

            img_link = x.select('a>img')[0].attrs['data-original']
            temp_list.append(img_link)
            photo_download(img_link)

            unit = x.select('.desc')[0].text
            temp_list.append(unit.strip())

            main_data_list.append(temp_list)
        print(main_data_list)
        print('本页爬取数据量*********', len(main_data_list))
        pages_total += len(main_data_list)


if __name__ == '__main__':
    page_total = 0
    current_city = '重庆'
    total_task = task_distribution_deploy()
    task1, task2 = task_distribution_policy(total_task)
    # 多线程启动
    start = time.time()
    t1 = Thread(target=spider, args=(task1,))
    t2 = Thread(target=spider, args=(task2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    time_consumed = time.time() -start
    print(time_consumed)
    print(page_total)
    print('任务完成')

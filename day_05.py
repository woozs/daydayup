# -*- coding: utf-8 -*-
# @Time    : 2018/6/17 10:22
# @Author  : mrwuzs
# @Email   : mrwuzs@163.com
# @File    : day_05.py
# @Software: PyCharm

# coding=utf-8
from bs4 import BeautifulSoup
def sechBodyUrl(path):
    url = []
    with open(path,encoding='utf-8') as fp:
        text = BeautifulSoup(fp, 'lxml')
        urls = text.findAll('a')
        for u in urls:
            url.append(u['href'])
        content = text.get_text().strip('\n')
    return content,url

print(sechBodyUrl('test.html'))
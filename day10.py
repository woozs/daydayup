# -*- coding: utf-8 -*-
# @Time    : 2018/6/24 10:54
# @Author  : mrwuzs
# @Email   : mrwuzs@163.com
# @File    : day10.py
# @Software: PyCharm


import json
from collections import OrderedDict
import xlwt
#获取一个有序字典
with open('number.txt',encoding='utf-8') as f:
    content =f.read()
    students_dict = json.loads(content, object_pairs_hook=OrderedDict)
    print(students_dict)

wb = xlwt.Workbook()  #创建一个工作簿
ws = wb.add_sheet('number') #创建一个sheet
for row , i in enumerate(students_dict):
    for col, j in enumerate(i):
        ws.write(row,col,j)

wb.save('number.xls')
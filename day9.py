# -*- coding: utf-8 -*-
# @Time    : 2018/6/24 10:43
# @Author  : mrwuzs
# @Email   : mrwuzs@163.com
# @File    : day9.py
# @Software: PyCharm

import json
from collections import OrderedDict
import xlwt
#获取一个有序字典
with open('city.txt',encoding='utf-8') as f:
    students_dict = OrderedDict(json.load(f))
    print(students_dict.items())

wb = xlwt.Workbook()  #创建一个工作簿
ws = wb.add_sheet('city') #创建一个sheet

row = 0
for k,v in students_dict.items():#items(返回由“键值对组成元素“的列表)

    ws.write(row,0,k)
    ws.write(row,1,v)
    row+=1
wb.save('city.xls')  #
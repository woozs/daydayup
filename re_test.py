# -*- coding: utf-8 -*-
# @Time    : 2018/6/17 18:22
# @Author  : mrwuzs
# @Email   : mrwuzs@163.com
# @File    : re_test.py
import re#

def re_split():
    str1 = "iii444abcddk12sdf98adsf000ppp"
    re_split_result = re.split('\d+', str1, maxsplit=0)
    print(re_split_result)  # ['iii', 'abcddk', 'sdf', 'adsf', 'ppp']

    re_split_result = re.split('\d+', str1, maxsplit=2)
    print(re_split_result)  # ['iii', 'abcddk', 'sdf98adsf000ppp']


re_split()
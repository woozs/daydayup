#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/23 22:34 
# @Author : wuzushun 
# @File : re_phonenumber.py
import re


def main():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    #(?<=exp)匹配exp后面的
    #（？=exp）匹配exp前面的
    sentence="""重要的事情说7813071089287，我的电话号码是：15516271232，不是13219929332，也不是110或者119，王大锤的手机是15890168992
    """
    mylist = re.findall(pattern,sentence)
    print(mylist)
    print("------------------------------华丽的分割线----------------------")
    for temp in pattern.finditer(sentence):
        #返回string中所有与pattern相匹配的全部字串，返回形式为迭代器。
        print(temp.group())
    print('------------------------------华丽的分割线----------------------')
    m = pattern.search(sentence)
    #若string中包含pattern子串，则返回Match对象，否则返回None，注意，如果string中存在多个pattern子串，只返回第一个。
    while m:
        print(m.group())
        m = pattern.search(sentence,m.end())


if __name__ == '__main__':
    main()
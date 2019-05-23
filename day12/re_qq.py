#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/23 22:27 
# @Author : wuzushun 
# @File : re_qq.py
import re


def main():
    usaname = input("请输入用户名:")
    qq =  input("请输入qq号码:")
    m1 =  re.match(r'^[0-9a-zA-Z]]{6,20}',usaname)
    if not m1:
        print("请输入有效的用户名:")
    m2 =  re.match(r'^[1-9]\d{4,10}$',qq)
    if not  m2:
        print("请输入有效的qq号:")
    if m1 and m2 :
        print("你输入的信息有效!")

if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/24 21:59 
# @Author : wuzushun 
# @File : computingintensive.py
from time import time


def main():
    totle = 0
    number_list = [x for x in range(1,100000001)]
    start = time()
    for number in number_list:
        totle += number
    print(totle)
    end=time()
    print("耗时%.fs"%(end-start))


if __name__ == '__main__':
    main()
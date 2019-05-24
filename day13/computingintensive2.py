#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/24 22:03
# @Author : wuzushun
# @File : computingintensive2.py
from multiprocessing import  Process,Queue
from random import randint
from time import time


def task_handler(curr_list,result_queue):
    totle = 0
    for number in curr_list:
        totle += number
    result_queue.put(totle)


def main():
    processes = []
    number_list = [x for x in range(1,100000001)]
    result_queue = Queue()
    index = 0
    for _ in range(8):
        p = Process(target=task_handler(),args=(number_list[index:index+12500000],result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    start = time()
    for p in processes:
        p.join()
    total = 0
    while not  result_queue.empty():
        total += result_queue
    print(total)
    end = time()
    print("耗时%.f s"%(end-start),sep='')


if __name__ == '__main__':
    main()
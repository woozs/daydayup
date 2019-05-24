#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/24 20:47 
# @Author : wuzushun 
# @File : superprocess01.py
from multiprocessing import Process
from time import time,sleep

counter = 0


def sub_task(string):
    global  counter
    while counter < 10:
        print(string,end=' ',flush=True)
        counter += 1
        sleep(0.01)

def main():
    Process(target=sub_task,args=('ping',)).start()
    Process(target=sub_task,args=('pong',)).start()

if __name__ == '__main__':
    main()

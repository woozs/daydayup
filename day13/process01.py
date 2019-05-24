#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/24 20:33 
# @Author : wuzushun 
# @File : process01.py
from multiprocessing import Process
from  os import  getpid
from random import randint
from time import  time,sleep


def download_task(filename):
    print('启动下载进程，进程号[%d]。'% getpid())
    print('开始下载%s...........'%filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成，耗费%d秒'%(filename,time_to_download))


def main():
    start = time()
    p1 =  Process(target=download_task,args=('笑傲江湖.pdf',))
    p1.start()
    p2 =  Process(target=download_task,args=('东京热.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('共耗时：%.2f秒'%(end-start))

if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/24 20:58 
# @Author : wuzushun 
# @File : thread01.py
from random import randint
from  threading import Thread
from  time import time,sleep


def download(filename):
    print('开始下载文件%s........'%filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成，耗费%d秒'%(filename,time_to_download))


def main():
    start = time()
    p1 = Thread(target=download, args=('笑傲江湖.pdf',))
    p1.start()
    p2 = Thread(target=download, args=('东京热.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('共耗时：%.2f秒' % (end - start))

if __name__ == '__main__':
    main()

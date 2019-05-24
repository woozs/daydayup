#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/24 21:02 
# @Author : wuzushun 
# @File : thread02.py
from random import randint
from threading import Thread
from time import time,sleep


class DownloadTask(Thread):

    def __init__(self,filename):
        super().__init__()
        self._filename = filename

    @property
    def filename(self):
        return self._filename

    def run(self):
        print('开始下载文件%s........' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成，耗费%d秒' % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownloadTask("笑傲江湖.pdf")
    t2 = DownloadTask('金瓶梅.txt')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('共耗时：%.2f秒' % (end - start))

if __name__ == '__main__':
    main()
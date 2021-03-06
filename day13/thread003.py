#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/24 21:08 
# @Author : wuzushun 
# @File : thread003.py
from time import sleep
from threading import Thread


class Account(object):

    def __init__(self):
        self._blance = 0


    def deposit(self,money):
        new_blance = self._blance + money
        sleep(0.01)
        self._blance = new_blance

    @property
    def blance(self):
        return self._blance


class AddMoneyThread(Thread):

    def __init__(self,account,money):
        super().__init__()
        self._account = account
        self._monry = money

    def run(self):
        self._account.deposit(self._monry)


def main():
    account = Account()
    threads = []
    for _ in  range(100):
        t = AddMoneyThread(account,1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print('账户余额为:%d'%account.blance)


if __name__ == '__main__':
    main()
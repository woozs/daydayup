#!/usr/bin/env python
# -*- coding:utf-8 -*-
#version:3.5.0
#author:wuzushun

"""
题目：设计一个猜数字的游戏，系统随机生成一个1~100之间的整数，
玩家有5次机会，每猜一次系统就会提示玩家该数字是偏大还是偏小，
如果猜中了，则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案。

"""
import random


answer = random.randint(1,100)

index = 5
while index > 0:
    guess = int(input("请查一个1-100之间的整数:"))
    if guess == answer:
        print("恭喜你，猜对了")
    elif guess > answer:
        print("猜大了，再来一次吧！")
    elif guess < answer:
        print("猜小了，再来一次吧！")
    else:
        print("你输入的不对")
    index -= 1

print("您的机会用完了,正确答案是：%s"%answer)



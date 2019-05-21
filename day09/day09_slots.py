#!/usr/bin/env python
# -*- coding:utf-8 -*-
#version:3.5.0
#author:wuzushun
"""
@property表示只读。
同时有@property和@x.setter表示可读可写。
同时有@property和@x.setter和@x.deleter表示可读可写可删除。
"""
class Person(object):


    #限定person对象只能绑定_name,_age和_gender属性
    __slots__ = ("_name",'_age',"_gender")

    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'

    # AttributeError: 'Person' object has no attribute '_is_gay'
    #person._is_gay = True


if __name__ == '__main__':
    main()
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/21 14:11 
# @Author : wuzushun 
# @File : day09_satcl_and_class.py
class Foo(object):
    X = 1
    Y = 2

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):
        return cls.averag(cls.X, cls.Y)

foo = Foo()
print(foo.static_method())
print(foo.class_method())
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/23 22:52 
# @Author : wuzushun 
# @File : replace_bad.py
import re


def main():
    sentence = "你丫是傻叉吗？我操你大爷的,fuck you。shit"
    purified = re.sub('[操肏艹]|fuck|shit|傻[逼叉缺屌吊]|煞笔',"*",sentence,flags=re.IGNORECASE)
    print(purified)



if __name__ == '__main__':
    main()
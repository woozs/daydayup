#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/22 21:27 
# @Author : wuzushun 
# @File : readfile.py
def main():
    f = open("致橡树.txt","r",encoding="utf-8")
    print(f.read())
    f.close()

if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/22 21:30 
# @Author : wuzushun 
# @File : readfile_try.py
def main():
    f = None
    try:
        f = open("致橡树.txt", "r", encoding="utf-8")
        print(f.read())
    except FileNotFoundError:
        print("无法打开文件")
    except LookupError:
        print("未知编码")
    except UnicodeDecodeError:
        print("解码错误")

    finally:
        if f:
            f.close()
if __name__ == '__main__':
    main()

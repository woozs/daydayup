#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/24 21:34 
# @Author : wuzushun 
# @File : task_thread.py
import time
import tkinter
import tkinter.messagebox


def download():
    time.sleep(10)
    tkinter.messagebox.showinfo('提示','下载完成！')


def show_about():
    tkinter.messagebox.showinfo('关于','作者：碳酸钙（v1.2）')

def main():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost',True)


    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel,text="下载",command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel,text='关于',command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()

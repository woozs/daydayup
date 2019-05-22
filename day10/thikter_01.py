#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/22 21:05 
# @Author : wuzushun 
# @File : thikter_01.py
import tkinter
import tkinter.messagebox


def main():
    flag =True

    #修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not  flag
        color ,msg =('red',"你好")\
            if flag else  ('blue',"再见")
        label.config(text=msg,fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel("温馨提示","确定要退出吗"):
            top.quit()

    top = tkinter.Tk()
    top.geometry("240x160")
    top.title("小游戏")
    label =  tkinter.Label(top,text="你好",font="Arial -32",fg="red")
    label.pack(expand=1)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()
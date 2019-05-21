# -*- coding: utf-8 -*-
# @Time    : 2018/6/16 23:21
# @Author  : mrwuzs
# @Email   : mrwuzs@163.com
# @File    : day_03.py
# @Software: PyCharm
import os,re
from collections import Counter

def get_file(dir):
    f_path =  []
    for root,directories, files in os.walk(dir):#遍历目录
        for filename in files :
            path = os.path.join(root,filename)
            f_path.append(path)

    return f_path

def counter_more_words(li):#统计文件种单词数
    word_dict = Counter(li)
    return [i[0] for i in word_dict.most_common()[:10]]


if __name__ == '__main__':
    for file in get_file(r'D:\4_code\test'):
        with open(file, 'r',encoding='utf-8') as f:
            word_li = re.findall("\w+", f.read())
            print (" ".join(counter_more_words(word_li)))


# -*- coding: utf-8 -*-
# @Time    : 2018/6/16 20:40
# @Author  : mrwuzs
# @Email   : mrwuzs@163.com
# @File    : day_02.py
# @Software: PyCharm
import re

def cont(file_path):
    lines_count = 0
    words_count = 0
    chars_count = 0
    words_dict = {}
    lines_list = []
    file = file_path
    with open(file,'r',encoding='utf-8') as f:
        for line in f:
            lines_count = lines_count + 1
            chars_count = chars_count + len(line)
            match = re.findall(r'[^a-zA-Z0-9]+', line)
            for i in match:
                # 只要英文单词，删掉其他字符
                line = line.replace(i, ' ')
            lines_list = line.split()
            for i in lines_list:
                if i not in words_dict: #word在不字典里，加入单词到字典，记1
                    words_dict[i] = 1
                else:#在字典里，value+1
                    words_dict[i] = words_dict[i] + 1
            print(words_dict)
    print('words_count is', len(words_dict))
    print('lines_count is', lines_count)
    print('chars_count is', chars_count)
    for k, v in words_dict.items():
        print(k,v)


if __name__ == '__main__':
    f= 'test.txt'
    cont(f)



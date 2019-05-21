# -*- coding: utf-8 -*-
# @Time    : 2018/6/16 23:52
# @Author  : mrwuzs
# @Email   : mrwuzs@163.com
# @File    : day_04.py
# @Software: PyCharm
import os


def get_files(path):
    files = os.listdir(path)
    files_path = []
    for fi in files:
        fi_path = path + '\\' + fi
        if os.path.isfile(fi_path):
            if fi.split('.')[-1] == 'py':
                files_path.append(fi_path)
        elif os.path.isdir(fi_path):
            files_path += get_files(fi_path)
    return files_path


def count(files):
    line_of_code, blank, comments = 0, 0, 0
    for filename in files:
        print(filename)

        with open(filename, 'r', encoding='utf-8') as f:
            type(f)
            for line in f:

                line = line.strip()
                line_of_code += 1
                if line == '':
                     blank += 1
                elif line[0] == "#" or line[0] == '/':
                    comments += 1

    return (line_of_code, blank, comments)


if __name__ == '__main__':
    files = get_files(r'D:\4_code\test')
    print(files)

    lines = count(files)
    print('行数: %d,  空行(s): %d, 注释(s): %d' % (lines[0], lines[1], lines[2]))


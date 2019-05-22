#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/22 20:08 
# @Author : wuzushun 
# @File : rmployee.py
from abc import ABCMeta,abstractmethod

class Employee(object,metaclass=ABCMeta):
    """员工"""

    def __init__(self,name):
        """
        初始化方法
        :param name:员工名称
        """
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        """
        获得月薪
        :return:返回月薪
        """
        pass

class Manager(Employee):
    """部门经理"""
    def get_salary(self):
        return 15000

class Programer(Employee):
    """程序员"""
    def __init__(self,name,working_hour=0):
        super().__init__(name)
        print(working_hour)

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self,working_hour):
        self._working_hour = working_hour if working_hour > 0  else 0

    def get_salary(self):
        return 150.0*self._working_hour

class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05


def main():
    emps = [
        Manager("刘备"),Programer("诸葛亮"),
        Manager("曹操"),Salesman("荀彧"),
        Salesman("吕布"),Programer("张辽"),
        Programer("赵云")
    ]
    for emp  in emps:
        if isinstance(emp,Programer):
            emp.working_hour = int(input("请输入%s本月的工作时间:"%emp.name))
        elif isinstance(emp,Salesman):
            emp.sales = int(input("请输入%s销售业绩:" % emp.name))
        print("%s的本月工资为:%d元"%(emp.name,emp.get_salary()))

if __name__ == '__main__':
    main()
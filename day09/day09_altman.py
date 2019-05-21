#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/21 21:01 
# @Author : wuzushun 
# @File : day09_altman.py
from abc import ABCMeta,abstractmethod
from  random import  randint,randrange


class Fighter(object,metaclass=ABCMeta):
    """战斗者"""

    #通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name','_hp')

    def __init__(self,name,hp):
        """
        初始化方法
        :param name:名字
        :param hp：生命值
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """攻击

        :param other: 被攻击的对象
        """
        pass

class Ultraman(Fighter):
    """奥特曼"""

    __slots__ = ('_name','_hp','_mp')

    def __init__(self,name,hp,mp):
        """
        初始化
        :param name: 名字
        :param hp: 生命值
        :param mp: 魔法值
        """
        super().__init__(name,hp)
        self._mp = mp

    def attack(self,other):
        other.hp -= randint(15,25)

    def huge_attack(self,other):
        """
        究极必杀技 打掉对方至少50血
        :param other: 被攻击的对象
        :return: 使用成功返回true，否则返回flase
        """
        if self._hp >=50:
            self._hp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >=50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self,others):
        """
        魔法攻击
        :param others:被攻击的群体
        :return: 使用没法成功返回True,否则返回Flase
        """
        if self._mp >= 20:
            self._mp -=20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10,15)
                return  True
        else:
            return False

    def resume(self):
        """恢复魔法"""
        incr_point = randint(1,10)
        self._mp += incr_point
        return incr_point


    def __str__(self):
        return  '~~~~%s奥特曼~~~~\n'%self._name+"生命值:%d\n"%self._hp



class Monster(Fighter):
    """小怪兽"""


    __slots__ = ('_name','_hp')


    def attack(self,other):
        other.hp -= randint(10,20)

    def __str__(self):
        return   '~~~~%s小怪兽~~~~\n'%self._name+"生命值:%d\n"%self._hp


def is_any_alive(monsters):
    """判断小怪兽是不是活着"""
    for monsters in monsters:
        if monsters.alive > 0:
            return True
    return False


def seleect_alive_one(monsters):
    """选一个活得"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return  monster


def dispaly_info(ultraman,monsters):
    """显示奥特曼和小怪兽得信息"""
    print(ultraman)
    for i in monsters:
        print(i,end='')

def main():
    u1 = Ultraman("wuzs",1000,120)
    m1 = Monster("狄仁杰",250)
    m2 = Monster("白远方",500)
    m3 = Monster("王大锤",750)
    ms = [m1,m2,m3]
    flight_round =1
    while u1.alive and is_any_alive(ms):
        print('***********%02d回合***************'%flight_round)
        m = seleect_alive_one(ms)
        skill = randint(1,10)
        if skill <= 6:
            print('%s使用了普通攻击打了%s'%(u1.name,m.name))
            u1.attack(m)
            print('%s的魔法值恢复到'%u1.resume())
        elif skill <= 9:
            if u1.magic_attack(ms):
                print("%s使用了魔法攻击"%u1.name)
            else:
                print('%s使用魔法攻击失败'%u1.name)
        else:
            if u1.huge_attack(m):
                print("%s使用了必杀技，打了%s"%(u1.name,m.name))
            else:
                print('%s使用必杀技失败')
                print('%s的魔法恢复到%d点'%(u1.name,u1.resume()))


        if m.alive > 0 :
            print('%s回击了%s'%(m.name,u1.name))
            m.attack(u1)

        dispaly_info(u1,ms)
        flight_round += 1
    print('\n===========================战斗结束===============\n')
    if u1.alive  > 0:
        print('%s奥特曼胜利'%u1.name)
    else:
        print("怪兽胜利")

if __name__ == '__main__':
    main()


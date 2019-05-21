#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/21 22:26 
# @Author : wuzushun 
# @File : card.py
import random


class Card(object):
    """一张牌"""

    def __init__(self,suite,face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str ='A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = "Q"
        elif self._face == 13:
            face_str = "k"
        else:
            face_str = str(self._face)

        return '%s%s'%(self._suite,self._face)

    def __repr__(self):
        return self.__str__()


class Poker(object):
    """一副牌"""

    def __init__(self):
        self._cards = [Card(suite,face)
                      for suite in "♠♥♦♣"
                      for face in range(1,14)]
        self._currnet = 0

    @property
    def cards(self):
        return self._cards

    def shutffle(self):
        """洗牌乱序"""
        self._currnet = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._currnet]
        self._currnet += 1
        return card

    @property
    def has_next(self):
        """还有没有牌"""
        return  self._currnet  < len(self.cards)


class Player(object):
    """玩家"""


    def __init__(self,name):
        self._name = name
        self._cards_on_hand = []


    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand


    def get(self,card):
        """摸牌"""
        self._cards_on_hand.append(card)

    def arrange(self,card_key):
        """整理牌"""
        self._cards_on_hand.sort(key=card_key)



def get_key(card):
    return (card.suite,card._face)


def main():
    p = Poker()
    p.shutffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get(p.next)

    for player in players:
        print(player.name+':',end='')
        player.arrange(get_key)
        print(player.cards_on_hand)

if __name__ == '__main__':
    main()

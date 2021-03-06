#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/23 22:58 
# @Author : wuzushun 
# @File : resplit.py
import re


def main():
    poem = '''
    为救苍生缚恶龙，文星笔架化三峰。
不输五岳名天下，秀奇险峻隐仙踪。
邻莱毗福荣齐地，波中起势跃长空。
断崖绝壁千寻立，九阙琼楼一径通。
朝观红日扶桑起，暮眺崦嵫落野禽。
云收雨霁天明净，但见群山披翠衿。
琅嬛圣地聚文脉，百占鳌头耀翰林。
奇石多姿难意料，拙朴方圆各不同。
娇纤憨厚无俗态，似坐似眠如虎熊。
一池一洞皆有典，千年神话著桑田。
镜湖波月麻姑恋，一石双观佛与猿。
太宗神武削金玺，秦皇祀奉阴主前。
八仙会饮无餐席，气吸巨石坐团圆。
岩石天育像形别，突兀凌虚悬欲坠，
五谷涧水流翡翠，虹霞隐现难暇接。
激流喷涌珠帘泄，飞瀑倒垂白练悬。
古藤虬柏龙凤翥，枝横根曲织壁帘。
仙洞蜇龙吞云雾，涎珠滴落奏琴弦。
溪泉福塔竹林连，绕松抱石绿盎然。
步云凌空七台护，四面峰峦笼薄烟。
云低近日天门立，通往中宸过此门。
两石矗立为武士，忠诚无语守晨昏。
诗仙舞袂歌长啸，苏子乘风好问天。
身倚天门举目望，烟台新景扑眼前。
会意乾坤振兴梦，接来时雨润山川。
春潮起伏声势壮，改革开元敢肇先。
赤轮缤纷群峰染，花木葱茏翠鸟喧。
岚气宝光兆百业，古今文明写巨篇。
镜海银湖起碧波，千帆竞发似穿梭。
邸第楼台多气色，朱门街树浴金光。
红豆情峡幽兰茂，温泉如脂玉生香。
引鸾招凤群贤至，八景点化应更芳。
天下名山多绮丽，唯有磁山诗韵长。
'''
    sentence_list = re.split(r'[,.，。]',poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)



if __name__ == '__main__':
    main()
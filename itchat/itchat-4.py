#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-07 13:23:01
# @Author  : WangGuo
# @Email   : guo_wang_113@163.com
# @Github  : https://github.com/King-Key
import sys 
reload(sys)  
sys.setdefaultencoding('utf-8')


from collections import Counter
from pyecharts import Geo
import json
import itchat
import io


#登录
itchat.auto_login()
#获取朋友数据
friends=itchat.get_friends(update=True)

friends_data=[]
for item in friends[1:]:
	friend={
	'NickName':item['NickName'],#昵称
	'RemarkName':item['RemarkName'],#备注
	'Province':item['Province'],#省份
	'City':item['City'],#城市
	}
	print friend
	friends_data.append(friend)



#可视化

#获取所在城市
cities=friends_data[3]
# with io.open('friends.txt',mode='r',encoding='utf-8') as f:
# 	rows=f.readlines()
# 	for row in rows:
# 		city=row.split(',')[3]
# 		if city!='':
# 			cities.append(city)

#handle(cities)

data=Counter(cities).most_common()
print(data)

#绘执地理坐标图
geo=Geo("好友位置分布",'',title_color='#fff',title_pos='center',width=1200,height=600,background_color='#404a59')
attr,value=geo.cast(data)
geo.add('',attr,value,visual_range=[0,500],visual_text_color='#fff',symbol_size=15,is_visualmap=True,is_piecewise=True)
geo.render('好友位置分布2.html')


# # 处理地名数据，解决坐标文件中找不到地名的问题
# def handle(cities):
#     # print(len(cities), len(set(cities)))

#     # 获取坐标文件中所有地名
#     data = None
#     with open('/home/guo/.local/lib/python2.7/site-packages/pyecharts/datasets/city_coordinates.json',mode='r') as f:
#         data = json.loads(f.read())  # 将str转换为json

#     # 循环判断处理
#     data_new = data.copy()  # 拷贝所有地名数据
#     for city in set(cities):  # 使用set去重
#         # 处理地名为空的数据
#         if city == '':
#             while city in cities:
#                 cities.remove(city)
#         count = 0
#         for k in data.keys():
#             count += 1
#             if k == city:
#                 break
#             if k.startswith(city):  # 处理简写的地名，如 达州市 简写为 达州
#                 # print(k, city)
#                 data_new[city] = data[k]
#                 break
#             if k.startswith(city[0:-1]) and len(city) >= 3:  # 处理行政变更的地名，如县改区 或 县改市等
#                 data_new[city] = data[k]
#                 break
#         # 处理不存在的地名
#         if count == len(data):
#             while city in cities:
#                 cities.remove(city)



#     # print(len(data), len(data_new))

#     # 写入覆盖坐标文件
#     with open('/home/guo/.local/lib/python2.7/site-packages/pyecharts/datasets/city_coordinates.json',mode='w') as f:
#         f.write(json.dumps(data_new, ensure_ascii=False))  # 将json转换为str




#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-12 16:21:22
# @Author  : King-Key
# @email   : guo_wang_113@163.com
# @Github  : https://github.com/King-Key
# @Link    : https://king-key.github.io



import os
import sys
import xlsxwriter
import itchat,time
from itchat.content import TEXT
import re
 #其中hotReload=True参数是为了短暂记忆登录状态，避免每登录一次就扫一次二维码
itchat.auto_login()
#获取群聊信息
roomslist = itchat.get_chatrooms(update=True)


find_name_1="东西"
find_name_2="智东西"
#插入excel

def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|\]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title

for i in range(0,len(roomslist)-1):
	#根据名称搜索群聊信息
	if find_name_1 in roomslist[i]['NickName'] or find_name_2 in roomslist[i]['NickName']:


		#根据群聊名称创建excel表单
		#name=validateTitle(roomslist[i]['NickName'])
		name=roomslist[i]['NickName']
		workbook=xlsxwriter.Workbook(name+".xlsx")
		worksheet=workbook.add_worksheet(name)

		#添加表头
		worksheet.write(0,0,"微信名称")
		worksheet.write(0,1,"群备注")
		#获取群聊用户列表
		myroom=itchat.search_chatrooms(name=roomslist[i]['NickName'])
		#获取群聊名称
		gsp=itchat.update_chatroom(myroom[0]['UserName'], detailedMember=True)
		#print("群名：{} \t 人数：{}".format(roomslist[i]['NickName'],len(gsp['MemberList'])))

		nickname=[]
		displayname=[]

		for c in gsp['MemberList']:
			nickname.append(c['NickName'])
			displayname.append(c['DisplayName'])
		#将用户信息写入相应的工作薄中
		for x in range(len(gsp['MemberList'])):
			worksheet.write(x+1,0,nickname[x])
			worksheet.write(x+1,1,displayname[x])
		#输出一点提示信息
		print("book {} finished".format(roomslist[i]['NickName']))
		#关闭工作表
		workbook.close()
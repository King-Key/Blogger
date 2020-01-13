#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-01-12 00:51:38
# @Author  : King-Key 
# @Link    : kingkey.club
# @E-mail  : guo_wang_113@163.com

import turtle
import time

import pygame

#添加音乐
def add_music(path):
	pygame.mixer.init()
	track = pygame.mixer.music.load(path)
	pygame.mixer.music.play()
	time.sleep(2)
#pygame.mixer.music.stop()

# 画心形圆弧
def hart_arc():
	for i in range(200):
		turtle.right(1)
		turtle.forward(2)
def move_pen_position(x, y):
	turtle.hideturtle()
	turtle.up()
	turtle.goto(x, y)
	turtle.down()
	turtle.showturtle()

#心
def love(self_x,self_y,self_left):
	turtle.setup(width=900, height=600)
	turtle.color('red', 'pink')
	turtle.pensize(5)
	turtle.speed(50)
	# 初始化画笔起始坐标
	move_pen_position(x=self_x,y=self_y)
	turtle.left(self_left)
	turtle.begin_fill()
	# 画心形直线（ 左下方 ）
	turtle.forward(224)
	# 画爱心圆弧
	hart_arc()
	turtle.left(120)
	hart_arc()
	# 画心形直线（ 右下方 ）
	turtle.forward(224)
	turtle.end_fill()

#文字
def text(txt,x,y,color,):
	move_pen_position(x,y)
	turtle.hideturtle()
	turtle.color(color, 'pink')
	# font:设定字体、尺寸（电脑下存在的字体都可设置）  align:中心对齐
	turtle.write(txt, font=('Arial', 30, 'bold'), align="center")



#箭
def arrow():
	turtle.pencolor('red')
	turtle.pensize(20)
	turtle.speed(20)

	move_pen_position(x=-400,y=-80)
	turtle.right(205)
	turtle.forward(850)

	move_pen_position(x=410,y=155)
	turtle.right(45)
	turtle.forward(25)
	turtle.right(90)
	turtle.forward(25)

	move_pen_position(x=660,y=-130)


def main():
	path='./咱们结婚吧-齐晨.mp3'
	add_music(path)

	love(self_x=170,self_y=-140,self_left=140)
	love(self_x=-170,self_y=-200,self_left=280)

	love = '老婆'
	signature = '老公'
	text(love,180,90,'#CD5C5C')
	text(signature,-160,20,'red')

	arrow()

	# 点击窗口关闭程序
	window = turtle.Screen()
	window.exitonclick()


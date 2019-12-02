#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-12-01 22:08:02
# @Author  : King-Key 
# @Link    : kingkey.club
# @E-mail  : guo_wang_113@163.com



import cv2
import numpy as np 
ＱＱ

def draw_circle(event,x,y,flags,param):
	if event==cv2.EVENT_LBUTTONDBLCLK:
		print(event,x,y)
		cv2.circle(event,(x,y),100,(255,0,0),-1)

image=np.zeros((512,512,3),np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback("image",draw_circle)

while(1):
	cv2.imshow("image",image)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break
cv2.destroyAllWindows()
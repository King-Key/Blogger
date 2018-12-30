#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-19 10:55:27
# @Author  : WangGuo
# @Email   : guo_wang_113@163.com
# @Github  : https://github.com/King-Key



import cv2
import os

file_path='./JPEGImages/'
for filename in os.listdir(file_path):

	print(filename)
	img=cv2.imread(file_path+filename)
	
	size=cv2.resize(img,(500,375))
	cv2.imwrite(file_path+filename,size)
	if img is not None:
		continue


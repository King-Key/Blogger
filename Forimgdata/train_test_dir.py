#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-18 07:54:38
# @Author  : WangGuo
# @Email   : guo_wang_113@163.com
# @Github  : https://github.com/King-Key



import os
import random
import shutil
# trainfiles = os.listdir('./images/105')
# num_train = len(trainfiles)
# index_list = range(num_train)
# random.shuffle(index_list)
# num = 0
# trainDir = 'train'
# validDir = 'test'
# for i in index_list:
#     fileName = os.path.join('./images/105', trainfiles[i])
#     if num < num_train*0.8:
#         copy2(fileName, trainDir)
#     else:
#         copy2(fileName, validDir)
#     num += 1

image_path="images/"
class_names=os.listdir(image_path) #获取当前路径下的文件夹名称（即类名)

print(class_names)
for name in class_names:
	path=image_path+name #拼接数据类别路径
	os.makedirs(image_path+"train/"+name) #创建训练数据的文件夹
	os.makedirs(image_path+"test/"+name) #创建测试图片的文件夹

	
	print(path)
	images=os.listdir(path) #获取图片
	nums=len(images) #图片的数量
	random.shuffle(images) #打乱图片
	num=0
	for i in range(nums):
		file=os.path.join(path,images[i]) #拼接图片路径
		print("file:",file)
		if num<len(images)*0.7: #划分训练集

			shutil.copy(file,image_path+"train/"+name) #拷贝到训练集文件夹
		else:
			shutil.copy(file,image_path+"test/"+name) #拷贝到测试集文件夹
		num+=1

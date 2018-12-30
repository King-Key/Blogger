#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-13 23:04:07
# @Author  : WangGuo
# @Email   : guo_wang_113@163.com
# @Github  : https://github.com/King-Key



import os
import tensorflow as tf 
from PIL import Image

#获取当前所在目录
#cwd=os.getcwd()

#读取类别数目。类名即为文件名
#classes={'1','2','3','4','5','6','7','8','10','11'}

def  list_label_prepare():
	#生成list.txt,label.txt文件，方便读取与查看
	#classes_to_ids={'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'10':8,'11':9}
	classes_to_ids={'image':1}
	data_dir = '../data/'
	list_output_path = '../data/list_licenseimage_.txt'
	label_output_apth='../data/label_licenseimage.txt'

	list_file_write= open(list_output_path, 'w')
	label_file_write=open(label_output_apth,'w')

	for class_name in classes_to_ids.keys():
	    images_list = os.listdir(data_dir + class_name)
	    label_file_write.write('{}\n'.format(class_name))

	    for image_name in images_list:
	        list_file_write.write('{}/{} {}\n'.format(class_name, image_name, classes_to_ids[class_name]))
	label_file_write.close()
	list_file_write.close()
	print "----------------------finshed----------------------"

#生成验证集和训练集
import random 
def create_data():
	#验证集的数目
	num_test=5
	num=19
	num_random=0

	#生成测试集和验证集的.txt文件
	list_path='../data/list_licenseimage_.txt'
	train_list_path='../data/list_train_licenseimage.txt'
	test_list_path='../data/list_test_licenseimage.txt'

	file=open(list_path)
	lines=file.readlines()
	file.close()

	#生成测试集和训练集
	random.seed(num_random)
	random.shuffle(lines)
	file=open(train_list_path,'w')
	for line in lines[num_test:]:
		file.write(line)
	file.close()

	file=open(test_list_path,'w')
	for line in lines[:num_test]:
		file.write(line)
	file.close()




if __name__ == '__main__':
	list_label_prepare()
	create_data()

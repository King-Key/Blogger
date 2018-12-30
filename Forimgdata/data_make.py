#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-17 21:04:34
# @Author  : WangGuo
# @Email   : guo_wang_113@163.com
# @Github  : https://github.com/King-Key



import xml.etree.ElementTree as ET 
from os import getcwd 

set_names=['train','trainval','val','test']
classes=['License']
def convert_annotation(image_id, list_file):
    in_file=open('./Annotations/%s.xml'%(image_id))
    tree=ET.parse(in_file)
    root=tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        print(cls)
        if cls not in classes or int(difficult)==1:
             continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for image_set in set_names:
    # 注意路径
    image_ids = open('ImageSets/Main/%s.txt'%(image_set)).read().split()
    #print("ids:",image_ids[1])

    list_file = open('%s.txt'%(image_set), 'w')

    for image_id in image_ids:
        # 注意路径
        #print(image_id)
        list_file.write('JPEGImages/%s.jpg'%(image_id))
        convert_annotation(image_id, list_file)
        list_file.write('\n')
    list_file.close()

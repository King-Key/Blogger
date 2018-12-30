import os
import random
import cv2
from numpy import *
import re
import xml.dom.minidom

file_num

#定义添加高斯噪声的函数
def GaussianNoise(src,means,sigma,percetage):
    NoiseImg=src
    NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(NoiseNum):
        randX=random.randint(0,src.shape[0]-1)
        randY=random.randint(0,src.shape[1]-1)
        NoiseImg[randX, randY]=NoiseImg[randX,randY]+random.gauss(means,sigma)
        if  NoiseImg[randX, randY]< 0:
                 NoiseImg[randX, randY]=0
        elif NoiseImg[randX, randY]>255:
                 NoiseImg[randX, randY]=255
    return NoiseImg

def PepperandSalt(src,percetage):
    NoiseImg=src
    NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(NoiseNum):
        randX=random.random_integers(0,src.shape[0]-1)
        randY=random.random_integers(0,src.shape[1]-1)
        if random.random_integers(0,1)<=0.5:
            NoiseImg[randX,randY]=0
        else:
            NoiseImg[randX,randY]=255
    return NoiseImg


def rename_file(file_name):
    if '.' in file_name:
        file_num = file_name.split('.')[0]
        add_file_name_num = int(file_num) + file_num

    return str(add_file_name_num).zfill(6)



im_path = 'JPEGImages/'
#xml_path='Annotations/'

im_names = os.listdir(im_path)
#xml_names=os.listdir(xml_path)
#print(xml_names)

file_num=len(im_names)
for im_name in im_names:

    im=cv2.imread(im_path+im_name)
    add_im = PepperandSalt(im,0.05)
    cv2.imwrite(im_path+rename_file(im_name)+'.jpg',add_im)

# for xml_name in xml_names:
#     dom=xml.dom.minidom.parse(xml_path+xml_name)
#     root=dom.documentElement
#     name=root.getElementsByTagName('filename')
#     print(name)


_dir = "./Annotations/"
xmlList = os.listdir(_dir)
n = 0
for xml in xmlList:
    #f = open(_dir + xml, "r")
    f = open(_dir + xml, "r")
    xmldata = f.read()
    xmldata = re.sub('\<path>(.*?)\</path>', '<path>/data/VOCdevkit2007/VOC2007/JPEGImages/' + rename_file(xml) + '.jpg</path>', xmldata)
    xmldata = re.sub('\<filename>(.*?)\</filename>', '<filename>' + rename_file(xml) + '.jpg</filename>', xmldata)
    f.close()
    f = open(_dir + rename_file(xml)+'.xml', "w")
    f.write(xmldata)
    f.close()
    n += 1

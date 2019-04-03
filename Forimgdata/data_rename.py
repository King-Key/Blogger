
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-18 12:50:31
# @Author  : WangGuo
# @Email   : guo_wang_113@163.com
# @Github  : https://github.com/King-Key



import os
import re
 
_dir = "./Annotations/"
xmlList = os.listdir(_dir)
n = 0
for xml in xmlList:
    #f = open(_dir + xml, "r")
    f = open(_dir + xml, "r")
    xmldata = f.read()
    xmldata = re.sub('\<path>(.*?)\</path>', '<path>/data/VOCdevkit2007/VOC2007/JPEGImages/' + str(n).zfill(3) + '.jpg</path>', xmldata)
    f.close()
    f = open(_dir + xml, "w")
    f.write(xmldata)
    f.close()
    n += 1

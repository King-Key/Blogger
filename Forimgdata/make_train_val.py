#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-18 08:47:40
# @Author  : WangGuo
# @Email   : guo_wang_113@163.com
# @Github  : https://github.com/King-Key



import os
import random


def _main():
    trainval_percent = 0.5
    train_percent = 0.5
    xmlfilepath = 'Annotations'
    total_xml = os.listdir(xmlfilepath)

    num = len(total_xml)
    list = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list, tv)
    train = random.sample(trainval, tr)

    ftrainval = open('ImageSets/Main/trainval.txt', 'w')
    ftest = open('ImageSets/Main/test.txt', 'w')
    ftrain = open('ImageSets/Main/train.txt', 'w')
    fval = open('ImageSets/Main/val.txt', 'w')

    for i in list:
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftest.write(name)
            else:
                fval.write(name)
        else:
            ftrain.write(name)

    ftrainval.close()
    ftrain.close()
    fval.close()
    ftest.close()


if __name__ == '__main__':
    _main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-24 16:55:49
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io

import logging
import threading


def doubler(number):
	print(threading.currentThread().getName()+'\n')
	print(number*2)
	print()

if __name__ == '__main__':
	for i in range(5):
		my_thred=threading.Thread(target=doubler,args=(i,))
		my_thred.start()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-05 23:46:39
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io


import _thread as thread
import time

def print_time(thread_name,delay):
	count=0
	while count<5:
		time.sleep(delay)
		count+=1
		print("{}:{}".format(thread_name,time.ctime(time.time())))

try:
	thread.start_new_thread(print_time,("Thread-1",2,))
	thread.start_new_thread(print_time,("Thread-2",4,))
except:
	print("error")

while 1:
	pass

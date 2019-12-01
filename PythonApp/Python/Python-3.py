#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-03 22:55:40
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io


import math

print(dir(math))
file = open("./课程内容差异化调研.md", "wb")

print(file.name)
print(file.closed)
print(file.mode)

file1 = open("test.txt", "w")
file1.write('hello world')
file1.close()

file2 = open("test.txt", "r+")
data = file2.read()
print(data)

print(file2.tell())

import os
os.remove("test.txt")

print(os.getcwd())
print(os.chdir("/home/king-key/下载/"))


try:
	file3=open("test.txt","r")
	file3.write("hello")
except IOError:
	print("error")
else:
	print("true")
	file3.close()
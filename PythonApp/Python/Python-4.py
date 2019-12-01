#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-04 00:10:20
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io


class Name:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print(self.name)

    def printage(self):
        print(self.age)

    def getname(self):
        self.name = input("name:")

    def getage(self):
        self.age = input("age:")


my = Name("wangguo", "25")
my.getname()
my.getage()
my.printname()
my.printage()

print(my.__doc__)


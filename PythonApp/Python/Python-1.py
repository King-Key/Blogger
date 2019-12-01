#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-03 10:12:21
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io


# list

list = ["hello", "wang", "guo"]
print(list)
print(type(list))

print(list[0])
print(list[0:2])
print(list*2)
print(list+list)

# tuple
tuple = ("hello", "wang", "guo")
print(tuple)
print(type(tuple))

print(tuple[0])
print(tuple[0:2])
print(tuple*2)
print(tuple+tuple)

# dict
dict = {"0": "hello", "1": "wang", "2": "guo"}
print(dict)
print(type(dict))

print(dict.keys())
print(dict.values())
print(dict["0"])
print(dict["0"]+dict["1"])


a = "123456789"
# print(list(a))
print(tuple(a))

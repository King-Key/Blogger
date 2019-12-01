#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-04 00:26:58
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io

import re
lines = "my name is wang guo!"
# match1 = re.match(r"(.*) is (.*?)",lines,re.M|re.I)
# print(match1)
# print(match1.group())
# print(len(match1.group()))
# print(type(match1.group()))
# print(match1.group(1))
# print(match1.group(2))


# match2 = re.search(r"(.*) is (.*?)",lines,re.M|re.I)
# print(match2)
# print(match2.group())
# print(len(match2.group()))
# print(type(match2.group()))
# print(match2.group(1))
# print(match2.group(2))

match3 = re.sub("is","are",lines)
print(match3)
print(re.sub("[Mm]y",lines))
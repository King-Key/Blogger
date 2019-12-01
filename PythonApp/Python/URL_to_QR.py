#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-19 20:06:30
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io


import qrcode
img=qrcode.make("https://king-key.github.io/about/")
img.save("./test.png")
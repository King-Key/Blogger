#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-21 13:29:24
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import turtle as p
import random

def snow(snow_count):
    p.hideturtle()
    p.speed(500)
    p.pensize(2)
    for i in range(snow_count):
        r = random.random()
        g = random.random()
        b = random.random()
        p.pencolor(r, g, b)
        p.pu()
        p.goto(random.randint(-350, 350), random.randint(1, 270))
        p.pd()
        dens = random.randint(8, 12)
        snowsize = random.randint(10, 14)
        for _ in range(dens):
            p.forward(snowsize)  # 向当前画笔方向移动snowsize像素长度
            p.backward(snowsize)  # 向当前画笔相反方向移动snowsize像素长度
            p.right(360 / dens)  # 顺时针移动360 / dens度

def main():
    p.setup(800, 600, 0, 0)
    # p.tracer(False)
    p.bgcolor("white")
    snow(30)

    # p.tracer(True)
    p.mainloop()

if __name__ == '__main__':
	main()

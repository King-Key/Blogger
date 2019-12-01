#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-18 15:38:09
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io


import tensorflow as tf 


#fetch
input1=tf.constant(3.0)
input2=tf.constant(2.0)
input3=tf.constant(5.0)

add=tf.add(input1,input2)
print("add:",add)
mu1=tf.multiply(input3,add)
print("mul:",mu1)

with tf.Session() as sess:
	result=sess.run([mu1,add])
	print(result)
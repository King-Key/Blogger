#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-10 23:47:53
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io


import numpy as np 
import cv2
cv2.namedWindow("image")
image=np.zeros((512,512,3),np.uint8)
# #line
cv2.line(image,(0,0),(511,511),(255,255,255),5)
#circle
cv2.circle(image,((int(512/2)),int(512/2)),int(512/2),(0,0,255),-1)
# #text
# font=cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(image,"HELLO",(10,500),font,4,(255,255,2),2)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows("image")

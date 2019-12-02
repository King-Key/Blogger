#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-09 00:26:06
# @Author  : King-Key
# @Email   : guo_wang_113@163.com
# @Link    : https://king-key.github.io


import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        cv2.imshow("vedio", frame)

        # vedio write
        #out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
# out.release()
cv2.destroyAllWindows()

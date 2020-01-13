#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-01-11 23:00:44
# @Author  : King-Key 
# @Link    : kingkey.club
# @E-mail  : guo_wang_113@163.com


import sys
import random
from PyQt5 import QtCore,QtMultimedia
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QDesktopWidget, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtGui import *
import cv2
from trueLove import *




class Example(QWidget):


    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制函数



    def initUI(self):
        self.truetext="我愿意"
        self.falsetext="拒绝"
        self.image=cv2.imread("./love.jpg")
        print(self.image.shape)
        
        # 设置窗口位置和大小
        self.setGeometry(300, 300, self.image.shape[1], self.image.shape[0])
        self.setWindowFlags(QtCore.Qt.WindowTitleHint|QtCore.Qt.WindowCloseButtonHint)
        self.center()
        # 设置标题
        self.setWindowTitle("我喜欢你")
        # 设置窗口图标
        self.setWindowIcon(
            QIcon("./love.jpg"))
        #设置背景图片

        background=QPalette()
        background.setBrush(self.backgroundRole(),QBrush(QPixmap("./love.jpg")))
        self.setPalette(background)

        # 创建按钮
        trueButton = QPushButton(self.truetext, self)
        trueButton.clicked.connect(self.trueButtonEvent)

        self.falseButton=QPushButton(self.falsetext,self)
        self.falseButton.installEventFilter(self)


        trueButton.move(self.image.shape[1]/3, (self.image.shape[0]/5)*4)
        self.falseButton.move(self.image.shape[1]/2,(self.image.shape[0]/5)*4)

        # 显示
        self.show()

    def trueButtonEvent(self):
        sender=self.sender()
        event=QApplication.instance()
        event.quit()


    #按钮移动事件
    def eventFilter(self,object,event):
    	if event.type()==QtCore.QEvent.HoverMove:
    		self.falseButton.move(random.randint(10,int(self.image.shape[1]/5)*4),random.randint(10,int(self.image.shape[0]/5)*4))
    		return True
    	return False

    #点击窗口关闭事件
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "小姐姐", "不能逃避的哦", QMessageBox.Yes, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
        	event.ignore()

    # 窗口显示在屏幕中间
    def center(self):
        # 获取窗口
        qr = self.frameGeometry()
        # 获取屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示在屏幕中间
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Example()
    sys.exit(app.exec_())

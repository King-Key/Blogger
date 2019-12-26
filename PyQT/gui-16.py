#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    		: 2019-12-25 16:36:03
# @Author  		: King-Key
# @E-mail  		: guo_wang_113@163.com
# @BlogLink     : kingkey.club
# @Version 		: 1.0

# 拖放
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat("text/plain"):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text())

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            return
        miniDara = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos()-self.rect().topLeft())
        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        QPushButton.mousePressEvent(self, e)
        if e.button() == Qt.LeftButton:
            print("press")


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # edit = QLineEdit("", self)
        # edit.setDragEnabled(True)
        # edit.move(30, 65)

        # button = Button("button", self)
        # button.move(190, 65)

        self.setAcceptDrops(True)
        self.button=Button("button",self)
        self.button.move(100,5)

        self.setWindowTitle("drag & drop")
        self.setGeometry(300, 300, 300, 150)

    def dragEnterEvent(self,e):
    	e.accept()

    def dropEvent(self,e):
    	position=e.pos()
    	self.button.move(position)
    	e.setDropAction(Qt.MoveAction)
    	e.accept()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()

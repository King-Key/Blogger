#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    		: 2019-12-25 19:02:28
# @Author  		: King-Key
# @E-mail  		: guo_wang_113@163.com
# @BlogLink     : kingkey.club
# @Version 		: 1.0

import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QColor,QPen
from PyQt5.QtCore import Qt

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(300,300,800,600)
		self.setWindowTitle("pen")
		self.show()

	def paintEvent(self,e):
		qp=QPainter()
		qp.begin(self)
		self.drawLines(qp)
		qp.end()

	def drawLines(self,qp):
		pen=QPen(Qt.black,2,Qt.SolidLine)

		qp.setPen(pen)
		qp.drawLine(20,40,250,40)

		pen.setStyle(Qt.DashLine)
		qp.setPen(pen)
		qp.drawLine(20,80,250,80)

		pen.setStyle(Qt.DashDotLine)
		qp.setPen(pen)
		qp.drawLine(20,120,250,120)

		pen.setStyle(Qt.DotLine)
		qp.setPen(pen)
		qp.drawLine(20,160,250,160)
if __name__=="__main__":
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())

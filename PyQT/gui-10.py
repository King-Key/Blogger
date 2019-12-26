#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    		: 2019-12-22 22:56:58
# @Author  		: King-Key
# @E-mail  		: guo_wang_113@163.com
# @BlogLink     : kingkey.club
# @Version 		: 1.0

#控件
import sys
from PyQt5.QtWidgets import QWidget,QCheckBox,QApplication
from PyQt5.QtCore import Qt

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		cb=QCheckBox("show title",self)
		cb.move(20,20)
		cb.toggle()
		cb.stateChanged.connect(self.changeTitle)

		self.setGeometry(300,300,250,150)
		self.setWindowTitle("QCheckBox")
		self.show()

	def changeTitle(self,state):
		if state==Qt.Checked:
			self.setWindowTitle("QCheckBox")
		else:
			self.setWindowTitle("none")

if __name__=="__main__":
	app=QApplication(sys.argv)
	wx=Example()
	sys.exit(app.exec_())




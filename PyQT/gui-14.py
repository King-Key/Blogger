#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    		: 2019-12-25 15:58:49
# @Author  		: King-Key
# @E-mail  		: guo_wang_113@163.com
# @BlogLink     : kingkey.club
# @Version 		: 1.0

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.lbl=QLabel(self)
		self.lbl.move(60,40)

		#文本框
		qle=QLineEdit(self)
		qle.move(60,100)

		qle.textChanged[str].connect(self.onChanged)

		self.setGeometry(300,300,300,200)
		self.setWindowTitle("QLineEdit")
		self.show()

	def onChanged(self,text):
		self.lbl.setText(text)
		self.lbl.adjustSize()

if __name__=="__main__":
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())
		

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   gui-6.py
@Time    :   2019/12/15 17:45:09
@Author  :   King-Key 
@Version :   1.0
@Contact :   guo_wang_113@163.com
@Blog    :   https://kingkey.club.
'''

import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QLineEdit,QInputDialog,QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button=QPushButton("dialog",self)
        self.button.move(20,20)
        self.button.clicked.connect(self.showDialog)

        self.le=QLineEdit(self)
        self.le.move(130,20)

        self.setGeometry(300,300,800,600)
        self.setWindowTitle("input dialog")
        self.show()

    def showDialog(self):
        #输入对话框
        # 标题+消息
        # return：输入的文本，一个布尔值
        text,ok=QInputDialog.getText(self,"input dialog","enter your name:")
        if ok:
            self.le.setText(str(text))

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
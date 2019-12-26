#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   gui-5.py
@Time    :   2019/12/11 19:31:20
@Author  :   King-Key 
@Version :   1.0
@Contact :   guo_wang_113@163.com
@Blog    :   https://kingkey.club.
'''

import sys
from PyQt5 .QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QPushButton, QMainWindow


# class Example(QWidget):
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    # #信号槽
    # def initUI(self):
    #     lcd = QLCDNumber(self)
    #     sld = QSlider(Qt.Horizontal, self)

    #     vbox = QVBoxLayout()
    #     vbox.addWidget(lcd)
    #     vbox.addWidget(sld)

    #     self.setLayout(vbox)
    #     #信号槽
    #     sld.valueChanged.connect(lcd.display)

    #     self.setGeometry(300, 300, 250, 150)
    #     self.setWindowTitle("signal & slot")
    #     self.show()

    # 信号判断
    def initUI(self):
        button = QPushButton("button", self)
        button.move(30, 50)

        button1 = QPushButton("button1", self)
        button1.move(150, 50)

        button.clicked.connect(self.buttonClicked)
        button1.clicked.connect(self.buttonClicked)

        self.statusBar()
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("event sender")
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text()+"  was pressesd")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

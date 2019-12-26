#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    		: 2019-12-19 14:59:19
# @Author  		: King-Key
# @E-mail  		: guo_wang_113@163.com
# @BlogLink     : kingkey.club
# @Version 		: 1.0

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFrame, QColorDialog

from PyQt5.QtGui import QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)
        self.button = QPushButton("dialog", self)
        self.button.move(20, 20)
        self.button.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget {background-color:%s}" % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle("color dialog")
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet(
                "QWidget {background-color:%s}" % col.name())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

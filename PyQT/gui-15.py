#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    		: 2019-12-25 16:09:10
# @Author  		: King-Key
# @E-mail  		: guo_wang_113@163.com
# @BlogLink     : kingkey.club
# @Version 		: 1.0

import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame, QSplitter, QStyleFactory, QApplication, QComboBox, QLabel
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 下拉列表
        self.lbl = QLabel("ubuntu", self)
        combo = QComboBox(self)
        combo.addItem("ubuntu")
        combo.addItem("mandriva")
        combo.addItem("fedora")
        combo.move(10, 10)
        self.lbl.move(50, 50)
        combo.activated[str].connect(self.onActivated)

        # hbox=QHBoxLayout(self)

        # topleft=QFrame(self)
        # topleft.setFrameShape(QFrame.StyledPanel)

        # topright=QFrame(self)
        # topright.setFrameShape(QFrame.StyledPanel)

        # buttom=QFrame(self)
        # buttom.setFrameShape(QFrame.StyledPanel)
        # buttom.addWidget(self.lbl)

        # splitter1=QSplitter(Qt.Horizontal)
        # splitter1.addWidget(topleft)
        # splitter1.addWidget(topright)

        # splitter2=QSplitter(Qt.Vertical)
        # splitter2.addWidget(splitter1)
        # splitter2.addWidget(buttom)

        # hbox.addWidget(splitter2)
        # self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("QSplitter")
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

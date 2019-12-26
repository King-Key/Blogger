#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   gui-3.py
@Time    :   2019/12/10 00:41:41
@Author  :   King-Key 
@Version :   1.0
@Contact :   guo_wang_113@163.com
@Blog    :   https://kingkey.club.
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout, QLineEdit, QTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # # 绝对定位、
    # def initUI(self):
    #     labl1 = QLabel("ZETCODE", self)
    #     labl1.move(15, 10)

    #     labl2 = QLabel("tutorials", self)
    #     labl2.move(35, 40)
    #     labl3 = QLabel("programmers", self)
    #     labl3.move(55, 70)

    #     self.setGeometry(300, 300, 250, 150)
    #     self.setWindowTitle("absolute")
    #     self.show()

    # # 框布局
    # def initUI(self):
    #     okbutton = QPushButton("ok")
    #     cancelbutton = QPushButton("cancel")

    #     hbox = QHBoxLayout()
    #     hbox.addStretch(1)
    #     hbox.addWidget(okbutton)
    #     hbox.addWidget(cancelbutton)

    #     vbox = QVBoxLayout()
    #     vbox.addStretch(1)
    #     vbox.addLayout(hbox)

    #     self.setLayout(vbox)

    #     self.setGeometry(300, 300, 800, 600)
    #     self.setWindowTitle("button")
    #     self.show()

    # # 表格布局
    # def initUI(self):
    #     grid = QGridLayout()
    #     self.setLayout(grid)

    #     names = ['Cls', 'Bck', '', 'Close',
    #             '7', '8', '9', '/',
    #             '4', '5', '6', '*',
    #             '1', '2', '3', '-',
    #             '0', '.', '=', '+']
    #     positions = [(i, j) for i in range(5) for j in range(4)]
    #     for position, name in zip(positions, names):
    #         if name == "":
    #             continue
    #         button = QPushButton(name)
    #         grid.addWidget(button, *position)
    #     self.move(300, 150)
    #     self.setWindowTitle("CALCULATOR")
    #     self.show()

    #控件在网格中跨行 or 列
    def initUI(self):
        title = QLabel("title")
        author = QLabel("author")
        review = QLabel("review")

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("review")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   gui-7.py
@Time    :   2019/12/15 19:03:05
@Author  :   King-Key 
@Version :   1.0
@Contact :   guo_wang_113@163.com
@Blog    :   https://kingkey.club.
'''


import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QTextEdit, QAction, QFileDialog, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(
            QIcon("C:\\Users\\guo_w\\Pictures\\Saved_Pictures\\Yosemite.jpg"), "open", self)
        openFile.setShortcut("ctrl+q")
        openFile.setStatusTip("open new file")
        openFile.triggered.connect(self.showDialog)

        openFile2=QAction(
            QIcon("C:\\Users\\guo_w\\Pictures\\Saved_Pictures\\Yosemite.jpg"), "open", self)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&file")
        fileMenu.addAction(openFile)
        fileMenu.addAction(openFile2)

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle("file dialog")
        self.show()
    #文件选择框
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, "open file", "./")
        print("filename:", fname)
        if fname[0]:
            print("open file name:", fname[0])
            f = open(fname[0], "r",encoding="utf-8")

            with f:
                data = f.read()
                print("data:", data)
                self.textEdit.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

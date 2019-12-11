#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @File    :   gui-4.py
# @Time    :   2019/12/10 22:05:00
# @Author  :   King-Key
# @Version :   1.0
# @Contact :   guo_wang_113@163.com
# @Blog   :   https://kingkey.club

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 图标
        exitAction = QAction(
            QIcon("/home/king-key/图片/cat1.jpeg"), "&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("exit application")
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        # 创建菜单栏
        menubar = self.menuBar()
        # 添加菜单
        fileMenu = menubar.addMenu("&File")
        # 添加事件
        fileMenu.addAction(exitAction)
        # 状态栏
        self.statusBar().showMessage("ready")

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("statusbar")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

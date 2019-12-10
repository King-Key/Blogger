#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   gui-2.py
@Time    :   2019/12/10 00:11:55
@Author  :   King-Key 
@Version :   1.0
@Contact :   guo_wang_113@163.com
@Blog    :   https://kingkey.club.
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QDesktopWidget, QMessageBox
from PyQt5.QtGui import QIcon, QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制函数

    def initUI(self):
        # 设置窗口位置和大小
        #self.setGeometry(300, 300, 800, 600)
        self.center()
        # 设置标题
        self.setWindowTitle("icon")
        # 设置窗口图标
        self.setWindowIcon(
            QIcon("C:\\Users\\guo_w\\Pictures\\Saved_Pictures\\Yosemite_4.jpg"))

        # 设置字体
        QToolTip.setFont(QFont("SansSerif", 10))
        self.setToolTip("this is a qwidget widget")

        # 创建按钮
        button = QPushButton("button", self)
        button.setToolTip("this is a qpushbutton widget")

        # button.sizeHint()默认大小
        button.resize(button.sizeHint())
        button.move(150, 150)

        # 显示
        self.show()

    # 窗口关闭确认
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "Message", "are you sure to quit", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 窗口显示在屏幕中间

    def center(self):
        # 获取窗口
        qr = self.frameGeometry()
        # 获取屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示在屏幕中间
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Example()
    sys.exit(app.exec_())

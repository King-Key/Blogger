#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   gui-1.py
@Time    :   2019/12/10 00:03:45
@Author  :   King-Key 
@Version :   1.0
@Contact :   guo_wang_113@163.com
@Blog    :   https://kingkey.club.
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    # 创建应用
    app = QApplication(sys.argv)
    # 创建窗口
    win = QWidget()
    # 设置窗口大小
    win.resize(800, 600)
    # 设置窗口起始位置
    win.move(300, 300)
    # 设置窗口标题
    win.setWindowTitle("gui-1")
    # 显示
    win.show()

    # 安全退出
    sys.exit(app.exec_())

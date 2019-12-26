#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    		: 2019-12-25 17:59:24
# @Author  		: King-Key
# @E-mail  		: guo_wang_113@163.com
# @BlogLink     : kingkey.club
# @Version 		: 1.0

import sys
import random

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text = u"\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430"
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle("draw")
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        #self.drawText(event, qp)
        self.drawPoints(qp)
        qp.end()
    #     #绘制文本
    # def drawText(self, event, qp):
    #     qp.setPen(QColor(168, 34, 3))
    #     qp.setFont(QFont("Decorative", 10))
    #     qp.drawText(event.rect(), Qt.AlignCenter, self.text)
        #绘制点
    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()
        print(size)

        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

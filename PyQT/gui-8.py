#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   gui-8.py
@Time    :   2019/12/15 19:34:53
@Author  :   King-Key 
@Version :   1.0
@Contact :   guo_wang_113@163.com
@Blog    :   https://kingkey.club.
'''

import sys
from PyQt5.QtWidgets import QWidget,QCheckBox,QApplication
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        #复选框
        cb=QCheckBox("show title",self)
        cb.move(20,20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300,300,800,600)
        self.setWindowTitle("qcheakbox")
        self.show()
    
    def changeTitle(self,state):
        if state ==Qt.Checked:
            self.setWindowTitle("qcheckbox")
        else:
            self.setWindowTitle("")

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
from mainFrame import MainFrame

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainFrame()
    window.show()
    app.exec_()
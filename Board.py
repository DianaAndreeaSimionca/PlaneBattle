from PyQt5 import QtCore, QtWidgets, QtGui

# https://stackoverflow.com/questions/12219727/dragging-moving-a-qpushbutton-in-pyqt


class Board(QtWidgets.QGraphicsScene):

    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event):
        super(Board, self).mouseReleaseEvent(event)

        if event.button() == QtCore.Qt.LeftButton:
            return event.globalPos()

    def mouseMoveEvent(self, event):
        super(Board, self).mouseReleaseEvent(event)

        if event.button() == QtCore.Qt.LeftButton:
            return event.globalPos()

    def mouseReleaseEvent(self, event):
        super(Board, self).mouseReleaseEvent(event)

        if event.button() == QtCore.Qt.LeftButton:
            return event.globalPos()

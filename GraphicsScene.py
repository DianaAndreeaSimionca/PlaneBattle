from threading import Lock

from PyQt5 import QtCore, QtWidgets, QtGui


class GraphicsScene(QtWidgets.QGraphicsScene):
    valid_plane_position = None

    def __init__(self):
        super().__init__()

        self.valid_plane_position = 0

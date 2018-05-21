from threading import Lock

from PyQt5 import QtWidgets


class GraphicsScene(QtWidgets.QGraphicsScene):
    valid_plane_position = None
    board_plane = None

    def __init__(self):
        super().__init__()

        self.board_plane = [[0 for x in range(16)] for y in range(16)]
        for i in range(16):
            for j in range(16):
                self.board_plane[i][j] = [False, False, False, False, False]

        self.valid_plane_position = 0

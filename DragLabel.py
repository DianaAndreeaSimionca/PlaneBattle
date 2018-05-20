from threading import Lock

from PyQt5 import QtCore, QtWidgets, QtGui

# https://stackoverflow.com/questions/12219727/dragging-moving-a-qpushbutton-in-pyqt

pen = QtGui.QPen(QtCore.Qt.darkCyan)
brushRed = QtGui.QBrush(QtGui.QColor(255, 15, 15, 70))
brushGreen = QtGui.QBrush(QtGui.QColor(15, 255, 15, 70))


class DragLabel(QtWidgets.QLabel):
    rotation_label = 0
    old_position = None
    array_of_current_pos = []

    row_obj = None
    column_obj = None
    side = 24
    offsetX = 22
    offsetY = -30
    valid_position = None
    obj_id = None
    board_game = [[0 for x in range(16)] for y in range(16)]

    def __init__(self, view, graphics_scene, id):
        super().__init__()

        for i in range(16):
            for j in range(16):
                self.board_game[i][j] = [False, False, False, False, False]

        self.obj_id = id
        self.__mousePressPos = None
        self.__mouseMovePos = None
        self.graphicsScene = graphics_scene

    def verify_valid(self, row, column, dx, dy, release_mouse):
        color = brushGreen
        self.valid_position = True

        for i in range(8):
            if not (0 <= column + dy[i] < 16 and
                    0 <= row + dx[i] < 16):
                self.valid_position = False
                color = brushRed
            else:
                for j in range(5):
                    if self.board_game[column + dy[i]][row + dx[i]][j]:
                        self.valid_position = False
                        color = brushRed

        for i in range(8):
            if 0 <= column + dy[i] < 16 and 0 <= row + dx[i] < 16:
                if release_mouse:
                    if self.valid_position:
                        self.board_game[column + dy[i]][row + dx[i]][self.obj_id] = True
                else:
                    self.board_game[column + dy[i]][row + dx[i]][self.obj_id] = False

                r = QtCore.QRectF(QtCore.QPointF((column + dy[i]) * self.side, (row + dx[i]) * self.side),
                                  QtCore.QSizeF(self.side, self.side))
                rect = QtWidgets.QGraphicsRectItem(r)
                rect.setPen(pen)
                rect.setBrush(color)
                self.graphicsScene.addItem(rect)
                self.array_of_current_pos.append(rect)

    def remove_array_obj(self):
        for obj in self.array_of_current_pos:
            self.graphicsScene.removeItem(obj)

        self.array_of_current_pos.clear()

    def color_x_grade(self, x, y, release_mouse):
        print("X: ", x, " Y: ", y, " S:", len(self.array_of_current_pos))
        self.row_obj = int((x + self.offsetX) / 24)
        self.column_obj = int((y + self.offsetY) / 24)

        self.remove_array_obj()

        if 0 <= self.row_obj <= 16 and 0 <= self.column_obj <= 16:
            if self.rotation_label == 0:
                self.color_0_grade(self.row_obj, self.column_obj, release_mouse)
            if self.rotation_label == 90:
                self.color_90_grade(self.row_obj, self.column_obj, release_mouse)
            if self.rotation_label == 180:
                self.color_180_grade(self.row_obj, self.column_obj, release_mouse)
            if self.rotation_label == 270:
                self.color_270_grade(self.row_obj, self.column_obj, release_mouse)

    def color_0_grade(self, row, column, release_mouse):
        dx = [-2, -1, 0, 0, 0, 0, 0, 1]
        dy = [0, 0, -2, -1, 0, 1, 2, 0]
        self.verify_valid(row, column, dx, dy, release_mouse)

    def color_90_grade(self, row, column, release_mouse):
        dx = [-2, -1, 0, 0, 0, 0, 1, 2]
        dy = [0, 0, -1, 0, 1, 2, 0, 0]
        self.verify_valid(row, column, dx, dy, release_mouse)

    def color_180_grade(self, row, column, release_mouse):
        dx = [-1, 0, 0, 0, 0, 0, 1, 2]
        dy = [0, -2, -1, 0, 1, 2, 0, 0]
        self.verify_valid(row, column, dx, dy, release_mouse)

    def color_270_grade(self, row, column, release_mouse):
        dx = [-2, -1, 0, 0, 0, 0, 1, 2]
        dy = [0, 0, -2, -1, 0, 1, 0, 0]
        self.verify_valid(row, column, dx, dy, release_mouse)

    def get_current_pos(self, event):
        curr_pos = self.mapToGlobal(self.pos())
        global_pos = event.globalPos()
        diff = global_pos - self.__mouseMovePos
        new_pos = self.mapFromGlobal(curr_pos + diff)

        return new_pos

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None

        if event.button() == QtCore.Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

            if self.old_position is None:
                self.old_position = self.get_current_pos(event)

        super(DragLabel, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            new_pos = self.get_current_pos(event)
            self.move(new_pos)

            self.__mouseMovePos = event.globalPos()

            self.color_x_grade(new_pos.y(), new_pos.x(), False)

        super(DragLabel, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
            else:
                self.rotation_label = (self.rotation_label + 90) % 360
                image_name = "images/plane_" + str(self.rotation_label) + ".png"
                self.setPixmap(QtGui.QPixmap(image_name))

            new_pos = self.get_current_pos(event)

            self.color_x_grade(new_pos.y(), new_pos.x(), True)
            if self.valid_position:
                self.move(self.column_obj * self.side - self.offsetY + 12, self.row_obj * self.side - self.offsetX + 3)
            else:
                self.move(self.old_position)
            self.remove_array_obj()

        super(DragLabel, self).mouseReleaseEvent(event)

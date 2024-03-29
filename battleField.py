import socket

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QMessageBox

from GraphicsScene import GraphicsScene
from Worker import Worker


class BattleField(QtWidgets.QWidget):
    graphics_scene_defense = None
    graphics_scene_attack = None

    next_move_shot = None

    side = 24

    def __init__(self, parent=None):
        super(BattleField, self).__init__(parent)
        self.parent = parent

        self.threadpool = QThreadPool()
        self.next_move_shot = False

        layout = QtWidgets.QHBoxLayout()
        self.verticalLayoutWidget = QtWidgets.QWidget()
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 791, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.graphics_scene_defense = GraphicsScene()
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setScene(self.graphics_scene_defense)
        pen = QtGui.QPen(QtCore.Qt.darkCyan)
        for i in range(16):
            for j in range(16):
                r = QtCore.QRectF(QtCore.QPointF(i * self.side, j * self.side), QtCore.QSizeF(self.side, self.side))
                self.graphics_scene_defense.addRect(r, pen)
        self.horizontalLayout.addWidget(self.graphicsView)

        self.graphicsView_2 = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphics_scene_attack = GraphicsScene()
        self.graphicsView_2.setMouseTracking(True)
        self.graphicsView_2.setScene(self.graphics_scene_attack)
        self.graphics_scene_attack.mousePressEvent = self.shot_bullet
        pen = QtGui.QPen(QtCore.Qt.darkCyan)
        for i in range(16):
            for j in range(16):
                r = QtCore.QRectF(QtCore.QPointF(i * self.side, j * self.side), QtCore.QSizeF(self.side, self.side))
                self.graphics_scene_attack.addRect(r, pen)
        self.horizontalLayout.addWidget(self.graphicsView_2)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        layout.addWidget(self.verticalLayoutWidget)
        self.setLayout(layout)

        if type(self.parent.conn) is socket.socket:
            self.next_move_shot = True
        else:
            self.wait_for_shot()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Form", "Battle"))

    def shot_bullet(self, event):
        try:
            if self.next_move_shot:
                self.next_move_shot = False

                row = int(event.scenePos().y() / 24)
                column = int(event.scenePos().x() / 24)

                strout = ('Fire;Row:' + str(row) + ';Column:' + str(column))
                if 0 <= row < 16 and 0 <= column < 16:
                    if type(self.parent.conn) is socket.socket:
                        self.parent.conn.send(strout.encode())
                        self.wait_for_shot()
                    else:
                        self.parent.conn.send(strout.encode()).fire()
                        self.wait_for_shot()
        except Exception as e:
            print(e)

    def wait_for_shot(self):
        worker = Worker(self.receive_shot)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        self.threadpool.start(worker)

    def progress_fn(self, output):
        print("%s" % output)

    def print_output(self, result):
        if result:
            try:
                result = result.decode('utf-8')
                tokens = result.split(';')

                if tokens[0] == 'Fire':
                    row = int(tokens[1].split(':')[1])
                    column = int(tokens[2].split(':')[1])
                    pen = QtGui.QPen(QtCore.Qt.darkCyan)
                    self.graphics_scene_defense.addLine(column * self.side + 2, row * self.side + 2,
                                                        column * self.side + self.side - 2,
                                                        row * self.side + self.side - 2, pen)
                    self.graphics_scene_defense.addLine(column * self.side + self.side - 2, row * self.side + 2,
                                                        column * self.side + 2, row * self.side + self.side - 2, pen)
                    if self.parent.board_plane[row][column]:
                        str_output = 'Result;Shot:Hit;Row:' + str(row) + ';Column:' + str(column)
                        self.parent.board_plane[row][column] = False
                    else:
                        str_output = 'Result;Shot:Miss;Row:' + str(row) + ";Column:" + str(column)

                    if self.finish_match():
                        str_output = str_output + ';Match:Won'
                        if type(self.parent.conn) is socket.socket:
                            self.parent.conn.send(str_output.encode())
                        else:
                            self.parent.conn.send(str_output.encode()).fire()

                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Too bad")
                        msg.setText("Too bad! You lost the match.")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec_()

                    self.next_move_shot = True
                elif tokens[0] == 'Result':
                    result = tokens[1].split(':')[1]
                    row = int(tokens[2].split(':')[1])
                    column = int(tokens[3].split(':')[1])
                    if len(tokens) == 5:
                        match = tokens[4].split(':')
                        if match[1] == 'Won':
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setWindowTitle("Congratulations")
                            msg.setText("Congratulations! You won the match.")
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.exec_()

                    if result == 'Hit':
                        pen = QtGui.QPen(QtCore.Qt.red)
                    else:
                        pen = QtGui.QPen(QtCore.Qt.green)

                    self.graphics_scene_attack.addLine(column * self.side + 2, row * self.side + 2,
                                                       column * self.side + self.side - 2,
                                                       row * self.side + self.side - 2, pen)
                    self.graphics_scene_attack.addLine(column * self.side + self.side - 2, row * self.side + 2,
                                                       column * self.side + 2, row * self.side + self.side - 2, pen)
                    self.next_move_shot = False
                    self.wait_for_shot()

            except Exception as e:
                print(e)

    def thread_complete(self):
        print("THREAD COMPLETE!")

    def finish_match(self):
        for i in range(16):
            for j in range(16):
                if self.parent.board_plane[i][j]:
                    return False
        return True

    def receive_shot(self, progress_callback):
        try:
            progress_callback.emit('Waiting for message. . .')
            if type(self.parent.conn) is socket.socket:
                data = self.parent.conn.recv(1024)
            else:
                data = self.parent.conn.recv(1024).fire()
        except Exception as e:
            data = 'NULL'
            print(e)
        finally:
            return data
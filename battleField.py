import socket

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QMessageBox

from DragLabel import DragLabel
from GraphicsScene import GraphicsScene
from Worker import Worker


class BattleField(QtWidgets.QWidget):
    graphics_scene_defense = None
    graphics_scene_attack = None

    side = 24

    def __init__(self, parent=None):
        super(BattleField, self).__init__(parent)

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
            self.wait_for_shot()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Form", "Battle"))

    def shot_bullet(self, event):
        try:
            row = event.scenePos().y()
            column = event.scenePos().x()

            if 0 <= row < 16 and 0 <= column < 16:
                if type(self.parent.conn) is socket.socket:
                    self.parent.conn.send(('Fire;Row:' + row + ';Column:' + column).encode())
                else:
                    self.parent.conn.send(('Fire;Row:' + row + ';Column:' + column).encode())
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
                row = tokens[1].split(':')
                column = tokens[2].split(':')

                if tokens[0] == 'Fire':
                    pen = QtGui.QPen(QtCore.Qt.darkCyan)
                    self.graphics_scene_defense.addLine(row + 2, column + 2, row + self.side - 2,
                                                        column + self.side - 2, pen)
                    self.graphics_scene_defense.addLine(row + 2, column + self.side - 2,
                                                        row + self.side - 2, column + 2,pen)
            except Exception as e:
                print(e)

    def thread_complete(self):
        print("THREAD COMPLETE!")

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
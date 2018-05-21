import socket

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import QMessageBox

from DragLabel import DragLabel
from GraphicsScene import GraphicsScene
from Worker import Worker


class PrepareBattle(QtWidgets.QWidget):
    graphics_scene = None
    other_player_is_set = None

    def __init__(self, parent=None):
        super(PrepareBattle, self).__init__(parent)
        self.threadpool = QThreadPool()
        layout = QtWidgets.QHBoxLayout()
        self.parent = parent
        self.other_player_is_set = False

        self.verticalLayoutWidget = QtWidgets.QWidget()
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 791, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setObjectName("graphicsView")

        self.graphics_scene = GraphicsScene()
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setScene(self.graphics_scene)
        pen = QtGui.QPen(QtCore.Qt.darkCyan)

        side = 24

        for i in range(16):
            for j in range(16):
                r = QtCore.QRectF(QtCore.QPointF(i * side, j * side), QtCore.QSizeF(side, side))
                self.graphics_scene.addRect(r, pen)

        self.horizontalLayout.addWidget(self.graphicsView)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        pixmap = QtGui.QPixmap("images/plane_0.png")

        self.label_2 = DragLabel(self.verticalLayoutWidget, self.graphics_scene, 0)
        self.label_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setAcceptDrops(True)
        self.label_2.setText("")
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.setMouseTracking(True)
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = DragLabel(self.verticalLayoutWidget, self.graphics_scene, 1)
        self.label_3.setMinimumSize(QtCore.QSize(100, 100))
        self.label_3.setMaximumSize(QtCore.QSize(100, 100))
        self.label_3.setAcceptDrops(True)
        self.label_3.setText("")
        self.label_3.setPixmap(pixmap)
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.setMouseTracking(True)
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = DragLabel(self.verticalLayoutWidget, self.graphics_scene, 2)
        self.label_4.setMinimumSize(QtCore.QSize(100, 100))
        self.label_4.setMaximumSize(QtCore.QSize(100, 100))
        self.label_4.setAcceptDrops(True)
        self.label_4.setText("")
        self.label_4.setPixmap(pixmap)
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_4.setMouseTracking(True)
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label = DragLabel(self.verticalLayoutWidget, self.graphics_scene, 3)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.label.setAcceptDrops(True)
        self.label.setText("")
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.setMouseTracking(True)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = DragLabel(self.verticalLayoutWidget, self.graphics_scene, 4)
        self.label_5.setMinimumSize(QtCore.QSize(100, 100))
        self.label_5.setMaximumSize(QtCore.QSize(100, 100))
        self.label_5.setAcceptDrops(True)
        self.label_5.setText("")
        self.label_5.setPixmap(pixmap)
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_5.setMouseTracking(True)
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.click_battle_now)
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        layout.addWidget(self.verticalLayoutWidget)
        self.setLayout(layout)

        self.wait_for_message()

    def click_battle_now(self):
        print('Battle')
        if self.graphics_scene.valid_plane_position != 0:
            try:
                self.parent.conn.send('Im set'.encode())
            except Exception as e:
                print(e)
            if self.other_player_is_set:
                print('Battle Time')
            else:
                print('Im ready')
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setWindowTitle("Error. . .")
            msg.setText("Invalid values")
            msg.setInformativeText("Not all the planes are set in the board")
            msg.setStandardButtons(QMessageBox.Ok)

            msg.exec_()

    def wait_for_message(self):
        worker = Worker(self.receive_message)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        self.threadpool.start(worker)

    def progress_fn(self, output):
        print("%s" % output)

    def print_output(self, result):
        print(result)
        if result:
            print(result)

    def thread_complete(self):
        print("THREAD COMPLETE!")

    def receive_message(self, progress_callback):
        try:
            progress_callback.emit('Waiting for message. . .')
            if type(self.parent.conn) is socket.socket:
                data = self.parent.conn.recv(1024)
            else:
                data = self.parent.conn.recv(1024).fire()
        except Exception as e:
            data = 'NULL'
        finally:
            return data


    def rotatePlane(self, arg):
        print('Test')

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Form", "Battle"))
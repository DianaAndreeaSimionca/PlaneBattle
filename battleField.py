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
    opponent_player = None
    self_player = None

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
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setScene(self.graphics_scene_attack)
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

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Form", "Battle"))
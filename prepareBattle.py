from PyQt5 import QtCore, QtWidgets, QtGui, Qt

from DragLabel import DragLabel


class PrepareBattle(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PrepareBattle, self).__init__(parent)
        layout = QtWidgets.QHBoxLayout()
        self.parent = parent

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

        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setScene(scene)
        pen = QtGui.QPen(QtCore.Qt.darkCyan)

        side = 24
        #scene.remove

        for i in range(16):
            for j in range(16):
                r = QtCore.QRectF(QtCore.QPointF(i * side, j * side), QtCore.QSizeF(side, side))
                scene.addRect(r, pen)

        self.horizontalLayout.addWidget(self.graphicsView)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        pixmap = QtGui.QPixmap("images/plane_0.png")

        self.label_2 = DragLabel(self.verticalLayoutWidget, scene, 0)
        self.label_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setAcceptDrops(True)
        self.label_2.setText("")
        self.label_2.setPixmap(pixmap)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.setMouseTracking(True)
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = DragLabel(self.verticalLayoutWidget, scene, 1)
        self.label_3.setMinimumSize(QtCore.QSize(100, 100))
        self.label_3.setMaximumSize(QtCore.QSize(100, 100))
        self.label_3.setAcceptDrops(True)
        self.label_3.setText("")
        self.label_3.setPixmap(pixmap)
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.setMouseTracking(True)
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = DragLabel(self.verticalLayoutWidget, scene, 2)
        self.label_4.setMinimumSize(QtCore.QSize(100, 100))
        self.label_4.setMaximumSize(QtCore.QSize(100, 100))
        self.label_4.setAcceptDrops(True)
        self.label_4.setText("")
        self.label_4.setPixmap(pixmap)
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_4.setMouseTracking(True)
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label = DragLabel(self.verticalLayoutWidget, scene, 3)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.label.setAcceptDrops(True)
        self.label.setText("")
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.setMouseTracking(True)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = DragLabel(self.verticalLayoutWidget, scene, 4)
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
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        layout.addWidget(self.verticalLayoutWidget)
        self.setLayout(layout)

    def rotatePlane(self, arg):
        print('Test')

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Form", "Battle"))
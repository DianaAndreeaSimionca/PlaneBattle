from PyQt5 import QtCore, QtWidgets


class PlayerTypeWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PlayerTypeWidget, self).__init__(parent)
        layout = QtWidgets.QHBoxLayout()

        self.verticalLayoutWidget_2 = QtWidgets.QWidget()
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 731, 481))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(parent.back_button_clicked)
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(240, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(parent.hostClicked)
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(240, 60))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(parent.guestClicked)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        layout.addWidget(self.verticalLayoutWidget_2)
        self.setLayout(layout)

    # todo: change the name of the function with lower case
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Form", "Host Mode"))
        self.pushButton_2.setText(_translate("Form", "Guest Mode"))
        self.pushButton_3.setText(_translate("Form", "Back"))

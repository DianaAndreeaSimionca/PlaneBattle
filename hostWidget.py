from PyQt5 import QtCore, QtWidgets
import netifaces as ni
import socket

from PyQt5.QtCore import QThreadPool

from Worker import Worker


class HostWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(HostWidget, self).__init__(parent)
        layout = QtWidgets.QHBoxLayout()
        self.parent = parent

        ni.ifaddresses('en0')

        try:
            self.ip = "Your IP Address: " + ni.ifaddresses('en0')[ni.AF_INET][0]['addr']
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except KeyError:
            self.ip = "There is a problem try again. . ."

        self.verticalLayoutWidget = QtWidgets.QWidget()
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 811, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.back_button_clicked)
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        layout.addWidget(self.verticalLayoutWidget)
        self.setLayout(layout)

        self.wait_for_client()

    def back_button_clicked(self):
        try:
            self.socket.close()
        except AttributeError as e:
            print("Catch an error. . .")
        self.parent.back_button_clicked()

    def wait_for_client(self):
        worker = Worker(self.wait_client_thread)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        threadpool = QThreadPool()
        threadpool.start(worker)

    def progress_fn(self, output):
        print("%s" % output)

    def print_output(self, result):
        print(result)
        if result:
            self.parent.conn = result
            self.parent.goto_prepare_battle()

    def thread_complete(self):
        print("THREAD COMPLETE!")

    def wait_client_thread(self, progress_callback):
        try:
            progress_callback.emit('Waiting for clients. . .')

            self.socket.bind(('', 8000))
            self.socket.listen(1)
            conn, addr = self.socket.accept()

            return conn
        except (TimeoutError, ConnectionRefusedError, ConnectionAbortedError, ConnectionError, OSError) as e:
            print('Catch the error')
            self.socket.close()
            return False
        except AttributeError as e:
            return False

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(self.ip)
        self.pushButton.setText(_translate("Form", "Back"))

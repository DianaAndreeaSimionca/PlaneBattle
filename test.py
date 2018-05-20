import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QApplication


def widgets_at(pos):
    """Return ALL widgets at `pos`

    Arguments:
        pos (QPoint): Position at which to get widgets

    """

    widgets = []
    widget_at = QtWidgets.qApp.widgetAt(pos)

    while widget_at:
        widgets.append(widget_at)

        # Make widget invisible to further enquiries
        widget_at.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        widget_at = QtWidgets.qApp.widgetAt(pos)

    # Restore attribute
    for widget in widgets:
        widget.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, False)

    return widgets

class Overlay(QWidget):
    def __init__(self, parent=None):
        super(Overlay, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.setStyleSheet("QWidget { background-color: rgba(0, 255, 0, 50) }")

    def mousePressEvent(self, event):
        pos = event.globalPos()
        print([w.objectName() for w in widgets_at(pos)])
        return super(Overlay, self).mousePressEvent(event)


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setObjectName("Window")
window.setFixedSize(200, 100)

button = QtWidgets.QPushButton("Button 1", window)
button.setObjectName("Button 1")
button.move(10, 10)
button = QtWidgets.QPushButton("Button 2", window)
button.setObjectName("Button 2")
button.move(50, 15)
overlay = Overlay(window)
overlay.setObjectName("Overlay")
overlay.setFixedSize(window.size())

window.show()
app.exec_()
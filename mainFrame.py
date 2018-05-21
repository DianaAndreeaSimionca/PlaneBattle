from PyQt5 import QtWidgets
from loginWidget import LoginWidget
from playerTypeWidget import PlayerTypeWidget
from hostWidget import HostWidget
from guestWidget import GuestWidget
from prepareBattle import PrepareBattle
from battleField import BattleField


class MainFrame(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainFrame, self).__init__(parent)
        self.setWindowTitle('Planes Battle')
        self.resize(830, 530)
        self.setMouseTracking(True)
        self.setFixedSize(830, 530)

        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        login_widget = LoginWidget(self)
        self.central_widget.addWidget(login_widget)

    def loginClicked(self):
        logged_in_widget = PlayerTypeWidget(self)
        self.central_widget.addWidget(logged_in_widget)
        self.central_widget.setCurrentWidget(logged_in_widget)

    def hostClicked(self):
        #self.goto_battle_field()
        host_widget = HostWidget(self)
        self.central_widget.addWidget(host_widget)
        self.central_widget.setCurrentWidget(host_widget)

    def guestClicked(self):
        guest_widget = GuestWidget(self)
        self.central_widget.addWidget(guest_widget)
        self.central_widget.setCurrentWidget(guest_widget)

    def goto_prepare_battle(self):
        prepare_widget = PrepareBattle(self)
        self.central_widget.addWidget(prepare_widget)
        self.central_widget.setCurrentWidget(prepare_widget)

    def goto_battle_field(self):
        battle_field = BattleField(self)
        self.central_widget.addWidget(battle_field)
        self.central_widget.setCurrentWidget(battle_field)

    def back_button_clicked(self):
        print('Back Button Clicked')
        self.central_widget.removeWidget(self.central_widget.currentWidget())

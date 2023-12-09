from PyQt6.QtWidgets import *
from gui import *


class Television(QMainWindow, Ui_MainWindow):
    """
    A class representing details for a Television object
    """
    def __init__(self) -> None:
        """
        Method that creates a Television object that starts turned off,
        not muted, a volume starting at 0, and a channel starting at 0
        """
        super().__init__()
        self.setupUi(self)

        self.status = False
        self.muted = False
        self.volume = 0
        self.channel = 0

        self.button_channel_down.clicked.connect(lambda: self.channel_changed(0))
        self.button_channel_up.clicked.connect(lambda: self.channel_changed(1))
        self.power_button.clicked.connect(lambda: self.power())
        self.mute_button.clicked.connect(lambda: self.mute())
        self.volume_slider.valueChanged.connect(lambda: self.volume_changed)

    def power(self) -> None:
        """
        Turns the TV On if it is Off and Off if it is On
        """
        self.status = not self.status
        if not self.status:
            self.button_channel_down.pyqtConfigure(enabled=False)
            self.button_channel_up.pyqtConfigure(enabled=False)
            self.volume_slider.pyqtConfigure(enabled=False)
            self.mute_button.pyqtConfigure(enabled=False)
            self.tele.setPixmap(QtGui.QPixmap("C:\\Users\\taz04\\PycharmProjects\\python\\black.png"))
        else:
            self.button_channel_down.pyqtConfigure(enabled=True)
            self.button_channel_up.pyqtConfigure(enabled=True)
            self.volume_slider.pyqtConfigure(enabled=True)
            self.mute_button.pyqtConfigure(enabled=True)
            self.channel_changed(2)

    def mute(self) -> None:
        """
        Mutes the TV if it is Unmuted and Unmutes the TV if it is Muted
        """
        self.muted = not self.muted
        if self.muted:
            self.volume_slider.pyqtConfigure(enabled=False)
        else:
            self.volume_slider.pyqtConfigure(enabled=True)
        self.volume_changed()

    def channel_changed(self, operation) -> None:
        """
        Changes the picture of the channel that is being shown to the user based on the operation given to
        it, which can be either 0 for down 1 for up and any other number to display the current channel
        """
        if operation == 0:
            if self.channel == 0:
                self.tele.setPixmap(QtGui.QPixmap("C:\\Users\\taz04\\PycharmProjects\\python\\fox.png"))
                self.channel = 3
            elif self.channel == 1:
                self.tele.setPixmap(QtGui.QPixmap("C:\\Users\\taz04\\PycharmProjects\\python\\abc.png"))
                self.channel = 0
            elif self.channel == 2:
                self.tele.setPixmap(QtGui.QPixmap("C:\\Users\\taz04\\PycharmProjects\\python\\cnn.png"))
                self.channel = 1
            elif self.channel == 3:
                self.tele.setPixmap(QtGui.QPixmap("C:\\Users\\taz04\\PycharmProjects\\python\\espn.png"))
                self.channel = 2
        elif operation == 1:
            if self.channel == 0:
                self.tele.setPixmap(QtGui.QPixmap("C:\\Users\\taz04\\PycharmProjects\\python\\cnn.png"))
                self.channel = 1
            elif self.channel == 1:
                self.tele.setPixmap(QtGui.QPixmap("C:\\Users\\taz04\\PycharmProjects\\python\\espn.png"))
                self.channel = 2
            elif self.channel == 2:
                self.tele.setPixmap(QtGui.QPixmap("C:\\Users\\taz04\\PycharmProjects\\python\\fox.png"))
                self.channel = 3
            elif self.channel == 3:
                self.tele.setPixmap(QtGui.QPixmap("C:\\Users\\taz04\\PycharmProjects\\python\\abc.png"))
                self.channel = 0
        else:
            if self.channel == 0:
                self.tele.setPixmap(QtGui.QPixmap("C:\\Users\\taz04\\PycharmProjects\\python\\abc.png"))
            elif self.channel == 1:
                self.tele.setPixmap(QtGui.QPixmap("C:\\Users\\taz04\\PycharmProjects\\python\\cnn.png"))
            elif self.channel == 2:
                self.tele.setPixmap(QtGui.QPixmap("C:\\Users\\taz04\\PycharmProjects\\python\\espn.png"))
            elif self.channel == 3:
                self.tele.setPixmap(QtGui.QPixmap("C:\\Users\\taz04\\PycharmProjects\\python\\fox.png"))

    def volume_changed(self) -> None:
        """
        Changes the TV's volume variable to 0 if the TV is muted and to the slider value if the TV is not muted
        """
        if self.muted:
            self.volume = 0
        else:
            self.volume = self.volume_slider.value()

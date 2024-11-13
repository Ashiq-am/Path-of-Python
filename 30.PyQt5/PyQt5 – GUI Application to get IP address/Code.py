# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import requests
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 400, 500)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        # create push button to perform function
        push = QPushButton("Press", self)

        # setting geometry to the push button
        push.setGeometry(125, 100, 150, 40)

        # creating label to show the ip
        self.label = QLabel("Press button to see your IP", self)

        # setting geometry to the push button
        self.label.setGeometry(100, 200, 200, 40)

        # setting alignment to the text
        self.label.setAlignment(Qt.AlignCenter)

        # adding border to the label
        self.label.setStyleSheet("border : 3px solid black;")

        # adding action to the push button
        push.clicked.connect(self.get_ip)

    # method called by push
    def get_ip(self):
        # getting data
        r = requests.get("http://httpbin.org / ip")

        # json data with key as origin
        ip = r.json()['origin']

        # parsing the data
        parsed = ip.split(", ")[0]

        # showing the ip in label
        self.label.setText(parsed)

        # setting font
        self.label.setFont(QFont('Times', 12))


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec())

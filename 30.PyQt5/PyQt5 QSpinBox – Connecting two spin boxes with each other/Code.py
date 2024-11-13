# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        # creating spin box
        self.spin1 = QSpinBox(self)

        # setting geometry to spin box
        self.spin1.setGeometry(100, 100, 150, 40)

        # setting prefix to spin
        self.spin1.setPrefix("Width : ")

        # add action to this spin box
        self.spin1.valueChanged.connect(self.action_spin1)

        # creating another spin box
        self.spin2 = QSpinBox(self)

        # setting geometry to spin box
        self.spin2.setGeometry(300, 100, 150, 40)

        # setting prefix to spin box
        self.spin2.setPrefix("Height : ")

        # add action to this spin box
        self.spin2.valueChanged.connect(self.action_spin2)

    # method called after editing finished
    def action_spin1(self):
        # getting current value of spin box
        current = self.spin1.value()

        # setting this value to second spin box
        self.spin2.setValue(current)

    # method called after editing finished
    def action_spin2(self):
        # getting current value of spin box
        current = self.spin2.value()

        # setting this value to the first spin box
        self.spin1.setValue(current)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())

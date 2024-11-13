# importing the required libraries
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title
        self.setWindowTitle("Tooltip")

        # set the geometry
        self.setGeometry(0, 0, 300, 300)

        # creating a button widget
        self.widget = QPushButton('Widget', self)

        # setting up the tooltip
        self.widget.setToolTip("This is a button widget !")

        # show all the widgets
        self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())

# importing libraries
from bs4 import BeautifulSoup as BS
import requests
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("PyQt5 Bit Coin ")

        # setting geometry
        self.setGeometry(100, 100, 400, 600)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        # creating label to show bit coin price
        self.label = QLabel("//BIT-COIN//", self)

        # setting geometry of label
        self.label.setGeometry(50, 150, 300, 50)

        # setting its alignment
        self.label.setAlignment(Qt.AlignCenter)

        # setting font to the label
        self.label.setFont(QFont('Times', 15))

        # setting border to the push button
        self.label.setStyleSheet("border : 3px solid black;")

        # creating push button to show current price
        button = QPushButton("Show price", self)

        # setting geometry to push button
        button.setGeometry(150, 300, 100, 40)

        # adding method to the push button
        button.clicked.connect(self.show_price)

        # setting tool tip to button
        button.setToolTip("Press to get Bit Coin Price")

    def show_price(self):
        # url of the bit coin price
        url = "https://www.google.com/search?q = bitcoin + price"

        # getting the request from url
        data = requests.get(url)

        # converting the text
        soup = BS(data.text, 'html.parser')

        # finding metha info for the current price
        ans = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text

        # setting this price to the label
        self.label.setText(ans)


# create pyqt5 app

App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())

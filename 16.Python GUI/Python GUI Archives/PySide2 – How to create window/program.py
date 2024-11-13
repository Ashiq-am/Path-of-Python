# import system module
import sys

# import PySide2 modules
from PySide2.QtWidgets import QApplication, QWidget

# create new app
app = QApplication(sys.argv)

# create main window
mainwindow = QWidget()

# resize window to 550 * 400
mainwindow.resize(550, 400)

# set title to the window frame
mainwindow.setWindowTitle('GeeksForGeeks')

# invoke show function
mainwindow.show()

# to kee in loop invoke exec_() function
app.exec_()

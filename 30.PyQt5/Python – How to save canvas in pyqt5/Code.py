# importing modules
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


# creating class fo winow
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Paint and save Application"

        top = 400
        left = 400
        width = 800
        height = 600

        # setting title of window
        self.setWindowTitle(title)

        # setting geometry
        self.setGeometry(top, left, width, height)

        # creating canvas
        self.image = QImage(self.size(), QImage.Format_RGB32)

        # setting canvas color to white
        self.image.fill(Qt.white)

        # creating menu bar
        mainMenu = self.menuBar()

        # adding file menu in it
        fileMenu = mainMenu.addMenu("File")

        # creating save action
        saveAction = QAction("Save", self)

        # setting save action shortcut
        saveAction.setShortcut("Ctrl + S")

        # adding save action to filemenu
        fileMenu.addAction(saveAction)

        # setting triggered method
        saveAction.triggered.connect(self.save)

        # calling draw_something method
        self.draw_something()

    # paintEvent for creating blank canvas
    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image,
                                self.image.rect())

    # this method will draw a line
    def draw_something(self):
        painter = QPainter(self.image)

        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine,
                            Qt.RoundCap, Qt.RoundJoin))

        # drawing a line
        painter.drawLine(100, 100, 300, 300)

        # updating it to canvas
        self.update()

    # save method
    def save(self):
        # selecting file path
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        # if file path is blank return back
        if filePath == "":
            return

        # saving canvas at desired path
        self.image.save(filePath)


# main method
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    # looping for window
    sys.exit(app.exec())

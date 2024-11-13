from PyQt5.uic.properties import QtWidgets


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyQt5 Demo App')
        self.initGui()

    def initGui(self):
        self.layout = QtWidgets.QGridLayout()
        self.window = QtWidgets.QWidget()
        self.window.setLayout(self.layout)
        self.setCentralWidget(self.window)

        self.num1_label = QtWidgets.QLabel('Enter first number:')
        self.num1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.text_box1 = QtWidgets.QLineEdit()
        self.num2_label = QtWidgets.QLabel('Enter second number:')
        self.text_box2 = QtWidgets.QLineEdit()

        self.get_answer = QtWidgets.QPushButton()
        calculate_icon = QtGui.QPixmap('path_to_image.png')
        self.get_answer.setIcon(QtGui.QIcon(calculate_icon))

        self.answer_label = QtWidgets.QLabel('---')

        self.layout.addWidget(self.num1_label, 0, 0)
        self.layout.addWidget(self.text_box1, 1, 0)
        self.layout.addWidget(self.num2_label, 2, 0)
        self.layout.addWidget(self.text_box2, 3, 0)
        self.layout.addWidget(self.get_answer, 4, 0)
        self.layout.addWidget(self.answer_label, 5, 0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    win = Window()
    win.show()

    sys.exit(app.exec_())

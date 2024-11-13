import sys
from PyQt5.QtWidgets import (QGridLayout)
from PyQt5.QtWidgets import (QMainWindow)
from PyQt5.QtWidgets import (QApplication)
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit
)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPixmap, QIcon)


class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyQt5 Demo App')
        self.initGui()

    def initGui(self):
        self.layout = QGridLayout()
        self.window = QWidget()
        self.window.setLayout(self.layout)
        self.setCentralWidget(self.window)

        self.num1_label = QLabel('Enter first number:')
        self.num1_label.setAlignment(Qt.AlignCenter)
        self.text_box1 = QLineEdit()
        self.num2_label = QLabel('Enter second number:')
        self.text_box2 = QLineEdit()

        self.get_answer = QPushButton()
        calculate_icon = QPixmap('path_to_image.png')
        self.get_answer.setIcon(QIcon(calculate_icon))

        self.answer_label = QLabel('---')

        self.layout.addWidget(self.num1_label, 0, 0)
        self.layout.addWidget(self.text_box1, 1, 0)
        self.layout.addWidget(self.num2_label, 2, 0)
        self.layout.addWidget(self.text_box2, 3, 0)
        self.layout.addWidget(self.get_answer, 4, 0)
        self.layout.addWidget(self.answer_label, 5, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = Window()
    win.show()

    sys.exit(app.exec_())

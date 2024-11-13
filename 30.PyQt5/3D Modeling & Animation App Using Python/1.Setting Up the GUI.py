class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('3D Modeling & Animation App')

        layout = QVBoxLayout()
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.glWidget = GLWidget()
        layout.addWidget(self.glWidget)

        btn_create_object = QPushButton('Create Object', self)
        btn_create_object.clicked.connect(self.create_object)
        layout.addWidget(btn_create_object)

        self.show()

    def create_object(self):
        print('Creating 3D object...')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

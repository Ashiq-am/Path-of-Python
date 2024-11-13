class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.init_gui()

	def init_gui(self):
		self.window = QtWidgets.QWidget()
		self.layout = QtWidgets.QGridLayout()
		self.setCentralWidget(self.window)
		self.window.setLayout(self.layout)

		self.textbox = QtWidgets.QLineEdit()
		self.echo_label = QtWidgets.QLabel('')

		self.textbox.textChanged.connect(self.textbox_text_changed)

		self.layout.addWidget(self.textbox, 0, 0)
		self.layout.addWidget(self.echo_label, 1, 0)

	def textbox_text_changed(self):
		self.echo_label.setText(self.textbox.text())

class MyWidget(QtWidgets.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.layout = QtWidgets.QGridLayout()
		self.setLayout(self.layout)

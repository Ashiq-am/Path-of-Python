class FileRenamer(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		# Create a label for the folder selection
		self.folderLabel = QtWidgets.QLabel('Folder:')
		# Create a line edit for displaying the selected folder
		self.folderEdit = QtWidgets.QLineEdit()
		# Create a button for selecting the folder
		self.folderButton = QtWidgets.QPushButton('Browse...')
		# Create a label for the search pattern
		self.searchLabel = QtWidgets.QLabel('Search Pattern:')
		# Create a line edit for the search pattern
		self.searchEdit = QtWidgets.QLineEdit()
		# Create a label for the replacement string
		self.replaceLabel = QtWidgets.QLabel('Replacement:')
		# Create a line edit for the replacement string
		self.replaceEdit = QtWidgets.QLineEdit()
		# Create a rename button
		self.renameButton = QtWidgets.QPushButton('Rename')

		# Create a grid layout and add the widgets to it
		layout = QtWidgets.QGridLayout()
		layout.addWidget(self.folderLabel, 0, 0)
		layout.addWidget(self.folderEdit, 0, 1)
		layout.addWidget(self.folderButton, 0, 2)
		layout.addWidget(self.searchLabel, 1, 0)
		layout.addWidget(self.searchEdit, 1, 1)
		layout.addWidget(self.replaceLabel, 2, 0)
		layout.addWidget(self.replaceEdit, 2, 1)
		layout.addWidget(self.renameButton, 3, 1)
		self.setLayout(layout)

		# Set the window title
		self.setWindowTitle('Bulk File Rename Tool')
		# Set the window icon
		self.setWindowIcon(QtGui.QIcon('icon.png'))

		# Connect the folder selection button to the folderSelection method
		self.folderButton.clicked.connect(self.folderSelection)
		# Connect the rename button to the renameFiles method
		self.renameButton.clicked.connect(self.renameFiles)

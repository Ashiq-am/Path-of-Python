def folderSelection(self):
    # Show a folder selection dialog and set the selected
    # folder in the line edit
    folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
    self.folderEdit.setText(folder)

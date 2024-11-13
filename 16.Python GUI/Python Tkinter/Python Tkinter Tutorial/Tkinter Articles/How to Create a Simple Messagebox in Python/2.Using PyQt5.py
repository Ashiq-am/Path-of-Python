from PyQt5.QtWidgets import QApplication, QMessageBox

app = QApplication([])

msg_box = QMessageBox()
msg_box.setIcon(QMessageBox.Information)
msg_box.setWindowTitle("MessageBox 2")
msg_box.setText("Hello GeeksforGeeks Once Again")
msg_box.exec_()

app.exec_()

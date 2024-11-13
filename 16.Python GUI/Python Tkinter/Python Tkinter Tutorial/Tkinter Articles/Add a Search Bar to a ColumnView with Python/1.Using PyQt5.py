import sys
from PyQt5.QtWidgets import QApplication, QColumnView, QFileSystemModel, QVBoxLayout, QLineEdit, QWidget

class GFG(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Search ColumnView')
        layout = QVBoxLayout(self)

        # Create search bar
        self.search_bar = QLineEdit(self)
        self.search_bar.textChanged.connect(self.filter_items)
        layout.addWidget(self.search_bar)

        # Create ColumnView
        self.column_view = QColumnView(self)
        model = QFileSystemModel()
        model.setRootPath('')
        self.column_view.setModel(model)
        layout.addWidget(self.column_view)
        self.setLayout(layout)

    def filter_items(self):
        search_query = self.search_bar.text()


        # Filter items based on search query
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GFG()
    window.show()
    sys.exit(app.exec_())

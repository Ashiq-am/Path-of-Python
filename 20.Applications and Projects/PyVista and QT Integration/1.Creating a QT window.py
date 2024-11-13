from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget


# Define a custom MainWindow class that inherits from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle('PyVistaQT Integration')

        # Set the geometry of the window
        # (position and size on the screen)
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget for the main window;
        # this is where other widgets will be placed
        central_widget = QWidget()

        # Set the central widget in the main window,
        # so it occupies the central area
        self.setCentralWidget(central_widget)

        # Create a vertical box layout,
        # which arranges widgets vertically
        layout = QVBoxLayout()

        # Assign the layout to the central widget
        central_widget.setLayout(layout)


# Create an instance of QApplication,
# which manages the GUI application’s control flow and main settings
app = QApplication([])

# Create an instance of the MainWindow class
window = MainWindow()

# Display the window on the screen
window.show()

# Start the event loop,
# which waits for and dispatches events such as user interactions
app.exec_()

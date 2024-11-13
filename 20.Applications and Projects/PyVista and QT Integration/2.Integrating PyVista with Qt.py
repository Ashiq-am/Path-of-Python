import pyvista as pv
import pyvistaqt as pvqt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set the window title
        self.setWindowTitle('PyVista QT Integration')
        # Set the window position and size (x, y, width, height)
        self.setGeometry(100, 100, 800, 600)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a vertical box layout to arrange widgets vertically
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Initialize a PyVistaQt interactor to embed PyVista in the Qt app
        self.plotter = pvqt.QtInteractor(self)
        layout.addWidget(self.plotter.interactor)

        # Create and add a 3D sphere mesh to the plotter for visualization
        self.plotter.add_mesh(pv.Sphere())
        self.plotter.show_grid()

# Set up the Qt application
app = QApplication([])
window = MainWindow()
window.show()

 # Start the event loop to keep
 # the application running and responsive to user interactions
app.exec_()

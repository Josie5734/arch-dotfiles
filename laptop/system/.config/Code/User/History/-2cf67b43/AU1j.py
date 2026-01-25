from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys 



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("The Pest Professor") # window title

        button = QPushButton("click") # make a button widget

        self.setCentralWidget(button) # set the button as the main widget of the main window



app = QApplication(sys.argv) # QApplication instance for command line arguments

window = MainWindow() # the main window object
window.show() # show the window

app.exec() # start the program

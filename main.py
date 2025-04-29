import sys
import threading
import random
from PySide6 import QtCore, QtWidgets, QtGui



class discordBot(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Submit")
        self.label = QtWidgets.QLabel("Enter key:")
        self.input_box = QtWidgets.QLineEdit(self)
        self.input_box.setMaximumSize(1000,25)
        
        

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input_box)
        self.layout.addWidget(self.button)
        

        self.setLayout(self.layout)
        self.show()
        self.button.clicked.connect(handletext(self))

def handletext(self):
    graph_thread = threading.Thread(target=sendtext(self), daemon=True)
    graph_thread.start()

    
def sendtext(self):
    a


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    widget = discordBot()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())


import json
import http.client
import sys
import threading
import random
from PySide6 import QtCore, QtWidgets, QtGui
import requests



class discordBot(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("QLabel {background: lightgrey}")
        oImage = QtGui.QImage("DiscordLogo.jpg")
        sImage = oImage.scaled(QtCore.QSize(800,600))
        #pixmap = QtGui.QPixmap('DiscordLogo.jpg')
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.ColorRole.Window, QtGui.QBrush(sImage))
        self.setPalette(palette)
        
        

        self.setFixedWidth(800)
        self.setFixedHeight(600)
        self.button = QtWidgets.QPushButton("Submit")
        self.label = QtWidgets.QLabel("Enter key:")
        self.input_box = QtWidgets.QLineEdit(self)
        self.input_box.setPlaceholderText("Enter UUID")
        self.label.setMaximumHeight(20)
        self.label.setMinimumWidth(75)
        self.label.setAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)
        
        
        

        self.myframe = QtWidgets.QFrame()
        self.myframe.setFrameStyle(QtWidgets.QFrame.Shape.StyledPanel | QtWidgets.QFrame.Shadow.Plain)
        

        buttonlayout = QtWidgets.QHBoxLayout(self.myframe) 
        buttonlayout.addWidget(self.label)
        buttonlayout.addWidget(self.input_box)
        buttonlayout.addWidget(self.button)

        

        self.setLayout(buttonlayout)
        self.show()
        text = self.input_box.text()
        #self.button.clicked.connect(handletext(self))
        self.button.clicked.connect(self.buttonClick)
    
    def buttonClick(self):
        text = self.input_box.text()
        sendtext(text)
        self.input_box.setText("")



def handletext(self):
    text_thread = threading.Thread(target=sendtext(self), daemon=True)
    text_thread.start()

   
def sendtext(text):
    

    data = {
        'method': 'auth',
        'auth': text

    }

    json_data = json.dumps(data)

    try:
        
        conn = http.client.HTTPConnection("127.0.0.1", 8000)
        conn.request("POST", "/", body=json_data, headers={'Content-Type': 'application/json'})
        #response = requests.post(url, data=json.dumps(self), headers={'Content-Type': 'application/json'})

        response = conn.getresponse()
        print(response)
        

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    except Exception as e:
        print(f"A System error has occured: {e}", file=sys.stderr)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    widget = discordBot()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())


import json
import sys
import threading
from PySide6 import QtCore, QtWidgets, QtGui
import requests
#from.thirdWindow import thirdWindow

id = {"uuid": ""}

class thirdWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("QLabel {background: lightgrey}")
        oImage = QtGui.QImage("DiscordLogo.jpg")
        sImage = oImage.scaled(QtCore.QSize(1000,800))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.ColorRole.Window, QtGui.QBrush(sImage))
        self.setPalette(palette)

        self.setFixedWidth(800)
        self.setFixedHeight(600)

        
        self.scroll = QtWidgets.QScrollArea()
        
       
        self.button3 = QtWidgets.QPushButton("GO BACK")
        self.button4 = QtWidgets.QPushButton("Enter into the Queue")

        self.input_box3 = QtWidgets.QLineEdit(self)
        

        self.myframe3 = QtWidgets.QFrame()
        self.myframe3.setFrameStyle(QtWidgets.QFrame.Shape.StyledPanel | QtWidgets.QFrame.Shadow.Plain)

        button3layout = QtWidgets.QHBoxLayout(self.myframe3) 
        button3layout.addWidget(self.button3)
    
        self.setLayout(button3layout)
        self.show()

        self.button3.clicked.connect(self.close)
        self.button4.clicked.connect(self.buttonClick4)

    def buttonClick4(self):
        text = self.input_box3.text()
        # hayden this is:: a small input box where they can enter the new index they want:: will grab the text to send whenever you want

    

class connectedWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("QLabel {background: lightgrey}")
        oImage = QtGui.QImage("DiscordLogo.jpg")
        sImage = oImage.scaled(QtCore.QSize(800,600))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.ColorRole.Window, QtGui.QBrush(sImage))
        self.setPalette(palette)

        self.w = None
        self.setFixedWidth(800)
        self.setFixedHeight(600)

        self.button = QtWidgets.QPushButton("Connect")
        self.input_box2 = QtWidgets.QLineEdit(self)
        self.input_box2.setPlaceholderText("Enter Link")

        self.myframe2 = QtWidgets.QFrame()
        self.myframe2.setFrameStyle(QtWidgets.QFrame.Shape.StyledPanel | QtWidgets.QFrame.Shadow.Plain)

        button2layout = QtWidgets.QHBoxLayout(self.myframe2) 
        button2layout.addWidget(self.button)
        button2layout.addWidget(self.input_box2)

        self.setLayout(button2layout)
        self.show()

        self.button.clicked.connect(self.buttonClick2)

    def buttonClick2(self):
        textLink = self.input_box2.text()
        handleLink(self, textLink)
        self.input_box2.setText("")

def handleLink(self, textLink):
    text_thread = threading.Thread(target=sendLink(self, textLink), daemon=True)
    text_thread.start()

def sendLink(self, textLink):
    
    data = {
        'method': 'sentlink',
        'sentlink': textLink,
        'auth': id["uuid"]
    }
    print(textLink, id["uuid"])
    json_data = json.dumps(data)

    try:
        response = requests.post("http://127.0.0.1:8000", data=json_data, headers={'Content-Type': 'application/json'})
        print(response)    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"A System error has occured: {e}", file=sys.stderr)

        if response.status_code == 200:
            open_connectedWindow2(self)

def open_connectedWindow2(self):
    self.hide()
    if self.w is None:
        self.w = thirdWindow()
    self.w.show()
    self.w.closed.connect(self.on_third_window_closed)

def on_third_window_closed(self):
    self.show()
    self.w = None

class discordBot(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("QLabel {background: lightgrey}")
        oImage = QtGui.QImage("DiscordLogo.jpg")
        sImage = oImage.scaled(QtCore.QSize(800,600))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.ColorRole.Window, QtGui.QBrush(sImage))
        self.setPalette(palette)
               
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        self.w = None
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
        
        self.button.clicked.connect(self.buttonClick)
    
    def buttonClick(self):
        text = self.input_box.text()
        handletext(self, text)
        self.input_box.setText("")


def handletext(self, text):
    text_thread = threading.Thread(target=sendtext(self, text), daemon=True)
    text_thread.start()
   

def sendtext(self, text):
    global id
    id["uuid"] = text
    data = {
        'method': 'auth',
        'auth': text
    }

    json_data = json.dumps(data)

    try:
        response = requests.post("http://127.0.0.1:8000", data=json_data, headers={'Content-Type': 'application/json'})
        print(response)    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"A System error has occured: {e}", file=sys.stderr)
    
    if response.status_code == 200:
        open_connectedWindow(self)

def open_connectedWindow(self):
    self.hide()
    if self.w is None:
        self.w = connectedWindow()
    self.w.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    widget = discordBot()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())


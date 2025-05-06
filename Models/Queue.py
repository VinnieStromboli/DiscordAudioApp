from PyQt6.QtHelp import senderSignalIndex
from PySide6 import QtCore, Qt
import Link

class LinkQueue(QtCore.QAbstractListModel):

    def __init__(self, *args, links=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.links = links or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure.
            name, time = self.links[index.row()]
            # Return the text only.
            return name
        return None

    def rowCount(self, index):
        return len(self.links)

    def addLink(self, link: Link):
        self.links.append(link)

    def removeLink(self, index: int):
        self.links.pop(index)
        if index == 0:
            self.sendNextLink()

    def moveLinkInQueue(self, oldPlace: int, newPlace: int):
        link = self.links[oldPlace]
        self.links.pop(oldPlace)
        self.links.insert(newPlace, link)
        if newPlace == 0:
            self.sendNextLink()

    def sendNextLink(self):
        self.links[0].sendLink()

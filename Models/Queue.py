from PySide6 import QtCore, Qt
import Link

class LinkQueue(QtCore.QAbstractListModel):

    def __init__(self, *args, links=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.links = links or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure.
            status, text = self.links[index.row()]
            # Return the text only.
            return text
        return None

    def rowCount(self, index):
        return len(self.links)

    def addLink(self, link: Link):
        self.links.append(link)

    def removeLink(self, index: int):
        self.links.pop(index)

    def moveLinkInQueue(self, oldPlace: int, newPlace: int):
        link = self.links[oldPlace]
        self.links.pop(oldPlace)
        self.links.insert(newPlace, link)

    def sendNextLink(self):
        return

from PySide6 import QtCore
from PySide6.QtCore import Qt, QModelIndex
from Models.Link import Link

class LinkQueue(QtCore.QAbstractListModel):
    def __init__(self, links=None, parent=None):
        super().__init__(parent)
        self.links = links or []

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            return self.links[index.row()].name
        return None

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self.links)

    def addLink(self, link: str):
        tempLink = Link(link)
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.links.append(tempLink)
        self.endInsertRows()

    def removeLink(self, index: int):
        if 0 <= index < self.rowCount():
            self.beginRemoveRows(QModelIndex(), index, index)
            self.links.pop(index)
            self.endRemoveRows()

    def moveLinkInQueue(self, oldPlace: int, newPlace: int):
        link = self.links[oldPlace]
        self.links.pop(oldPlace)
        self.links.insert(newPlace, link)
        # if newPlace == 0:
        #     self.sendNextLink()

    # def sendNextLink(self):
    #     self.links[0].sendLink()

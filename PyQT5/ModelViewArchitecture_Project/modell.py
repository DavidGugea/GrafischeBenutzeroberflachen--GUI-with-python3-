import sys
from PyQt5 import QtCore, QtWidgets

class Modell(QtCore.QAbstractListModel):
    def __init__(self, filename, parent = None):
        super().__init__(parent) 
        self.data = list() 
        
        with open(filename) as f:
            lst = list()
            for line in f:
                if not line.strip():
                    self.data.append(lst) 
                    lst = list()
                else:
                    lst.append(line.strip())
            
            if lst:
                self.data.append(lst)

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.data)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        return self.data[index.row()]
    
    def flags(self, index):
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled

    def setData(self, index, value, role = QtCore.Qt.EditRole):
        self.data[index.row()] = value
        self.layoutChanged.emit()
        return True
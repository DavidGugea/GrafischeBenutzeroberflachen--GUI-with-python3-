import sys
from PyQt5 import QtWidgets, uic

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent) 
        self.ui = uic.loadUi("hauptdialog.ui", self)

app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.show()
sys.exit(app.exec_())
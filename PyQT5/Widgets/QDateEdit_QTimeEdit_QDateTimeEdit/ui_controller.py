import sys
import datetime
from PyQt5 import QtWidgets, uic

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = uic.loadUi("time.ui", self)

        self.ui.timeEdit.timeChanged.connect(self.timeChanged_event)
        self.ui.dateEdit.dateChanged.connect(self.dateChanged_event)
        self.ui.dateTimeEdit.dateTimeChanged.connect(self.dateTimeChanged_event)

    def timeChanged_event(self):
        self.ui.label1.setText(self.ui.timeEdit.date().toString())
    
    def dateChanged_event(self):
        self.ui.label2.setText(self.ui.dateEdit.date().toString())

    def dateTimeChanged_event(self):
        self.ui.label3.setText(self.ui.dateTimeEdit.date().toString())

app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.show()
sys.exit(app.exec_())
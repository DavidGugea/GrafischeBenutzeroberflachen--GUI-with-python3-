import sys 
from PyQt5 import QtWidgets, QtCore, uic

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = uic.loadUi("progress.ui", self)

        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.ui.progressBar.setValue(0)

        self.ui.increaseValue_button.clicked.connect(self.increase_value)
        self.ui.decreaseValue_button.clicked.connect(self.decrease_value)
        self.ui.setValue_button.clicked.connect(self.setValue_event)

    def increase_value(self):
        self.ui.progressBar.setValue(self.ui.progressBar.value() + 5)

    def decrease_value(self):
        self.ui.progressBar.setValue(self.ui.progressBar.value() - 5)

    def setValue_event(self):
        self.ui.progressBar.setValue(int(self.ui.lineEdit.text()))

app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.show()
sys.exit(app.exec_())
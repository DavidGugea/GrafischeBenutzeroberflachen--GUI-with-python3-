import sys
from PyQt5 import QtWidgets, uic, QtCore

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = uic.loadUi("combobox.ui", self)

        for letter in [chr(i) for i in list(range(ord("a"), ord("z")+1, 1))]:
            self.ui.comboBox.addItem(letter)

        self.ui.comboBox.currentIndexChanged.connect(self.combobox_change)
        self.ui.deleteButton.clicked.connect(self.delete)

    def combobox_change(self):
        self.ui.label.setText("{0} / {1}".format(self.comboBox.currentIndex(), self.comboBox.currentText()))
    
    def delete(self):
        self.ui.comboBox.clear()

app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.show()
sys.exit(app.exec_())
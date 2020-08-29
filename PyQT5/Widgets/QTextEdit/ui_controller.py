import sys
from PyQt5 import QtWidgets, uic

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = uic.loadUi("text_edit.ui", self)

        self.ui.textEdit.setPlainText("Write something here")
        self.ui.textEdit.textChanged.connect(self.textChanged_event)

    def textChanged_event(self):
        self.ui.label.setText(self.ui.textEdit.toPlainText())

app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.show()
sys.exit(app.exec_())
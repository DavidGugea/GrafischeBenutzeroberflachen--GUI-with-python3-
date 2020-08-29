import sys
from PyQt5 import QtWidgets, uic

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = uic.loadUi("LineEdit.ui", self)

        self.ui.line_edit_widget.setText("Type something here")
        self.ui.line_edit_widget.textChanged.connect(self.text_changed_event)

    def text_changed_event(self):
        self.ui.label.setText(self.ui.line_edit_widget.text())

app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.show()
sys.exit(app.exec_())
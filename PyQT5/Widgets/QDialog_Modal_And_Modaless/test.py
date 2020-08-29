import sys
from PyQt5 import QtWidgets

class Dialog(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.show()
sys.exit(app.exec_())
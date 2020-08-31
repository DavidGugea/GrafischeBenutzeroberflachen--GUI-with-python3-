import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.image= QtGui.QImage("image.jpg")
        self.ziel = QtCore.QRect(10, 10, 130, 130)
        self.quelle = QtCore.QRect(0, 0, self.image.width(), self.image.height())

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(self.ziel, self.image, self.quelle)

app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.resize(150, 150)
dialog.show()
sys.exit(app.exec_())
import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.font = QtGui.QFont("Helvetica", 16)
        self.pen = QtGui.QPen(QtGui.QColor(0, 0, 255))
    
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        painter.setPen(self.pen)
        painter.setFont(self.font)

        painter.drawText(self.rect(), QtCore.Qt.AlignCenter, "Hello World")
        painter.drawText(0, 16, "Hello World 2")

app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.resize(150, 150)
dialog.show()
sys.exit(app.exec_())
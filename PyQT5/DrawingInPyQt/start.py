import sys 
from PyQt5 import QtWidgets, QtGui

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        # Pen
        self.pen = QtGui.QPen(QtGui.QColor(0, 0, 0))
        self.pen.setWidth(3)

        # Brush
        self.brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        # Set up brush & pen
        painter.setPen(self.pen)
        painter.setBrush(self.brush)

        # Draw
        painter.drawRect(10, 10, 130, 130)

app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.resize(150, 150) # !!!!!!! -- > Dispatches the paint event
dialog.show()
sys.exit(app.exec_())
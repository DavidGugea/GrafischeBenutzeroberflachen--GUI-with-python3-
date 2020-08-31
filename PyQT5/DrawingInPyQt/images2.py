import sys 
from PyQt5 import QtWidgets, QtCore, QtGui

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.image = QtGui.QImage("image.jpg")
        #self.target = QtCore.QRect(10, 10, 150, 100)
        self.target = QtCore.QRect(10, 10, 200, 200)
        #self.source = QtCore.QRect(0, 0, 100, 100)
        #self.source = QtCore.QRect(0, 0, self.image.width(), self.image.height())
        self.source = QtCore.QRect(0, 0, 200, 200)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        '''
        target -- > The Rect in the Widget where the image will be drawn
        source -- > The Rect that represents the outline of the image that will be drawn
        '''
        painter.drawImage(self.target, self.image, self.source) 

app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.resize(200, 200)
dialog.show()
sys.exit(app.exec_())
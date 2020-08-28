import sys
from PyQt5 import uic, QtWidgets

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = uic.loadUi("checkbox.ui", self)

        self.ui.toggleX_button.clicked.connect(self.onToggleX)
        self.ui.toggleY_button.clicked.connect(self.onToggleY)

        self.ui.X_CHECKBOX.stateChanged.connect(self.state_changed)
        self.ui.Y_CHECKBOX.stateChanged.connect(self.state_changed)

    def onToggleX(self):
        if self.ui.X_CHECKBOX.checkState():
            self.ui.X_CHECKBOX.setCheckState(False)
        else:
            self.ui.X_CHECKBOX.setCheckState(True)

    def onToggleY(self):
        if self.ui.Y_CHECKBOX.checkState():
            self.ui.Y_CHECKBOX.setCheckState(False)
        else:
            self.ui.Y_CHECKBOX.setCheckState(True)

    def state_changed(self):
        x_text = str()
        y_text = str()
        
        if self.ui.X_CHECKBOX.checkState():
            x_text = "x ON"
        else:
            x_text = "x OFF"

        if self.ui.Y_CHECKBOX.checkState():
            y_text = "y ON"
        else:
            y_text = "y OFF"

        self.ui.resultLbl.setText("{0} {1}".format(x_text, y_text)) 
        
app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.show()
sys.exit(app.exec_())
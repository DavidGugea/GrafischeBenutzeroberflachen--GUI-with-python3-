import sys 
from PyQt5 import QtWidgets, uic

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = uic.loadUi("Slider_Dial.ui", self)

        self.ui.verticalSlider.setMinimum(0)
        self.ui.horizontalSlider.setMinimum(0)
        self.ui.dial.setMinimum(0)
        self.ui.verticalSlider.setMaximum(100)
        self.ui.horizontalSlider.setMaximum(100)
        self.ui.dial.setMaximum(100)

        self.ui.verticalSlider.setValue(0)
        self.ui.horizontalSlider.setValue(0)
        self.ui.dial.setValue(0)

        self.ui.verticalSlider.valueChanged.connect(self.verticalSlider_valueChange_event)
        self.ui.horizontalSlider.valueChanged.connect(self.horizontalSlider_valueChange_event)
        self.ui.dial.valueChanged.connect(self.dial_valueChange_event)

    def verticalSlider_valueChange_event(self):
        self.ui.verticalSlider_label.setText("Vertical Slider : {0}".format(self.ui.verticalSlider.value()))

    def horizontalSlider_valueChange_event(self):
        self.ui.horizontalSlider_label.setText("Horizontal Slider : {0}".format(self.ui.horizontalSlider.value()))

    def dial_valueChange_event(self):
        self.ui.dial_label.setText("Dial : {0}".format(self.ui.dial.value()))
    
app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.show()
sys.exit(app.exec_())
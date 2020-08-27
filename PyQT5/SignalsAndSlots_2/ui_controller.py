import sys
from PyQt5 import QtWidgets, uic

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = uic.loadUi("hauptdialog.ui", self)

        # Slots
        self.ui.buttonOK.clicked.connect(self.onOK)
        self.ui.buttonAbbrechen.clicked.connect(self.onAbbrechen)

    def onOK(self):
        vorname = self.ui.vorname.text()
        nachname = self.ui.nachname.text()

        agb = self.ui.agb.checkState()
        katalog = self.ui.katalog.checkState()        
        
        print("{0} {1}. Agb : {2} || Katalog : {3}".format(
            vorname,
            nachname,
            agb,
            katalog
        ))

        self.close()

    def onAbbrechen():
        print("Abbrechen")
        sys.exit()

app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.show()
sys.exit(app.exec_())
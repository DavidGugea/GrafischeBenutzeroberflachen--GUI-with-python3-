import sys 
from PyQt5 import QtWidgets, QtCore, uic 

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent) 
        self.ui = uic.loadUi("hauptdialog.ui", self)

        # Slots
        self.ui.buttonOK.clicked.connect(self.onOK)
        self.ui.buttonAbbrechen.clicked.connect(self.onAbbrechen)

    def onOK(self):
        # Daten auslesen
        vorname = self.ui.vorname.text()
        nachname = self.ui.nachname.text()
        adresse = self.ui.adresse.toPlainText()

        print("Vorname : {0}".format(vorname))
        print("Nachname : {0}".format(nachname))
        print("Adresse: {0}".format(adresse))

        datum = self.ui.geburtsdatum.date().toString("dd.MM.yyyy")
        print("Geburtsdatum : {0}".format(datum))

        if self.ui.agb.checkState():
            print("AGBS akzeptiert")
        if self.ui.katalog.checkState():
            print("Katalog bestellt")
        
        self.close()
        
    def onAbbrechen():
        print("Abbrechen")
        self.close()

app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.show()
sys.exit(app.exec_())
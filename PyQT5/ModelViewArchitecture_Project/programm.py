from PyQt5 import QtWidgets
import sys, modell, view

m = modell.Modell("adressbuch.txt")
app = QtWidgets.QApplication(sys.argv)
liste = view.View(m)
liste.resize(200, 250)
liste.show()
sys.exit(app.exec_())
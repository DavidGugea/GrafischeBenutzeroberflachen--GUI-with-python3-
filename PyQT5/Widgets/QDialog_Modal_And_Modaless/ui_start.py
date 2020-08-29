import sys
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("main.ui")
toplevel = uic.loadUi("toplevel_QDialog.ui")


def create_toplevel():
    if window.modal_checkbox.checkState():
        # Modal
        toplevel.exec_()
    else:
        # Modaless
        toplevel.show()

window.create_toplevel_button.clicked.connect(create_toplevel)
window.show()
sys.exit(app.exec_())
import sys
from PyQt5 import QtWidgets, uic, QtGui

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = uic.loadUi("list.ui", self)

        self.model = QtGui.QStandardItemModel()
        self.ui.list_view.setModel(self.model)

        for i in [chr(z) for z in range(ord("a"), ord("z") + 1, 1)]:
            self.ui.list_widget.addItem(i)
            self.model.appendRow(QtGui.QStandardItem(i))

        self.ui.list_widget.currentItemChanged.connect(self.item_changed_widget)

    def item_changed_widget(self):
        self.ui.list_widget_label.setText(str(self.ui.list_widget.currentItem()))

app = QtWidgets.QApplication(sys.argv)
dialog = Dialog()
dialog.show()
sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(544, 661)
        dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        dialog.setAutoFillBackground(False)
        dialog.setSizeGripEnabled(True)
        dialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.web = QtWebEngineWidgets.QWebEngineView(dialog)
        self.web.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.web.setUrl(QtCore.QUrl("about:blank"))
        self.web.setObjectName("web")
        self.verticalLayout_2.addWidget(self.web)
        self.btns = QtWidgets.QDialogButtonBox(dialog)
        self.btns.setOrientation(QtCore.Qt.Horizontal)
        self.btns.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btns.setObjectName("btns")
        self.verticalLayout_2.addWidget(self.btns)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Markdown"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
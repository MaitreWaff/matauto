# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'access.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ConnectionDialog(object):
    def setupUi(self, ConnectionDialog):
        ConnectionDialog.setObjectName(_fromUtf8("ConnectionDialog"))
        ConnectionDialog.resize(267, 171)
        self.gridLayout = QtGui.QGridLayout(ConnectionDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.labeluser = QtGui.QLabel(ConnectionDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labeluser.setFont(font)
        self.labeluser.setObjectName(_fromUtf8("labeluser"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labeluser)
        self.lineedituser = QtGui.QLineEdit(ConnectionDialog)
        self.lineedituser.setObjectName(_fromUtf8("lineedituser"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineedituser)
        self.labelmdp = QtGui.QLabel(ConnectionDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelmdp.setFont(font)
        self.labelmdp.setObjectName(_fromUtf8("labelmdp"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelmdp)
        self.lineeditmdp = QtGui.QLineEdit(ConnectionDialog)
        self.lineeditmdp.setEchoMode(QtGui.QLineEdit.Password)
        self.lineeditmdp.setObjectName(_fromUtf8("lineeditmdp"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineeditmdp)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(ConnectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.checkboxremember = QtGui.QCheckBox(ConnectionDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.checkboxremember.setFont(font)
        self.checkboxremember.setObjectName(_fromUtf8("checkboxremember"))
        self.gridLayout.addWidget(self.checkboxremember, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(98, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 2)

        self.retranslateUi(ConnectionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ConnectionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ConnectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConnectionDialog)
        ConnectionDialog.setTabOrder(self.lineedituser, self.lineeditmdp)
        ConnectionDialog.setTabOrder(self.lineeditmdp, self.checkboxremember)
        ConnectionDialog.setTabOrder(self.checkboxremember, self.buttonBox)

    def retranslateUi(self, ConnectionDialog):
        ConnectionDialog.setWindowTitle(_translate("ConnectionDialog", "Matauto - Connection", None))
        self.labeluser.setText(_translate("ConnectionDialog", "User:", None))
        self.labelmdp.setText(_translate("ConnectionDialog", "Mot De Passe:", None))
        self.checkboxremember.setText(_translate("ConnectionDialog", "Se Souvenir De Moi", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ConnectionDialog = QtGui.QDialog()
    ui = Ui_ConnectionDialog()
    ui.setupUi(ConnectionDialog)
    ConnectionDialog.show()
    sys.exit(app.exec_())


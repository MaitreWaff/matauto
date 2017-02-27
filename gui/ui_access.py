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
        ConnectionDialog.resize(267, 174)
        self.gridLayout = QtGui.QGridLayout(ConnectionDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.UserLabel = QtGui.QLabel(ConnectionDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.UserLabel.setFont(font)
        self.UserLabel.setObjectName(_fromUtf8("UserLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.UserLabel)
        self.userLineEdit = QtGui.QLineEdit(ConnectionDialog)
        self.userLineEdit.setObjectName(_fromUtf8("userLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.userLineEdit)
        self.pwdLabel = QtGui.QLabel(ConnectionDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pwdLabel.setFont(font)
        self.pwdLabel.setObjectName(_fromUtf8("pwdLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.pwdLabel)
        self.pwdLineEdit = QtGui.QLineEdit(ConnectionDialog)
        self.pwdLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.pwdLineEdit.setObjectName(_fromUtf8("pwdLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.pwdLineEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 2)
        self.line = QtGui.QFrame(ConnectionDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(98, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 2, 1)
        self.rememberCheckBox = QtGui.QCheckBox(ConnectionDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.rememberCheckBox.setFont(font)
        self.rememberCheckBox.setObjectName(_fromUtf8("rememberCheckBox"))
        self.gridLayout.addWidget(self.rememberCheckBox, 3, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ConnectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)
        self.UserLabel.setBuddy(self.userLineEdit)
        self.pwdLabel.setBuddy(self.pwdLineEdit)

        self.retranslateUi(ConnectionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ConnectionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ConnectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConnectionDialog)
        ConnectionDialog.setTabOrder(self.userLineEdit, self.pwdLineEdit)
        ConnectionDialog.setTabOrder(self.pwdLineEdit, self.rememberCheckBox)
        ConnectionDialog.setTabOrder(self.rememberCheckBox, self.buttonBox)

    def retranslateUi(self, ConnectionDialog):
        ConnectionDialog.setWindowTitle(_translate("ConnectionDialog", "Matauto - Connection", None))
        self.UserLabel.setText(_translate("ConnectionDialog", "&User:", None))
        self.userLineEdit.setToolTip(_translate("ConnectionDialog", "<html><head/><body><p>UserName Gesiard</p></body></html>", None))
        self.userLineEdit.setWhatsThis(_translate("ConnectionDialog", "<html><head/><body><p>UserName Gesiard</p></body></html>", None))
        self.pwdLabel.setText(_translate("ConnectionDialog", "&Mot De Passe:", None))
        self.pwdLineEdit.setToolTip(_translate("ConnectionDialog", "<html><head/><body><p>Mot De Passe Gesiard</p></body></html>", None))
        self.pwdLineEdit.setWhatsThis(_translate("ConnectionDialog", "<html><head/><body><p>Mot De Passe Gesiard</p></body></html>", None))
        self.rememberCheckBox.setToolTip(_translate("ConnectionDialog", "<html><head/><body><p>Se Souvenir de Mes Informations.</p></body></html>", None))
        self.rememberCheckBox.setWhatsThis(_translate("ConnectionDialog", "<html><head/><body><p>Se Souvenir de Mes Informations.</p></body></html>", None))
        self.rememberCheckBox.setText(_translate("ConnectionDialog", "Se Souvenir De Moi", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ConnectionDialog = QtGui.QDialog()
    ui = Ui_ConnectionDialog()
    ui.setupUi(ConnectionDialog)
    ConnectionDialog.show()
    sys.exit(app.exec_())


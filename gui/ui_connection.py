# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connection.ui'
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

class Ui_Connection(object):
    def setupUi(self, Connection):
        Connection.setObjectName(_fromUtf8("Connection"))
        Connection.resize(313, 163)
        self.verticalLayout = QtGui.QVBoxLayout(Connection)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.labeluser = QtGui.QLabel(Connection)
        self.labeluser.setObjectName(_fromUtf8("labeluser"))
        self.gridLayout.addWidget(self.labeluser, 1, 0, 1, 1)
        self.lineedituser = QtGui.QLineEdit(Connection)
        self.lineedituser.setMaxLength(128)
        self.lineedituser.setObjectName(_fromUtf8("lineedituser"))
        self.gridLayout.addWidget(self.lineedituser, 1, 1, 1, 1)
        self.labelmdp = QtGui.QLabel(Connection)
        self.labelmdp.setObjectName(_fromUtf8("labelmdp"))
        self.gridLayout.addWidget(self.labelmdp, 2, 0, 1, 1)
        self.lineeditmdp = QtGui.QLineEdit(Connection)
        self.lineeditmdp.setEnabled(True)
        self.lineeditmdp.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.lineeditmdp.setInputMask(_fromUtf8(""))
        self.lineeditmdp.setMaxLength(128)
        self.lineeditmdp.setEchoMode(QtGui.QLineEdit.Password)
        self.lineeditmdp.setObjectName(_fromUtf8("lineeditmdp"))
        self.gridLayout.addWidget(self.lineeditmdp, 2, 1, 1, 1)
        self.checkboxremember = QtGui.QCheckBox(Connection)
        self.checkboxremember.setObjectName(_fromUtf8("checkboxremember"))
        self.gridLayout.addWidget(self.checkboxremember, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Connection)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Connection)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Connection.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Connection.reject)
        QtCore.QMetaObject.connectSlotsByName(Connection)
        Connection.setTabOrder(self.lineedituser, self.lineeditmdp)
        Connection.setTabOrder(self.lineeditmdp, self.checkboxremember)
        Connection.setTabOrder(self.checkboxremember, self.buttonBox)

    def retranslateUi(self, Connection):
        Connection.setWindowTitle(_translate("Connection", "Connection a Gesiard", None))
        self.labeluser.setText(_translate("Connection", "Utilisateur", None))
        self.labelmdp.setText(_translate("Connection", "Mot De Passe", None))
        self.checkboxremember.setText(_translate("Connection", "Se Souvenir De Moi", None))


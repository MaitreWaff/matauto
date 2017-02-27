# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recherchemouvementdanssinistre.ui'
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

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName(_fromUtf8("GroupBox"))
        GroupBox.resize(493, 81)
        self.horizontalLayout = QtGui.QHBoxLayout(GroupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(GroupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.immatriculationLineEdit = QtGui.QLineEdit(GroupBox)
        self.immatriculationLineEdit.setObjectName(_fromUtf8("immatriculationLineEdit"))
        self.horizontalLayout.addWidget(self.immatriculationLineEdit)
        self.label_2 = QtGui.QLabel(GroupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.dateLineEdit = QtGui.QLineEdit(GroupBox)
        self.dateLineEdit.setObjectName(_fromUtf8("dateLineEdit"))
        self.horizontalLayout.addWidget(self.dateLineEdit)

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox", None))
        GroupBox.setTitle(_translate("GroupBox", "Recherche du Mouvement Implique dans le Sinistre", None))
        self.label.setText(_translate("GroupBox", "Immatriculation", None))
        self.label_2.setText(_translate("GroupBox", "Date de Survenance", None))


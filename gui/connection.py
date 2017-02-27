# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

# version ~GUI
import sys
from PyQt4 import QtGui, QtCore, QtSql
from PyQt4.QtCore import Qt, SIGNAL

import ui_connection


class Connection(QtGui.QDialog, ui_connection.Ui_Connection):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.initUI()
        # self.styleGui()
        self.setFixedSize(300, 125)

    def initUI(self):
        # x and y coordinates on the screen, width, height
        # self.setGeometry(500, 350, 300, 100)

        self.gridLayout.setSpacing(1)

        self.connect(self.buttonBox, SIGNAL("accepted()"), self.validerButtonBox)
        self.connect(self.buttonBox, SIGNAL("rejected()"), self.rejeterButtonBox)
        # self.connect(self.buttonBox.Cancel, SIGNAL("clicked()"), self.validerButtonBox)

        self.connect(self.checkboxremember, SIGNAL("clicked()"), self.rememberMe)
        # self.checkboxremember.click()

        # self.setWindowTitle("Writer")

    def styleGui(self):
        #(qlabelColor, qlineEditColor)
        #floralwhite, oldlace, seashell, lemonchiffon

        # self.setStyleSheet(styleSheet)
        pass



    def validerButtonBox(self):
        query = QtSql.QSqlQuery()
        query.prepare("SELECT nom_utilisateur, mot_passe FROM utilisateur "
                      "WHERE nom_utilisateur=:username AND mot_passe=:pwd")
        query.bindValue(":username", QtCore.QVariant(QtCore.QString(self.lineedituser.text())))
        query.bindValue(":pwd", QtCore.QVariant(QtCore.QString(self.lineeditmdp.text())))
        query.exec_()
        if not query.isValid():
            print "Username ou Mot de Passe errone"
            print query.lastError().text()
            return False

        print "OK"
        return True

    def rejeterButtonBox(self):
        print "Cancel"
        return False

    def rememberMe(self):
        if self.checkboxremember.isChecked():
            print "Remember Me is Checked!"
        else:
            print "Remember Me is Not Checked!"

def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyle("plastique")

    main = Connection()
    main.show()
    main.raise_()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


# * { border: none;}
# QCheckBox { background: lightyellow; color: red; }
# QLabel { background: lightyellow;}

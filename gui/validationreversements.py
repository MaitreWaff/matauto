# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

# version ~GUI
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import QMessageBox

import ui_reversements

class ValidationReversements(QtGui.QMainWindow, ui_reversements.Ui_Reversements):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.initUI()
        # self.styleGui()

    def initUI(self):
        # x and y coordinates on the screen, width, height
        # self.setGeometry(100, 100, 1030, 800)
        self.connect(self.fichierNouveau, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierEnregistrer, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierImprimBordereauReversement, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierFermer, SIGNAL("triggered()"), self.close)

        self.connect(self.editionAnnuler, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionRefaire, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionPremier, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionPrecedent, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionSuivant, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionDernier, SIGNAL("triggered()"), self.nouveauFichier)



        # self.setWindowTitle("Writer")

    def styleGui(self):

        #floralwhite, oldlace, seashell, lemonchiffon

        # self.setStyleSheet(styleSheet)
        pass


    def nouveauFichier(self):
        print "Nouveau Fichier"

    def okToContinue(self):
        reply = QMessageBox.question(self,
                                     "Quitter",
                                     "Quitter Gesiard?",
                                     QMessageBox.Yes|QMessageBox.Cancel)
        if reply == QMessageBox.Cancel:
            return False
        elif reply == QMessageBox.Yes:
            print "Ok To Continue"
        return True

    def closeEvent(self, event):
        # print event
        if self.okToContinue():
            print "Fermeture Gestionnaire Portefeuille!"
        else:
            event.ignore()


def main():
    app = QtGui.QApplication(sys.argv)

    main = ValidationReversements()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
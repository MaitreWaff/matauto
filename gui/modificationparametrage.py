# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

# DRIVER = "QPSQL"
DRIVER = "QPSQL"
DBNAME = "gesiard"
USER = "postgres"
PASSWORD = "postgres"
HOST = "127.0.0.1"
PORT = "5432"

# version ~GUI
import sys
from PyQt4 import QtGui, QtCore, QtSql
from PyQt4.QtCore import Qt, SIGNAL

import ui_modificationparametrage

class DemandeModificationParametrage(QtGui.QMainWindow, ui_modificationparametrage.Ui_DemandeModificationParametrages):
    PREMIER, PRECEDENT, SUIVANT, DERNIER, SAUVEGARDE = range(5)
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.initUI()
        # self.styleGui()

        # self.setFixedSize(600, 550)

        if sys.platform == 'win32':
            self.setFixedSize(700, 600)
        elif sys.platform == 'darwin':
            self.setFixedSize(600, 550)
        elif sys.platfom == 'linux2':
            self.setFixedSize(600, 550)


    def initUI(self):
        # x and y coordinates on the screen, width, height

        # self.setGeometry(0, 0, 800, 500)


        self.toolBar.setMovable(False)

        self.statusbar.setVisible(False)

        self.gridLayout.setSpacing(1)
        self.gridLayout_2.setSpacing(1)


        self.gridLayout.setMargin(1)
        self.gridLayout_2.setMargin(1)

        # Connection des Actions
        self.connect(self.fichierNouveau, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierEnregistrer, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierImprimFicheMP, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierFermer, SIGNAL("triggered()"), self.close)

        self.connect(self.editionAnnuler, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionRefaire, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionPremier, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionPrecedent, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionSuivant, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionDernier, SIGNAL("triggered()"), self.nouveauFichier)
        # self.setWindowTitle("Writer")

        # self.sinistrRadioButton.click()
        self.geneRadioButton.click()

    def styleGui(self):


        # qlabelColor = QtCore.QString("oldlace")
        # qlineEditColor = QtCore.QString("white")

        #(qlabelColor, qlineEditColor)
        #floralwhite, oldlace, seashell, lemonchiffon

        # self.setStyleSheet(styleSheet)
        pass




    def nouveauFichier(self):
        print "Done!"
    #
    # def okToContinue(self):
    #     reply = QMessageBox.question(self,
    #                                  "Quitter",
    #                                  "Quitter Gesiard?",
    #                                  QMessageBox.Yes|QMessageBox.Cancel)
    #     if reply == QMessageBox.Cancel:
    #         return False
    #     elif reply == QMessageBox.Yes:
    #         print "Ok To Continue"
    #     return True

    def closeEvent(self, event):
        print "Fermeture Gestionnaire Portefeuille!"
        event.accept()

    def loadInitialFile(self):
        pass

def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyle("plastique")

    db = QtSql.QSqlDatabase.addDatabase(DRIVER)
    # db.setDatabaseName(filename)
    db.setDatabaseName(DBNAME)
    db.setUserName(USER)
    db.setHostName(HOST)
    db.setPassword(PASSWORD)
    db.setPort(int(PORT))
    if not db.open():
        print db.lastError().text()
        return

    print "Database successfully Opened!"

    main = DemandeModificationParametrage()
    main.show()
    main.raise_()
    main.activateWindow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
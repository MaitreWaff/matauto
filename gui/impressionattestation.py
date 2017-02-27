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

import ui_impressionattestation
from models.detail_operation_production import DetailOperationProduction
from models.objet_assure import ObjetAssure
from models.police import Police

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


class ImpressionAttestation(QtGui.QMainWindow, ui_impressionattestation.Ui_ImpressionAttestations):
    PREMIER, PRECEDENT, SUIVANT, DERNIER, SAUVEGARDE = range(5)
    ATTESTATION, CARTEROSE = range(2)
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.model_det_op_prod = DetailOperationProduction()
        self.model_obj_assure = ObjetAssure()
        self.model_police = Police()

        self.printer = None

        self.initUI()
        # self.styleGui()

        if sys.platform == 'win32':
            self.setFixedSize(450, 450)
        elif sys.platform == 'darwin':
            self.setFixedSize(450, 400)
        elif sys.platfom == 'linux2':
            self.setFixedSize(450, 400)





    def initUI(self):
        """
        Methode Initialisant les connections des evenements
        :return:
        """
        # self.setGeometry(0, 0, 500, 400)

        self.toolBar.setMovable(False)

        self.statusbar.setVisible(False)

        self.gridLayout.setSpacing(1)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_3.setSpacing(1)


        self.gridLayout.setMargin(1)
        self.gridLayout_2.setMargin(1)
        self.gridLayout_3.setMargin(1)

        # Connections des Actions
        self.connect(self.fichierNouveau, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierEnregistrer, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierImprimer, SIGNAL("triggered()"), self.imprimer)
        self.connect(self.fichierFermer, SIGNAL("triggered()"), self.close)

        self.connect(self.editionAnnuler, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionRefaire, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionPremier, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionPrecedent, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionSuivant, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionDernier, SIGNAL("triggered()"), self.nouveauFichier)

        # Connections des Bouttons
        # self.connect(self.imprimAttestToolButton, SIGNAL("clicked()"), self.imprimerAttestation)
        # self.connect(self.imprimCartRosToolButton, SIGNAL("clicked()"), self.imprimerCarteRose)

        # self.connect(self.imprimAttestToolButton, SIGNAL("clicked()"), lambda: self.typeDocument(self.ATTESTATION))
        # self.connect(self.imprimCartRosToolButton, SIGNAL("clicked()"), lambda: self.typeDocument(self.CARTEROSE))

        self.connect(self.imprimAttestToolButton, SIGNAL("pressed()"), lambda: self.typeDocument(self.ATTESTATION))
        self.connect(self.imprimCartRosToolButton, SIGNAL("pressed()"), lambda: self.typeDocument(self.CARTEROSE))

        # Mapper
        self.mapperObjetAssure = QtGui.QDataWidgetMapper(self)
        self.mapperObjetAssure.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapperObjetAssure.setItemDelegate(QtSql.QSqlRelationalDelegate(self))
        self.mapperObjetAssure.setModel(self.model_obj_assure)

        self.mapperObjetAssure.addMapping(self.numPoliceLineEdit, ObjetAssure.POLICE_ID)
        self.mapperObjetAssure.addMapping(self.nomLineEdit, ObjetAssure.NOM_ASSURE)
        self.mapperObjetAssure.addMapping(self.adressLineEdit, ObjetAssure.ADRESSE_ASSURE)
        self.mapperObjetAssure.addMapping(self.markLineEdit, ObjetAssure.MARQUE)
        self.mapperObjetAssure.addMapping(self.immatLineEdit, ObjetAssure.IMMATRICULATION)
        self.mapperObjetAssure.addMapping(self.genrLineEdit, ObjetAssure.GENRE_OBJET_ID)
        self.mapperObjetAssure.addMapping(self.catUsageLineEdit, ObjetAssure.CATEGORIE_PERMIS)
        # self.mapperObjetAssure.addMapping(self.dateEffetLineEdit, ObjetAssure.DATE)
        # self.mapperObjetAssure.addMapping(self.dateExpLineEdit, ObjetAssure.TERME_ANNUEL_CONTRAT)


        # if self.imprimAttestToolButton.isChecked():
        #     print "Attestation"
        #     # self.mapperObjetAssure.addMapping(self.numAffLineEdit, ObjetAssure.)
        # elif self.imprimCartRosToolButton.isChecked():
        #     print "Carte Rose"
        #     # self.mapperObjetAssure.addMapping(self.numAffLineEdit, ObjetAssure.)

        self.mapperObjetAssure.toFirst()

        immRM = self.model_det_op_prod.relationModel(DetailOperationProduction.OBJET_ASSURE_ID)
        self.listView.setModel(immRM)
        self.listView.setModelColumn(immRM.fieldIndex("immatriculation"))
        self.listView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        # self.setWindowTitle("Writer")


        # self.labelDetailsGaranties.setText(_translate("ImpressionAttestations", "Valider ou Modifier le Numero du Preimprime", None))
        # self.typePieceLabel.setText(_translate("ImpressionAttestations", "ATTESTATION dans le cas echeant.", None))
        self.retranslateUi(self)
        QtCore.QObject.connect(self.imprimAttestToolButton, QtCore.SIGNAL(_fromUtf8("pressed()")), lambda: self.typeDocument(self.ATTESTATION))
        QtCore.QObject.connect(self.imprimCartRosToolButton, QtCore.SIGNAL(_fromUtf8("pressed()")), lambda: self.typeDocument(self.CARTEROSE))
        # QtCore.QObject.connect(self.imprimAttestToolButton, QtCore.SIGNAL(_fromUtf8("pressed()")), self.typePieceLabel.update)
        # QtCore.QObject.connect(self.imprimCartRosToolButton, QtCore.SIGNAL(_fromUtf8("pressed()")), self.typePieceLabel.update)

        self.typeDocument(self.ATTESTATION)

    def styleGui(self):

        # qlabelColor = QtCore.QString("oldlace")
        # qlineEditColor = QtCore.QString("white")

        #(qlabelColor, qlineEditColor)
        #floralwhite, oldlace, seashell, lemonchiffon

        # self.setStyleSheet(styleSheet)
        pass




    def nouveauFichier(self):
        """
        Nouveau Fichier
        :return:
        """
        print "Well Done!"

    def printViaHtml(self):
        print "HTML"
        html = u""
        html += ("<html>"
                 "<head>"
                 "</head>"
                 "<body>"
                 "<h1>Gesiard</h1>"
                 "<p>Alpha Access International</p>"
                 "<p>GMC</p>"
                 "<p>Alpha Access International</p>"
                 "</body>"
                 "</html>")
        # document = QtGui.QTextDocument(QtCore.QString("%s" % html))

        if self.printer is None:
            self.printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
            self.printer.setPageSize(QtGui.QPrinter.Letter)
            self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
            self.printer.setOutputFileName("attestation.pdf")

        document = QtGui.QTextDocument()
        document.setHtml(html)
        document.print_(self.printer)



        # form = QtGui.QPrintDialog(self.printer, self)
        # form = QtGui.QPrintDialog(self.printer, self)
        # self.printer.newPage()
        # if form.exec_():
        #     document = QtGui.QTextDocument()
        #     document.setHtml(html)
        #     document.print_(self.printer)
            # document.print_(self.printer)
            # dialog = QtGui.QPrintDialog()

    def imprimer(self):
        msg = "Impression Ok pour "
        if self.imprimAttestToolButton.isChecked():
            msg += "Attestation"
            self.imprimerAttestation()
        else:
            msg += "Carte Rose"
            self.imprimerCarteRose()
        print msg

    def imprimerAttestation(self):
        """
        Nouveau Fichier
        :return:
        """
        print "Attestation!"
        self.printViaHtml()

    def imprimerCarteRose(self):
        """
        Nouveau Fichier
        :return:
        """
        print "Carte Rose!"
        self.printViaHtml()

    def typeDocument(self, typeDoc):
        # print typeDoc
        if typeDoc == self.ATTESTATION:
            typeImprime = "ATTESTATION"
            self.frameTypePreImprime.setStyleSheet("background-color:yellow;")
            self.numAffLineEdit.setStyleSheet("background-color: white;")
            self.frameTypePreImprime.show()
        elif typeDoc == self.CARTEROSE:
            typeImprime = "CARTE ROSE"
            # self.frameTypePreImprime.setStyleSheet("background-color:fuchsia;")
            self.frameTypePreImprime.setStyleSheet("background-color:hotpink;")
            self.numAffLineEdit.setStyleSheet("background-color: white;")
            self.frameTypePreImprime.show()
        else:
            print "Not Implemented!"
            return
        # if self.imprimAttestToolButton.isChecked():
        #     print "Attestation TB is checked!"
        #     # self.mapperObjetAssure.addMapping(self.numAffLineEdit, ObjetAssure.)
        # elif self.imprimCartRosToolButton.isChecked():
        #     print "Carte Rose TB is chekcked!"
        #     # self.mapperObjetAssure.addMapping(self.numAffLineEdit, ObjetAssure.)

        self.retranslateUi(self, typeImprime)
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
        print "Fermeture Impression Attestations"
        event.accept()

    def retranslateUi(self, ImpressionAttestations, typeDoc=None):
        # self.typePieceLabel.setText(_translate("ImpressionAttestations", "ATTESTATION dans le cas echeant.", None))
        ui_impressionattestation.Ui_ImpressionAttestations.retranslateUi(self, ImpressionAttestations)
        if not typeDoc == None:
            self.typePieceLabel.setText(_translate("ImpressionAttestations", "%s dans le cas echeant." % str(typeDoc), None))
        else:
            pass

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


    main = ImpressionAttestation()
    main.show()
    main.raise_()
    main.activateWindow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
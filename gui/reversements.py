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

import ui_reversements
from models.bordereau_reversement_production import BordereauReversementProduction
from models.operation_production import OperationProduction

class Reversement(QtGui.QMainWindow, ui_reversements.Ui_Reversements):
    # DATETIME_FORMAT = "dd/MM/yyyy hh:mm:ss"
    DATETIME_FORMAT = "dd/MM/yyyy"
    PREMIER, PRECEDENT, SUIVANT, DERNIER, SAUVEGARDE = range(5)
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.model_brp = BordereauReversementProduction()
        self.model_op  = OperationProduction()
        self.model_op_2  = OperationProduction()
        self.setupUi(self)

        self.initUI()
        # self.styleGui()
        self.setFixedSize(950, 550)

    def initUI(self):
        # x and y coordinates on the screen, width, height

        # self.setGeometry(0, 0, 900, 400)

        self.toolBar.setMovable(False)

        self.statusbar.setVisible(False)

        self.gridLayout.setSpacing(1)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_4.setSpacing(1)
        self.gridLayout_5.setSpacing(1)
        self.gridLayout_6.setSpacing(1)


        self.gridLayout.setMargin(1)
        self.gridLayout_2.setMargin(1)
        self.gridLayout_3.setMargin(1)
        self.gridLayout_4.setMargin(1)
        self.gridLayout_5.setMargin(1)
        self.gridLayout_6.setMargin(1)

        # Connection des Actions
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

        # Mapper pour connecter les elements GUI aux colonnes des modeles
        self.mapperBrp = QtGui.QDataWidgetMapper(self)
        self.mapperBrp.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapperBrp.setModel(self.model_brp)
        self.mapperBrp.setItemDelegate(QtSql.QSqlRelationalDelegate(self))

        self.mapperBrp.addMapping(self.numBordLineEdit, BordereauReversementProduction.NUMERO_BORDEREAU_REVERSEMENT)
        self.mapperBrp.addMapping(self.cieLineEdit, BordereauReversementProduction.ASSUREUR_ID)
        # self.mapperBrp.addMapping(self.resAgenceLineEdit, BordereauReversementProduction.RESEAU_ID)
        self.mapperBrp.addMapping(self.opLineEdit, BordereauReversementProduction.OPERATEUR_ID)
        self.mapperBrp.addMapping(self.dateVersementDateEdit, BordereauReversementProduction.DATE_REVERSEMENT)
        self.mapperBrp.addMapping(self.montantAReverserLineEdit, BordereauReversementProduction.MONTANT_A_REVERSER)
        self.mapperBrp.addMapping(self.montantReverseLineEdit, BordereauReversementProduction.MONTANT_REVERSE)
        self.mapperBrp.addMapping(self.soldeCourantLineEdit, BordereauReversementProduction.SOLDE_COURANT)
        self.mapperBrp.addMapping(self.designationLineEdit, BordereauReversementProduction.DESCRIPTION_BORDEREAU)
        self.mapperBrp.addMapping(self.commentTextEdit, BordereauReversementProduction.COMMENTAIRE)

        self.mapperBrp.toFirst()

        self.model_op.setHeaderData(OperationProduction.DATE_OPERATION, Qt.Horizontal, QtCore.QVariant("Date Operation"))
        self.model_op.setHeaderData(OperationProduction.LIBELLE_OPERATION_PRODUCTION, Qt.Horizontal, \
                                    QtCore.QVariant("Type Operation"))
        self.model_op.setHeaderData(OperationProduction.COTISATION_NETTE, Qt.Horizontal, QtCore.QVariant("Nettes"))
        self.model_op.setHeaderData(OperationProduction.COTISATION_TOTALE, Qt.Horizontal, \
                                    QtCore.QVariant("Cotisations Totales"))

        # Ordonne suivant les Rangs
        self.model_op.setSort(OperationProduction.RANG_OPERATION, Qt.AscendingOrder)
        self.model_op.select()


        self.model_op_2.setHeaderData(OperationProduction.DATE_OPERATION, Qt.Horizontal, QtCore.QVariant("Date Operation"))
        self.model_op_2.setHeaderData(OperationProduction.LIBELLE_OPERATION_PRODUCTION, Qt.Horizontal, \
                                    QtCore.QVariant("Type Operation"))
        self.model_op_2.setHeaderData(OperationProduction.COTISATION_NETTE, Qt.Horizontal, QtCore.QVariant("Nettes"))
        self.model_op_2.setHeaderData(OperationProduction.COTISATION_TOTALE, Qt.Horizontal, \
                                    QtCore.QVariant("Cotisations Totales"))

        # Ordonne suivant les Rangs
        self.model_op_2.setSort(OperationProduction.RANG_OPERATION, Qt.AscendingOrder)
        self.model_op_2.select()

        self.operationProductionTableView.setModel(self.model_op)
        self.operationProductionTableView.setItemDelegate(QtSql.QSqlRelationalDelegate(self))
        self.operationProductionTableView.setSelectionMode(QtGui.QTableView.SingleSelection)
        self.operationProductionTableView.setSelectionBehavior(QtGui.QTableView.SelectRows)

        self.operationProductionTableView.setColumnHidden(OperationProduction.ID_OPERATION_PRODUCTION, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.NATURE_OPERATION_ID, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.UTILISATEUR_ID, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.POLICE_ID, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.NUMERO_OPERATION, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.DUREE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.TYPE_BAREME, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.DATE_EFFET, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.POLICE_ACTIVE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.DATE_TERME, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.PRIME_MANUELLE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.PRIME_ANNUELLE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.TAUX_PERIODE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.PRIME_BASE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.REMISE, True)
        # self.operationProductionTableView.setColumnHidden(OperationProduction.COTISATION_NETTE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.ACCESSOIRES, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.ACCESSOIRES_IMPOSES, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.EXONERE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.TVA, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.FRAIS_FICHIER_CENTRAL, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.AUTRES_FRAIS, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.MOTIF_AVENANT, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.NUMERO_AVENANT, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.NUMERO_QUITTANCE_EMISSION, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.NUMERO_ATTESTATION, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.A_RELANCER, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.DATE_POUR_RELANCE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.A_COMMISSIONNER, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.COMMISSION_POTENTIELLE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.AVANCE_COMMISSION, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.DATE_AVANCE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.OBSERVATION, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.STATUT_OPERATION, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.RISTOURNE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.DATE_IMPUTATION, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.DATE_TRAITEMENT, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.DATE_SAISIE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.ACTIF, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.VALIDE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.COMMISSION_A_PAYER, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.VALIDER_COMMISSIONNEMENT, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.DATE_COMMISSIONNEMENT, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G01, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G02, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G03, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G04, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G05, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G06, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G07, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G08, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G09, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G10, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G11, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G12, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G13, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G14, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G15, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G16, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G17, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G18, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G19, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G20, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G21, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G22, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G23, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.G24, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.EMISSION_EN_DIFFERE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.EXTENSION_GARANTIE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.RANG_OPERATION, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.RELANCE_EFFECTUEE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.DATE_RELANCE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.ENVOYER_SMS, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.SMS_ENVOYE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.DATE_ENVOI_SMS, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.REFERENCE_MOUVEMENT_CONSECUTIF, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.REFERENCE_MOUVEMENT_ANTERIEUR, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.REDUCTION_IMPOSEE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.BONUS_MALUS_IMPOSE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.A_REVERSER, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.REVERSEMENT_VALIDE, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.DATE_REVERSEMENT, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.DATE_CREATION, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.REF_IMPORTATION, True)
        self.operationProductionTableView.setColumnHidden(OperationProduction.DATE_IMPORTATION, True)

        self.operationProductionTableView.resizeColumnsToContents()
        self.operationProductionTableView.horizontalHeader().setStretchLastSection(True)


        self.operationProductionAReverserTableView.setModel(self.model_op_2)
        self.operationProductionAReverserTableView.setItemDelegate(QtSql.QSqlRelationalDelegate(self))
        self.operationProductionAReverserTableView.setSelectionMode(QtGui.QTableView.SingleSelection)
        self.operationProductionAReverserTableView.setSelectionBehavior(QtGui.QTableView.SelectRows)

        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.ID_OPERATION_PRODUCTION, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.NATURE_OPERATION_ID, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.UTILISATEUR_ID, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.POLICE_ID, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.NUMERO_OPERATION, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.DUREE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.TYPE_BAREME, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.DATE_EFFET, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.POLICE_ACTIVE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.DATE_TERME, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.PRIME_MANUELLE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.PRIME_ANNUELLE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.TAUX_PERIODE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.PRIME_BASE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.REMISE, True)
        # self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.COTISATION_NETTE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.ACCESSOIRES, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.ACCESSOIRES_IMPOSES, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.EXONERE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.TVA, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.FRAIS_FICHIER_CENTRAL, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.AUTRES_FRAIS, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.MOTIF_AVENANT, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.NUMERO_AVENANT, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.NUMERO_QUITTANCE_EMISSION, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.NUMERO_ATTESTATION, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.A_RELANCER, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.DATE_POUR_RELANCE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.A_COMMISSIONNER, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.COMMISSION_POTENTIELLE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.AVANCE_COMMISSION, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.DATE_AVANCE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.OBSERVATION, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.STATUT_OPERATION, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.RISTOURNE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.DATE_IMPUTATION, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.DATE_TRAITEMENT, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.DATE_SAISIE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.ACTIF, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.VALIDE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.COMMISSION_A_PAYER, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.VALIDER_COMMISSIONNEMENT, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.DATE_COMMISSIONNEMENT, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G01, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G02, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G03, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G04, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G05, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G06, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G07, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G08, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G09, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G10, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G11, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G12, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G13, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G14, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G15, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G16, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G17, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G18, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G19, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G20, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G21, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G22, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G23, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.G24, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.EMISSION_EN_DIFFERE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.EXTENSION_GARANTIE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.RANG_OPERATION, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.RELANCE_EFFECTUEE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.DATE_RELANCE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.ENVOYER_SMS, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.SMS_ENVOYE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.DATE_ENVOI_SMS, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.REFERENCE_MOUVEMENT_CONSECUTIF, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.REFERENCE_MOUVEMENT_ANTERIEUR, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.REDUCTION_IMPOSEE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.BONUS_MALUS_IMPOSE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.A_REVERSER, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.REVERSEMENT_VALIDE, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.DATE_REVERSEMENT, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.DATE_CREATION, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.REF_IMPORTATION, True)
        self.operationProductionAReverserTableView.setColumnHidden(OperationProduction.DATE_IMPORTATION, True)

        self.operationProductionAReverserTableView.resizeColumnsToContents()
        self.operationProductionAReverserTableView.horizontalHeader().setStretchLastSection(True)

    def styleGui(self):
        self.dateVersementDateEdit.setDisplayFormat(self.DATETIME_FORMAT)

        # qlabelColor = QtCore.QString("oldlace")
        # qlineEditColor = QtCore.QString("white")

        #(qlabelColor, qlineEditColor)
        #floralwhite, oldlace, seashell, lemonchiffon

        # self.setStyleSheet(styleSheet)




    def nouveauFichier(self):
        print "Cool"

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

    # model_brp = BordereauReversementProduction()
    # model_op  = OperationProduction()
    main = Reversement()
    main.show()
    main.raise_()
    main.activateWindow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
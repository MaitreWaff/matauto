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

import ui_paiements
from models.detail_paiement import DetailPaiement
from models.paiement import Paiement
from models.operation_production import OperationProduction
from models.detail_paiement import DetailPaiement

class Paiements(QtGui.QMainWindow, ui_paiements.Ui_Paiements):
    # DATETIME_FORMAT = "dd/MM/yyyy hh:mm:ss"
    DATETIME_FORMAT = "dd.MM.yyyy"
    PREMIER, PRECEDENT, SUIVANT, DERNIER, SAUVEGARDE = range(5)
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.model_paiement = Paiement()
        self.model_op_prod = OperationProduction()
        self.model_detail_paiement = DetailPaiement()
        self.setupUi(self)


        self.initUI()
        # self.styleGui()


        if sys.platform == 'win32':
            self.setFixedSize(700, 400) # (700, 450)
        elif sys.platform == 'darwin':
            self.setFixedSize(700, 400)
        elif sys.platfom == 'linux2':
            self.setFixedSize(700, 400)


    def initUI(self):
        # x and y coordinates on the screen, width, height

        # self.setGeometry(0, 0, 700, 400)


        self.toolBar.setMovable(False)

        self.statusbar.setVisible(False)

        self.gridLayout.setSpacing(1)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_4.setSpacing(1)


        self.gridLayout.setMargin(1)
        self.gridLayout_2.setMargin(1)
        self.gridLayout_3.setMargin(1)
        self.gridLayout_4.setMargin(1)

        # Connection des Actions
        self.connect(self.fichierNouveau, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierEnregistrer, SIGNAL("triggered()"), lambda: self.saveRecord(Paiements.SAUVEGARDE))
        self.connect(self.fichierImprimPiecesEncaissement, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierFermer, SIGNAL("triggered()"), self.close)

        self.connect(self.editionAnnuler, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionRefaire, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionPremier, SIGNAL("triggered()"), lambda: self.saveRecord(Paiements.PREMIER))
        self.connect(self.editionPrecedent, SIGNAL("triggered()"), lambda: self.saveRecord(Paiements.PRECEDENT))
        self.connect(self.editionSuivant, SIGNAL("triggered()"), lambda: self.saveRecord(Paiements.SUIVANT))
        self.connect(self.editionDernier, SIGNAL("triggered()"), lambda: self.saveRecord(Paiements.DERNIER))

        self.mapperPaiement = QtGui.QDataWidgetMapper(self)
        self.mapperPaiement.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapperPaiement.setModel(self.model_paiement)
        self.mapperPaiement.setItemDelegate(QtSql.QSqlRelationalDelegate(self))

        self.mapperPaiement.addMapping(self.numRecuLineEdit, Paiement.NUMERO_RECU)

        mpRM = self.model_paiement.relationModel(Paiement.MODE_PAIEMENT_ID)
        self.modPaiementComboBox.setModel(mpRM)
        self.modPaiementComboBox.setModelColumn(mpRM.fieldIndex("libelle_mode_paiement"))
        self.mapperPaiement.addMapping(self.modPaiementComboBox, Paiement.MODE_PAIEMENT_ID)

        self.mapperPaiement.addMapping(self.datePaiementDateEdit, Paiement.DATE_PAIEMENT)
        self.mapperPaiement.addMapping(self.montantPaiementLineEdit, Paiement.MONTANT_PAIEMENT)

        self.paiementValideComboBox.setModel(self.model_paiement)
        self.paiementValideComboBox.setModelColumn(self.model_paiement.fieldIndex("paiement_valide"))
        self.mapperPaiement.addMapping(self.paiementValideComboBox, Paiement.PAIEMENT_VALIDE)

        peRM = self.model_paiement.relationModel(Paiement.PAYEUR_EFFET_ID)
        self.payeurEffetComboBox.setModel(peRM)
        self.payeurEffetComboBox.setModelColumn(peRM.fieldIndex("libelle_payeur_effet"))
        self.mapperPaiement.addMapping(self.payeurEffetComboBox, Paiement.PAYEUR_EFFET_ID)

        self.mapperPaiement.addMapping(self.numPieceLineEdit, Paiement.NUMERO_EFFET)
        self.mapperPaiement.addMapping(self.titulaireLineEdit, Paiement.TITULAIRE_COMPTE_EFFET)
        self.mapperPaiement.addMapping(self.dateEncaisEffetDateEdit, Paiement.DATE_ENCAISSEMENT_EFFET)
        self.mapperPaiement.addMapping(self.autrInfosplainTextEdit, Paiement.AUTRES_INFORMATIONS)

        opRM = self.model_paiement.relationModel(Paiement.OPERATION_PRODUCTION_ID)
        self.opAImputerComboBox.setModel(opRM)
        self.opAImputerComboBox.setModelColumn(opRM.fieldIndex("libelle_operation_production"))

        self.mapperPaiement.toFirst()

        self.mapperOpProd = QtGui.QDataWidgetMapper(self)
        self.mapperOpProd.setModel(self.model_op_prod)
        self.mapperOpProd.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapperOpProd.setItemDelegate(QtSql.QSqlRelationalDelegate(self))

        # self.mapperOpProd.addMapping(self.cumulReglementLineEdit, OperationProduction.)
        self.mapperOpProd.addMapping(self.primDueLineEdit, OperationProduction.COTISATION_NETTE)
        self.mapperOpProd.addMapping(self.cartRosLineEdit, OperationProduction.EXTENSION_GARANTIE)
        self.mapperOpProd.addMapping(self.autrPPLineEdit, OperationProduction.AUTRES_FRAIS)
        self.mapperOpProd.addMapping(self.totalAPayerLineEdit, OperationProduction.COTISATION_TOTALE)

        self.mapperOpProd.toFirst()


        # Tableau Details Paiements.

        self.model_detail_paiement.setHeaderData(DetailPaiement.LIBELLE_PAIEMENT_ID, Qt.Horizontal, QtCore.QVariant("libelle_paiement_id"))
        self.model_detail_paiement.setHeaderData(DetailPaiement.SOMME_REGLEE, Qt.Horizontal, QtCore.QVariant("somme_reglee"))
        self.model_detail_paiement.setHeaderData(DetailPaiement.OBSERVATION, Qt.Horizontal, QtCore.QVariant("observation"))

        self.model_detail_paiement.select()

        self.detailsPaiementTableView.setModel(self.model_detail_paiement)
        self.detailsPaiementTableView.setItemDelegate(QtSql.QSqlRelationalDelegate(self))
        self.detailsPaiementTableView.setSelectionMode(QtGui.QTableView.SingleSelection)
        self.detailsPaiementTableView.setSelectionBehavior(QtGui.QTableView.SelectRows)

        # self.detailsPaiementTableView.setAlternatingRowColors(True)

        self.detailsPaiementTableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.detailsPaiementTableView.setColumnHidden(DetailPaiement.ID_DETAIL_PAIEMENT, True)
        self.detailsPaiementTableView.setColumnHidden(DetailPaiement.PAIEMENT_ID, True)
        self.detailsPaiementTableView.setColumnHidden(DetailPaiement.VALIDE, True)
        self.detailsPaiementTableView.setColumnHidden(DetailPaiement.DATE_VALIDATION, True)
        self.detailsPaiementTableView.setColumnHidden(DetailPaiement.REF_IMPORTATION, True)
        self.detailsPaiementTableView.setColumnHidden(DetailPaiement.DATE_CREATION, True)
        self.detailsPaiementTableView.setColumnHidden(DetailPaiement.DATE_IMPORTATION, True)


        self.detailsPaiementTableView.resizeColumnsToContents()
        # self.detailsPaiementTableView.horizontalHeader().setStretchLastSection(True)




        self.model_op_prod.setHeaderData(OperationProduction.DATE_OPERATION, Qt.Horizontal, QtCore.QVariant("Date Operation"))
        self.model_op_prod.setHeaderData(OperationProduction.LIBELLE_OPERATION_PRODUCTION, Qt.Horizontal, \
                                    QtCore.QVariant("Type Operation"))
        self.model_op_prod.setHeaderData(OperationProduction.COTISATION_NETTE, Qt.Horizontal, QtCore.QVariant("Nettes"))
        self.model_op_prod.setHeaderData(OperationProduction.COTISATION_TOTALE, Qt.Horizontal, \
                                    QtCore.QVariant("Cotisations Totales"))

        # Ordonne suivant les Rangs
        self.model_op_prod.setSort(OperationProduction.RANG_OPERATION, Qt.AscendingOrder)
        self.model_op_prod.select()

        self.operationProductionTableView.setModel(self.model_op_prod)
        self.operationProductionTableView.setItemDelegate(QtSql.QSqlRelationalDelegate(self))
        self.operationProductionTableView.setSelectionMode(QtGui.QTableView.SingleSelection)
        self.operationProductionTableView.setSelectionBehavior(QtGui.QTableView.SelectRows)
        self.operationProductionTableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

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

        # self.setWindowTitle("Writer")

    def styleGui(self):
        self.datePaiementDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.dateEncaisEffetDateEdit.setDisplayFormat(self.DATETIME_FORMAT)

        # qlabelColor = QtCore.QString("oldlace")
        # qlineEditColor = QtCore.QString("white")


        #(qlabelColor, qlineEditColor)
        #floralwhite, oldlace, seashell, lemonchiffon

        # self.labelMouvAssocies
        # self.setStyleSheet(styleSheet)




    def nouveauFichier(self):
        print "Hey!"

    def addRecord(self):
        # row = self.model_gest.rowCount()
        # self.mapperPers.submit()
        # self.model_gest.insertRow(row)
        # self.mapperPers.setCurrentIndex(row)
        # self.prenomComboBox.setFocus()
        pass

    def saveRecord(self, where, current=None):
        if self.detailsPaiementTableView.hasFocus():
            # detailsPaiementTableView a le Focus
            # gest = self.mapperPers.currentIndex() # Int
            index = self.detailsPaiementTableView.currentIndex()
            if index.isValid():
                row = index.row()
                if where == Paiements.PREMIER:
                    print "Premier"
                    row = 0
                elif where == Paiements.PRECEDENT:
                    row = 0 if row <= 1 else row - 1
                    print "Precedent"
                elif where == Paiements.SUIVANT:
                    row += 1
                    if row >= self.model_detail_paiement.rowCount():
                        row = self.model_detail_paiement.rowCount() - 1
                    print "Suivant"
                elif where == Paiements.DERNIER:
                    # row = self.model_gest.rowCount() - 1
                    row = self.model_detail_paiement.rowCount() - 1
                    print "Dernier"
                elif where == Paiements.SAUVEGARDE:
                    # self.mapperPers.submit()
                    print "Save"
                self.detailsPaiementTableView.selectRow(row)
        elif self.operationProductionTableView.hasFocus():
            # operationProductionTableView a le Focus
            # gest = self.mapperPers.currentIndex() # Int
            index = self.operationProductionTableView.currentIndex()
            if index.isValid():
                row = index.row()
                if where == Paiements.PREMIER:
                    print "Premier"
                    row = 0
                elif where == Paiements.PRECEDENT:
                    row = 0 if row <= 1 else row - 1
                    print "Precedent"
                elif where == Paiements.SUIVANT:
                    row += 1
                    if row >= self.model_op_prod.rowCount():
                        row = self.model_op_prod.rowCount() - 1
                    print "Suivant"
                elif where == Paiements.DERNIER:
                    # row = self.model_gest.rowCount() - 1
                    row = self.model_op_prod.rowCount() - 1
                    print "Dernier"
                elif where == Paiements.SAUVEGARDE:
                    # self.mapperPers.submit()
                    print "Save"
                self.operationProductionTableView.selectRow(row)
        else:
            # Le Mapper a le focus
            row = self.mapperPaiement.currentIndex()
            self.mapperPaiement.submit()
            if where == Paiements.PREMIER:
                row = 0
            elif where == Paiements.PRECEDENT:
                row = 0 if row <= 1 else row - 1
            elif where == Paiements.SUIVANT:
                row += 1
                if row >= self.model_paiement.rowCount():
                    row = self.model_paiement.rowCount() - 1
            elif where == Paiements.DERNIER:
                row = self.model_paiement.rowCount() - 1
            elif where == Paiements.SAUVEGARDE:
                self.mapperPaiement.submit()

            self.mapperPaiement.setCurrentIndex(row)
            #
            # gest_en_cours = self.mapperPers.currentIndex()
            # record = self.model_paiement.record(gest_en_cours)
            # id_gest = record.value("id_gestionnaire").toInt()[0]
            # self.model_op_prod.setFilter(QtCore.QString("gestionnaire_id = %1").arg(id_gest))



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

    # model_paiement = Paiement()
    main = Paiements()
    main.show()
    main.raise_()
    main.activateWindow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
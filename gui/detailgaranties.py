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

import ui_detailgaranties
from models.operation_production import OperationProduction
from models.detail_operation_production import DetailOperationProduction
from models.detail_garantie_souscrite import DetailGarantieSouscrite

class DetailGaranties(QtGui.QMainWindow, ui_detailgaranties.Ui_DetailGaranties):
    PREMIER, PRECEDENT, SUIVANT, DERNIER, SAUVEGARDE = range(5)
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.model_op_prod = OperationProduction()
        self.model_det_op_prod = DetailOperationProduction()
        self.model_det_garant = DetailGarantieSouscrite()
        self.setupUi(self)

        self.initUI()
        # self.styleGui()
        #     self.setFixedSize(900, 450)

        if sys.platform == 'win32':
            self.setFixedSize(900, 500)
        elif sys.platform == 'darwin':
            self.setFixedSize(900, 450)
        elif sys.platfom == 'linux2':
            self.setFixedSize(900, 450)



    def initUI(self):
        """
        Methode initialisant les connections des evenements de l'interface.
        :return:
        """
        # self.setGeometry(0, 0, 800, 500)

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
        self.connect(self.fichierEnregistrer, SIGNAL("triggered()"), lambda: self.saveRecord(DetailGaranties.SAUVEGARDE))
        self.connect(self.fichierImprimer, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierFermer, SIGNAL("triggered()"), self.close)

        self.connect(self.editionAnnuler, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionRefaire, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionPremier, SIGNAL("triggered()"), lambda: self.saveRecord(DetailGaranties.PREMIER))
        self.connect(self.editionPrecedent, SIGNAL("triggered()"), lambda: self.saveRecord(DetailGaranties.PRECEDENT))
        self.connect(self.editionSuivant, SIGNAL("triggered()"), lambda: self.saveRecord(DetailGaranties.SUIVANT))
        self.connect(self.editionDernier, SIGNAL("triggered()"), lambda: self.saveRecord(DetailGaranties.DERNIER))


        # self.setWindowTitle("Writer")

        self.listView.setModel(self.model_det_op_prod)
        self.listView.setModelColumn(DetailOperationProduction.STATUT_MOUVEMENT)

        self.mapperOpProd = QtGui.QDataWidgetMapper(self)
        self.mapperOpProd.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapperOpProd.setModel(self.model_op_prod)
        self.mapperOpProd.setItemDelegate(QtSql.QSqlRelationalDelegate(self))

        self.mapperOpProd.addMapping(self.tauxPeriodeLineEdit, OperationProduction.TAUX_PERIODE)
        self.mapperOpProd.addMapping(self.primAnnuelLineEdit, OperationProduction.PRIME_ANNUELLE)
        self.mapperOpProd.addMapping(self.primPeriodLineEdit, OperationProduction.PRIME_BASE)
        self.mapperOpProd.addMapping(self.remiseLineEdit, OperationProduction.REMISE)
        self.mapperOpProd.addMapping(self.primNetLineEdit, OperationProduction.COTISATION_NETTE)
        self.mapperOpProd.addMapping(self.ristournLineEdit, OperationProduction.RISTOURNE)
        self.mapperOpProd.addMapping(self.accessLineEdit, OperationProduction.ACCESSOIRES)
        self.mapperOpProd.addMapping(self.fichierCentralLineEdit, OperationProduction.FRAIS_FICHIER_CENTRAL)
        self.mapperOpProd.addMapping(self.tvaLineEdit, OperationProduction.TVA)
        self.mapperOpProd.addMapping(self.cartRosLineEdit, OperationProduction.EXTENSION_GARANTIE)
        # self.mapperOpProd.addMapping(self.autrTaxLineEdit, OperationProduction.AUTRES_TAXE)
        self.mapperOpProd.addMapping(self.autrFraisLineEdit, OperationProduction.AUTRES_FRAIS)
        self.mapperOpProd.addMapping(self.primttcLineEdit, OperationProduction.COTISATION_TOTALE)

        self.mapperOpProd.toFirst()

        self.mapperDetOpProd = QtGui.QDataWidgetMapper(self)
        self.mapperDetOpProd.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapperDetOpProd.setModel(self.model_det_op_prod)
        self.mapperDetOpProd.setItemDelegate(QtSql.QSqlRelationalDelegate(self))

        self.mapperDetOpProd.addMapping(self.G01CheckBoxDetails, DetailOperationProduction.G01)
        self.mapperDetOpProd.addMapping(self.G02CheckBoxDetails, DetailOperationProduction.G02)
        self.mapperDetOpProd.addMapping(self.G03CheckBoxDetails, DetailOperationProduction.G03)
        self.mapperDetOpProd.addMapping(self.G04CheckBoxDetails, DetailOperationProduction.G04)
        self.mapperDetOpProd.addMapping(self.G05CheckBoxDetails, DetailOperationProduction.G05)
        self.mapperDetOpProd.addMapping(self.G06CheckBoxDetails, DetailOperationProduction.G06)
        self.mapperDetOpProd.addMapping(self.G07CheckBoxDetails, DetailOperationProduction.G07)
        self.mapperDetOpProd.addMapping(self.G08CheckBoxDetails, DetailOperationProduction.G08)
        self.mapperDetOpProd.addMapping(self.G09CheckBoxDetails, DetailOperationProduction.G09)
        self.mapperDetOpProd.addMapping(self.G10CheckBoxDetails, DetailOperationProduction.G10)
        self.mapperDetOpProd.addMapping(self.G11CheckBoxDetails, DetailOperationProduction.G11)
        self.mapperDetOpProd.addMapping(self.G12CheckBoxDetails, DetailOperationProduction.G12)
        self.mapperDetOpProd.addMapping(self.G13CheckBoxDetails, DetailOperationProduction.G13)
        self.mapperDetOpProd.addMapping(self.G14CheckBoxDetails, DetailOperationProduction.G14)
        self.mapperDetOpProd.addMapping(self.G15CheckBoxDetails, DetailOperationProduction.G15)
        self.mapperDetOpProd.addMapping(self.G16CheckBoxDetails, DetailOperationProduction.G16)
        self.mapperDetOpProd.addMapping(self.G17CheckBoxDetails, DetailOperationProduction.G17)
        self.mapperDetOpProd.addMapping(self.G18CheckBoxDetails, DetailOperationProduction.G18)
        self.mapperDetOpProd.addMapping(self.G19CheckBoxDetails, DetailOperationProduction.G19)
        self.mapperDetOpProd.addMapping(self.G20CheckBoxDetails, DetailOperationProduction.G20)
        self.mapperDetOpProd.addMapping(self.G21CheckBoxDetails, DetailOperationProduction.G21)
        self.mapperDetOpProd.addMapping(self.G22CheckBoxDetails, DetailOperationProduction.G22)
        self.mapperDetOpProd.addMapping(self.G23CheckBoxDetails, DetailOperationProduction.G23)
        self.mapperDetOpProd.addMapping(self.G24CheckBoxDetails, DetailOperationProduction.G24)

        self.mapperDetOpProd.addMapping(self.textAvenantTextEdit, DetailOperationProduction.TEXTE_AVENANT)
        self.mapperDetOpProd.toFirst()

        self.model_det_garant.setHeaderData(DetailGarantieSouscrite.RANG, Qt.Horizontal, QtCore.QVariant("Rang"))
        self.model_det_garant.setHeaderData(DetailGarantieSouscrite.VALEUR_CAPITAL, Qt.Horizontal, \
                                            QtCore.QVariant("Valeur Capital"))
        self.model_det_garant.setHeaderData(DetailGarantieSouscrite.ANNUITE_PRIME, Qt.Horizontal, \
                                            QtCore.QVariant("Annuite Prime"))
        self.model_det_garant.setHeaderData(DetailGarantieSouscrite.TAUX_PRIME_APPLIQUE, Qt.Horizontal, \
                                            QtCore.QVariant("Taux Prime Appliquee"))
        self.model_det_garant.setHeaderData(DetailGarantieSouscrite.BASE_PRIME, Qt.Horizontal, \
                                            QtCore.QVariant("Base Prime"))
        self.model_det_garant.setHeaderData(DetailGarantieSouscrite.TAUX_REDUCTION_APPLIQUE, Qt.Horizontal, \
                                            QtCore.QVariant("Taux Reduction Appliquee"))
        self.model_det_garant.setHeaderData(DetailGarantieSouscrite.PRIME, Qt.Horizontal, QtCore.QVariant("Prime"))
        self.model_det_garant.setHeaderData(DetailGarantieSouscrite.PRIME_MANUELLE, Qt.Horizontal, \
                                            QtCore.QVariant("Prime Manuelle"))
        self.model_det_garant.setHeaderData(DetailGarantieSouscrite.RISTOURNE_GARANTIE, Qt.Horizontal, \
                                            QtCore.QVariant("Ristourne Garantie"))
        self.model_det_garant.setHeaderData(DetailGarantieSouscrite.TAUX_COMMISSION, Qt.Horizontal, \
                                            QtCore.QVariant("Taux Commission"))
        self.model_det_garant.setHeaderData(DetailGarantieSouscrite.COMMISSION_POTENTIELLE, Qt.Horizontal, \
                                            QtCore.QVariant("Commission Potentielle"))

        self.model_det_garant.setSort(DetailGarantieSouscrite.RANG, Qt.AscendingOrder)
        self.model_det_garant.select()

        self.detailGarantiesTableView.setModel(self.model_det_garant)
        self.detailGarantiesTableView.setItemDelegate(QtSql.QSqlRelationalDelegate(self))
        self.detailGarantiesTableView.setSelectionMode(QtGui.QTableView.SingleSelection)
        self.detailGarantiesTableView.setSelectionBehavior(QtGui.QTableView.SelectRows)

        self.detailGarantiesTableView.setColumnHidden(DetailGarantieSouscrite.ID_DETAIL_GARANTIE_SOUSCRITE, True)
        self.detailGarantiesTableView.setColumnHidden(DetailGarantieSouscrite.GARANTIE_ID, True)
        self.detailGarantiesTableView.setColumnHidden(DetailGarantieSouscrite.DETAIL_OPERATION_PRODUCTION_ID, True)
        self.detailGarantiesTableView.setColumnHidden(DetailGarantieSouscrite.DATE_OPERATION_REFERANTE, True)
        self.detailGarantiesTableView.setColumnHidden(DetailGarantieSouscrite.ACTIF, True)
        self.detailGarantiesTableView.setColumnHidden(DetailGarantieSouscrite.REDUCTION, True)
        self.detailGarantiesTableView.setColumnHidden(DetailGarantieSouscrite.EMPLACEMENT_GARANTIE_ID, True)
        self.detailGarantiesTableView.setColumnHidden(DetailGarantieSouscrite.REMARQUES, True)
        self.detailGarantiesTableView.setColumnHidden(DetailGarantieSouscrite.EMPLACEMENT_RESERVE, True)
        self.detailGarantiesTableView.setColumnHidden(DetailGarantieSouscrite.DATE_CREATION, True)
        self.detailGarantiesTableView.setColumnHidden(DetailGarantieSouscrite.REF_IMPORTATION, True)
        self.detailGarantiesTableView.setColumnHidden(DetailGarantieSouscrite.DATE_IMPORTATION, True)
        self.detailGarantiesTableView.resizeColumnsToContents()


        self.recapPrimesTableView.setModel(self.model_det_garant)
        self.recapPrimesTableView.setItemDelegate(QtSql.QSqlRelationalDelegate(self))
        self.recapPrimesTableView.setSelectionMode(QtGui.QTableView.SingleSelection)
        self.recapPrimesTableView.setSelectionBehavior(QtGui.QTableView.SelectRows)

        self.recapPrimesTableView.setColumnHidden(DetailGarantieSouscrite.ID_DETAIL_GARANTIE_SOUSCRITE, True)
        self.recapPrimesTableView.setColumnHidden(DetailGarantieSouscrite.GARANTIE_ID, True)
        self.recapPrimesTableView.setColumnHidden(DetailGarantieSouscrite.DETAIL_OPERATION_PRODUCTION_ID, True)
        self.recapPrimesTableView.setColumnHidden(DetailGarantieSouscrite.DATE_OPERATION_REFERANTE, True)
        self.recapPrimesTableView.setColumnHidden(DetailGarantieSouscrite.ACTIF, True)
        self.recapPrimesTableView.setColumnHidden(DetailGarantieSouscrite.REDUCTION, True)
        self.recapPrimesTableView.setColumnHidden(DetailGarantieSouscrite.EMPLACEMENT_GARANTIE_ID, True)
        self.recapPrimesTableView.setColumnHidden(DetailGarantieSouscrite.REMARQUES, True)
        self.recapPrimesTableView.setColumnHidden(DetailGarantieSouscrite.EMPLACEMENT_RESERVE, True)
        self.recapPrimesTableView.setColumnHidden(DetailGarantieSouscrite.DATE_CREATION, True)
        self.recapPrimesTableView.setColumnHidden(DetailGarantieSouscrite.REF_IMPORTATION, True)
        self.recapPrimesTableView.setColumnHidden(DetailGarantieSouscrite.DATE_IMPORTATION, True)
        self.recapPrimesTableView.resizeColumnsToContents()

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
        print "OK!"

    def addRecord(self):
        # row = self.model_gest.rowCount()
        # self.mapperPers.submit()
        # self.model_gest.insertRow(row)
        # self.mapperPers.setCurrentIndex(row)
        # self.prenomComboBox.setFocus()
        pass

    def saveRecord(self, where, current=None):
        if self.detailGarantiesTableView.hasFocus():
            # detailGarantiesTableView a le Focus
            # gest = self.mapperOpProd.currentIndex() # Int
            index = self.detailGarantiesTableView.currentIndex()
            if index.isValid():
                row = index.row()
                if where == DetailGaranties.PREMIER:
                    print "Premier"
                    row = 0
                elif where == DetailGaranties.PRECEDENT:
                    row = 0 if row <= 1 else row - 1
                    print "Precedent"
                elif where == DetailGaranties.SUIVANT:
                    row += 1
                    if row >= self.model_det_garant.rowCount():
                        row = self.model_det_garant.rowCount() - 1
                    print "Suivant"
                elif where == DetailGaranties.DERNIER:
                    # row = self.model_gest.rowCount() - 1
                    row = self.model_det_garant.rowCount() - 1
                    print "Dernier"
                elif where == DetailGaranties.SAUVEGARDE:
                    # self.mapperPers.submit()
                    print "Save"
                self.detailGarantiesTableView.selectRow(row)
        elif self.recapPrimesTableView.hasFocus():
            # recapPrimesTableView a le Focus
            gest = self.mapperOpProd.currentIndex() # Int
            print type(gest) # Int
            index = self.recapPrimesTableView.currentIndex()
            if index.isValid():
                row = index.row()

                if where == DetailGaranties.PREMIER:
                    print "Premier"
                    row = 0
                elif where == DetailGaranties.PRECEDENT:
                    row = 0 if row <= 1 else row - 1
                    print "Precedent"
                elif where == DetailGaranties.SUIVANT:
                    row += 1
                    if row >= self.model_det_garant.rowCount():
                        row = self.model_det_garant.rowCount() - 1
                    print "Suivant"
                elif where == DetailGaranties.DERNIER:
                    row = self.model_det_garant.rowCount() - 1
                    print "Dernier"
                elif where == DetailGaranties.SAUVEGARDE:
                    # self.mapperOpProd.submit()
                    print "Save"
                self.recapPrimesTableView.selectRow(row)
        else:
            # Le Mapper a le focus
            row = self.mapperOpProd.currentIndex()
            self.mapperOpProd.submit()
            if where == DetailGaranties.PREMIER:
                row = 0
            elif where == DetailGaranties.PRECEDENT:
                row = 0 if row <= 1 else row - 1
            elif where == DetailGaranties.SUIVANT:
                row += 1
                if row >= self.model_det_garant.rowCount():
                    row = self.model_det_garant.rowCount() - 1
            elif where == DetailGaranties.DERNIER:
                row = self.model_det_garant.rowCount() - 1
            elif where == DetailGaranties.SAUVEGARDE:
                self.mapperOpProd.submit()

            self.mapperOpProd.setCurrentIndex(row)

            # val = self.mapperOpProd.currentIndex()
            # record = self.model_op_prod.record(val)
            # id = record.value("id_operation_production").toInt()[0]
            # # self.model_dist.setFilter()
            # self.model_dist.setFilter(QtCore.QString("gestionnaire_id = %1").arg(id))



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
        print "Fermeture Details Garanties!"
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

    # model_operation_production = OperationProduction()
    # model_detail_operation_production = DetailOperationProduction()
    # model_detail_garantie_souscrite = DetailGarantieSouscrite()
    main = DetailGaranties()
    main.show()
    main.raise_()
    main.activateWindow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
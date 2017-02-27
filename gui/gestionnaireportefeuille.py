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
from PyQt4.QtGui import QMessageBox


# sys.path.insert(0, '../models')

import ui_gestionnaireportefeuille
# from models.personne import Personne
from models.gestionnaire import Gestionnaire
from models.distribution_gestionnaire import DistributionGestionnaire


class GestionnairePortefeuille(QtGui.QMainWindow, ui_gestionnaireportefeuille.Ui_GestionnairePortefeuille):
    DATETIME_FORMAT = "yy-MM-dd hh:mm:ss"
    PREMIER, PRECEDENT, SUIVANT, DERNIER, SAUVEGARDE = range(5)
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.model_gest = Gestionnaire()
        self.model_dist = DistributionGestionnaire()
        self.setupUi(self)

        selected = None
        self.printer = None


        self.initUI()
        # self.styleGui()

        if sys.platform == 'win32':
            self.setFixedSize(700, 350)
        elif sys.platform == 'darwin':
            self.setFixedSize(600, 350)
        elif sys.platfom == 'linux2':
            self.setFixedSize(600, 350)


            # self.setFixedSize(600, 350)


    def initUI(self):
        # x and y coordinates on the screen, width, height
        # self.setGeometry(100, 100, 1030, 800)

        # self.setGeometry(0, 0, 700, 400)

        self.gridLayout.setSpacing(1)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_4.setSpacing(1)

        # self.gridLayout.setMargin(1)
        # self.gridLayout_2.setMargin(1)
        # self.gridLayout_3.setMargin(1)
        # self.gridLayout_4.setMargin(1)

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        # self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        # self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        # self.gridLayout_4.setContentsMargins(0, 0, 0, 0)

        # self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        # self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        # self.gridLayout_4.setContentsMargins(0, 0, 0, 0)

        self.toolBar.setMovable(False)

        self.statusbar.setVisible(False)

        self.connect(self.fichierNouveau, SIGNAL("triggered()"), self.addRecord)
        self.connect(self.fichierEnregistrer, SIGNAL("triggered()"), lambda: self.saveRecord(GestionnairePortefeuille.SAUVEGARDE))
        self.connect(self.fichierImprimer, SIGNAL("triggered()"), self.printViaHtml)
        self.connect(self.fichierFermer, SIGNAL("triggered()"), self.close)

        self.connect(self.editionPremier, SIGNAL("triggered()"), lambda: self.saveRecord(GestionnairePortefeuille.PREMIER))
        self.connect(self.editionPrecedent, SIGNAL("triggered()"), lambda: self.saveRecord(GestionnairePortefeuille.PRECEDENT))
        self.connect(self.editionSuivant, SIGNAL("triggered()"), lambda: self.saveRecord(GestionnairePortefeuille.SUIVANT))
        self.connect(self.editionDernier, SIGNAL("triggered()"), lambda: self.saveRecord(GestionnairePortefeuille.DERNIER))

        self.connect(self.editionAnnuler, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionRefaire, SIGNAL("triggered()"), self.nouveauFichier)
        # self.setWindowTitle("Writer")




        # Mapper pour connecter les elements GUI aux colonnes des modeles
        self.mapperPers = QtGui.QDataWidgetMapper(self)

        self.mapperPers.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)

        self.mapperPers.setModel(self.model_gest)
        self.mapperPers.setItemDelegate(QtSql.QSqlRelationalDelegate(self))

        self.numGestComboBox.setModel(self.model_gest)
        self.numGestComboBox.setModelColumn(self.model_gest.fieldIndex("code_gestionnaire"))
        self.mapperPers.addMapping(self.numGestComboBox, Gestionnaire.CODE_GESTIONNAIRE)

        self.prenomComboBox.setModel(self.model_gest)
        self.prenomComboBox.setModelColumn(self.model_gest.fieldIndex("prenom_gestionnaire"))
        self.mapperPers.addMapping(self.prenomComboBox, Gestionnaire.PRENOM_GESTIONNAIRE)

        self.nomComboBox.setModel(self.model_gest)
        self.nomComboBox.setModelColumn(self.model_gest.fieldIndex("nom_famille_gestionnaire"))
        self.mapperPers.addMapping(self.nomComboBox, Gestionnaire.NOM_FAMILLE_GESTIONNAIRE)


        tcRelationModel = self.model_gest.relationModel(Gestionnaire.TITRE_CIVILITE_ID)
        self.civiliteComboBox.setModel(tcRelationModel)
        self.civiliteComboBox.setModelColumn(tcRelationModel.fieldIndex("libelle_titre_civilite"))
        self.mapperPers.addMapping(self.civiliteComboBox, Gestionnaire.TITRE_CIVILITE_ID)

        self.mapperPers.addMapping(self.adressLineEdit, Gestionnaire.ADRESSE_GESTIONNAIRE)
        self.mapperPers.addMapping(self.posteOccupeLineEdit, Gestionnaire.POSTE_TRAVAIL)

        self.typeGestComboBox.setModel(self.model_gest)
        self.typeGestComboBox.setModelColumn(self.model_gest.fieldIndex("libelle_type_gestionnaire"))
        self.mapperPers.addMapping(self.typeGestComboBox, Gestionnaire.TYPE_GESTIONNAIRE_ID)

        self.mapperPers.addMapping(self.phoneWLineEdit, Gestionnaire.NUMERO_TELEPHONE_PROFESSIONNEL)
        self.mapperPers.addMapping(self.phoneHLineEdit, Gestionnaire.NUMERO_TELEPHONE_MOBILE)
        self.mapperPers.addMapping(self.faxLineEdit, Gestionnaire.NUMERO_TELECOPIE)
        self.mapperPers.addMapping(self.mailLineEdit, Gestionnaire.ADRESSE_COURRIER_ELECTRONIQUE)

        self.mapperPers.toFirst()
        # self.mapperPers.setRootIndex(self.model_gest.fieldIndex("code_gestionnaire"))

        #
        # val = self.mapperPers.currentIndex()
        # record = self.model_gest.record(val)
        # id = record.value("id_gestionnaire").toInt()[0]
        # self.model_dist.setFilter(QtCore.QString("gestionnaire_id = %1").arg(id))
        #

        self.model_dist.setHeaderData(DistributionGestionnaire.RESEAU_ID, Qt.Horizontal, QtCore.QVariant("Reseau"))
        self.model_dist.setHeaderData(DistributionGestionnaire.GESTIONNAIRE_ID, Qt.Horizontal, QtCore.QVariant("Gestionnaire"))
        self.model_dist.setHeaderData(DistributionGestionnaire.MODELE_COMMISSIONNEMENT_ID, Qt.Horizontal, QtCore.QVariant("Model Commis"))
        self.model_dist.setHeaderData(DistributionGestionnaire.DATE_DEBUT_PRODUCTION, Qt.Horizontal, QtCore.QVariant("Date Deb Prod"))

        # self.model_dist.setHeaderData(DistributionGestionnaire().ACTIF, Qt.Horizontal, QtCore.QVariant("Actif?"))
        # self.model_dist.setHeaderData(DistributionGestionnaire().DATE_CREATION, Qt.Horizontal, QtCore.QVariant("Date Creation"))
        # self.model_dist.setHeaderData(DistributionGestionnaire().REF_IMPORTATION, Qt.Horizontal, QtCore.QVariant("Ref. Importation"))
        # self.model_dist.setHeaderData(DistributionGestionnaire().DATE_IMPORTATION, Qt.Horizontal, QtCore.QVariant("Date Importation"))

        # Ordonne suivant les Modeles de Commissionnement Croissant
        self.model_dist.setSort(DistributionGestionnaire.MODELE_COMMISSIONNEMENT_ID, Qt.AscendingOrder)
        self.model_dist.select()
        # self.tableView.horizontalHeader().setVisible(self.model_dist.rowCount() > 0)


        self.tableView.setModel(self.model_dist)
        self.tableView.setItemDelegate(QtSql.QSqlRelationalDelegate(self))
        self.tableView.setSelectionMode(QtGui.QTableView.SingleSelection)
        # self.tableView.setSelectionBehavior(QtGui.QTableView.SelectItems)
        self.tableView.setSelectionBehavior(QtGui.QTableView.SelectRows)

        # self.tableView.setAlternatingRowColors(True)

        self.tableView.setEditTriggers(QtGui.QTableView.NoEditTriggers)

        # Colonnes a Masquer lors de l'affichage du Tableau
        self.tableView.setColumnHidden(DistributionGestionnaire.ID_DISTRIBUTION_GESTIONNAIRE, True)
        # self.tableView.setColumnHidden(DistributionGestionnaire.GESTIONNAIRE_ID, True)
        self.tableView.setColumnHidden(DistributionGestionnaire.ACTIF, True)
        self.tableView.setColumnHidden(DistributionGestionnaire.DATE_CREATION, True)
        self.tableView.setColumnHidden(DistributionGestionnaire.REF_IMPORTATION, True)
        self.tableView.setColumnHidden(DistributionGestionnaire.DATE_IMPORTATION, True)

        self.tableView.resizeColumnsToContents()
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.saveRecord(GestionnairePortefeuille.PREMIER)

    def styleGui(self):

        # styleSheet2 = """
        # * { font: 75 12pt "Arial Narrow"; }
        # QLabel { background-color: floralwhite; }
        # QLineEdit { background-color: white; }
        # QComboBox { background-color: white; }
        # """

        # qlabelColor = QtCore.QString("oldlace")
        # qlineEditColor = QtCore.QString("white")

        # self.setStyleSheet(styleSheet)
        pass



    def nouveauFichier(self):
        print "You Got It!!!!!!"

    def printViaHtml(self):
        print "HTML"
        html = u""
        html += ("<html>"
                 "<head>"
                 "</head>"
                 "<body>"
                 "<h1>Contrat Gestionnaire</h1>"
                 "<p>Nouveau Gestionnaire:</p>"
                 "<p>Agence</p>"
                 "<p>Parametres</p>"
                 "</body>"
                 "</html>")
        # document = QtGui.QTextDocument(QtCore.QString("%s" % html))

        if self.printer is None:
            self.printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
            self.printer.setPageSize(QtGui.QPrinter.Letter)
            self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
            self.printer.setOutputFileName("contrat_gestionnaire.pdf")

        document = QtGui.QTextDocument()
        document.setHtml(html)
        document.print_(self.printer)



    def addRecord(self):
        row = self.model_gest.rowCount()
        # row = self.mapperPers.currentIndex()
        # md = self.model_gest.index(0, 0)
        # print "Row = ", row, md
        # index = self.model_gest.createIndex(row, 0)
        # print index
        # if self.model_gest.isDirty(index):
        #     print "Dirty"
        # else:
        #     print "Not Dirty"
        # self.mapperPers.submit()

        print "Before InsertRow: ", self.model_gest.rowCount()
        # self.model_gest.insertRow(row)

        query = QtSql.QSqlQuery()
        query = QtSql.QSqlQuery("SELECT MAX(id_gestionnaire) FROM gestionnaire")
        if query.next():
            id_gest = query.value(0).toInt()[0]
            print "MAX ID_Gest = ", id_gest
            id_gest += 1

        query.prepare("INSERT INTO gestionnaire (id_gestionnaire, personne_id, code_gestionnaire, titre_civilite_id,"
                      "type_gestionnaire_id, actif)"
                      "VALUES (:id_gest, :pers, :code_gest, :titre_c, :type_g, :actif)")
        query.bindValue(":id_gest", QtCore.QVariant(QtCore.QString("%1").arg(id_gest)))
        query.bindValue(":pers", QtCore.QVariant(QtCore.QString("%1").arg(0)))
        query.bindValue(":code_gest", QtCore.QVariant(QtCore.QString("%1").arg("WAF")))
        query.bindValue(":titre_c", QtCore.QVariant(QtCore.QString("%1").arg(0)))
        query.bindValue(":type_g", QtCore.QVariant(QtCore.QString("%1").arg(0)))
        query.bindValue(":actif", QtCore.QVariant(QtCore.QString("%1").arg(0)))

        query.exec_()

        if not query.isActive():
            print query.lastError().text()

        row = self.model_gest.rowCount()
        print "After InsertRow: ", row
        self.mapperPers.setCurrentIndex(row)
        self.numGestComboBox.setFocus()

        # now = QtCore.QDateTime.currentDateTime().toPyDateTime()
        # now = QtCore.QDateTime.currentDateTime().toString(self.DATETIME_FORMAT)
        # print now

    def saveRecord(self, where, current=None):
        if self.tableView.hasFocus():
            # TableView a le Focus
            # gest = self.mapperPers.currentIndex() # Int
            index = self.tableView.currentIndex()
            if index.isValid():
                row = index.row()
                if where == GestionnairePortefeuille.PREMIER:
                    print "Premier"
                    row = 0
                elif where == GestionnairePortefeuille.PRECEDENT:
                    row = 0 if row <= 1 else row - 1
                    print "Precedent"
                elif where == GestionnairePortefeuille.SUIVANT:
                    row += 1
                    if row >= self.model_dist.rowCount():
                        row = self.model_dist.rowCount() - 1
                    print "Suivant"
                elif where == GestionnairePortefeuille.DERNIER:
                    # row = self.model_gest.rowCount() - 1
                    row = self.model_dist.rowCount() - 1
                    print "Dernier"
                elif where == GestionnairePortefeuille.SAUVEGARDE:
                    # self.mapperPers.submit()
                    print "Save"
                self.tableView.selectRow(row)
        else:
            # Le Mapper a le focus
            row = self.mapperPers.currentIndex()
            if where == GestionnairePortefeuille.PREMIER:
                row = 0
            elif where == GestionnairePortefeuille.PRECEDENT:
                row = 0 if row <= 1 else row - 1
            elif where == GestionnairePortefeuille.SUIVANT:
                row += 1
                if row >= self.model_gest.rowCount():
                    row = self.model_gest.rowCount() - 1
            elif where == GestionnairePortefeuille.DERNIER:
                row = self.model_gest.rowCount() - 1
            elif where == GestionnairePortefeuille.SAUVEGARDE:
                print "Sauvegarde Nouveau Gestionnaire"
                # now = QtCore.QDateTime.currentDateTime().toString(self.DATETIME_FORMAT)
                # print now
                # lastrow = self.model_gest.rowCount() - 1

                # if self.numGestComboBox.currentText().isEmpty():
                #     print "Empty NumGest"
                #     return
                # if self.civiliteComboBox.currentText().isEmpty():
                #     print "Empty Civility"
                #     return
                # if self.typeGestComboBox.currentText().isEmpty():
                #     print "Empty Type of Gestionnaire"
                #     return

                print "Valeur de ROW dans Sauvegarde: ROW = ", row
                print "Current Index du Mapper = ", self.mapperPers.currentIndex()
                # self.model_gest.insertRow(row)
                self.mapperPers.setCurrentIndex(row)

                self.numGestComboBox.setEditText(QtCore.QString("%1").arg(""))


                # row = self.model_gest.rowCount() - 1

                # self.model_gest.setData(self.model_gest.index(row, self.model_gest.ID_GESTIONNAIRE), \
                #                         QtCore.QVariant(id_gest+1))
                # self.model_gest.setData(self.model_gest.index(row, self.model_gest.PERSONNE_ID), \
                #                         QtCore.QVariant(0))
                # self.model_gest.setData(self.model_gest.index(row, self.model_gest.CODE_GESTIONNAIRE), \
                #                         QtCore.QVariant("Test"))
                # self.model_gest.select()
                # self.model_gest.submitAll()
                # self.mapperPers.submit()

                # print "Before ", self.model_gest.rowCount()
                # self.model_gest.insertRow(row)
                # print "After ", self.model_gest.rowCount()
                # return

            #test = "UPDATE SET VAL=TEST FROM TABLE"

            self.mapperPers.submit()
            self.mapperPers.setCurrentIndex(row)

            gest_en_cours = self.mapperPers.currentIndex()
            record = self.model_gest.record(gest_en_cours)
            id_gest = record.value("id_gestionnaire").toInt()[0]
            self.model_dist.setFilter(QtCore.QString("gestionnaire_id = %1").arg(id_gest))
            self.model_dist.select()
            # self.tableView.horizontalHeader().setVisible(self.model_dist.rowCount() > 0)


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
    db.setDatabaseName(DBNAME)
    db.setUserName(USER)
    db.setHostName(HOST)
    db.setPassword(PASSWORD)
    db.setPort(int(PORT))
    if not db.open():
        print db.lastError().text()
        return

    print "Database successfully Opened!"

    main = GestionnairePortefeuille()
    main.show()
    main.raise_()
    main.activateWindow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


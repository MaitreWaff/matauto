__author__ = 'Luc Mathurin Waffo Modjom'
__version__= '1.0.0'

# DRIVER = "QPSQL"
DRIVER = "QPSQL"
DBNAME = "gesiard"
USER = "postgres"
PASSWORD = "postgres"
HOST = "127.0.0.1"
PORT = "5432"


import sys
import os

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *

#sys.path.insert(0, './gui')
from gui import ui_gesiard, connection, declarationsinistres, emissions, gestionnaireportefeuille, modificationparametrage, paiements, \
    reversements, suivitsinistres, suivitvictimesinistre

# from models.personne import Personne
# from models.distribution_gestionnaire import DistributionGestionnaire


class Gesiard(QMainWindow, ui_gesiard.Ui_Gesiard):
    """ Lanceur de l'Application Gesiard

    """
    def __init__(self, parent = None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUi()

        self.setWindowIcon(QIcon(":/logo/Logo_Officiel_Alpha_Access.png"))


        self.filename = None
        self.setFixedSize(800, 400)

        QTimer.singleShot(0, self.loadInitialFile)

    def initUi(self):
        """
        Initialiseur du Client Lourd
        :return:
        """

        # self.setGeometry(0, 0, 800, 400)

        # self.setGeometry(250, 200, 800, 400)
        # self.resize(800, 400)
        # self.centerOnScreen()

        self.toolBar.setMovable(False)

        self.statusbar.setVisible(False)


        self.gestionnairePortefeuille = None
        self.mouvementEmission = None
        self.declarationSinistre = None
        self.modificationParamatrage = None

        # Menu Traitements
        self.paiement = None
        self.preparationReversements = None
        self.validationReversements = None
        self.suivitSinistres = None
        self.suivitVictimes = None


        # self.screen = QCoreApplication.instance().desktop().screenGeometry()

        # Modeles
        # self.modelPersonne = Personne(self)
        # self.modelDistribGest = DistributionGestionnaire(self)

        # Menu Edition Etats

        # Connection des Actions du Menu Fichier

        self.connect(self.FichierNouvGest, SIGNAL("triggered()"), self.fichierNouvGestionnaire)
        self.connect(self.fichierNouvMouvEmission, SIGNAL("triggered()"), self.fichierNouvMouvementEmission)
        self.connect(self.fichierNouvDecSinistre, SIGNAL("triggered()"), self.fichierNouvDeclarationSinistre)

        self.connect(self.fichierExporter, SIGNAL("triggered()"), self.fileSave)
        self.connect(self.fichierImporter, SIGNAL("triggered()"), self.fileOpen)
        self.connect(self.fichierParametrage, SIGNAL("triggered()"), self.fichierParam)
        self.connect(self.fichierQuitter, SIGNAL("triggered()"), self.close)

        # Connection des Actions du Menu Traitement

        self.connect(self.traitEnregPaiement, SIGNAL("triggered()"), self.traitEnregistrementPaiement)
        self.connect(self.traitPrepaRev, SIGNAL("triggered()"), self.traitPreparationReversement)
        self.connect(self.traitValidRev, SIGNAL("triggered()"), self.traitValidationReversement)
        self.connect(self.traitSuiviSinistr, SIGNAL("triggered()"), self.traitSuivitSinistres)
        self.connect(self.traitSuiviVictim, SIGNAL("triggered()"), self.traitSuivitVictimes)

        # Connection des Actions du Menu Edition des Etats
        self.connect(self.editionListingClient, SIGNAL("triggered()"), self.editionListingClients)
        self.connect(self.editionReleveCompteClient, SIGNAL("triggered()"), self.editionReleveCompteClients)
        self.connect(self.editionEmissionBrut, SIGNAL("triggered()"), self.editionEmissionBrutes)
        self.connect(self.editionEmissionAnnulations, SIGNAL("triggered()"), self.editionEmissionAnnulation)
        self.connect(self.editionEmissionResiRistournes, SIGNAL("triggered()"), self.editionEmissionResiRistourn)
        self.connect(self.editionEmissionNetAnnulations, SIGNAL("triggered()"), self.editionEmissionNetAnnulation)
        self.connect(self.editionEmissionNetResiRistournes, SIGNAL("triggered()"), self.editionEmissionNetResiRistourn)

        # self.connect(self.editionEmission, SIGNAL("triggered()"), self.)
        self.connect(self.editionAttestationVP, SIGNAL("triggered()"), self.editionDesAttestationVP)
        self.connect(self.editionAttestationTPV, SIGNAL("triggered()"), self.editionDesAttestationTPV)
        self.connect(self.editionAttestationCartRos, SIGNAL("triggered()"), self.editionDesAttestationCartRos)
        self.connect(self.editionGestListingGest, SIGNAL("triggered()"), self.editionGestDesListingGest)
        self.connect(self.editionGestCommis, SIGNAL("triggered()"), self.editionGestDesCommis)
        self.connect(self.editionPVCaissEspeces, SIGNAL("triggered()"), self.editionPVDesCaissEspeces)
        self.connect(self.editionPVEffetAutrEncais, SIGNAL("triggered()"), self.editionPVDesEffetAutrEncais)
        self.connect(self.editionPVCaissDetail, SIGNAL("triggered()"), self.editionPVDesCaissDetail)
        self.connect(self.editionEcheancierListingRenouvel, SIGNAL("triggered()"), self.editionEcheancierListingDesRenouvel)
        self.connect(self.editionSinistrListingDecEnreg, SIGNAL("triggered()"), self.editionSinistrDesListingDecEnreg)
        self.connect(self.editionSinistreSituationPeriodiqSinistres, SIGNAL("triggered()"), self.editionSinistreDesSituationPeriodiqSinistres)

    # def centerOnScreen(self):
    #     screen = QDesktopWidget.screenGeometry()
    #     # screen = QDesktopWidget.screenGeometry(QDesktopWidget.primaryScreen())
    #     mysize = self.geometry()
    #     hpos = (screen.width() - mysize.width()) / 2
    #     vpos = (screen.height() - mysize.height()) /2
    #     self.move(hpos, vpos)


    # Methode des Actions du Menu Fichier


    def fichierNouvGestionnaire(self):
        """
        :return:Nouveau Gestionnaire
        """
        print "Nouveau Gestionnaire"
        if self.gestionnairePortefeuille == None:
            self.gestionnairePortefeuille = gestionnaireportefeuille.GestionnairePortefeuille(self)

        screen = QCoreApplication.instance().desktop().screenGeometry()
        mysize = self.gestionnairePortefeuille.geometry()
        hpos = (screen.width() - mysize.width()) / 2
        vpos = (screen.height() - mysize.height()) / 2
        self.gestionnairePortefeuille.move(hpos, vpos)

        self.gestionnairePortefeuille.show()
        self.gestionnairePortefeuille.raise_()
        self.gestionnairePortefeuille.activateWindow()


    def fichierNouvMouvementEmission(self):
        print "Nouveau Mouvement Emission"
        if self.mouvementEmission == None:
            self.mouvementEmission = emissions.Emissions(self)

        screen = QCoreApplication.instance().desktop().screenGeometry()
        mysize = self.mouvementEmission.geometry()
        hpos = (screen.width() - mysize.width()) / 2
        vpos = (screen.height() - mysize.height()) / 2
        self.mouvementEmission.move(hpos, vpos)

        self.mouvementEmission.show()
        self.mouvementEmission.raise_()
        self.mouvementEmission.activateWindow()


    def fichierNouvDeclarationSinistre(self):
        print "Nouvelle Declaration Sinistre"

        if self.declarationSinistre == None:
            self.declarationSinistre = declarationsinistres.DeclarationSinistre(self)

        screen = QCoreApplication.instance().desktop().screenGeometry()
        mysize = self.declarationSinistre.geometry()
        hpos = (screen.width() - mysize.width()) / 2
        vpos = (screen.height() - mysize.height()) /2
        self.declarationSinistre.move(hpos, vpos)


        self.declarationSinistre.show()
        self.declarationSinistre.raise_()
        self.declarationSinistre.activateWindow()

    def fichierExport(self):
        print "Fichier Exportation"

    def fichierImport(self):
        print "Fichier Importation"

    def fileOpen(self):
        rep = os.path.dirname(self.filename) \
                if self.filename is not None else "."

        formats = """Text files (*.txt)
        EXCEL files (*.xls)
        HTML files (*.htm *.html)
        PDF files (*.pdf)
        XML files (*.xml)
        All types (*.*)"""

        fname = unicode(QFileDialog.getOpenFileName(self,
                                                    "%s - Choose a file" % QApplication.applicationName(),
                                                    rep,
                                                    formats))
        if fname:
            self.filename = fname
            print self.filename


    def fileSave(self):
        if self.filename is None:
            self.fileSaveAs()
        else:
            print "Saving %s" % self.filename

    def fileSaveAs(self):
        fname = self.filename \
                if self.filename is not None else "."

        formats = """Text files (*.txt)
        EXCEL files (*.xls)
        HTML files (*.htm *.html)
        PDF files (*.pdf)
        XML files (*.xml)
        All types (*.*)"""

        fname = unicode(QFileDialog.getSaveFileName(self,
                                                    "%s - Save a file" % QApplication.applicationName(),
                                                    fname,
                                                    formats))
        if fname:
            if "." not in fname:
                fname += ".waf"
            self.filename = fname
            print fname
            self.fileSave()

    def fichierParam(self):
        print "Fichier Parametrage"

        if self.modificationParamatrage == None:
            self.modificationParamatrage = modificationparametrage.DemandeModificationParametrage(self)

        screen = QCoreApplication.instance().desktop().screenGeometry()
        mysize = self.modificationParamatrage.geometry()
        hpos = (screen.width() - mysize.width()) / 2
        vpos = (screen.height() - mysize.height()) /2
        self.modificationParamatrage.move(hpos, vpos)


        self.modificationParamatrage.show()
        self.modificationParamatrage.raise_()
        self.modificationParamatrage.activateWindow()

    def fichierFermer(self):
        print "Quitter!"



    # Methode des Actions du Menu Traitement

    def traitEnregistrementPaiement(self):
        print "Traitement Enregistrement Paiement"
        if self.paiement == None:
            self.paiement = paiements.Paiements(self)

        screen = QCoreApplication.instance().desktop().screenGeometry()
        mysize = self.paiement.geometry()
        hpos = (screen.width() - mysize.width()) / 2
        vpos = (screen.height() - mysize.height()) /2
        self.paiement.move(hpos, vpos)


        self.paiement.show()
        self.paiement.raise_()
        self.paiement.activateWindow()

    def traitPreparationReversement(self):
        print "Traitement Preparation des Bordereaux de Versements"
        if self.preparationReversements == None:
            self.preparationReversements = reversements.Reversement(self)
            self.preparationReversements.setWindowTitle("Preparation des Bordereaux de Reversements")

        screen = QCoreApplication.instance().desktop().screenGeometry()
        mysize = self.preparationReversements.geometry()
        hpos = (screen.width() - mysize.width()) / 2
        vpos = (screen.height() - mysize.height()) /2
        self.preparationReversements.move(hpos, vpos)


        self.preparationReversements.show()
        self.preparationReversements.raise_()
        self.preparationReversements.activateWindow()

    def traitValidationReversement(self):
        print "Traitement Validation des Bordereaux de Versements"
        if self.validationReversements == None:
            self.validationReversements = reversements.Reversement(self)
            self.validationReversements.setWindowTitle("Validation des Bordereaux de Reversements")

        screen = QCoreApplication.instance().desktop().screenGeometry()
        mysize = self.validationReversements.geometry()
        hpos = (screen.width() - mysize.width()) / 2
        vpos = (screen.height() - mysize.height()) /2
        self.validationReversements.move(hpos, vpos)

        self.validationReversements.show()
        self.validationReversements.raise_()
        self.validationReversements.activateWindow()

    def traitSuivitSinistres(self):
        print "Traitement Suivit des Sinistres"
        if self.suivitSinistres == None:
            self.suivitSinistres = suivitsinistres.SuivitSinistres(self)

        screen = QCoreApplication.instance().desktop().screenGeometry()
        mysize = self.suivitSinistres.geometry()
        hpos = (screen.width() - mysize.width()) / 2
        vpos = (screen.height() - mysize.height()) /2
        self.suivitSinistres.move(hpos, vpos)


        self.suivitSinistres.show()
        self.suivitSinistres.raise_()
        self.suivitSinistres.activateWindow()

    def traitSuivitVictimes(self):
        print "Traitement Suivit des Victimes"
        if self.suivitVictimes == None:
            self.suivitVictimes = suivitvictimesinistre.VictimeSinistre(self)

        screen = QCoreApplication.instance().desktop().screenGeometry()
        mysize = self.suivitVictimes.geometry()
        hpos = (screen.width() - mysize.width()) / 2
        vpos = (screen.height() - mysize.height()) /2
        self.suivitVictimes.move(hpos, vpos)

        self.suivitVictimes.show()
        self.suivitVictimes.raise_()
        self.suivitVictimes.activateWindow()


    # Methode des Actions du Menu Traitement

    def editionListingClients(self):
        print "Edition Listing Clients"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)

    def editionReleveCompteClients(self):
        print "Edition Releve Compte Client"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)


    def editionEmissionBrutes(self):
        print "Edition Emission Brutes"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)


    def editionEmissionAnnulation(self):
        print "Edition Emissions Annulation"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)

    def editionEmissionResiRistourn(self):
        print "Edition Emissions Resiliation Ristournes"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)

    def editionEmissionNetAnnulation(self):
        print "Edition Emissions Nettes Annulations"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)

    def editionEmissionNetResiRistourn(self):
        print "Edition Emissions Nettes Resiliation et Ristournes"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)


    def editionDesAttestationVP(self):
        print "Edition Attestations VP"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)

    def editionDesAttestationTPV(self):
        print "Edition Attestations TVP"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)

    def editionDesAttestationCartRos(self):
        print "Edition Attestations Cartes Roses"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)

    def editionGestDesListingGest(self):
        print "Edition Gestion Listing Gestionnaires"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)

    def editionGestDesCommis(self):
        print "Edition Gestion Commissions"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)

    def editionPVDesCaissEspeces(self):
        print "Edition PV Caisse Especes"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)

    def editionPVDesEffetAutrEncais(self):
        print "Edition PV Effets et Autres Encaissements"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)

    def editionPVDesCaissDetail(self):
        print "Edition PV Caisse Detaillee"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)

    def editionEcheancierListingDesRenouvel(self):
        print "Edition Echeancier Listing Renouvellement"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)

    def editionSinistrDesListingDecEnreg(self):
        print "Edition Sinistres Listing Declaration Sinistres"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)

    def editionSinistreDesSituationPeriodiqSinistres(self):
        print "Edition Sinistres Situation Periodique Sinistres"
        QMessageBox.information(self, "Message", "En Cours d'Implementation", QMessageBox.Ok)

    def createAction(self, text, slot=None, shorcut=None, icon=None,
                     tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shorcut is not None:
            action.setShortcut(shorcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def okToContinue(self):
        reply = QMessageBox.question(self,
                                     "Quitter",
                                     "Voulez-vous fermer l'application?\n\n"
                                     "Cliquez sur :\n"
                                     "     - [YES] pour fermer Gesiard\n"
                                     "     - [NO] pour annuler votre action et laisser le programme se derouler.\n\n"
                                     "Veuillez confirmer votre choix SVP!",
                                     QMessageBox.Yes|QMessageBox.No)
        if reply == QMessageBox.No:
            return False
        elif reply == QMessageBox.Yes:
            print "Ok To Continue"
        return True

    def closeEvent(self, event):
        pass
        # if self.okToContinue():
        #     event.accept()
        #     print "Fermeture De Gesiard"
        # else:
        #     event.ignore()

    def loadInitialFile(self):
        pass

# def centerOnScreen():

def main(args):
    app = QApplication(args)
    app.setOrganizationName("Alpha Access International")
    app.setOrganizationDomain("gedsiard.com")
    app.setApplicationName("Gesiard")
    app.setWindowIcon(QIcon(":/logo/Logo_Officiel_Alpha_Access.png"))
    app.setStyle("plastique")

    if sys.platform == 'win32':
        css_file = "./gui/gesiard_win32_StyleSheet.qss"
    elif sys.platform == 'darwin':
        css_file = "./gui/gesiard_darwin_StyleSheet.qss"
    elif sys.platfom == 'linux2':
        css_file = "./gui/gesiard_linux2_StyleSheet.qss"
    else:
        css_file = "./gui/gesiardStyleSheet.qss"

    css = open(css_file).read()
    app.setStyleSheet(css)


    db = QSqlDatabase.addDatabase(DRIVER)
    db.setDatabaseName(DBNAME)
    db.setUserName(USER)
    db.setHostName(HOST)
    db.setPassword(PASSWORD)
    db.setPort(int(PORT))
    if not db.open():
        # return
        pass
    print db.lastError().text()

    print "%s Database successfully Opened!" % (DBNAME)


    connect = connection.Connection()
    if not connect.exec_():
        # sys.exit(0)
        pass

    window = Gesiard()

    screen = app.desktop().screenGeometry()
    mysize = window.geometry()
    hpos = (screen.width() - mysize.width()) / 2
    vpos = (screen.height() - mysize.height()) /2
    window.move(hpos, vpos)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    print "Lancement De L'Application - Gesiard..."
    main(sys.argv)

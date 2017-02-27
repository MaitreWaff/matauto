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
from PyQt4.QtCore import Qt, SIGNAL, QTimer
from PyQt4.QtGui import QAction, QIcon, QMessageBox


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


import impressionattestation, suivitvictimesinistre, ui_declarationsinistres, ui_recherchemouvementdanssinistre

from models.personne import Personne
from models.police import Police
from models.objet_assure import ObjetAssure
from models.sinistre import Sinistre

LEFT, RIGHT =  range(2)

class LabelledLineEdit(QtGui.QWidget):
    def __init__(self, labelText=QtCore.QString(), position=LEFT, parent=None):
        super(LabelledLineEdit, self).__init__(parent)
        self.label = QtGui.QLabel(labelText)
        self.lineEdit = QtGui.QLineEdit()
        self.lineEdit.setPlaceholderText("%s recherchee" % labelText)
        self.label.setBuddy(self.lineEdit)
        layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight\
                    if position ==  LEFT else QtGui.QBoxLayout.RightToLeft)
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)

    def getLineEdit(self):
        return self.lineEdit




class RechercheMouvementImpliqueDansSinistre(QtGui.QGroupBox):
    def __init__(self, position=LEFT, parent=None):
        super(RechercheMouvementImpliqueDansSinistre, self).__init__(parent)
        self.setTitle("Recherche du Mouvement Implique dans le Sinistre")
        self.immatriculation = LabelledLineEdit("Immatriculation")
        self.dateSurvenance  = LabelledLineEdit("Date de Survenance")
        # self.groupbox = QtGui.QGroupBox("Recherche")

        layout = QtGui.QBoxLayout(QtGui.QBoxLayout.LeftToRight\
                    if position == LEFT else QtGui.QBoxLayout.TopToBottom)
        # layout = QtGui.QHBoxLayout()
        layout.addWidget(self.immatriculation)
        layout.addWidget(self.dateSurvenance)

        # self.groupbox.setLayout(layout)
        self.setMaximumHeight(80)
        styleSheet = """
        QGroupBox {
            margin: 0px;
            padding: -5px; }"""
        # self.setStyleSheet(styleSheet)
        self.setLayout(layout)

    def getImmatriculation(self):
        return self.immatriculation

    def getDateSurvenance(self):
        return self.dateSurvenance

class Recherche(QtGui.QGroupBox, ui_recherchemouvementdanssinistre.Ui_GroupBox):
    def __init__(self, parent=None):
        super(Recherche, self).__init__(parent)

class DeclarationSinistre(QtGui.QMainWindow, ui_declarationsinistres.Ui_DeclarationSinistres):
    # DATETIME_FORMAT = "dd/MM/yyyy hh:mm:ss"
    DATETIME_FORMAT = "dd.MM.yyyy"
    PREMIER, PRECEDENT, SUIVANT, DERNIER, SAUVEGARDE = range(5)
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.model_personne = Personne()
        self.model_police = Police()
        self.model_obj_assur = ObjetAssure()
        self.model_sinistre = Sinistre()
        self.setupUi(self)

        self.initUI()
        self.styleGui()

            # self.setFixedSize(900, 620)

        if sys.platform == 'win32':
            self.setFixedSize(1000, 650) #(980, 650) # (1000, 700)
        elif sys.platform == 'darwin':
            self.setFixedSize(1000, 590) #(920, 590) # (900, 620)
        elif sys.platfom == 'linux2':
            self.setFixedSize(920, 590)



        # self.centerOnScreen()

        QTimer.singleShot(0, self.loadInitialFile)

    def initUI(self):
        """
        Initialisations connections
        :return:
        """

        # self.setGeometry(0, 0, 900, 500)

        self.toolBar.setMovable(False)

        self.statusbar.setVisible(False)

        self.gridLayout.setSpacing(1)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_4.setSpacing(1)
        self.gridLayout_5.setSpacing(1)
        self.gridLayout_6.setSpacing(1)
        # self.gridLayout_7.setSpacing(1)
        self.gridLayout_8.setSpacing(1)
        self.gridLayout_9.setSpacing(1)
        self.gridLayout_10.setSpacing(1)
        self.gridLayout_11.setSpacing(1)
        self.gridLayout_12.setSpacing(1)
        # self.gridLayout_13.setSpacing(1)
        # self.gridLayout_14.setSpacing(1)
        self.gridLayout_15.setSpacing(1)
        self.gridLayout_16.setSpacing(1)
        self.gridLayout_17.setSpacing(1)
        self.gridLayout_18.setSpacing(1)
        self.gridLayout_19.setSpacing(1)
        self.gridLayout_20.setSpacing(1)


        self.gridLayout.setMargin(1)
        self.gridLayout_2.setMargin(1)
        self.gridLayout_3.setMargin(1)
        self.gridLayout_4.setMargin(1)
        self.gridLayout_5.setMargin(1)
        self.gridLayout_6.setMargin(1)
        # self.gridLayout_7.setMargin(1)
        self.gridLayout_8.setMargin(1)
        self.gridLayout_9.setMargin(1)
        self.gridLayout_10.setMargin(1)
        self.gridLayout_11.setMargin(1)
        self.gridLayout_12.setMargin(1)
        # self.gridLayout_13.setMargin(1)
        # self.gridLayout_14.setMargin(1)
        self.gridLayout_15.setMargin(1)
        self.gridLayout_16.setMargin(1)
        self.gridLayout_17.setMargin(1)
        self.gridLayout_18.setMargin(1)
        self.gridLayout_19.setMargin(1)
        self.gridLayout_20.setMargin(1)

        # Variables
        self.attest = None
        self.victim = None

        self.recherche = RechercheMouvementImpliqueDansSinistre()

        self.actionRechercher = self.createAction("&Rechercher", self.rechercheObjet, QtGui.QKeySequence.Find, \
                                    "Validation", "Rechercher un Objet Assure")

        # self.addAction(self.rechercher)

        # self.rechercher.setIcon(icon)
        # self.rechercher.setObjectName(_fromUtf8("actionRechercher"))
        # self.rechercher = QtGui.QAction(self)


        # self.recherche2 = Recherche()
        # self.recherche2.show()

        self.toolBar.addWidget(self.recherche)
        self.toolBar.addAction(self.actionRechercher)

        # Connection des Actions
        self.connect(self.fichierNouveau, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierEnregistrer, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierImprimer, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierFermer, SIGNAL("triggered()"), self.close)

        self.connect(self.editionAnnuler, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionRefaire, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionPremier, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionPrecedent, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionSuivant, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionDernier, SIGNAL("triggered()"), self.nouveauFichier)

        # Connection des Bouttons
        self.connect(self.condPartToolButton, SIGNAL("clicked()"), self.conditionsParticulieres)
        self.connect(self.attAssurToolButton, SIGNAL("clicked()"), self.attestationsAssurance)
        self.connect(self.enregistrementVictimesToolButton, SIGNAL("clicked()"), self.enregistrementVictime)
        # self.setWindowTitle("Writer")

        # Mapper pour connecter les elements GUI aux colonnes des modeles
        self.mapperPers = QtGui.QDataWidgetMapper(self)
        self.mapperPers.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)

        self.mapperPers.setModel(self.model_personne)
        self.mapperPers.setItemDelegate(QtSql.QSqlRelationalDelegate(self))

        self.numClientComboBox.setModel(self.model_personne)
        self.numClientComboBox.setModelColumn(self.model_personne.fieldIndex("numero_personne"))
        self.mapperPers.addMapping(self.numClientComboBox, Personne.NUMERO_PERSONNE)

        self.prenomComboBox.setModel(self.model_personne)
        self.prenomComboBox.setModelColumn(self.model_personne.fieldIndex("prenom_personne"))
        self.mapperPers.addMapping(self.prenomComboBox, Personne.PRENOM_PERSONNE)

        self.nomComboBox.setModel(self.model_personne)
        self.nomComboBox.setModelColumn(self.model_personne.fieldIndex("nom_personne"))
        self.mapperPers.addMapping(self.nomComboBox, Personne.NOM_PERSONNE)

        self.ProfessionComboBox.setModel(self.model_personne)
        self.ProfessionComboBox.setModelColumn(self.model_personne.fieldIndex("profession"))
        self.mapperPers.addMapping(self.ProfessionComboBox, Personne.PROFESSION)

        tcRelationModel = self.model_personne.relationModel(Personne.TITRE_CIVILITE_ID)
        self.civiliteComboBox.setModel(tcRelationModel)
        self.civiliteComboBox.setModelColumn(tcRelationModel.fieldIndex("libelle_titre_civilite"))
        self.mapperPers.addMapping(self.civiliteComboBox, Personne.TITRE_CIVILITE_ID)

        self.localisationComboBox.setModel(self.model_personne)
        self.localisationComboBox.setModelColumn(self.model_personne.fieldIndex("localisation"))
        self.mapperPers.addMapping(self.localisationComboBox, Personne.LOCALISATION)

        self.mapperPers.addMapping(self.bpLineEdit, Personne.CODE_POSTAL)

        self.villeComboBox.setModel(self.model_personne)
        self.villeComboBox.setModelColumn(self.model_personne.fieldIndex("ville"))
        self.mapperPers.addMapping(self.villeComboBox, Personne.VILLE)

        self.mapperPers.addMapping(self.adresseLineEdit, Personne.ADRESSE_FACTURATION)
        self.mapperPers.addMapping(self.societeLineEdit, Personne.POSTE_TRAVAIL)
        self.mapperPers.addMapping(self.posteLineEdit, Personne.POSTE_OCCUPE)

        self.deptComboBox.setModel(self.model_personne)
        self.deptComboBox.setModelColumn(self.model_personne.fieldIndex("departement_ou_region"))
        self.mapperPers.addMapping(self.deptComboBox, Personne.DEPARTEMENT_OU_REGION)

        # ztRelationModel = self.model_personne.relationModel(Personne.ZONE_TARIFICATION_ID)
        # self.zoneTarifLineEdit.setModel(ztRelationModel)
        # self.zoneTarifComboBox.setModelColumn(ztRelationModel.fieldIndex("libelle_zone_tarification"))
        self.mapperPers.addMapping(self.zoneTarifLineEdit, Personne.ZONE_TARIFICATION_ID)

        self.mapperPers.addMapping(self.phoneWLineEdit, Personne.NUMERO_TELEPHONE_BUREAU)
        self.mapperPers.addMapping(self.phoneHLineEdit, Personne.NUMERO_TELEPHONE_PORTABLE)
        self.mapperPers.addMapping(self.faxLineEdit, Personne.NUMERO_TELECOPIE)
        self.mapperPers.addMapping(self.mailLineEdit, Personne.ADRESSE_COURRIER_ELECTRONIQUE)
        self.mapperPers.addMapping(self.entreePortefeuilleDateEdit, Personne.DATE_ENTREE_PORTEFEUILLE)

        self.mapperPers.toFirst()

        #
        # # Mapper Police
        self.mapperPolice = QtGui.QDataWidgetMapper(self)
        self.mapperPolice.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapperPolice.setModel(self.model_police)
        self.mapperPolice.setItemDelegate(QtSql.QSqlRelationalDelegate(self))

        self.mapperPolice.addMapping(self.cieLineEdit, Police.ASSUREUR_ID)
        self.mapperPolice.addMapping(self.resAgenceLineEdit, Police.RESEAU_ID)
        self.mapperPolice.addMapping(self.gesLineEdit, Police.GESTIONNAIRE_ID)
        self.mapperPolice.addMapping(self.branchLineEdit, Police.BRANCHE_ID)
        self.mapperPolice.addMapping(self.policeCieLineEdit, Police.REFERENCE_ASSUREUR)
        self.mapperPolice.addMapping(self.policeAgenceLineEdit, Police.NUMERO_POLICE)
        self.mapperPolice.addMapping(self.flotteLineEdit, Police.FLOTTE_BIT)
        self.mapperPolice.addMapping(self.dateCreationLineEdit, Police.DATE_SOUSCRIPTION)
        self.mapperPolice.addMapping(self.debAnnuelLineEdit, Police.EFFET_ANNUEL_CONTRAT)
        self.mapperPolice.addMapping(self.termAnnuelLineEdit, Police.TERME_ANNUEL_CONTRAT)

        self.mapperPolice.toFirst()


        self.mapperObjAssure = QtGui.QDataWidgetMapper(self)
        self.mapperObjAssure.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapperObjAssure.setModel(self.model_obj_assur)
        self.mapperObjAssure.setItemDelegate(QtSql.QSqlRelationalDelegate(self))

        self.mapperObjAssure.addMapping(self.numChassiLineEdit, ObjetAssure.NUMERO_SERIE)
        self.mapperObjAssure.addMapping(self.ImmatLineEdit, ObjetAssure.IMMATRICULATION)
        self.mapperObjAssure.addMapping(self.datePremMCLineEdit, ObjetAssure.DATE_ACQUISITION)
        self.mapperObjAssure.addMapping(self.valNeuvLineEdit, ObjetAssure.VALEUR_NEUVE)
        self.mapperObjAssure.addMapping(self.valVenaleLineEdit, ObjetAssure.VALEUR_VENALE)
        self.mapperObjAssure.addMapping(self.valAccessLineEdit, ObjetAssure.VALEUR_ACCESSOIRES)
        self.mapperObjAssure.addMapping(self.markLineEdit, ObjetAssure.MARQUE)
        self.mapperObjAssure.addMapping(self.modelTypLineEdit, ObjetAssure.MODELE)
        self.mapperObjAssure.addMapping(self.genreLineEdit, ObjetAssure.GENRE_OBJET_ID)
        self.mapperObjAssure.addMapping(self.nbPlacesLineEdit, ObjetAssure.NOMBRE_PLACES_CABINE)
        self.mapperObjAssure.addMapping(self.lineEditPuissance, ObjetAssure.PUISSANCE)
        self.mapperObjAssure.addMapping(self.energieLineEdit, ObjetAssure.ENERGIE)
        self.mapperObjAssure.addMapping(self.nomAssureLineEdit, ObjetAssure.NOM_ASSURE)
        self.mapperObjAssure.addMapping(self.adressAssureLineEdit, ObjetAssure.ADRESSE_ASSURE)
        self.mapperObjAssure.addMapping(self.nomConducteurLineEdit, ObjetAssure.CONDUCTEUR)
        self.mapperObjAssure.addMapping(self.ZoneTarifLineEdit, ObjetAssure.ZONE_TARIFICATION_ID)
        self.mapperObjAssure.addMapping(self.numPermiLineEdit, ObjetAssure.NUMERO_PERMIS_CONDUIRE)
        self.mapperObjAssure.addMapping(self.classifPermiLineEdit, ObjetAssure.PERMIS_CONDUIRE_ID)
        self.catPermiComboBox.setModel(self.model_obj_assur)
        self.catPermiComboBox.setModelColumn(self.model_obj_assur.fieldIndex("categorie_permis"))
        self.mapperObjAssure.addMapping(self.catPermiComboBox, ObjetAssure.CATEGORIE_PERMIS)
        self.mapperObjAssure.addMapping(self.dateObtPermiDateEdit, ObjetAssure.DATE_OBTENTION_PERMIS)
        self.mapperObjAssure.addMapping(self.validitPermiDateEdit, ObjetAssure.DATE_VALIDITE_PERMIS)
        self.mapperObjAssure.addMapping(self.numCapaLineEdit, ObjetAssure.CAPACITE)
        self.mapperObjAssure.addMapping(self.validitCapaDateEdit, ObjetAssure.DATE_VALIDITE_CAPACITE)
        self.mapperObjAssure.addMapping(self.catSocioProLineEdit, ObjetAssure.CATEGORIE_SOCIOPROFESSIONNELLE)
        self.mapperObjAssure.addMapping(self.checkBoxInflammable, ObjetAssure.TRANSPORT_MATIERE_INFLAMMABLE)
        self.mapperObjAssure.addMapping(self.checkBoxCarteRose, ObjetAssure.EMISSION_CARTE_ROSE)
        self.mapperObjAssure.addMapping(self.checkBoxVehiculeActif, ObjetAssure.ACTIF)
        # self.mapperObjAssure.addMapping(self.attRemCheckBox, ObjetAssure.ATTELAGE_REMORQUE)
        self.mapperObjAssure.addMapping(self.markAtRemLineEdit, ObjetAssure.MARQUE_REMORQUE)
        self.mapperObjAssure.addMapping(self.typAtRemLineEdit, ObjetAssure.TYPE_REMORQUE)
        self.mapperObjAssure.addMapping(self.ImmatAtRemLineEdit, ObjetAssure.IMMATRICULATION_REMORQUE)
        self.mapperObjAssure.addMapping(self.ValRemAtRemLineEdit, ObjetAssure.VALEUR_REMORQUE)

        self.mapperObjAssure.toFirst()

        self.mapperSinistre = QtGui.QDataWidgetMapper(self)
        self.mapperSinistre.setItemDelegate(QtSql.QSqlRelationalDelegate(self))
        self.mapperSinistre.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapperSinistre.setModel(self.model_sinistre)

        self.mapperSinistre.addMapping(self.numPoliceLineEdit, Sinistre.NUMERO_POLICE)
        self.mapperSinistre.addMapping(self.riskEnCausLineEdit, Sinistre.RISQUE_ADVERSE)
        self.mapperSinistre.addMapping(self.resLineEdit, Sinistre.RESEAU)
        self.mapperSinistre.addMapping(self.refCieLineEdit, Sinistre.REFERENCE_ADVERSAIRE)
        self.mapperSinistre.addMapping(self.numDossierLineEdit, Sinistre.NUMERO_DOSSIER)
        self.mapperSinistre.addMapping(self.dateSurvenancLineEdit, Sinistre.DATE_SINISTRE)
        self.mapperSinistre.addMapping(self.dateEnregDateEdit, Sinistre.DATE_CREATION)
        self.mapperSinistre.addMapping(self.dateDeclarDateEdit, Sinistre.DATE_DECLARATION)

        self.usagAuSinistrComboBox.setModel(self.model_sinistre)
        self.usagAuSinistrComboBox.setModelColumn(self.model_sinistre.fieldIndex("usage_lors_du_sinistre"))
        self.mapperSinistre.addMapping(self.usagAuSinistrComboBox, Sinistre.USAGE_LORS_DU_SINISTRE)
        self.mapperSinistre.addMapping(self.lieuSinistrLineEdit, Sinistre.LIEU_SINISTRE)
        self.mapperSinistre.addMapping(self.declarantLineEdit, Sinistre.SOCIETAIRE_DECLARANT)

        self.cieAdvComboBox.setModel(self.model_sinistre)
        self.cieAdvComboBox.setModelColumn(self.model_sinistre.fieldIndex("adversaire"))
        self.mapperSinistre.addMapping(self.cieAdvComboBox, Sinistre.ADVERSAIRE)
        self.mapperSinistre.addMapping(self.riskAdvLineEdit, Sinistre.RISQUE_ADVERSE)
        self.mapperSinistre.addMapping(self.proprioAdvLineEdit, Sinistre.PROPRIETAIRE_VEHICULE_ADVERSE)
        self.mapperSinistre.addMapping(self.adressAdvLineEdit, Sinistre.ADRESSE_PROPRIETAIRE_VEHICULE_ADVERSE)
        self.mapperSinistre.addMapping(self.adressAssurAdvLineEdit, Sinistre.ADRESSE_ASSURE_ADVERSE)
        self.mapperSinistre.addMapping(self.conducteurAdvLineEdit, Sinistre.CONDUCTEUR_ADVERSAIRE)
        self.mapperSinistre.addMapping(self.policeAdvLineEdit, Sinistre.POLICE_ADVERSAIRE)
        self.mapperSinistre.addMapping(self.lineEditPassagersAuSinistre, Sinistre.PASSAGERS_PENDANT_SINISTRE)
        self.mapperSinistre.addMapping(self.obsTextBrowser, Sinistre.OBSERVATION)

        self.mapperSinistre.addMapping(self.circonstancesTextBrowser, Sinistre.CIRCONSTANCES)

        self.mapperSinistre.toFirst()

        self.enCourRadioButton.click()


    def styleGui(self):
        #
        self.entreePortefeuilleDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.dateObtPermiDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.validitPermiDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.validitCapaDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.dateEnregDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.dateDeclarDateEdit.setDisplayFormat(self.DATETIME_FORMAT)

        # qlabelColor = QtCore.QString("oldlace")
        # qlineEditColor = QtCore.QString("white")

        self.numClientLabel.setProperty('readonly', QtCore.QVariant(True))
        self.labelPrenom.setProperty('readonly', QtCore.QVariant(True))
        self.labelNom.setProperty('readonly', QtCore.QVariant(True))
        self.labelZoneTarification.setProperty('readonly', QtCore.QVariant(True))
        self.labelEntreePortefeuille.setProperty('readonly', QtCore.QVariant(True))

        self.labelCie.setProperty('readonly', QtCore.QVariant(True))
        self.labelFlotte.setProperty('readonly', QtCore.QVariant(True))
        self.labelResAgence.setProperty('readonly', QtCore.QVariant(True))
        self.labelCreeeLe.setProperty('readonly', QtCore.QVariant(True))
        self.labelGestionnaire.setProperty('readonly', QtCore.QVariant(True))
        self.labelDebutAnnuel.setProperty('readonly', QtCore.QVariant(True))
        self.labelBranche.setProperty('readonly', QtCore.QVariant(True))
        self.labelTermeAnnuel.setProperty('readonly', QtCore.QVariant(True))
        self.labelPoliceAgence.setProperty('readonly', QtCore.QVariant(True))
        self.labelPoliceCie.setProperty('readonly', QtCore.QVariant(True))

        self.labelNumChassi.setProperty('readonly', QtCore.QVariant(True))
        self.labelMarque.setProperty('readonly', QtCore.QVariant(True))
        self.labelImmatriculation.setProperty('readonly', QtCore.QVariant(True))
        self.labelModelType.setProperty('readonly', QtCore.QVariant(True))
        self.labelDatePremMC.setProperty('readonly', QtCore.QVariant(True))
        self.labelGenre.setProperty('readonly', QtCore.QVariant(True))
        self.labelValNeuve.setProperty('readonly', QtCore.QVariant(True))
        self.labelNbPlace.setProperty('readonly', QtCore.QVariant(True))
        self.labelValVenale.setProperty('readonly', QtCore.QVariant(True))
        self.labelPuissance.setProperty('readonly', QtCore.QVariant(True))
        self.labelValAccessoire.setProperty('readonly', QtCore.QVariant(True))
        self.labelEnergie.setProperty('readonly', QtCore.QVariant(True))

        self.labelNomAssure.setProperty('readonly', QtCore.QVariant(True))
        self.labelNomConducteur.setProperty('readonly', QtCore.QVariant(True))

        self.labelZoneTarif.setProperty('readonly', QtCore.QVariant(True))
        self.labelClassifPermis.setProperty('readonly', QtCore.QVariant(True))
        self.labelCatSocioPro.setProperty('readonly', QtCore.QVariant(True))

        self.checkBoxInflammable.setProperty('readonly', QtCore.QVariant(True))
        self.checkBoxCarteRose.setProperty('readonly', QtCore.QVariant(True))
        self.checkBoxVehiculeActif.setProperty('readonly', QtCore.QVariant(True))

        # self.attRemCheckBox.setProperty('readonly', QtCore.QVariant(True))
        self.attRemGroupBoxSinistres.setProperty('readonly', QtCore.QVariant(True))
        self.labelMarqueAtRem.setProperty('readonly', QtCore.QVariant(True))
        self.labelImmatriculationAtRem.setProperty('readonly', QtCore.QVariant(True))
        self.labelTypeAtRem.setProperty('readonly', QtCore.QVariant(True))
        self.labelValeurRemorqueAtRem.setProperty('readonly', QtCore.QVariant(True))

        self.labelNumPolice.setProperty('readonly', QtCore.QVariant(True))
        self.labelDateSurvenance.setProperty('readonly', QtCore.QVariant(True))
        self.labelRisqueEnCause.setProperty('readonly', QtCore.QVariant(True))
        self.labelReseau.setProperty('readonly', QtCore.QVariant(True))


        #(qlabelColor, qlineEditColor)
        #floralwhite, oldlace, seashell, lemonchiffon

        # self.

        # self.setStyleSheet(styleSheet)
        # pass

    def centerOnScreen(self):
        # frameGm = self.frameGeometry()
        # screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        # centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        # frameGm.moveCenter(centerPoint)
        # self.move(frameGm.topLeft())

        # screen = QtGui.QDesktopWidget.screenGeometry()
        # print QtGui.QApplication.desktop().numScreens()

        screen_number = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        # screen = QtGui.QApplication.desktop().screenGeometry(screen_number)
        # mysize = self.geometry()
        # hpos = (screen.width() - mysize.width()) / 2
        # vpos = (screen.height() - mysize.height()) /2
        # self.move(hpos, vpos)

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget.availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



    def nouveauFichier(self):
        """
        Action Nouveau Fichier
        :return:
        """
        print "Dec Sinistre Action Ok!"

    def rechercheObjet(self):
        """
        Action Nouveau Fichier
        :return:
        """
        # print "Recherche Action Ok!"
        errormsg = "Veuillez entrer: \n"
        if unicode(self.recherche.getImmatriculation().getLineEdit().text()) == "":
            errormsg += "L\'Immatriculation du Vehicule\n"
        elif unicode(self.recherche.getDateSurvenance().getLineEdit().text()) == "":
            errormsg += "La Date de Survenance."
        else:
            print "Immatriculation = %s" % unicode(self.recherche.getImmatriculation().getLineEdit().text())
            print "Date Survenance = %s" % unicode(self.recherche.getDateSurvenance().getLineEdit().text())
            return

        QMessageBox.warning(self, "Rechercher", errormsg, QMessageBox.Ok)



    def conditionsParticulieres(self):
        """
        Action Conditions Particulieres
        :return:
        """
        print "Btn Conditions Particulieres Ok!"
        QMessageBox.information(self, "Conditions Particulieres", "Impression Conditions Particulieres", QMessageBox.Ok)

    def attestationsAssurance(self):
        """
        Action Attestations Assurance
        :return:
        """
        print "Btn Attestations Assurances Ok!"
        if self.attest == None:
            self.attest = impressionattestation.ImpressionAttestation(self)

        screen = QtCore.QCoreApplication.instance().desktop().screenGeometry()
        mysize = self.attest.geometry()
        hpos = (screen.width() - mysize.width()) / 2
        vpos = (screen.height() - mysize.height()) /2
        self.attest.move(hpos, vpos)


        self.attest.show()
        self.attest.raise_()
        self.attest.activateWindow()

    def enregistrementVictime(self):
        """
        Action Enregistrer Victime Sinistre
        :return:
        """
        print "Btn Enregistrement Victime Sinistre Ok!"
        if self.victim == None:
            self.victim = suivitvictimesinistre.VictimeSinistre(self)

        screen = QtCore.QCoreApplication.instance().desktop().screenGeometry()
        mysize = self.victim.geometry()
        hpos = (screen.width() - mysize.width()) / 2
        vpos = (screen.height() - mysize.height()) /2
        self.victim.move(hpos, vpos)


        self.victim.show()
        self.victim.raise_()
        self.victim.activateWindow()

    def createAction(self, text, slot=None, shorcut=None, icon=None,
                     tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:

            # icone = QtGui.QIcon()
            # icone.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/%s.ico" % icon )), QtGui.QIcon.Normal, QtGui.QIcon.Off)


            action.setIcon(QIcon(":/icones/%s.ico" % icon))
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
        print "Fermeture Declaration Sinistres!"
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

    main = DeclarationSinistre()
    main.show()
    main.raise_()
    main.activateWindow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
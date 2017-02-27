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

import ui_suivitvictimesinistre

from models.personne import Personne
from models.prejudice import Prejudice
from models.sinistre import Sinistre
from models.victime import Victime

class VictimeSinistre(QtGui.QMainWindow, ui_suivitvictimesinistre.Ui_VictimesSinistre):
    # DATETIME_FORMAT = "dd/MM/yyyy hh:mm:ss"
    DATETIME_FORMAT = "dd.MM.yyyy"
    PREMIER, PRECEDENT, SUIVANT, DERNIER, SAUVEGARDE = range(5)
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.model_personne = Personne()
        self.model_prejudice = Prejudice()
        self.model_sinistre = Sinistre()
        self.model_victime = Victime()
        self.setupUi(self)

        self.initUI()
        self.styleGui()

            # self.setFixedSize(900, 550)

        if sys.platform == 'win32':
            self.setFixedSize(1000, 550)
        elif sys.platform == 'darwin':
            self.setFixedSize(900, 550)
        elif sys.platfom == 'linux2':
            self.setFixedSize(900, 550)

    def initUI(self):
        # x and y coordinates on the screen, width, height

        # self.setGeometry(0, 0, 900, 500)

        self.toolBar.setMovable(False)

        self.statusbar.setVisible(False)

        self.gridLayout.setSpacing(1)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_4.setSpacing(1)
        self.gridLayout_5.setSpacing(1)
        self.gridLayout_6.setSpacing(1)
        self.gridLayout_7.setSpacing(1)
        self.gridLayout_8.setSpacing(1)
        self.gridLayout_9.setSpacing(1)
        self.gridLayout_10.setSpacing(1)
        self.gridLayout_11.setSpacing(1)
        self.gridLayout_12.setSpacing(1)
        self.gridLayout_13.setSpacing(1)


        self.gridLayout.setMargin(1)
        self.gridLayout_2.setMargin(1)
        self.gridLayout_3.setMargin(1)
        self.gridLayout_4.setMargin(1)
        self.gridLayout_5.setMargin(1)
        self.gridLayout_6.setMargin(1)
        self.gridLayout_7.setMargin(1)
        self.gridLayout_8.setMargin(1)
        self.gridLayout_9.setMargin(1)
        self.gridLayout_10.setMargin(1)
        self.gridLayout_11.setMargin(1)
        self.gridLayout_12.setMargin(1)
        self.gridLayout_13.setMargin(1)

        # Connection des Actions
        self.connect(self.fichierNouveau, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierEnregistrer, SIGNAL("triggered()"), lambda: self.saveRecord(self.SAUVEGARDE))
        self.connect(self.fichierImprimer, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierFermer, SIGNAL("triggered()"), self.close)

        self.connect(self.editionAnnuler, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionRefaire, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionPremier, SIGNAL("triggered()"), lambda: self.saveRecord(self.PREMIER))
        self.connect(self.editionPrecedent, SIGNAL("triggered()"), lambda: self.saveRecord(self.PRECEDENT))
        self.connect(self.editionSuivant, SIGNAL("triggered()"), lambda: self.saveRecord(self.SUIVANT))
        self.connect(self.editionDernier, SIGNAL("triggered()"), lambda: self.saveRecord(self.DERNIER))
        # self.setWindowTitle("Writer")

        # Liste des Sinistres de la Victime
        self.victimesEnregistreesListView.setModel(self.model_sinistre)
        self.victimesEnregistreesListView.setModelColumn(self.model_sinistre.fieldIndex("numero_dossier"))
        self.victimesEnregistreesListView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        # Mapper Victime
        self.mapperPersonne = QtGui.QDataWidgetMapper(self)
        self.mapperPersonne.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapperPersonne.setModel(self.model_personne)
        self.mapperPersonne.setItemDelegate(QtSql.QSqlRelationalDelegate(self))


        # persRM = self.model_personne.relationModel(Personne.PRENOM_PERSONNE)
        self.prenomComboBox.setModel(self.model_personne)
        self.prenomComboBox.setModelColumn(self.model_personne.fieldIndex("prenom_personne"))
        self.mapperPersonne.addMapping(self.prenomComboBox, Personne.PRENOM_PERSONNE)

        # pnRM = self.model_victime.relationModel(Victime.PERSONNE_ID)
        self.nomComboBox.setModel(self.model_personne)
        self.nomComboBox.setModelColumn(self.model_personne.fieldIndex("nom_personne"))
        self.mapperPersonne.addMapping(self.nomComboBox, Personne.NOM_PERSONNE)

        # profRM = self.model_personne.relationModel(Personne.PROFESSION)
        self.professionComboBox.setModel(self.model_personne)
        self.professionComboBox.setModelColumn(self.model_personne.fieldIndex("profession"))
        self.mapperPersonne.addMapping(self.professionComboBox, Personne.PROFESSION)

        civRM = self.model_personne.relationModel(Personne.TITRE_CIVILITE_ID)
        self.civiliteComboBox.setModel(civRM)
        self.civiliteComboBox.setModelColumn(civRM.fieldIndex("libelle_titre_civilite"))
        self.mapperPersonne.addMapping(self.civiliteComboBox, Personne.TITRE_CIVILITE_ID)

        self.localisationComboBox.setModel(self.model_personne)
        self.localisationComboBox.setModelColumn(self.model_personne.fieldIndex("localisation"))
        self.mapperPersonne.addMapping(self.localisationComboBox, Personne.LOCALISATION)

        self.mapperPersonne.addMapping(self.bpLineEdit, Personne.CODE_POSTAL)

        self.villeComboBox.setModel(self.model_personne)
        self.villeComboBox.setModelColumn(self.model_personne.fieldIndex("ville"))
        self.mapperPersonne.addMapping(self.villeComboBox, Personne.VILLE)

        self.mapperPersonne.addMapping(self.adressLineEdit, Personne.ADRESSE_FACTURATION)
        self.mapperPersonne.addMapping(self.steLineEdit, Personne.POSTE_TRAVAIL)
        self.mapperPersonne.addMapping(self.posteLineEdit, Personne.POSTE_OCCUPE)

        self.deptComboBox.setModel(self.model_personne)
        self.deptComboBox.setModelColumn(self.model_personne.fieldIndex("departement_ou_region"))
        self.mapperPersonne.addMapping(self.deptComboBox, Personne.DEPARTEMENT_OU_REGION)

        self.mapperPersonne.addMapping(self.PhoneWLineEdit, Personne.NUMERO_TELEPHONE_BUREAU)
        self.mapperPersonne.addMapping(self.PhoneHLineEdit, Personne.NUMERO_TELEPHONE_PORTABLE)
        self.mapperPersonne.addMapping(self.faxLineEdit, Personne.NUMERO_TELECOPIE)
        self.mapperPersonne.addMapping(self.mailLineEdit, Personne.ADRESSE_COURRIER_ELECTRONIQUE)


        self.statutMatComboBox.setModel(self.model_personne)
        self.statutMatComboBox.setModelColumn(self.model_personne.fieldIndex("statut_personne"))
        self.mapperPersonne.addMapping(self.statutMatComboBox, Personne.STATUT_PERSONNE)
        self.mapperPersonne.addMapping(self.lieuNaissLineEdit, Personne.LIEU_NAISSANCE)
        self.mapperPersonne.addMapping(self.numCniLineEdit, Personne.NUMERO_CNI)
        self.mapperPersonne.addMapping(self.dateDelivranceDateEdit, Personne.DATE_DELIVRANCE_CNI)
        self.mapperPersonne.addMapping(self.dateNaissDateEdit, Personne.DATE_NAISSANCE)
        self.mapperPersonne.addMapping(self.validiteDateEdit, Personne.DATE_VALIDITE_CNI)
        self.mapperPersonne.addMapping(self.lieuDelivranceLineEdit, Personne.LIEU_DELIVRANCE_CNI)


        self.mapperPersonne.toFirst()




        # Mapper Victime
        self.mapperVictime = QtGui.QDataWidgetMapper(self)
        self.mapperVictime.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapperVictime.setModel(self.model_victime)
        self.mapperVictime.setItemDelegate(QtSql.QSqlRelationalDelegate(self))

        self.numIdComboBox.setModel(self.model_victime)
        self.numIdComboBox.setModelColumn(self.model_victime.fieldIndex("numero_victime"))
        self.mapperPersonne.addMapping(self.numIdComboBox, Victime.NUMERO_VICTIME)

        self.etatActuelVictimComboBox.setModel(self.model_victime)
        self.etatActuelVictimComboBox.setModelColumn(self.model_victime.fieldIndex("etat_actuel_victime"))
        self.mapperVictime.addMapping(self.etatActuelVictimComboBox, Victime.ETAT_ACTUEL_VICTIME)

        prRM = self.model_victime.relationModel(Victime.PROFESSION_ID)
        self.professionVictimComboBox.setModel(prRM)
        self.professionVictimComboBox.setModelColumn(prRM.fieldIndex("libelle_profession"))
        self.mapperVictime.addMapping(self.professionVictimComboBox, Victime.PROFESSION_ID)

        self.descDommageComboBox.setModel(self.model_victime)
        self.descDommageComboBox.setModelColumn(self.model_victime.fieldIndex("description_dommage"))
        self.mapperVictime.addMapping(self.descDommageComboBox, Victime.DESCRIPTION_DOMMAGE)

        natRM = self.model_victime.relationModel(Victime.NATURE_DOMMAGE_ID)
        self.natDommageComboBox.setModel(natRM)
        self.natDommageComboBox.setModelColumn(natRM.fieldIndex("libelle_nature_dommage"))
        self.mapperVictime.addMapping(self.natDommageComboBox, Victime.NATURE_DOMMAGE_ID)

        # self.mapperVictime.addMapping(self.DescPrejudiceVictimTextEdit, Victime.DESCRIPTION_PREJUDICE)

        self.natLesionComboBox.setModel(self.model_victime)
        self.natLesionComboBox.setModelColumn(self.model_victime.fieldIndex("nature_lesions"))
        self.mapperVictime.addMapping(self.natLesionComboBox, Victime.NATURE_LESIONS)

        self.mapperVictime.addMapping(self.ageVictimSpinBox, Victime.AGE_VICTIME)
        self.mapperVictime.addMapping(self.dureeProbHospSpinBox, Victime.DUREE_PROBABLE_HOSPITALISATION)

        stpRM = self.model_victime.relationModel(Victime.PERSONNE_ID)
        self.statutMatComboBox.setModel(stpRM)
        self.statutMatComboBox.setModelColumn(stpRM.fieldIndex("libelle_statut_personne"))
        self.mapperVictime.addMapping(self.statutMatComboBox, Victime.STATUT_PERSONNE_ID)

        self.parenteAvecAssureComboBox.setModel(self.model_victime)
        self.parenteAvecAssureComboBox.setModelColumn(self.model_victime.fieldIndex("parente_avec_assure"))
        self.mapperVictime.addMapping(self.parenteAvecAssureComboBox, Victime.PARENTE_AVEC_ASSURE)

        self.parenteAvecConducteurComboBox.setModel(self.model_victime)
        self.parenteAvecConducteurComboBox.setModelColumn(self.model_victime.fieldIndex("parente_avec_conducteur"))
        self.mapperVictime.addMapping(self.parenteAvecConducteurComboBox, Victime.PARENTE_AVEC_CONDUCTEUR)

        emRM = self.model_victime.relationModel(Victime.EMPLACEMENT_VICTIME_ID)
        self.emplacementVictimAuSinistrComboBox.setModel(emRM)
        self.emplacementVictimAuSinistrComboBox.setModelColumn(emRM.fieldIndex("designation_emplacement_victime"))
        self.mapperVictime.addMapping(self.emplacementVictimAuSinistrComboBox, Victime.EMPLACEMENT_VICTIME_ID)

        self.destVictimApresSinistrComboBox.setModel(self.model_victime)
        self.destVictimApresSinistrComboBox.setModelColumn(self.model_victime.fieldIndex("destination_apres_sinistre"))
        self.mapperVictime.addMapping(self.destVictimApresSinistrComboBox, Victime.DESTINATION_APRES_SINISTRE)

        self.conclusionCertificatMedicalComboBox.setModel(self.model_victime)
        self.conclusionCertificatMedicalComboBox.setModelColumn(self.model_victime.fieldIndex("conclusions_certificat_medical"))
        self.mapperVictime.addMapping(self.conclusionCertificatMedicalComboBox, Victime.CONCLUSIONS_CERTIFICAT_MEDICAL)
        self.mapperVictime.addMapping(self.ObsSurVictimTextEdit, Victime.OBSERVATION_SUR_VICTIME)
        self.mapperVictime.addMapping(self.montantEstimeLineEdit, Victime.MONTANT_ESTIME)


        self.mapperVictime.toFirst()




        # Tableaux
        # Modele Sinistre
        self.model_sinistre.setHeaderData(Sinistre.NUMERO_DOSSIER, Qt.Horizontal, QtCore.QVariant("Numero Dossier"))
        self.model_sinistre.setHeaderData(Sinistre.DATE_SINISTRE, Qt.Horizontal, QtCore.QVariant("Date Sinistre"))
        self.model_sinistre.setHeaderData(Sinistre.LIEU_SINISTRE, Qt.Horizontal, QtCore.QVariant("Lieu Sinistre"))
        self.model_sinistre.setHeaderData(Sinistre.ID_SINISTRE, Qt.Horizontal, QtCore.QVariant("ID Sinistre"))
        self.model_sinistre.setHeaderData(Sinistre.MONTANT_CONCLUSIONS_EXPERT, Qt.Horizontal, QtCore.QVariant("Montant Estime"))

        self.model_sinistre.setHeaderData(Sinistre.ASSUREUR_ID, Qt.Horizontal, QtCore.QVariant("ID Assureur"))
        self.model_sinistre.setHeaderData(Sinistre.LIBELLE_ASSUREUR_ADVERSE, Qt.Horizontal, QtCore.QVariant("Assureur"))

        self.model_sinistre.select()

        # Liste Sinistres de la Victime
        self.listeSinistresVictimeTableView.setModel(self.model_sinistre)
        self.listeSinistresVictimeTableView.setItemDelegate(QtSql.QSqlRelationalDelegate(self))
        self.listeSinistresVictimeTableView.setSelectionMode(QtGui.QTableView.SingleSelection)
        self.listeSinistresVictimeTableView.setSelectionBehavior(QtGui.QTableView.SelectRows)

        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.ID_SINISTRE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.POLICE_ADVERSAIRE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.SOCIETAIRE_DECLARANT, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.REFERENCES_FICHIER, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.PROPRIETAIRE_VEHICULE_ADVERSE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.ASSUREUR_ADVERSE_ID, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.NATURE_SINISTRE_ID, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.VEHICULE_MIS_EN_CAUSE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.POLICE_ID, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DATE_DECLARATION, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.MIS_EN_CAUSE_PAR_TIERS, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.UTILISATEUR_ID, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DATE_OUVERTURE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.OBJET_ASSURE_ID, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.GARANTIE_EN_COURS, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.CIRCONSTANCES, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DOMMAGE_VEHICULE_ASSURE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.USAGE_LORS_DU_SINISTRE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.APPROBATION_INITIALE_ASSURE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.PASSAGERS_PENDANT_SINISTRE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.CONSTAT_AMIABLE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.COMPTE_RENDU_CONSTAT, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.OBSERVATION, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.REGLEMENT, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DOSSIER_COMPLET, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.PIECE_FOURNIE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DOSSIER_TRANSMIS_A_ASSUREUR, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DATE_TRANSMISSION, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.ACCUSE_RECEPTION_ASSUREUR, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DATE_ACCUSE_ASSUREUR, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.EXPERT_SOLLICITE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DATE_SOLLICITATION_EXPERT, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.EXPERTISE_EFFECTUEE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DATE_REPONSE_EXPERTISE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.CONCLUSIONS_EXPERT_ACCEPTEES, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DATE_ACCORD_CONCLUSION, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.MONTANT_PROPOSITION_ASSUREUR, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.MONTANT_REGLEMENT, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DATE_REGLEMENT, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.EXERCICE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.NUMERO_ORDRE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.NUMERO_POLICE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.GARANTIE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.USAGE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.RESEAU, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.PSAP_OUVERTURE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.PAIEMENT_PRINCIPAL, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.PAIEMENT_ACCESSOIRES, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.TERMINE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.CLASSE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.EN_COURS, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.STAND_BY, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.RISQUE_ADVERSE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.ASSUREUR_ID, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.EFFET_POLICE_ADVERSAIRE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.TERME_POLICE_ADVERSAIRE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.POLICE_CONNEXE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.ADRESSE_PROPRIETAIRE_VEHICULE_ADVERSE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.ASSURE_ADVERSE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.ADRESSE_ASSURE_ADVERSE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.CONDUCTEUR_ADVERSAIRE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DOMMAGE_ADVERSAIRES, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DECLARATION_ADVERSAIRE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DATE_DECLARATION_ADVERSAIRE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.ADVERSAIRE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.REFERENCE_ADVERSAIRE, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.PERSONNE_ID, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DATE_CREATION, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.REF_IMPORTATION, True)
        self.listeSinistresVictimeTableView.setColumnHidden(Sinistre.DATE_IMPORTATION, True)

        self.listeSinistresVictimeTableView.resizeColumnsToContents()
        self.listeSinistresVictimeTableView.horizontalHeader().setStretchLastSection(True)

        # Liste Assureurs de la Victime
        self.assureurVictimeSinistreTableView.setModel(self.model_sinistre)
        self.assureurVictimeSinistreTableView.setItemDelegate(QtSql.QSqlRelationalDelegate(self))
        self.assureurVictimeSinistreTableView.setSelectionMode(QtGui.QTableView.SingleSelection)
        self.assureurVictimeSinistreTableView.setSelectionBehavior(QtGui.QTableView.SelectRows)



        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.ID_SINISTRE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.POLICE_ADVERSAIRE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.SOCIETAIRE_DECLARANT, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.REFERENCES_FICHIER, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.PROPRIETAIRE_VEHICULE_ADVERSE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.ASSUREUR_ADVERSE_ID, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.NATURE_SINISTRE_ID, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.VEHICULE_MIS_EN_CAUSE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.POLICE_ID, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DATE_DECLARATION, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.MIS_EN_CAUSE_PAR_TIERS, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.UTILISATEUR_ID, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DATE_OUVERTURE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.OBJET_ASSURE_ID, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.GARANTIE_EN_COURS, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.CIRCONSTANCES, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DOMMAGE_VEHICULE_ASSURE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.USAGE_LORS_DU_SINISTRE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.APPROBATION_INITIALE_ASSURE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.PASSAGERS_PENDANT_SINISTRE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.CONSTAT_AMIABLE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.COMPTE_RENDU_CONSTAT, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.OBSERVATION, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.REGLEMENT, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DOSSIER_COMPLET, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.PIECE_FOURNIE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DOSSIER_TRANSMIS_A_ASSUREUR, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DATE_TRANSMISSION, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.ACCUSE_RECEPTION_ASSUREUR, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DATE_ACCUSE_ASSUREUR, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.EXPERT_SOLLICITE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DATE_SOLLICITATION_EXPERT, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.EXPERTISE_EFFECTUEE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DATE_REPONSE_EXPERTISE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.CONCLUSIONS_EXPERT_ACCEPTEES, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DATE_ACCORD_CONCLUSION, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.MONTANT_PROPOSITION_ASSUREUR, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.MONTANT_REGLEMENT, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DATE_REGLEMENT, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.EXERCICE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.NUMERO_ORDRE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.NUMERO_POLICE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.GARANTIE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.USAGE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.RESEAU, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.PSAP_OUVERTURE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.PAIEMENT_PRINCIPAL, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.PAIEMENT_ACCESSOIRES, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.TERMINE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.CLASSE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.EN_COURS, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.STAND_BY, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.RISQUE_ADVERSE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.ASSUREUR_ID, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.EFFET_POLICE_ADVERSAIRE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.TERME_POLICE_ADVERSAIRE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.POLICE_CONNEXE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.ADRESSE_PROPRIETAIRE_VEHICULE_ADVERSE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.ASSURE_ADVERSE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.ADRESSE_ASSURE_ADVERSE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.CONDUCTEUR_ADVERSAIRE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DOMMAGE_ADVERSAIRES, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DECLARATION_ADVERSAIRE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DATE_DECLARATION_ADVERSAIRE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.ADVERSAIRE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.REFERENCE_ADVERSAIRE, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.PERSONNE_ID, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DATE_CREATION, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.REF_IMPORTATION, True)
        self.assureurVictimeSinistreTableView.setColumnHidden(Sinistre.DATE_IMPORTATION, True)


        self.assureurVictimeSinistreTableView.resizeColumnsToContents()
        self.assureurVictimeSinistreTableView.horizontalHeader().setStretchLastSection(True)

        # Modele Prejudices de la Victime
        self.model_prejudice.setHeaderData(Prejudice.VICTIME_ID, Qt.Horizontal, QtCore.QVariant("ID Victime"))
        self.model_prejudice.setHeaderData(Prejudice.POSTE_PREJUDICE_ID, Qt.Horizontal, QtCore.QVariant("ID Poste Prejudice"))
        self.model_prejudice.setHeaderData(Prejudice.MONTANT_PROVISION, Qt.Horizontal, QtCore.QVariant("Montant Provision"))
        self.model_prejudice.setHeaderData(Prejudice.MONTANT_RECLAMATION, Qt.Horizontal, QtCore.QVariant("Montant Reclamation"))
        self.model_prejudice.setHeaderData(Prejudice.DIRE_EXPERT_RECLAMATION, Qt.Horizontal, QtCore.QVariant("Dire Expert Reclamation"))
        self.model_prejudice.setHeaderData(Prejudice.EVALUATION_FINALE, Qt.Horizontal, QtCore.QVariant("Evaluation Finale"))

        self.model_prejudice.select()

        self.analysePrejudicesVictimeTableView.setModel(self.model_prejudice)
        self.analysePrejudicesVictimeTableView.setItemDelegate(QtSql.QSqlRelationalDelegate(self))
        self.analysePrejudicesVictimeTableView.setSelectionMode(QtGui.QTableView.SingleSelection)
        self.analysePrejudicesVictimeTableView.setSelectionBehavior(QtGui.QTableView.SelectRows)

        self.analysePrejudicesVictimeTableView.setColumnHidden(Prejudice.ID_PREJUDICE_VICTIME, True)
        self.analysePrejudicesVictimeTableView.setColumnHidden(Prejudice.MONTANT_EVALUATION_EXPERT, True)
        self.analysePrejudicesVictimeTableView.setColumnHidden(Prejudice.MONTANT_AVIS_CHEF_SERVICE, True)
        self.analysePrejudicesVictimeTableView.setColumnHidden(Prejudice.MONTANT_AVIS_DIRECTEUR_AGENCE, True)
        self.analysePrejudicesVictimeTableView.setColumnHidden(Prejudice.MONTANT_AVIS_DIRECTEUR_GENERAL, True)
        self.analysePrejudicesVictimeTableView.setColumnHidden(Prejudice.ACTIF, True)
        self.analysePrejudicesVictimeTableView.setColumnHidden(Prejudice.DATE_CREATION, True)
        self.analysePrejudicesVictimeTableView.setColumnHidden(Prejudice.REF_IMPORTATION, True)
        self.analysePrejudicesVictimeTableView.setColumnHidden(Prejudice.DATE_IMPORTATION, True)

        self.analysePrejudicesVictimeTableView.resizeColumnsToContents()
        self.analysePrejudicesVictimeTableView.horizontalHeader().setStretchLastSection(True)

    def styleGui(self):
        self.dateDelivranceDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.dateNaissDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.validiteDateEdit.setDisplayFormat(self.DATETIME_FORMAT)

        # qlabelColor = QtCore.QString("oldlace")
        # qlineEditColor = QtCore.QString("white")

        self.labelProfessionVictime.setProperty('readonly', QtCore.QVariant(True))
        self.labelStatutMatVictime.setProperty('readonly', QtCore.QVariant(True))

        #(qlabelColor, qlineEditColor)
        #floralwhite, oldlace, seashell, lemonchiffon

        # self.labelEtatCivilVictime

        # self.setStyleSheet(styleSheet)




    def nouveauFichier(self):
        print "Halooo!"

    def addRecord(self):
        row = self.model_gest.rowCount()
        self.mapperPers.submit()
        self.model_gest.insertRow(row)
        self.mapperPers.setCurrentIndex(row)
        self.prenomComboBox.setFocus()

    def saveRecord(self, where, current=None):
        if self.listeSinistresVictimeTableView.hasFocus():
            # listeSinistresVictimeTableView a le Focus
            # gest = self.mapperPers.currentIndex() # Int
            index = self.listeSinistresVictimeTableView.currentIndex()
            if index.isValid():
                row = index.row()
                if where == VictimeSinistre.PREMIER:
                    print "Premier"
                    row = 0
                elif where == VictimeSinistre.PRECEDENT:
                    row = 0 if row <= 1 else row - 1
                    print "Precedent"
                elif where == VictimeSinistre.SUIVANT:
                    row += 1
                    if row >= self.model_sinistre.rowCount():
                        row = self.model_sinistre.rowCount() - 1
                    print "Suivant"
                elif where == VictimeSinistre.DERNIER:
                    # row = self.model_gest.rowCount() - 1
                    row = self.model_sinistre.rowCount() - 1
                    print "Dernier"
                elif where == VictimeSinistre.SAUVEGARDE:
                    # self.mapperPers.submit()
                    print "Save"
                self.listeSinistresVictimeTableView.selectRow(row)
        elif self.assureurVictimeSinistreTableView.hasFocus():
            # TableView a le Focus
            # gest = self.mapperPers.currentIndex() # Int
            index = self.assureurVictimeSinistreTableView.currentIndex()
            if index.isValid():
                row = index.row()
                if where == VictimeSinistre.PREMIER:
                    print "Premier"
                    row = 0
                elif where == VictimeSinistre.PRECEDENT:
                    row = 0 if row <= 1 else row - 1
                    print "Precedent"
                elif where == VictimeSinistre.SUIVANT:
                    row += 1
                    if row >= self.model_sinistre.rowCount():
                        row = self.model_sinistre.rowCount() - 1
                    print "Suivant"
                elif where == VictimeSinistre.DERNIER:
                    # row = self.model_gest.rowCount() - 1
                    row = self.model_sinistre.rowCount() - 1
                    print "Dernier"
                elif where == VictimeSinistre.SAUVEGARDE:
                    # self.mapperPers.submit()
                    print "Save"
                self.assureurVictimeSinistreTableView.selectRow(row)
        elif self.analysePrejudicesVictimeTableView.hasFocus():
            # TableView a le Focus
            # gest = self.mapperPers.currentIndex() # Int
            index = self.analysePrejudicesVictimeTableView.currentIndex()
            if index.isValid():
                row = index.row()
                if where == VictimeSinistre.PREMIER:
                    print "Premier"
                    row = 0
                elif where == VictimeSinistre.PRECEDENT:
                    row = 0 if row <= 1 else row - 1
                    print "Precedent"
                elif where == VictimeSinistre.SUIVANT:
                    row += 1
                    if row >= self.model_prejudice.rowCount():
                        row = self.model_prejudice.rowCount() - 1
                    print "Suivant"
                elif where == VictimeSinistre.DERNIER:
                    # row = self.model_gest.rowCount() - 1
                    row = self.model_prejudice.rowCount() - 1
                    print "Dernier"
                elif where == VictimeSinistre.SAUVEGARDE:
                    # self.mapperPers.submit()
                    print "Save"
                self.analysePrejudicesVictimeTableView.selectRow(row)
        else:
            # Le Mapper a le focus
            row = self.mapperPersonne.currentIndex()
            self.mapperPers.submit()
            if where == VictimeSinistre.PREMIER:
                row = 0
            elif where == VictimeSinistre.PRECEDENT:
                row = 0 if row <= 1 else row - 1
            elif where == VictimeSinistre.SUIVANT:
                row += 1
                if row >= self.model_gest.rowCount():
                    row = self.model_gest.rowCount() - 1
            elif where == VictimeSinistre.DERNIER:
                row = self.model_gest.rowCount() - 1
            elif where == VictimeSinistre.SAUVEGARDE:
                self.mapperPersonne.submit()

            self.mapperPersonne.setCurrentIndex(row)

            gest_en_cours = self.mapperPersonne.currentIndex()
            record = self.model_gest.record(gest_en_cours)
            id_gest = record.value("id_personne").toInt()[0]
            self.model_personne.setFilter(QtCore.QString("personne_id = %1").arg(id_gest))

    #
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
        print "Fermeture Suivit Victimes Sinistre"
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
    # for counter, tab in enumerate(sorted(db.tables())):
    #     print "Tab ", counter, " = ", tab

    main = VictimeSinistre()
    main.show()
    main.raise_()
    main.activateWindow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
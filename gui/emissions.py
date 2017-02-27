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

import detailgaranties, impressionattestation, paiements, ui_emissions

from models.personne import Personne
from models.police import Police
from models.objet_assure import ObjetAssure
from models.operation_production import OperationProduction

class Emissions(QtGui.QMainWindow, ui_emissions.Ui_Emissions):
    # DATETIME_FORMAT = "dd/MM/yyyy hh:mm:ss"
    DATETIME_FORMAT = "dd.MM.yyyy"
    PREMIER, PRECEDENT, SUIVANT, DERNIER, SAUVEGARDE = range(5)
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.model_personne = Personne()
        self.model_police = Police()
        self.model_obj_assur = ObjetAssure()
        self.model_op_prod = OperationProduction()
        # self.model_paiement = Paiement()
        self.setupUi(self)

        self.initUI()
        # self.styleGui()

        if sys.platform == 'win32':
            self.setFixedSize(1000, 650) #(1000, 635) # (1000, 650)
        elif sys.platform == 'darwin':
            self.setFixedSize(1000, 590) #(1000, 550) # (960, 550)
        elif sys.platfom == 'linux2':
            self.setFixedSize(1000, 550)

    def initUI(self):
        """
        Methode Initialisant les evenement de l'interface.
        :return:
        """
        # self.setGeometry(0, 0, 800, 450)

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
        # self.gridLayout_12.setSpacing(1)
        self.gridLayout_13.setSpacing(1)
        self.gridLayout_14.setSpacing(1)
        self.gridLayout_15.setSpacing(1)
        self.gridLayout_16.setSpacing(1)
        # self.gridLayout_17.setSpacing(1)
        # self.gridLayout_18.setSpacing(1)

        self.horizontalLayout_3.setSpacing(1)

        self.gridLayout_20.setSpacing(1)
        self.gridLayout_21.setSpacing(1)


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
        self.gridLayout_14.setMargin(1)
        self.gridLayout_15.setMargin(1)
        self.gridLayout_16.setMargin(1)
        # self.gridLayout_17.setMargin(1)
        # self.gridLayout_18.setMargin(1)

        # self.verticalLayout_2.setMargin(1)

        self.gridLayout_20.setMargin(1)
        self.gridLayout_21.setMargin(1)

        # Variables
        self.paie = None
        self.garantiesDetaillees = None
        self.attestations = None

        # Connection des Actions
        self.connect(self.fichierNouveau, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierEnregistrer, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierImprimAttestations, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierImprimerPiecesContrat, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.fichierFermer, SIGNAL("triggered()"), self.close)

        self.connect(self.editionAnnuler, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionRefaire, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionPremier, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionPrecedent, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionSuivant, SIGNAL("triggered()"), self.nouveauFichier)
        self.connect(self.editionDernier, SIGNAL("triggered()"), self.nouveauFichier)

        self.connect(self.traitementDetailsGarantiesSouscrites, SIGNAL("triggered()"), self.garanties)
        self.connect(self.traitementDetailsPaiements, SIGNAL("triggered()"), self.paiement)

        # Connection des Boutons
        self.connect(self.condPartToolButton, SIGNAL("clicked()"), self.conditionsParticulieres)
        self.connect(self.attAssurToolButton, SIGNAL("clicked()"), self.attestationsAssurance)
        self.connect(self.garantiesDetailleesToolButton, SIGNAL("clicked()"), self.garanties)
        self.connect(self.paiementsDetaillesToolButton, SIGNAL("clicked()"), self.paiement)
        # self.condPartToolButton.connect(self, SIGNAL("clicked()"), self.nouveauFichier)
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

        self.professionComboBox.setModel(self.model_personne)
        self.professionComboBox.setModelColumn(self.model_personne.fieldIndex("profession"))
        self.mapperPers.addMapping(self.professionComboBox, Personne.PROFESSION)

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
        self.mapperPers.addMapping(self.posteOccupeLineEdit, Personne.POSTE_OCCUPE)

        self.deptComboBox.setModel(self.model_personne)
        self.deptComboBox.setModelColumn(self.model_personne.fieldIndex("departement_ou_region"))
        self.mapperPers.addMapping(self.deptComboBox, Personne.DEPARTEMENT_OU_REGION)

        ztRelationModel = self.model_personne.relationModel(Personne.ZONE_TARIFICATION_ID)
        self.zoneTarifComboBox.setModel(ztRelationModel)
        self.zoneTarifComboBox.setModelColumn(ztRelationModel.fieldIndex("libelle_zone_tarification"))
        self.mapperPers.addMapping(self.zoneTarifComboBox, Personne.ZONE_TARIFICATION_ID)

        self.mapperPers.addMapping(self.phoneWLineEdit, Personne.NUMERO_TELEPHONE_BUREAU)
        self.mapperPers.addMapping(self.phoneHLineEdit, Personne.NUMERO_TELEPHONE_PORTABLE)
        self.mapperPers.addMapping(self.faxLineEdit, Personne.NUMERO_TELECOPIE)
        self.mapperPers.addMapping(self.mailLineEdit, Personne.ADRESSE_COURRIER_ELECTRONIQUE)
        self.mapperPers.addMapping(self.entreePortefeuilleDateEdit, Personne.DATE_ENTREE_PORTEFEUILLE)

        self.mapperPers.toFirst()


        # Mapper Police
        self.mapperPolice = QtGui.QDataWidgetMapper(self)
        self.mapperPolice.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapperPolice.setModel(self.model_police)
        self.mapperPolice.setItemDelegate(QtSql.QSqlRelationalDelegate(self))

        cieRM = self.model_police.relationModel(Police.ASSUREUR_ID)
        self.cieComboBox.setModel(cieRM)
        self.cieComboBox.setModelColumn(cieRM.fieldIndex("libelle_assureur"))
        self.mapperPolice.addMapping(self.cieComboBox, Police.ASSUREUR_ID)

        self.policeAgenceComboBox.setModel(self.model_police)
        self.policeAgenceComboBox.setModelColumn(self.model_police.fieldIndex("numero_police"))
        self.mapperPolice.addMapping(self.policeAgenceComboBox, Police.NUMERO_POLICE)

        resRM = self.model_police.relationModel(Police.RESEAU_ID)
        self.resAgenceComboBox.setModel(resRM)
        self.resAgenceComboBox.setModelColumn(resRM.fieldIndex("libelle_reseau"))
        self.mapperPolice.addMapping(self.resAgenceComboBox, Police.RESEAU_ID)

        # # gstRM = self.model_police.relationModel(Police.GESTIONNAIRE_ID)
        # self.gestComboBox.setModel(self.model_police)
        # self.gestComboBox.setModelColumn(self.model_police.fieldIndex("gestionnaire_id"))
        # self.mapperPolice.addMapping(self.gestComboBox, Police.GESTIONNAIRE_ID)

        gstRM = self.model_police.relationModel(Police.GESTIONNAIRE_ID)
        self.gestComboBox.setModel(gstRM)
        self.gestComboBox.setModelColumn(gstRM.fieldIndex("code_gestionnaire"))
        self.mapperPolice.addMapping(self.gestComboBox, Police.GESTIONNAIRE_ID)
        #
        brRM = self.model_police.relationModel(Police.BRANCHE_ID)
        self.branchComboBox.setModel(brRM)
        self.branchComboBox.setModelColumn(brRM.fieldIndex("libelle_branche"))
        self.mapperPolice.addMapping(self.branchComboBox, Police.BRANCHE_ID)

        self.mapperPolice.addMapping(self.policeCieLineEdit, Police.REFERENCE_ASSUREUR)

        self.mapperPolice.addMapping(self.commMemoTextEdit, Police.REMARQUES)

        self.flotteComboBox.setModel(self.model_police)
        self.flotteComboBox.setModelColumn(self.model_police.fieldIndex("flotte"))
        self.mapperPolice.addMapping(self.flotteComboBox, Police.FLOTTE_BIT)

        self.mapperPolice.addMapping(self.dateCreationDateEdit, Police.DATE_SOUSCRIPTION)
        self.mapperPolice.addMapping(self.debutAnnuelDateEdit, Police.EFFET_ANNUEL_CONTRAT)
        self.mapperPolice.addMapping(self.termAnnuelDateEdit, Police.TERME_ANNUEL_CONTRAT)

        self.valideComboBox.setModel(self.model_police)
        self.valideComboBox.setModelColumn(self.model_police.fieldIndex("etat"))
        self.mapperPolice.addMapping(self.valideComboBox, Police.ETAT)

        self.mapperPolice.addMapping(self.bonusMalusLineEdit, Police.BONUSMALUS_COURANT)
        self.mapperPolice.addMapping(self.reductionLineEdit, Police.TAUX_REDUCTION_COURANT)
        self.mapperPolice.addMapping(self.valAnnuelLineEdit, Police.VALEUR_ANNUELLE)

        self.mapperPolice.toFirst()


        # Liste
        self.listView.setModel(self.model_obj_assur)
        self.listView.setModelColumn(self.model_obj_assur.fieldIndex("immatriculation"))
        self.listView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)


        # Mapper Objet Assure
        self.mapperObjAssure = QtGui.QDataWidgetMapper(self)
        self.mapperObjAssure.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapperObjAssure.setModel(self.model_obj_assur)
        self.mapperObjAssure.setItemDelegate(QtSql.QSqlRelationalDelegate(self))

        self.mapperObjAssure.addMapping(self.numChassiLineEdit, ObjetAssure.NUMERO_SERIE)
        self.mapperObjAssure.addMapping(self.ImmatLineEdit, ObjetAssure.IMMATRICULATION)
        self.mapperObjAssure.addMapping(self.datePremMCDateEdit, ObjetAssure.DATE_ACQUISITION)
        self.mapperObjAssure.addMapping(self.valNeuvLineEdit, ObjetAssure.VALEUR_NEUVE)
        self.mapperObjAssure.addMapping(self.valVenalLineEdit, ObjetAssure.VALEUR_VENALE)
        self.mapperObjAssure.addMapping(self.valAccessLineEdit, ObjetAssure.VALEUR_ACCESSOIRES)

        self.markComboBox.setModel(self.model_obj_assur)
        self.markComboBox.setModelColumn(self.model_obj_assur.fieldIndex("marque"))
        self.mapperObjAssure.addMapping(self.markComboBox, ObjetAssure.MARQUE)

        self.modelTypComboBox.setModel(self.model_obj_assur)
        self.modelTypComboBox.setModelColumn(self.model_obj_assur.fieldIndex("modele"))
        self.mapperObjAssure.addMapping(self.modelTypComboBox, ObjetAssure.MODELE)

        genrRM = self.model_obj_assur.relationModel(ObjetAssure.GENRE_OBJET_ID)
        self.genrComboBox.setModel(genrRM)
        self.genrComboBox.setModelColumn(genrRM.fieldIndex("libelle_genre_objet"))
        self.mapperObjAssure.addMapping(self.genrComboBox, ObjetAssure.GENRE_OBJET_ID)

        self.mapperObjAssure.addMapping(self.nbPlaceSpinBox, ObjetAssure.NOMBRE_PLACES_CABINE)

        self.puissComboBox.setModel(self.model_obj_assur)
        self.puissComboBox.setModelColumn(self.model_obj_assur.fieldIndex("puissance"))
        self.mapperObjAssure.addMapping(self.puissComboBox, ObjetAssure.PUISSANCE)

        self.energiComboBox.setModel(self.model_obj_assur)
        self.energiComboBox.setModelColumn(self.model_obj_assur.fieldIndex("energie"))
        self.mapperObjAssure.addMapping(self.energiComboBox, ObjetAssure.ENERGIE)

        self.mapperObjAssure.addMapping(self.nomAssureLineEdit, ObjetAssure.NOM_ASSURE)
        self.mapperObjAssure.addMapping(self.adressAssureLineEdit, ObjetAssure.ADRESSE_ASSURE)
        self.mapperObjAssure.addMapping(self.nomConducteurLineEdit, ObjetAssure.CONDUCTEUR)

        ztRM = self.model_obj_assur.relationModel(ObjetAssure.ZONE_TARIFICATION_ID)
        self.zoneTarificationComboBox.setModel(ztRM)
        self.zoneTarificationComboBox.setModelColumn(ztRM.fieldIndex("libelle_zone_tarification"))
        self.mapperObjAssure.addMapping(self.zoneTarificationComboBox, ObjetAssure.ZONE_TARIFICATION_ID)

        self.mapperObjAssure.addMapping(self.numPermiLineEdit, ObjetAssure.NUMERO_PERMIS_CONDUIRE)

        pRM = self.model_obj_assur.relationModel(ObjetAssure.PERMIS_CONDUIRE_ID)
        self.classifPermiComboBox.setModel(pRM)
        self.classifPermiComboBox.setModelColumn(pRM.fieldIndex("libelle_permis_conduire"))
        self.mapperObjAssure.addMapping(self.classifPermiComboBox, ObjetAssure.PERMIS_CONDUIRE_ID)

        self.catPermiComboBox.setModel(self.model_obj_assur)
        self.catPermiComboBox.setModelColumn(self.model_obj_assur.fieldIndex("categorie_permis"))
        self.mapperObjAssure.addMapping(self.catPermiComboBox, ObjetAssure.CATEGORIE_PERMIS)
        self.mapperObjAssure.addMapping(self.dateObtPermiDateEdit, ObjetAssure.DATE_OBTENTION_PERMIS)
        self.mapperObjAssure.addMapping(self.validitePermiDateEdit, ObjetAssure.DATE_VALIDITE_PERMIS)
        self.mapperObjAssure.addMapping(self.numCapaLineEdit, ObjetAssure.CAPACITE)
        self.mapperObjAssure.addMapping(self.validiteCapaDateEdit, ObjetAssure.DATE_VALIDITE_CAPACITE)

        self.catSocioProComboBox.setModel(self.model_obj_assur)
        self.catSocioProComboBox.setModelColumn(self.model_obj_assur.fieldIndex("categorie_socioprofessionnelle"))
        self.mapperObjAssure.addMapping(self.catSocioProComboBox, ObjetAssure.CATEGORIE_SOCIOPROFESSIONNELLE)
        self.mapperObjAssure.addMapping(self.matInflamCheckBox, ObjetAssure.TRANSPORT_MATIERE_INFLAMMABLE)
        self.mapperObjAssure.addMapping(self.cartRosCheckBox, ObjetAssure.EMISSION_CARTE_ROSE)
        self.mapperObjAssure.addMapping(self.vehiculeActifCheckBox, ObjetAssure.ACTIF)

        self.mapperObjAssure.addMapping(self.attRemGroupBoxEmissions, ObjetAssure.ATTELAGE_REMORQUE)

        self.markAtRemComboBox.setModel(self.model_obj_assur)
        self.markAtRemComboBox.setModelColumn(self.model_obj_assur.fieldIndex("marque_remorque"))
        self.mapperObjAssure.addMapping(self.markAtRemComboBox, ObjetAssure.MARQUE_REMORQUE)
        self.typAtRemComboBox.setModel(self.model_obj_assur)
        self.typAtRemComboBox.setModelColumn(self.model_obj_assur.fieldIndex("type_remorque"))
        self.mapperObjAssure.addMapping(self.typAtRemComboBox, ObjetAssure.TYPE_REMORQUE)
        self.mapperObjAssure.addMapping(self.ImmatAtRemLineEdit, ObjetAssure.IMMATRICULATION_REMORQUE)
        self.mapperObjAssure.addMapping(self.valRemAtRemLineEdit, ObjetAssure.VALEUR_REMORQUE)

        self.mapperObjAssure.toFirst()

        # Mapper Operation Production
        self.mapperOpProd = QtGui.QDataWidgetMapper(self)
        self.mapperOpProd.setModel(self.model_op_prod)
        self.mapperOpProd.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
        self.mapperOpProd.setItemDelegate(QtSql.QSqlRelationalDelegate(self))

        natRM = self.model_op_prod.relationModel(OperationProduction.NATURE_OPERATION_ID)
        self.natMouvComboBox.setModel(natRM)
        self.natMouvComboBox.setModelColumn(natRM.fieldIndex("libelle_nature_operation"))
        self.mapperOpProd.addMapping(self.natMouvComboBox, OperationProduction.NATURE_OPERATION_ID)

        redRM = self.model_op_prod.relationModel(OperationProduction.UTILISATEUR_ID)
        self.redacteurComboBox.setModel(redRM)
        self.redacteurComboBox.setModelColumn(redRM.fieldIndex("numero_utilisateur"))
        self.mapperOpProd.addMapping(self.redacteurComboBox, OperationProduction.UTILISATEUR_ID)

        self.baremComboBox.setModel(self.model_op_prod)
        self.baremComboBox.setModelColumn(self.model_op_prod.fieldIndex("type_bareme"))

        self.mapperOpProd.addMapping(self.baremComboBox, OperationProduction.TYPE_BAREME)
        self.mapperOpProd.addMapping(self.dateEmissionDateEdit, OperationProduction.DATE_OPERATION)
        self.mapperOpProd.addMapping(self.dateEffetDateEdit, OperationProduction.DATE_EFFET)
        self.mapperOpProd.addMapping(self.dateExpDateEdit, OperationProduction.DATE_TERME)
        self.mapperOpProd.addMapping(self.dureeLineEdit, OperationProduction.DUREE)
        self.mapperOpProd.addMapping(self.tauxPeriodLineEdit, OperationProduction.TAUX_PERIODE)
        self.mapperOpProd.addMapping(self.primAnnuelLineEdit, OperationProduction.PRIME_ANNUELLE)
        self.mapperOpProd.addMapping(self.primPeriodLineEdit, OperationProduction.PRIME_BASE)
        self.mapperOpProd.addMapping(self.remiseLineEdit, OperationProduction.REMISE)
        self.mapperOpProd.addMapping(self.primNetLineEdit, OperationProduction.COTISATION_NETTE)
        self.mapperOpProd.addMapping(self.ristournLineEdit, OperationProduction.RISTOURNE)
        self.mapperOpProd.addMapping(self.accessLineEdit, OperationProduction.ACCESSOIRES)
        self.mapperOpProd.addMapping(self.fichierCentralLineEdit, OperationProduction.FRAIS_FICHIER_CENTRAL)
        self.mapperOpProd.addMapping(self.tvaLineEdit, OperationProduction.TVA)
        self.mapperOpProd.addMapping(self.primttcLineEdit, OperationProduction.COTISATION_TOTALE)

        self.mapperOpProd.addMapping(self.G01CheckBoxEmissions, OperationProduction.G01)
        self.mapperOpProd.addMapping(self.G02CheckBoxEmissions, OperationProduction.G02)
        self.mapperOpProd.addMapping(self.G03CheckBoxEmissions, OperationProduction.G03)
        self.mapperOpProd.addMapping(self.G04CheckBoxEmissions, OperationProduction.G04)
        self.mapperOpProd.addMapping(self.G05CheckBoxEmissions, OperationProduction.G05)
        self.mapperOpProd.addMapping(self.G06CheckBoxEmissions, OperationProduction.G06)
        self.mapperOpProd.addMapping(self.G07CheckBoxEmissions, OperationProduction.G07)
        self.mapperOpProd.addMapping(self.G08CheckBoxEmissions, OperationProduction.G08)
        self.mapperOpProd.addMapping(self.G09CheckBoxEmissions, OperationProduction.G09)
        self.mapperOpProd.addMapping(self.G10CheckBoxEmissions, OperationProduction.G10)
        self.mapperOpProd.addMapping(self.G11CheckBoxEmissions, OperationProduction.G11)
        self.mapperOpProd.addMapping(self.G12CheckBoxEmissions, OperationProduction.G12)
        self.mapperOpProd.addMapping(self.G13CheckBoxEmissions, OperationProduction.G13)
        self.mapperOpProd.addMapping(self.G14CheckBoxEmissions, OperationProduction.G14)
        self.mapperOpProd.addMapping(self.G15CheckBoxEmissions, OperationProduction.G15)
        self.mapperOpProd.addMapping(self.G16CheckBoxEmissions, OperationProduction.G16)
        self.mapperOpProd.addMapping(self.G17CheckBoxEmissions, OperationProduction.G17)
        self.mapperOpProd.addMapping(self.G18CheckBoxEmissions, OperationProduction.G18)
        self.mapperOpProd.addMapping(self.G19CheckBoxEmissions, OperationProduction.G19)
        self.mapperOpProd.addMapping(self.G20CheckBoxEmissions, OperationProduction.G20)
        self.mapperOpProd.addMapping(self.G21CheckBoxEmissions, OperationProduction.G21)
        self.mapperOpProd.addMapping(self.G22CheckBoxEmissions, OperationProduction.G22)
        self.mapperOpProd.addMapping(self.G23CheckBoxEmissions, OperationProduction.G23)
        self.mapperOpProd.addMapping(self.G24CheckBoxEmissions, OperationProduction.G24)

        self.mapperOpProd.toFirst()

    def styleGui(self):
        self.entreePortefeuilleDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.dateCreationDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.debutAnnuelDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.termAnnuelDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.datePremMCDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.dateObtPermiDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.validitePermiDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.validiteCapaDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.dateEmissionDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.dateEffetDateEdit.setDisplayFormat(self.DATETIME_FORMAT)
        self.dateExpDateEdit.setDisplayFormat(self.DATETIME_FORMAT)

        # qlabelColor = QtCore.QString("oldlace")
        # qlineEditColor = QtCore.QString("white")
        # qtextEditColor = QtCore.QString("springgreen")
        # qlabelEmissionColor = QtCore.QString("blue")
        # mandatoryFieldColor = QtCore.QString("red")

        # self.labelEmission.setProperty("colored", True)
        # self.labelPaiement.setProperty("colored", True)
        # self.labelSolde.setProperty("colored", True)

        # self.labelNumClient.setProperty("mandatoryField", True)

        #(qlabelColor, qlineEditColor)
        #floralwhite, oldlace, seashell, lemonchiffon

        # self.setStyleSheet(styleSheet)




    def nouveauFichier(self):
        """
        Action Nouveau Fichier
        :return:
        """
        print "Connected!!!"

    def conditionsParticulieres(self):
        """
        Action Conditions Particulieres
        :return:
        """
        QMessageBox.information(self, "Gesiard", "Imprimer Conditions Particulieres", QMessageBox.Ok)

    def attestationsAssurance(self):
        """
        Action Attestations Assurance
        :return:
        """
        if self.attestations == None:
            self.attestations = impressionattestation.ImpressionAttestation(self)

        screen = QtCore.QCoreApplication.instance().desktop().screenGeometry()
        mysize = self.attestations.geometry()
        hpos = (screen.width() - mysize.width()) / 2
        vpos = (screen.height() - mysize.height()) /2
        self.attestations.move(hpos, vpos)


        self.attestations.show()
        self.attestations.raise_()
        self.attestations.activateWindow()

    def garanties(self):
        """
        Action Garanties Detaillees
        :return:
        """
        if self.garantiesDetaillees == None:
            self.garantiesDetaillees = detailgaranties.DetailGaranties(self)

        screen = QtCore.QCoreApplication.instance().desktop().screenGeometry()
        mysize = self.garantiesDetaillees.geometry()
        hpos = (screen.width() - mysize.width()) / 2
        vpos = (screen.height() - mysize.height()) /2
        self.garantiesDetaillees.move(hpos, vpos)


        self.garantiesDetaillees.show()
        self.garantiesDetaillees.raise_()
        self.garantiesDetaillees.activateWindow()


    def paiement(self):
        """
        Action Paiements Detailles
        :return:
        """
        if self.paie == None:
            self.paie = paiements.Paiements(self)

        screen = QtCore.QCoreApplication.instance().desktop().screenGeometry()
        mysize = self.paie.geometry()
        hpos = (screen.width() - mysize.width()) / 2
        vpos = (screen.height() - mysize.height()) /2
        self.paie.move(hpos, vpos)


        self.paie.show()
        self.paie.raise_()
        self.paie.activateWindow()

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
        print "Fermeture Emission"
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

    # model_pers = Personne()
    # model_police = Police()
    # model_obj_assure = ObjetAssure()

    main = Emissions()
    main.show()
    main.raise_()
    main.activateWindow()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



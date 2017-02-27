#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

from PyQt4 import QtCore, QtGui, QtSql


class Personne(QtSql.QSqlRelationalTableModel):
    # Constantes
    ID_PERSONNE, NUMERO_PERSONNE, PRENOM_PERSONNE, NOM_PERSONNE, TITRE_CIVILITE_ID, PERSONNE_MORALE, GENRE_PERSONNE_ID, \
    STATUT_PERSONNE, TYPE_PERSONNE_ID, COMPTE_PRINCIPAL, NOM_ETABLISSEMENT, ADRESSE_FACTURATION, LOCALISATION, \
    VILLE, DEPARTEMENT_OU_REGION, CODE_POSTAL, QUARTIER, NUMERO_DOMICILE, PAYS_ID, NUMERO_TELEPHONE_BUREAU, \
    NUMERO_TELECOPIE, NUMERO_TELEPHONE_PORTABLE, NUMERO_TELEPHONE_SUPPLEMENTAIRE, ADRESSE_COURRIER_ELECTRONIQUE, \
    SITUATION_MATRIMONIALE, SECTEUR_PROFESSIONNEL, PROFESSION, POSTE_TRAVAIL, POSTE_OCCUPE, ZONE_TARIFICATION_ID, \
    DATE_ENTREE_PORTEFEUILLE, EXONERE_TAXE, REMARQUES, NUMERO_CNI, DATE_DELIVRANCE_CNI, LIEU_DELIVRANCE_CNI, \
    DATE_VALIDITE_CNI, ANCIEN_NUMERO_PERSONNE, REDACTEUR, DATE_NAISSANCE, LIEU_NAISSANCE, PHOTOGRAPHIE, \
    TELPROFESSIONNEL, LIMITE_CREDIT, DUREE_CREDIT, OUTREPASSER_LIMITES, MODIFIER_DELAI_REGLEMENT, \
    MODIFIER_PLAFOND_DECOUVERT, REPORT_EMISSIONS, REPORT_ENCAISSEMENTS, SOLDE_VERIFIE, DATE_VERIFICATION, \
    SOLDE_VALIDE, DATE_VALIDATION, RECOMMANDE_PAR, ENVOYER_SMS_AU_CLIENT, SMS_ENVOYE_AU_CLIENT, \
    DATE_ENVOI_SMS_AU_CLIENT, ACCORDER_DEBIT, ENCAISSER_CHEQUES, ACTIF, DATE_CREATION, REF_IMPORTATION, \
    DATE_IMPORTATION = range(64)

    def __init__(self, parent=None):
        super(Personne, self).__init__(parent)
        self.setTable("personne")
        self.setRelation(self.GENRE_PERSONNE_ID, QtSql.QSqlRelation("genre_personne", "id_genre_personne", "libelle_genre_personne"))
        self.setRelation(self.PAYS_ID, QtSql.QSqlRelation("pays", "id_pays", "libelle_pays"))
        self.setRelation(self.TITRE_CIVILITE_ID, QtSql.QSqlRelation("titre_civilite", "id_titre_civilite", "libelle_titre_civilite"))
        self.setRelation(self.TYPE_PERSONNE_ID, QtSql.QSqlRelation("type_personne", "id_type_personne", "libelle_type_personne"))
        self.setRelation(self.ZONE_TARIFICATION_ID, QtSql.QSqlRelation("zone_tarification", "id_zone_tarification", "libelle_zone_tarification"))


        self.select()





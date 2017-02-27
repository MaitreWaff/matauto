#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

from PyQt4 import QtCore, QtGui, QtSql

class Police(QtSql.QSqlRelationalTableModel):
    # Constantes
    ID_POLICE, RESEAU_ID, GESTIONNAIRE_ID, BRANCHE_ID, PERSONNE_ID, ASSUREUR_ID, DATE_SOUSCRIPTION, NUMERO_POLICE, \
    REFERENCE_ASSUREUR, FLOTTE_BIT, PROPOSITION, EFFET_ANNUEL_CONTRAT, FIXER_EFFET_ANNUEL, TERME_ANNUEL_CONTRAT, \
    TAUX_REDUCTION_COURANT, BONUSMALUS_COURANT, VALEUR_ANNUELLE, MONTANT_FORFAITAIRE, POLICE_HORS_TAXE, REMARQUES, \
    STATUT_POLICE, IMPOSER_PRIME_ANNUELLE, PRIME_CONCLUE, ETAT, RECONDUCTION, DUREE_CONSOMMEE, DATE_CREATION, \
    REF_IMPORTATION, DATE_IMPORTATION = range(29)

    def __init__(self, parent=None):
        super(Police, self).__init__(parent)

        self.setTable("police")
        self.setRelation(self.ASSUREUR_ID, QtSql.QSqlRelation("assureur", "id_assureur", "libelle_assureur"))
        self.setRelation(self.BRANCHE_ID, QtSql.QSqlRelation("branche", "id_branche", "libelle_branche"))
        self.setRelation(self.GESTIONNAIRE_ID, QtSql.QSqlRelation("gestionnaire", "id_gestionnaire", "code_gestionnaire"))
        self.setRelation(self.PERSONNE_ID, QtSql.QSqlRelation("personne", "id_personne", "nom_personne"))
        self.setRelation(self.RESEAU_ID, QtSql.QSqlRelation("reseau", "id_reseau", "libelle_reseau"))

        self.select()
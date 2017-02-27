#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

from PyQt4 import QtCore, QtGui, QtSql

class Prejudice(QtSql.QSqlRelationalTableModel):
    # Constantes
    ID_PREJUDICE_VICTIME, VICTIME_ID, POSTE_PREJUDICE_ID, MONTANT_PROVISION, MONTANT_RECLAMATION, \
    DIRE_EXPERT_RECLAMATION, MONTANT_EVALUATION_EXPERT, MONTANT_AVIS_CHEF_SERVICE, MONTANT_AVIS_DIRECTEUR_AGENCE, \
    MONTANT_AVIS_DIRECTEUR_GENERAL, EVALUATION_FINALE, ACTIF, DATE_CREATION, REF_IMPORTATION, DATE_IMPORTATION = range(15)

    def __init__(self, parent=None):
        super(Prejudice, self).__init__(parent)

        self.setTable("prejudice")
        self.setRelation(self.POSTE_PREJUDICE_ID, QtSql.QSqlRelation("poste_prejudice", "id_poste_prejudice", "libelle_poste_prejudice"))
        self.setRelation(self.VICTIME_ID, QtSql.QSqlRelation("victime", "id_victime", "numero_victime"))

        self.select()
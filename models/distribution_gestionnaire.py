#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

from PyQt4 import QtCore, QtGui, QtSql #, Qt


class DistributionGestionnaire(QtSql.QSqlRelationalTableModel):
    # Constantes
    ID_DISTRIBUTION_GESTIONNAIRE, RESEAU_ID, GESTIONNAIRE_ID, MODELE_COMMISSIONNEMENT_ID, DATE_DEBUT_PRODUCTION, \
    ACTIF, DATE_CREATION, REF_IMPORTATION, DATE_IMPORTATION = range(9)

    def __init__(self, parent=None):
        super(DistributionGestionnaire, self).__init__(parent)

        self.setTable("distribution_gestionnaire")
        self.setRelation(self.GESTIONNAIRE_ID, QtSql.QSqlRelation("gestionnaire", "id_gestionnaire", \
                                                             "nom_famille_gestionnaire"))
        self.setRelation(self.MODELE_COMMISSIONNEMENT_ID, QtSql.QSqlRelation("modele_commissionnement", \
                                                        "id_modele_commissionnement", "libelle_modele_commissionnement"))
        self.setRelation(self.RESEAU_ID, QtSql.QSqlRelation("reseau", "id_reseau", "libelle_reseau"))
        self.select()
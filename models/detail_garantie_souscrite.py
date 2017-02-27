#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

from PyQt4 import QtCore, QtGui, QtSql

class DetailGarantieSouscrite(QtSql.QSqlRelationalTableModel):
    # Constantes
    ID_DETAIL_GARANTIE_SOUSCRITE, GARANTIE_ID, DETAIL_OPERATION_PRODUCTION_ID, DATE_OPERATION_REFERANTE, ACTIF, \
    VALEUR_CAPITAL, ANNUITE_PRIME, TAUX_PRIME_APPLIQUE, BASE_PRIME, TAUX_REDUCTION_APPLIQUE, REDUCTION, PRIME, \
    PRIME_MANUELLE, RISTOURNE_GARANTIE, TAUX_COMMISSION, COMMISSION_POTENTIELLE, RANG, EMPLACEMENT_GARANTIE_ID, \
    REMARQUES, EMPLACEMENT_RESERVE, DATE_CREATION , REF_IMPORTATION, DATE_IMPORTATION = range(23)

    def __init__(self, parent=None):
        super(DetailGarantieSouscrite, self).__init__(parent)

        self.setTable("detail_garantie_souscrite")
        self.setRelation(self.DETAIL_OPERATION_PRODUCTION_ID, QtSql.QSqlRelation("detail_operation_production", \
                                                                "id_detail_operation_production", "statut_mouvement"))
        self.setRelation(self.EMPLACEMENT_GARANTIE_ID, QtSql.QSqlRelation("emplacement_garantie", \
                                                                "id_emplacement_garantie", "libelle_emplacement_garantie"))
        self.setRelation(self.GARANTIE_ID, QtSql.QSqlRelation("garantie", "id_garantie", \
                                                                     "libelle_garantie"))
        # self.setRelation(self.GARANTIE_ID, QtSql.QSqlRelation("garantie_generique", "id_garantie_generique", \
        #                                                       "libelle_garantie_generique"))
        self.select()


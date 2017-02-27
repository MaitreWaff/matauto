#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

from PyQt4 import QtCore, QtGui, QtSql


class DetailPaiement(QtSql.QSqlRelationalTableModel):
    # Constantes
    ID_DETAIL_PAIEMENT, PAIEMENT_ID, LIBELLE_PAIEMENT_ID, SOMME_REGLEE, VALIDE, DATE_VALIDATION, OBSERVATION, \
    REF_IMPORTATION, DATE_CREATION, DATE_IMPORTATION = range(10)

    def __init__(self, parent=None):
        super(DetailPaiement, self).__init__(parent)

        self.setTable("detail_paiement")
        self.setRelation(self.LIBELLE_PAIEMENT_ID, QtSql.QSqlRelation("libelle_paiement", "id_libelle_paiement", \
                                                                 "libelle_libelle_paiement"))
        self.setRelation(self.PAIEMENT_ID, QtSql.QSqlRelation("paiement", "id_paiement", "numero_paiement"))
        self.select()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

from PyQt4 import QtCore, QtGui, QtSql

class BordereauReversementProduction(QtSql.QSqlRelationalTableModel):
    # Constantes
    ID_BORDEREAU_REVERSEMENT_PRODUCTION, ASSUREUR_ID, OPERATEUR_ID, DATE_REVERSEMENT, NUMERO_BORDEREAU_REVERSEMENT, \
    REVERSEMENT_SUR_ENCAISSEMENT, MONTANT_A_REVERSER, PLAFONNE, MONTANT_REVERSE, SOLDE_COURANT, VALIDATION, \
    DATE_VALIDATION, DESCRIPTION_BORDEREAU, COMMENTAIRE, DATE_CREATION, REF_IMPORTATION, DATE_IMPORTATION = range(17)

    def __init__(self, parent=None):
        super(BordereauReversementProduction, self).__init__(parent)

        self.setTable("bordereau_reversement_production")
        self.setRelation(self.ASSUREUR_ID, QtSql.QSqlRelation("assureur", "id_assureur", "code_assureur"))
        self.select()
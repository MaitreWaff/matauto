#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

from PyQt4 import QtCore, QtGui, QtSql

class Pays(QtSql.QSqlRelationalTableModel):
    # Constantes
    ID_PAYS, LIBELLE_PAYS, LIBELLE_NATIONALITE_FEMININ, LIBELLE_NATIONALITE_MASCULIN, DATE_CREATION, REF_IMPORTATION, \
    DATE_IMPORTATION = range(7)

    def __init__(self, parent=None):
        super(Pays, self).__init__(parent)

        self.setTable("pays")

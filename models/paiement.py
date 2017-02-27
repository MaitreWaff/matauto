#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

from PyQt4 import QtCore, QtGui, QtSql

class Paiement(QtSql.QSqlRelationalTableModel):
    # Constantes
    ID_PAIEMENT, MODE_PAIEMENT_ID, OPERATION_PRODUCTION_ID, LIBELLE_ECRITURE, NUMERO_PAIEMENT, MONTANT_PAIEMENT, \
    DATE_PAIEMENT, NUMERO_RECU, PAYEUR_EFFET_ID, NUMERO_EFFET, TITULAIRE_COMPTE_EFFET, DATE_ENCAISSEMENT_EFFET, \
    AUTRES_INFORMATIONS, VALIDER_COMMISSIONNEMENT, COMMISSIONS_A_PAYER, PAIEMENT_VALIDE, RECU_IMPRIME, \
    JOUR_IMPUTATION, NUMERO_PROTOCOLE, RANG_PAIEMENT, GENERER_DUPLICATA, CHOISI, NUMERO_PAIEMENT_IMPORTE, \
    NUMERO_PIECE_IMPORTEE, REGLEMENTS_CUMULES, NUMERO_PAIEMENT_REFERENCE, DATE_CREATION, REF_IMPORTATION, \
    DATE_IMPORTATION = range(29)

    def __init__(self, parent=None):
        super(Paiement, self).__init__(parent)
        self.setTable("paiement")
        self.setRelation(self.MODE_PAIEMENT_ID, QtSql.QSqlRelation("mode_paiement", "id_mode_paiement", \
                                                                   "libelle_mode_paiement"))
        self.setRelation(self.OPERATION_PRODUCTION_ID, QtSql.QSqlRelation("operation_production", "id_operation_production", \
                                                                   "libelle_operation_production"))
        self.setRelation(self.PAYEUR_EFFET_ID, QtSql.QSqlRelation("payeur_effet", "id_payeur_effet", \
                                                                   "libelle_payeur_effet"))
        self.select()
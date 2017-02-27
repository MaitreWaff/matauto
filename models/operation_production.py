#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

from PyQt4 import QtCore, QtGui, QtSql

class OperationProduction(QtSql.QSqlRelationalTableModel):
    # Constantes
    ID_OPERATION_PRODUCTION, NATURE_OPERATION_ID, UTILISATEUR_ID, POLICE_ID, LIBELLE_OPERATION_PRODUCTION, NUMERO_OPERATION, \
    DATE_OPERATION, DUREE, TYPE_BAREME, DATE_EFFET, POLICE_ACTIVE, DATE_TERME, PRIME_MANUELLE, PRIME_ANNUELLE, TAUX_PERIODE, \
    PRIME_BASE, REMISE, COTISATION_NETTE, ACCESSOIRES, ACCESSOIRES_IMPOSES, EXONERE, TVA, FRAIS_FICHIER_CENTRAL, AUTRES_FRAIS, \
    COTISATION_TOTALE, MOTIF_AVENANT, NUMERO_AVENANT, NUMERO_QUITTANCE_EMISSION, NUMERO_ATTESTATION, A_RELANCER, \
    DATE_POUR_RELANCE, A_COMMISSIONNER, COMMISSION_POTENTIELLE, AVANCE_COMMISSION, DATE_AVANCE, OBSERVATION, STATUT_OPERATION, \
    RISTOURNE, DATE_IMPUTATION, DATE_TRAITEMENT, DATE_SAISIE, ACTIF, VALIDE, COMMISSION_A_PAYER, VALIDER_COMMISSIONNEMENT, \
    DATE_COMMISSIONNEMENT, G01, G02, G03, G04, G05, G06, G07, G08, G09, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20, \
    G21, G22, G23, G24, EMISSION_EN_DIFFERE, EXTENSION_GARANTIE, RANG_OPERATION, RELANCE_EFFECTUEE, DATE_RELANCE, ENVOYER_SMS, \
    SMS_ENVOYE, DATE_ENVOI_SMS, REFERENCE_MOUVEMENT_CONSECUTIF, REFERENCE_MOUVEMENT_ANTERIEUR, REDUCTION_IMPOSEE, \
    BONUS_MALUS_IMPOSE, A_REVERSER, REVERSEMENT_VALIDE, DATE_REVERSEMENT, DATE_CREATION, REF_IMPORTATION, \
    DATE_IMPORTATION = range(88)
    def __init__(self, parent=None):
        super(OperationProduction, self).__init__(parent)

        self.setTable("operation_production")
        self.setRelation(self.NATURE_OPERATION_ID, QtSql.QSqlRelation("nature_operation", "id_nature_operation", "libelle_nature_operation"))
        self.setRelation(self.POLICE_ID, QtSql.QSqlRelation("police", "id_police", "numero_police"))
        self.setRelation(self.UTILISATEUR_ID, QtSql.QSqlRelation("utilisateur", "id_utilisateur", "numero_utilisateur"))

        self.select()
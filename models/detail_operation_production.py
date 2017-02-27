#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

from PyQt4 import QtCore, QtGui, QtSql

class DetailOperationProduction(QtSql.QSqlRelationalTableModel):
    # Constantes
    ID_DETAIL_OPERATION_PRODUCTION, OPERATION_PRODUCTION_ID, OBJET_ASSURE_ID, CATEGORIE_ID, RANG, DATE_OPERATION_BASE, \
    ATTESTATION_UTILISEE, NUMERO_ATTESTATION, ATTESTATION_IMPOSEE, CARTE_ROSE_UTILISEE, NUMERO_CARTE_ROSE, \
    CARTE_ROSE_IMPOSEE, PRIME_BASE_ANNUELLE, TAUX_PERIODE, BASE_PRIME, REDUCTION, PRIME, RISTOURNE_OBJET, \
    PRIME_MANUELLE, VALEUR_CARTE_ROSE, CARTE_ROSE_REGLEE, TAUX_COMMISSION_PRIME_NETTE, COMMISSION_POTENTIELLE, \
    STATUT_MOUVEMENT, REFERENCE_FLOTTE, G01, G02, G03, G04, G05, G06, G07, G08, G09, G10, G11, G12, G13, G14, G15, \
    G16, G17, G18, G19, G20, G21, G22, G23, G24, OPTION_G06, ATTESTATION_A_IMPRIMER, ATTESTATION_DEJA_IMPRIMEE, \
    DATE_IMPRESSION_ATTESTATION, CARTE_EXTENSION_A_IMPRIMER, CARTE_EXTENSION_DEJA_IMPRIMEE, \
    DATE_IMPRESSION_CARTE_EXTENSION, TEXTE_AVENANT, DATE_TRAITEMENT, DATE_CREATION, REF_IMPORTATION, \
    DATE_IMPORTATION = range(61)

    def __init__(self, parent=None):
        super(DetailOperationProduction, self).__init__(parent)

        self.setTable("detail_operation_production")
        self.setRelation(self.CATEGORIE_ID, QtSql.QSqlRelation("categorie", "id_categorie", "libelle_categorie"))
        self.setRelation(self.OBJET_ASSURE_ID, QtSql.QSqlRelation("objet_assure", "id_objet_assure", "libelle_objet_assure"))
        self.setRelation(self.OPERATION_PRODUCTION_ID, QtSql.QSqlRelation("operation_production", "id_operation_production", \
                                                                     "libelle_operation_production"))

        self.select()


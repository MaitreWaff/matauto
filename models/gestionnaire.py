#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

from PyQt4 import QtCore, QtGui, QtSql


class Gestionnaire(QtSql.QSqlRelationalTableModel):
    # Constantes
    ID_GESTIONNAIRE, PERSONNE_ID, CODE_GESTIONNAIRE, PRENOM_GESTIONNAIRE, NOM_FAMILLE_GESTIONNAIRE, \
    ADRESSE_GESTIONNAIRE, TITRE_CIVILITE_ID, DATE_NAISSANCE, LIEU_NAISSANCE, POSTE_TRAVAIL, \
    NUMERO_TELEPHONE_PROFESSIONNEL, NUMERO_TELEPHONE_PERSONNEL, NUMERO_TELEPHONE_MOBILE, \
    NUMERO_TELECOPIE, ADRESSE_COURRIER_ELECTRONIQUE, CENTRES_INTERETS, DATE_RECRUTEMENT, \
    TAUX_COMMISSION, VALEUR_MAX_TAUX_COMMISSION, TAUX_COMMISSION_2, VALEUR_MAX_TAUX_COMMISSION_2, \
    TAUX_COMMISSION_3, VALEUR_MAX_TAUX_COMMISSION_3, REMARQUES, TAUX_COMMISSION_PRIME_NETTE, \
    TAUX_COMMISSION_PRIME_ACCESSOIRES, TAUX_COMMISSION_AUTRES, DIVERS, SUGGESTIONS, TYPE_GESTIONNAIRE_ID, \
    FIXE_MENSUEL, ACTIF, DATE_CREATION, REF_IMPORTATION, DATE_IMPORTATION = range(35)

    def __init__(self, parent=None):
        super(Gestionnaire, self).__init__(parent)
        self.setTable("gestionnaire")
        self.setRelation(self.PERSONNE_ID, QtSql.QSqlRelation("personne", "id_personne", "nom_personne"))
        # self.setRelation(PERSONNE_ID, QtSql.QSqlRelation("personne", "id_personne", "profession"))
        self.setRelation(self.TITRE_CIVILITE_ID, QtSql.QSqlRelation("titre_civilite", "id_titre_civilite", \
                                                                    "libelle_titre_civilite"))
        self.setRelation(self.TYPE_GESTIONNAIRE_ID, QtSql.QSqlRelation("type_gestionnaire", "id_type_gestionnaire", \
                                                                       "libelle_type_gestionnaire"))

        self.select()


if __name__ == '__main__':
    test = Gestionnaire()
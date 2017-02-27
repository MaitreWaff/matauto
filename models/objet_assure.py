#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

from PyQt4 import QtCore, QtGui, QtSql

class ObjetAssure(QtSql.QSqlRelationalTableModel):
    # Constantes
    ID_OBJET_ASSURE, POLICE_ID, LIBELLE_OBJET_ASSURE, DESCRIPTION_OBJET_ASSURE, RANG, MARQUE, MODELE, GENRE_OBJET_ID, \
    NUMERO_SERIE, IMMATRICULATION, NOM_ASSURE, PROFESSION_ASSURE, ADRESSE_ASSURE, DATE_ACQUISITION, VALEUR_NEUVE, \
    VALEUR_VENALE, VALEUR_ACCESSOIRES, PUISSANCE, ENERGIE, CHARGE_UTILE, NOMBRE_PLACES_CABINE, NOMBRE_PLACES_HORS_CABINE, \
    CARROSSERIE, DATE_DERNIERE_VISITE, CONDUCTEUR, PERMIS_CONDUIRE_ID, CATEGORIE_PERMIS, NUMERO_PERMIS_CONDUIRE, \
    DATE_OBTENTION_PERMIS, DATE_VALIDITE_PERMIS, CAPACITE, DATE_VALIDITE_CAPACITE, COMMENTAIRE, DERNIER_MOUVEMENT, \
    ATTELAGE_REMORQUE, MARQUE_REMORQUE, TYPE_REMORQUE, VALEUR_REMORQUE, IMMATRICULATION_REMORQUE, \
    TRANSPORT_MATIERE_INFLAMMABLE, STATUT_OBJET, ZONE_TARIFICATION_ID, EMISSION_CARTE_ROSE, CATEGORIE_SOCIOPROFESSIONNELLE, \
    ACTIF, G01, G02, G03, G04, G05, G06, G07, G08, G09, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20, \
    G21, G22, G23, G24, OPTION_GO6, DATE_NAISSANCE_ASSURE, LIEU_NAISSANCE_ASSURE, GENRE_PERSONNE_ID, \
    DATE_CREATION, REF_IMPORTATION, DATE_IMPORTATION = range(76)

    def __init__(self, parent=None):
        super(ObjetAssure, self).__init__(parent)
        self.setTable("objet_assure")
        self.setRelation(self.GENRE_OBJET_ID, QtSql.QSqlRelation("genre_objet", "id_genre_objet", "libelle_genre_objet"))
        self.setRelation(self.GENRE_PERSONNE_ID, QtSql.QSqlRelation("genre_personne", "id_genre_personne", \
                                                                    "libelle_genre_personne"))
        self.setRelation(self.PERMIS_CONDUIRE_ID, QtSql.QSqlRelation("permis_conduire", "id_permis_conduire", \
                                                                     "libelle_permis_conduire"))
        self.setRelation(self.POLICE_ID, QtSql.QSqlRelation("police", "id_police", "numero_police"))
        self.setRelation(self.ZONE_TARIFICATION_ID, QtSql.QSqlRelation("zone_tarification", "id_zone_tarification", \
                                                                       "libelle_zone_tarification"))

        self.select()
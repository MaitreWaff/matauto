#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Luc Mathurin Waffo Modjom'
__version__ = '1.0.0'

from PyQt4 import QtCore, QtGui, QtSql

# from PyQt4.QtCore import SIGNAL

class Victime(QtSql.QSqlRelationalTableModel):
    # Constantes
    ID_VICTIME, NUMERO_VICTIME, SINISTRE_ID, PERSONNE_ID, AGE_VICTIME, PROFESSION_ID, NATURE_DOMMAGE_ID, DESCRIPTION_DOMMAGE, \
    PREJUDICE, NATURE_LESIONS, STATUT_PERSONNE_ID, ETAT_ACTUEL_VICTIME, PARENTE_AVEC_ASSURE, PARENTE_AVEC_CONDUCTEUR, \
    MONTANT_ESTIME, EMPLACEMENT_VICTIME_ID, DESTINATION_APRES_SINISTRE, DUREE_PROBABLE_HOSPITALISATION, \
    CONCLUSIONS_CERTIFICAT_MEDICAL, OBSERVATION_SUR_VICTIME, DATE_CREATION, REF_IMPORTATION, DATE_IMPORTATION = range(23)

    def __init__(self, parent=None):
        super(Victime, self).__init__(parent)

        self.setTable("victime")
        self.setRelation(self.EMPLACEMENT_VICTIME_ID, QtSql.QSqlRelation("emplacement_victime", "id_emplacement_victime", \
                                                                    "designation_emplacement_victime"))
        self.setRelation(self.NATURE_DOMMAGE_ID, QtSql.QSqlRelation("nature_dommage", "id_nature_dommage", \
                                                               "libelle_nature_dommage"))
        self.setRelation(self.PERSONNE_ID, QtSql.QSqlRelation("personne", "id_personne", "nom_personne"))
        self.setRelation(self.PROFESSION_ID, QtSql.QSqlRelation("profession", "id_profession", "libelle_profession"))
        self.setRelation(self.SINISTRE_ID, QtSql.QSqlRelation("sinistre", "id_sinistre", "numero_dossier"))
        self.setRelation(self.STATUT_PERSONNE_ID, QtSql.QSqlRelation("statut_personne", "id_statut_personne", \
                                                                "libelle_statut_personne"))
        self.select()
#
# class Gui(QtGui.QDialog):
#     def __init__(self, parent=None):
#         super(Gui, self).__init__(parent)
#         self.label = QtGui.QLabel("Numero Victime")
#         self.numVict = QtGui.QLineEdit()
#         ok = QtGui.QPushButton("Ok")
#         lay = QtGui.QHBoxLayout()
#         lay.addWidget(self.label)
#         lay.addWidget(self.numVict)
#
#         layout = QtGui.QVBoxLayout()
#         layout.addItem(lay)
#         layout.addWidget(ok)
#
#         self.setLayout(layout)
#
#         self.model_victime = Victime()
#
#         self.mapperVictime = QtGui.QDataWidgetMapper(self)
#         self.mapperVictime.setModel(self.model_victime)
#         self.mapperVictime.setItemDelegate(QtSql.QSqlRelationalDelegate(self))
#         self.mapperVictime.setSubmitPolicy(QtGui.QDataWidgetMapper.ManualSubmit)
#
#         self.mapperVictime.addMapping(self.numVict, Victime.NUMERO_VICTIME)
#         self.mapperVictime.toFirst()
#
#         self.connect(ok, SIGNAL("clicked()"), self.ok_process)
#
#     def ok_process(self):
#         # QtGui.QMessageBox("Ok", "Ok", QtGui.QMessageBox.Ok)
#         pass
# def main(args):
#     app = QtGui.QApplication(args)
#
#     form = Gui()
#     form.show()
#     app.exec_()
#
# if __name__ == '__main__':
#     import sys
#     main(sys.argv)
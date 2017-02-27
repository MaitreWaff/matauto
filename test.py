#! /usr/bin/python
# -*- coding: utf-8 -*-


#! /usr/bin/python
# -*- coding: utf-8 -*-
from PyQt4.QtGui import QVBoxLayout, QWidget, QApplication, QPushButton, QListView, QStringListModel, QMessageBox, QAbstractItemView
from PyQt4.QtCore import SIGNAL, Qt #, QTimer
import sys

__author__ = 'Luc Mathurin Waffo Modjom'


class MaFenetre(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        self.list_pays = ['Argentine', 'Bolivie', 'Cameroun', 'Danmark', 'Espagne', 'France', 'Germany', \
                          'Hongrie', 'Italie', 'Japon', 'Ka', 'Luxembourg', 'Malawi', 'Norverge', \
                          'Ousbekistan']
        self.modele = QStringListModel(self.list_pays)
        self.vue = QListView()
        self.vue.setModel(self.modele)

        self.vue.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.afficherButton = QPushButton(u"Afficher la sélection")
        self.connect(self.afficherButton, SIGNAL('clicked()'), self.clicSelection)

        self.layout.addWidget(self.vue)
        self.layout.addWidget(self.afficherButton)
        self.setLayout(self.layout)

    def clicSelection(self):
        # selection = self.vue.selectionModel()                               #QItemSelectionModel
        # listeSelections = selection.selectedIndexes()                       #QModelIndexList
        # L = [unicode(s.data().toString()) for s in listeSelections]
        # QMessageBox.information(self, u"Eléments sélectionnés", '<br>'.join(L))

        selection = [unicode(s.data().toString()) for s in self.vue.selectionModel().selectedIndexes()]
        QMessageBox.information(self, u"Eléments sélectionnés", '<br>'.join(selection))

        # selection = self.vue.selectionModel()
        # indexElementSelectionne = selection.currentIndex()
        # elementSelectionne = self.modele.data(indexElementSelectionne, Qt.DisplayRole)
        # print elementSelectionne.toString()
        # QMessageBox.information(self, u"Elément sélectionné", elementSelectionne.toString())


if __name__=="__main__":
    a=QApplication(sys.argv)
    a.setStyle("plastique")
    f = MaFenetre()
    f.show()
    #QTimer.singleShot(0, a.quit)
    a.exec_()
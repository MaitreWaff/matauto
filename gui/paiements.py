# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paiements.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Paiements(object):
    def setupUi(self, Paiements):
        Paiements.setObjectName(_fromUtf8("Paiements"))
        Paiements.resize(1066, 610)
        self.centralwidget = QtGui.QWidget(Paiements)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowserList = QtGui.QTextBrowser(self.frame_2)
        self.textBrowserList.setObjectName(_fromUtf8("textBrowserList"))
        self.verticalLayout.addWidget(self.textBrowserList)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.labelOpAImputer = QtGui.QLabel(self.frame_3)
        self.labelOpAImputer.setObjectName(_fromUtf8("labelOpAImputer"))
        self.gridLayout_2.addWidget(self.labelOpAImputer, 0, 0, 1, 4)
        self.labelCumulsReglements = QtGui.QLabel(self.frame_3)
        self.labelCumulsReglements.setObjectName(_fromUtf8("labelCumulsReglements"))
        self.gridLayout_2.addWidget(self.labelCumulsReglements, 0, 4, 1, 1)
        self.lineEditCumulsReglements = QtGui.QLineEdit(self.frame_3)
        self.lineEditCumulsReglements.setText(_fromUtf8(""))
        self.lineEditCumulsReglements.setObjectName(_fromUtf8("lineEditCumulsReglements"))
        self.gridLayout_2.addWidget(self.lineEditCumulsReglements, 1, 4, 1, 1)
        self.labelPrimeDue = QtGui.QLabel(self.frame_3)
        self.labelPrimeDue.setObjectName(_fromUtf8("labelPrimeDue"))
        self.gridLayout_2.addWidget(self.labelPrimeDue, 2, 0, 1, 1)
        self.labelCartesRoses = QtGui.QLabel(self.frame_3)
        self.labelCartesRoses.setObjectName(_fromUtf8("labelCartesRoses"))
        self.gridLayout_2.addWidget(self.labelCartesRoses, 2, 1, 1, 1)
        self.labelAutresPP = QtGui.QLabel(self.frame_3)
        self.labelAutresPP.setObjectName(_fromUtf8("labelAutresPP"))
        self.gridLayout_2.addWidget(self.labelAutresPP, 2, 2, 1, 1)
        self.labelTotalAPayer = QtGui.QLabel(self.frame_3)
        self.labelTotalAPayer.setObjectName(_fromUtf8("labelTotalAPayer"))
        self.gridLayout_2.addWidget(self.labelTotalAPayer, 2, 3, 1, 1)
        self.labelCumulsImputations = QtGui.QLabel(self.frame_3)
        self.labelCumulsImputations.setObjectName(_fromUtf8("labelCumulsImputations"))
        self.gridLayout_2.addWidget(self.labelCumulsImputations, 2, 4, 1, 1)
        self.lineEditPrimeDue = QtGui.QLineEdit(self.frame_3)
        self.lineEditPrimeDue.setText(_fromUtf8(""))
        self.lineEditPrimeDue.setObjectName(_fromUtf8("lineEditPrimeDue"))
        self.gridLayout_2.addWidget(self.lineEditPrimeDue, 3, 0, 1, 1)
        self.lineEditCartesRoses = QtGui.QLineEdit(self.frame_3)
        self.lineEditCartesRoses.setText(_fromUtf8(""))
        self.lineEditCartesRoses.setObjectName(_fromUtf8("lineEditCartesRoses"))
        self.gridLayout_2.addWidget(self.lineEditCartesRoses, 3, 1, 1, 1)
        self.lineEditAutresPP = QtGui.QLineEdit(self.frame_3)
        self.lineEditAutresPP.setText(_fromUtf8(""))
        self.lineEditAutresPP.setObjectName(_fromUtf8("lineEditAutresPP"))
        self.gridLayout_2.addWidget(self.lineEditAutresPP, 3, 2, 1, 1)
        self.lineEditTotalAPayer = QtGui.QLineEdit(self.frame_3)
        self.lineEditTotalAPayer.setText(_fromUtf8(""))
        self.lineEditTotalAPayer.setObjectName(_fromUtf8("lineEditTotalAPayer"))
        self.gridLayout_2.addWidget(self.lineEditTotalAPayer, 3, 3, 1, 1)
        self.lineEditCumulsImputions = QtGui.QLineEdit(self.frame_3)
        self.lineEditCumulsImputions.setText(_fromUtf8(""))
        self.lineEditCumulsImputions.setObjectName(_fromUtf8("lineEditCumulsImputions"))
        self.gridLayout_2.addWidget(self.lineEditCumulsImputions, 3, 4, 1, 1)
        self.comboBoxOpAImputer = QtGui.QComboBox(self.frame_3)
        self.comboBoxOpAImputer.setObjectName(_fromUtf8("comboBoxOpAImputer"))
        self.gridLayout_2.addWidget(self.comboBoxOpAImputer, 1, 0, 1, 4)
        self.labelOpAImputer.raise_()
        self.lineEditCumulsReglements.raise_()
        self.labelCumulsReglements.raise_()
        self.labelPrimeDue.raise_()
        self.lineEditPrimeDue.raise_()
        self.labelCartesRoses.raise_()
        self.lineEditCartesRoses.raise_()
        self.labelAutresPP.raise_()
        self.lineEditAutresPP.raise_()
        self.labelTotalAPayer.raise_()
        self.lineEditTotalAPayer.raise_()
        self.labelCumulsImputations.raise_()
        self.lineEditCumulsImputions.raise_()
        self.comboBoxOpAImputer.raise_()
        self.gridLayout_3.addWidget(self.frame_3, 0, 2, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.labelNumRecu = QtGui.QLabel(self.frame)
        self.labelNumRecu.setObjectName(_fromUtf8("labelNumRecu"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelNumRecu)
        self.lineEditNumRecu = QtGui.QLineEdit(self.frame)
        self.lineEditNumRecu.setObjectName(_fromUtf8("lineEditNumRecu"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNumRecu)
        self.labelModePaiement = QtGui.QLabel(self.frame)
        self.labelModePaiement.setObjectName(_fromUtf8("labelModePaiement"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelModePaiement)
        self.labelDatePaiement = QtGui.QLabel(self.frame)
        self.labelDatePaiement.setObjectName(_fromUtf8("labelDatePaiement"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelDatePaiement)
        self.labelMontantPaiement = QtGui.QLabel(self.frame)
        self.labelMontantPaiement.setObjectName(_fromUtf8("labelMontantPaiement"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelMontantPaiement)
        self.lineEditMontantPaiement = QtGui.QLineEdit(self.frame)
        self.lineEditMontantPaiement.setObjectName(_fromUtf8("lineEditMontantPaiement"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditMontantPaiement)
        self.labelPaiementValide = QtGui.QLabel(self.frame)
        self.labelPaiementValide.setObjectName(_fromUtf8("labelPaiementValide"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.labelPaiementValide)
        self.labelPayeurEffet = QtGui.QLabel(self.frame)
        self.labelPayeurEffet.setObjectName(_fromUtf8("labelPayeurEffet"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.labelPayeurEffet)
        self.labelNumPiece = QtGui.QLabel(self.frame)
        self.labelNumPiece.setObjectName(_fromUtf8("labelNumPiece"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.labelNumPiece)
        self.lineEditNumPiece = QtGui.QLineEdit(self.frame)
        self.lineEditNumPiece.setObjectName(_fromUtf8("lineEditNumPiece"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEditNumPiece)
        self.labelTitulaire = QtGui.QLabel(self.frame)
        self.labelTitulaire.setObjectName(_fromUtf8("labelTitulaire"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.labelTitulaire)
        self.lineEdit_10 = QtGui.QLineEdit(self.frame)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEdit_10)
        self.labelDateEncaissementEffet = QtGui.QLabel(self.frame)
        self.labelDateEncaissementEffet.setObjectName(_fromUtf8("labelDateEncaissementEffet"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.labelDateEncaissementEffet)
        self.labelAutresInfos = QtGui.QLabel(self.frame)
        self.labelAutresInfos.setObjectName(_fromUtf8("labelAutresInfos"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.labelAutresInfos)
        self.lineEditAutresInfos = QtGui.QLineEdit(self.frame)
        self.lineEditAutresInfos.setObjectName(_fromUtf8("lineEditAutresInfos"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.lineEditAutresInfos)
        self.comboBoxModePaiement = QtGui.QComboBox(self.frame)
        self.comboBoxModePaiement.setObjectName(_fromUtf8("comboBoxModePaiement"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBoxModePaiement)
        self.dateEditDatePaiement = QtGui.QDateEdit(self.frame)
        self.dateEditDatePaiement.setObjectName(_fromUtf8("dateEditDatePaiement"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dateEditDatePaiement)
        self.comboBoxPaiementValide = QtGui.QComboBox(self.frame)
        self.comboBoxPaiementValide.setObjectName(_fromUtf8("comboBoxPaiementValide"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.comboBoxPaiementValide)
        self.comboBoxPayeurEffet = QtGui.QComboBox(self.frame)
        self.comboBoxPayeurEffet.setObjectName(_fromUtf8("comboBoxPayeurEffet"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.comboBoxPayeurEffet)
        self.dateEditDateEncaissementEffet = QtGui.QDateEdit(self.frame)
        self.dateEditDateEncaissementEffet.setObjectName(_fromUtf8("dateEditDateEncaissementEffet"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.dateEditDateEncaissementEffet)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 2, 1)
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout = QtGui.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem1 = QtGui.QSpacerItem(298, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.frame_4)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 1, 1, 2)
        self.labelResteAImputer = QtGui.QLabel(self.frame_4)
        self.labelResteAImputer.setObjectName(_fromUtf8("labelResteAImputer"))
        self.gridLayout.addWidget(self.labelResteAImputer, 1, 1, 1, 1)
        self.labelSoldeOperation = QtGui.QLabel(self.frame_4)
        self.labelSoldeOperation.setObjectName(_fromUtf8("labelSoldeOperation"))
        self.gridLayout.addWidget(self.labelSoldeOperation, 1, 2, 1, 1)
        self.lineEditResteAImputer = QtGui.QLineEdit(self.frame_4)
        self.lineEditResteAImputer.setText(_fromUtf8(""))
        self.lineEditResteAImputer.setObjectName(_fromUtf8("lineEditResteAImputer"))
        self.gridLayout.addWidget(self.lineEditResteAImputer, 2, 1, 1, 1)
        self.lineEditSoldeOperation = QtGui.QLineEdit(self.frame_4)
        self.lineEditSoldeOperation.setText(_fromUtf8(""))
        self.lineEditSoldeOperation.setObjectName(_fromUtf8("lineEditSoldeOperation"))
        self.gridLayout.addWidget(self.lineEditSoldeOperation, 2, 2, 1, 1)
        self.gridLayout_3.addWidget(self.frame_4, 1, 2, 1, 1)
        self.frame_5 = QtGui.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelMouvAssocies = QtGui.QLabel(self.frame_5)
        self.labelMouvAssocies.setObjectName(_fromUtf8("labelMouvAssocies"))
        self.verticalLayout_2.addWidget(self.labelMouvAssocies)
        self.textBrowserMouvAssocies = QtGui.QTextBrowser(self.frame_5)
        self.textBrowserMouvAssocies.setObjectName(_fromUtf8("textBrowserMouvAssocies"))
        self.verticalLayout_2.addWidget(self.textBrowserMouvAssocies)
        self.gridLayout_3.addWidget(self.frame_5, 2, 2, 1, 1)
        Paiements.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Paiements)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1066, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_Fichier = QtGui.QMenu(self.menubar)
        self.menu_Fichier.setObjectName(_fromUtf8("menu_Fichier"))
        self.menu_Edition = QtGui.QMenu(self.menubar)
        self.menu_Edition.setObjectName(_fromUtf8("menu_Edition"))
        Paiements.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Paiements)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Paiements.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Paiements)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Paiements.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNouveau = QtGui.QAction(Paiements)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/document-new.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNouveau.setIcon(icon)
        self.actionNouveau.setObjectName(_fromUtf8("actionNouveau"))
        self.actionEnregistrer = QtGui.QAction(Paiements)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/document-save.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnregistrer.setIcon(icon1)
        self.actionEnregistrer.setObjectName(_fromUtf8("actionEnregistrer"))
        self.actionImprimer_les_pieces_d_Encaissement = QtGui.QAction(Paiements)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/Imprimer.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImprimer_les_pieces_d_Encaissement.setIcon(icon2)
        self.actionImprimer_les_pieces_d_Encaissement.setObjectName(_fromUtf8("actionImprimer_les_pieces_d_Encaissement"))
        self.actionFermer = QtGui.QAction(Paiements)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/system-log-out.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFermer.setIcon(icon3)
        self.actionFermer.setObjectName(_fromUtf8("actionFermer"))
        self.actionAnnuler = QtGui.QAction(Paiements)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/edit-undo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnnuler.setIcon(icon4)
        self.actionAnnuler.setObjectName(_fromUtf8("actionAnnuler"))
        self.actionRefaire = QtGui.QAction(Paiements)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/edit-redo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefaire.setIcon(icon5)
        self.actionRefaire.setObjectName(_fromUtf8("actionRefaire"))
        self.actionPremier = QtGui.QAction(Paiements)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/go-first.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPremier.setIcon(icon6)
        self.actionPremier.setObjectName(_fromUtf8("actionPremier"))
        self.actionPrecedent = QtGui.QAction(Paiements)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/go-previous.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrecedent.setIcon(icon7)
        self.actionPrecedent.setObjectName(_fromUtf8("actionPrecedent"))
        self.actionSuivant = QtGui.QAction(Paiements)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/go-next.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSuivant.setIcon(icon8)
        self.actionSuivant.setObjectName(_fromUtf8("actionSuivant"))
        self.actionDernier = QtGui.QAction(Paiements)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/go-last.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDernier.setIcon(icon9)
        self.actionDernier.setObjectName(_fromUtf8("actionDernier"))
        self.menu_Fichier.addAction(self.actionNouveau)
        self.menu_Fichier.addAction(self.actionEnregistrer)
        self.menu_Fichier.addSeparator()
        self.menu_Fichier.addAction(self.actionImprimer_les_pieces_d_Encaissement)
        self.menu_Fichier.addSeparator()
        self.menu_Fichier.addAction(self.actionFermer)
        self.menu_Edition.addAction(self.actionAnnuler)
        self.menu_Edition.addAction(self.actionRefaire)
        self.menu_Edition.addSeparator()
        self.menu_Edition.addAction(self.actionPremier)
        self.menu_Edition.addAction(self.actionPrecedent)
        self.menu_Edition.addAction(self.actionSuivant)
        self.menu_Edition.addAction(self.actionDernier)
        self.menubar.addAction(self.menu_Fichier.menuAction())
        self.menubar.addAction(self.menu_Edition.menuAction())
        self.toolBar.addAction(self.actionNouveau)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPremier)
        self.toolBar.addAction(self.actionPrecedent)
        self.toolBar.addAction(self.actionSuivant)
        self.toolBar.addAction(self.actionDernier)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRefaire)
        self.toolBar.addAction(self.actionAnnuler)
        self.toolBar.addAction(self.actionEnregistrer)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionImprimer_les_pieces_d_Encaissement)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFermer)

        self.retranslateUi(Paiements)
        QtCore.QMetaObject.connectSlotsByName(Paiements)
        Paiements.setTabOrder(self.lineEditNumRecu, self.lineEditMontantPaiement)
        Paiements.setTabOrder(self.lineEditMontantPaiement, self.lineEditNumPiece)
        Paiements.setTabOrder(self.lineEditNumPiece, self.lineEdit_10)
        Paiements.setTabOrder(self.lineEdit_10, self.lineEditAutresInfos)
        Paiements.setTabOrder(self.lineEditAutresInfos, self.lineEditCumulsReglements)
        Paiements.setTabOrder(self.lineEditCumulsReglements, self.lineEditPrimeDue)
        Paiements.setTabOrder(self.lineEditPrimeDue, self.lineEditCartesRoses)
        Paiements.setTabOrder(self.lineEditCartesRoses, self.lineEditAutresPP)
        Paiements.setTabOrder(self.lineEditAutresPP, self.lineEditTotalAPayer)
        Paiements.setTabOrder(self.lineEditTotalAPayer, self.lineEditCumulsImputions)
        Paiements.setTabOrder(self.lineEditCumulsImputions, self.lineEditResteAImputer)
        Paiements.setTabOrder(self.lineEditResteAImputer, self.lineEditSoldeOperation)
        Paiements.setTabOrder(self.lineEditSoldeOperation, self.tableWidget)
        Paiements.setTabOrder(self.tableWidget, self.textBrowserMouvAssocies)
        Paiements.setTabOrder(self.textBrowserMouvAssocies, self.textBrowserList)

    def retranslateUi(self, Paiements):
        Paiements.setWindowTitle(_translate("Paiements", "Paiements", None))
        self.labelOpAImputer.setText(_translate("Paiements", "Operation a Imputer", None))
        self.labelCumulsReglements.setText(_translate("Paiements", "Cumuls Reglements", None))
        self.labelPrimeDue.setText(_translate("Paiements", "Prime Due", None))
        self.labelCartesRoses.setText(_translate("Paiements", "Cartes Roses", None))
        self.labelAutresPP.setText(_translate("Paiements", "Autres/PP", None))
        self.labelTotalAPayer.setText(_translate("Paiements", "Total a Payer", None))
        self.labelCumulsImputations.setText(_translate("Paiements", "Cumuls Imputations", None))
        self.labelNumRecu.setText(_translate("Paiements", "NUMERO RECU", None))
        self.labelModePaiement.setText(_translate("Paiements", "Mode de Paiement", None))
        self.labelDatePaiement.setText(_translate("Paiements", "Date du Paiement", None))
        self.labelMontantPaiement.setText(_translate("Paiements", "Montant du Paiement", None))
        self.labelPaiementValide.setText(_translate("Paiements", "Paiement Valide ?", None))
        self.labelPayeurEffet.setText(_translate("Paiements", "Payeur effet", None))
        self.labelNumPiece.setText(_translate("Paiements", "Numero de la Piece", None))
        self.labelTitulaire.setText(_translate("Paiements", "Titulaire du Compte", None))
        self.labelDateEncaissementEffet.setText(_translate("Paiements", "Date encaissement effet", None))
        self.labelAutresInfos.setText(_translate("Paiements", "Autres Informations", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Paiements", "Line1", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Paiements", "Line2", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Paiements", "Line3", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Paiements", "Line4", None))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Paiements", "Line5", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Paiements", "Col1", None))
        self.labelResteAImputer.setText(_translate("Paiements", "Reste a Imputer", None))
        self.labelSoldeOperation.setText(_translate("Paiements", "Solde Operation", None))
        self.labelMouvAssocies.setText(_translate("Paiements", "Mouvements associes au Paiement", None))
        self.menu_Fichier.setTitle(_translate("Paiements", "&Fichier", None))
        self.menu_Edition.setTitle(_translate("Paiements", "&Edition", None))
        self.toolBar.setWindowTitle(_translate("Paiements", "toolBar", None))
        self.actionNouveau.setText(_translate("Paiements", "Nouveau", None))
        self.actionEnregistrer.setText(_translate("Paiements", "Enregistrer", None))
        self.actionImprimer_les_pieces_d_Encaissement.setText(_translate("Paiements", "Imprimer les pieces d\'Encaissement", None))
        self.actionFermer.setText(_translate("Paiements", "Fermer", None))
        self.actionAnnuler.setText(_translate("Paiements", "Annuler", None))
        self.actionRefaire.setText(_translate("Paiements", "Refaire", None))
        self.actionPremier.setText(_translate("Paiements", "Premier", None))
        self.actionPrecedent.setText(_translate("Paiements", "Precedent", None))
        self.actionSuivant.setText(_translate("Paiements", "Suivant", None))
        self.actionDernier.setText(_translate("Paiements", "Dernier", None))

import ressources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Paiements = QtGui.QMainWindow()
    ui = Ui_Paiements()
    ui.setupUi(Paiements)
    Paiements.show()
    sys.exit(app.exec_())


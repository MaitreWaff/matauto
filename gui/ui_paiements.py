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
        Paiements.setWindowModality(QtCore.Qt.ApplicationModal)
        Paiements.resize(897, 646)
        self.centralwidget = QtGui.QWidget(Paiements)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.operationsNonPayeesListView = QtGui.QListView(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.operationsNonPayeesListView.setFont(font)
        self.operationsNonPayeesListView.setObjectName(_fromUtf8("operationsNonPayeesListView"))
        self.verticalLayout.addWidget(self.operationsNonPayeesListView)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.labelOpAImputer = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelOpAImputer.setFont(font)
        self.labelOpAImputer.setObjectName(_fromUtf8("labelOpAImputer"))
        self.gridLayout_2.addWidget(self.labelOpAImputer, 0, 0, 1, 4)
        self.labelCumulsReglements = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelCumulsReglements.setFont(font)
        self.labelCumulsReglements.setObjectName(_fromUtf8("labelCumulsReglements"))
        self.gridLayout_2.addWidget(self.labelCumulsReglements, 0, 4, 1, 1)
        self.cumulReglementLineEdit = QtGui.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.cumulReglementLineEdit.setFont(font)
        self.cumulReglementLineEdit.setText(_fromUtf8(""))
        self.cumulReglementLineEdit.setObjectName(_fromUtf8("cumulReglementLineEdit"))
        self.gridLayout_2.addWidget(self.cumulReglementLineEdit, 1, 4, 1, 1)
        self.labelPrimeDue = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelPrimeDue.setFont(font)
        self.labelPrimeDue.setObjectName(_fromUtf8("labelPrimeDue"))
        self.gridLayout_2.addWidget(self.labelPrimeDue, 2, 0, 1, 1)
        self.labelCartesRoses = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelCartesRoses.setFont(font)
        self.labelCartesRoses.setObjectName(_fromUtf8("labelCartesRoses"))
        self.gridLayout_2.addWidget(self.labelCartesRoses, 2, 1, 1, 1)
        self.labelAutresPP = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelAutresPP.setFont(font)
        self.labelAutresPP.setObjectName(_fromUtf8("labelAutresPP"))
        self.gridLayout_2.addWidget(self.labelAutresPP, 2, 2, 1, 1)
        self.labelTotalAPayer = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelTotalAPayer.setFont(font)
        self.labelTotalAPayer.setObjectName(_fromUtf8("labelTotalAPayer"))
        self.gridLayout_2.addWidget(self.labelTotalAPayer, 2, 3, 1, 1)
        self.labelCumulsImputations = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelCumulsImputations.setFont(font)
        self.labelCumulsImputations.setObjectName(_fromUtf8("labelCumulsImputations"))
        self.gridLayout_2.addWidget(self.labelCumulsImputations, 2, 4, 1, 1)
        self.primDueLineEdit = QtGui.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.primDueLineEdit.setFont(font)
        self.primDueLineEdit.setText(_fromUtf8(""))
        self.primDueLineEdit.setObjectName(_fromUtf8("primDueLineEdit"))
        self.gridLayout_2.addWidget(self.primDueLineEdit, 3, 0, 1, 1)
        self.cartRosLineEdit = QtGui.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.cartRosLineEdit.setFont(font)
        self.cartRosLineEdit.setText(_fromUtf8(""))
        self.cartRosLineEdit.setObjectName(_fromUtf8("cartRosLineEdit"))
        self.gridLayout_2.addWidget(self.cartRosLineEdit, 3, 1, 1, 1)
        self.autrPPLineEdit = QtGui.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.autrPPLineEdit.setFont(font)
        self.autrPPLineEdit.setText(_fromUtf8(""))
        self.autrPPLineEdit.setObjectName(_fromUtf8("autrPPLineEdit"))
        self.gridLayout_2.addWidget(self.autrPPLineEdit, 3, 2, 1, 1)
        self.totalAPayerLineEdit = QtGui.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.totalAPayerLineEdit.setFont(font)
        self.totalAPayerLineEdit.setText(_fromUtf8(""))
        self.totalAPayerLineEdit.setObjectName(_fromUtf8("totalAPayerLineEdit"))
        self.gridLayout_2.addWidget(self.totalAPayerLineEdit, 3, 3, 1, 1)
        self.cumulImputionLineEdit = QtGui.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.cumulImputionLineEdit.setFont(font)
        self.cumulImputionLineEdit.setText(_fromUtf8(""))
        self.cumulImputionLineEdit.setObjectName(_fromUtf8("cumulImputionLineEdit"))
        self.gridLayout_2.addWidget(self.cumulImputionLineEdit, 3, 4, 1, 1)
        self.opAImputerComboBox = QtGui.QComboBox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.opAImputerComboBox.setFont(font)
        self.opAImputerComboBox.setObjectName(_fromUtf8("opAImputerComboBox"))
        self.gridLayout_2.addWidget(self.opAImputerComboBox, 1, 0, 1, 4)
        self.labelOpAImputer.raise_()
        self.cumulReglementLineEdit.raise_()
        self.labelCumulsReglements.raise_()
        self.labelPrimeDue.raise_()
        self.primDueLineEdit.raise_()
        self.labelCartesRoses.raise_()
        self.cartRosLineEdit.raise_()
        self.labelAutresPP.raise_()
        self.autrPPLineEdit.raise_()
        self.labelTotalAPayer.raise_()
        self.totalAPayerLineEdit.raise_()
        self.labelCumulsImputations.raise_()
        self.cumulImputionLineEdit.raise_()
        self.opAImputerComboBox.raise_()
        self.gridLayout_3.addWidget(self.frame_3, 0, 2, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.frame.setFont(font)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.labelAutresInfos = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelAutresInfos.setFont(font)
        self.labelAutresInfos.setObjectName(_fromUtf8("labelAutresInfos"))
        self.gridLayout_4.addWidget(self.labelAutresInfos, 9, 0, 1, 1)
        self.labelTitulaire = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelTitulaire.setFont(font)
        self.labelTitulaire.setObjectName(_fromUtf8("labelTitulaire"))
        self.gridLayout_4.addWidget(self.labelTitulaire, 7, 0, 1, 1)
        self.labelDateEncaissementEffet = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelDateEncaissementEffet.setFont(font)
        self.labelDateEncaissementEffet.setObjectName(_fromUtf8("labelDateEncaissementEffet"))
        self.gridLayout_4.addWidget(self.labelDateEncaissementEffet, 8, 0, 1, 1)
        self.paiementValideComboBox = QtGui.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.paiementValideComboBox.setFont(font)
        self.paiementValideComboBox.setObjectName(_fromUtf8("paiementValideComboBox"))
        self.gridLayout_4.addWidget(self.paiementValideComboBox, 4, 1, 1, 1)
        self.labelModePaiement = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelModePaiement.setFont(font)
        self.labelModePaiement.setObjectName(_fromUtf8("labelModePaiement"))
        self.gridLayout_4.addWidget(self.labelModePaiement, 1, 0, 1, 1)
        self.labelPaiementValide = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelPaiementValide.setFont(font)
        self.labelPaiementValide.setObjectName(_fromUtf8("labelPaiementValide"))
        self.gridLayout_4.addWidget(self.labelPaiementValide, 4, 0, 1, 1)
        self.labelPayeurEffet = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelPayeurEffet.setFont(font)
        self.labelPayeurEffet.setObjectName(_fromUtf8("labelPayeurEffet"))
        self.gridLayout_4.addWidget(self.labelPayeurEffet, 5, 0, 1, 1)
        self.numRecuLineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.numRecuLineEdit.setFont(font)
        self.numRecuLineEdit.setObjectName(_fromUtf8("numRecuLineEdit"))
        self.gridLayout_4.addWidget(self.numRecuLineEdit, 0, 1, 1, 1)
        self.titulaireLineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.titulaireLineEdit.setFont(font)
        self.titulaireLineEdit.setObjectName(_fromUtf8("titulaireLineEdit"))
        self.gridLayout_4.addWidget(self.titulaireLineEdit, 7, 1, 1, 1)
        self.payeurEffetComboBox = QtGui.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.payeurEffetComboBox.setFont(font)
        self.payeurEffetComboBox.setObjectName(_fromUtf8("payeurEffetComboBox"))
        self.gridLayout_4.addWidget(self.payeurEffetComboBox, 5, 1, 1, 1)
        self.labelNumRecu = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelNumRecu.setFont(font)
        self.labelNumRecu.setObjectName(_fromUtf8("labelNumRecu"))
        self.gridLayout_4.addWidget(self.labelNumRecu, 0, 0, 1, 1)
        self.dateEncaisEffetDateEdit = QtGui.QDateEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.dateEncaisEffetDateEdit.setFont(font)
        self.dateEncaisEffetDateEdit.setObjectName(_fromUtf8("dateEncaisEffetDateEdit"))
        self.gridLayout_4.addWidget(self.dateEncaisEffetDateEdit, 8, 1, 1, 1)
        self.labelNumPiece = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelNumPiece.setFont(font)
        self.labelNumPiece.setObjectName(_fromUtf8("labelNumPiece"))
        self.gridLayout_4.addWidget(self.labelNumPiece, 6, 0, 1, 1)
        self.modPaiementComboBox = QtGui.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.modPaiementComboBox.setFont(font)
        self.modPaiementComboBox.setObjectName(_fromUtf8("modPaiementComboBox"))
        self.gridLayout_4.addWidget(self.modPaiementComboBox, 1, 1, 1, 1)
        self.montantPaiementLineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.montantPaiementLineEdit.setFont(font)
        self.montantPaiementLineEdit.setObjectName(_fromUtf8("montantPaiementLineEdit"))
        self.gridLayout_4.addWidget(self.montantPaiementLineEdit, 3, 1, 1, 1)
        self.labelMontantPaiement = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelMontantPaiement.setFont(font)
        self.labelMontantPaiement.setObjectName(_fromUtf8("labelMontantPaiement"))
        self.gridLayout_4.addWidget(self.labelMontantPaiement, 3, 0, 1, 1)
        self.numPieceLineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.numPieceLineEdit.setFont(font)
        self.numPieceLineEdit.setObjectName(_fromUtf8("numPieceLineEdit"))
        self.gridLayout_4.addWidget(self.numPieceLineEdit, 6, 1, 1, 1)
        self.labelDatePaiement = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelDatePaiement.setFont(font)
        self.labelDatePaiement.setObjectName(_fromUtf8("labelDatePaiement"))
        self.gridLayout_4.addWidget(self.labelDatePaiement, 2, 0, 1, 1)
        self.datePaiementDateEdit = QtGui.QDateEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.datePaiementDateEdit.setFont(font)
        self.datePaiementDateEdit.setObjectName(_fromUtf8("datePaiementDateEdit"))
        self.gridLayout_4.addWidget(self.datePaiementDateEdit, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 10, 1, 1, 1)
        self.autrInfosplainTextEdit = QtGui.QPlainTextEdit(self.frame)
        self.autrInfosplainTextEdit.setObjectName(_fromUtf8("autrInfosplainTextEdit"))
        self.gridLayout_4.addWidget(self.autrInfosplainTextEdit, 9, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 2, 1)
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout = QtGui.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem2 = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.labelSoldeOperation = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelSoldeOperation.setFont(font)
        self.labelSoldeOperation.setObjectName(_fromUtf8("labelSoldeOperation"))
        self.gridLayout.addWidget(self.labelSoldeOperation, 1, 2, 1, 1)
        self.soldOpLineEdit = QtGui.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.soldOpLineEdit.setFont(font)
        self.soldOpLineEdit.setText(_fromUtf8(""))
        self.soldOpLineEdit.setObjectName(_fromUtf8("soldOpLineEdit"))
        self.gridLayout.addWidget(self.soldOpLineEdit, 2, 2, 1, 1)
        self.detailsPaiementTableView = QtGui.QTableView(self.frame_4)
        self.detailsPaiementTableView.setMinimumSize(QtCore.QSize(250, 0))
        self.detailsPaiementTableView.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.detailsPaiementTableView.setFont(font)
        self.detailsPaiementTableView.setObjectName(_fromUtf8("detailsPaiementTableView"))
        self.gridLayout.addWidget(self.detailsPaiementTableView, 0, 1, 1, 2)
        self.labelResteAImputer = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelResteAImputer.setFont(font)
        self.labelResteAImputer.setObjectName(_fromUtf8("labelResteAImputer"))
        self.gridLayout.addWidget(self.labelResteAImputer, 1, 1, 1, 1)
        self.restAImputerLineEdit = QtGui.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.restAImputerLineEdit.setFont(font)
        self.restAImputerLineEdit.setText(_fromUtf8(""))
        self.restAImputerLineEdit.setObjectName(_fromUtf8("restAImputerLineEdit"))
        self.gridLayout.addWidget(self.restAImputerLineEdit, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_4, 1, 2, 1, 1)
        self.frame_5 = QtGui.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelMouvAssocies = QtGui.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.labelMouvAssocies.setFont(font)
        self.labelMouvAssocies.setObjectName(_fromUtf8("labelMouvAssocies"))
        self.verticalLayout_2.addWidget(self.labelMouvAssocies)
        self.operationProductionTableView = QtGui.QTableView(self.frame_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        self.operationProductionTableView.setFont(font)
        self.operationProductionTableView.setAlternatingRowColors(True)
        self.operationProductionTableView.setObjectName(_fromUtf8("operationProductionTableView"))
        self.verticalLayout_2.addWidget(self.operationProductionTableView)
        self.gridLayout_3.addWidget(self.frame_5, 2, 2, 1, 1)
        Paiements.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Paiements)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 897, 22))
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
        self.fichierNouveau = QtGui.QAction(Paiements)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/document-new.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fichierNouveau.setIcon(icon)
        self.fichierNouveau.setObjectName(_fromUtf8("fichierNouveau"))
        self.fichierEnregistrer = QtGui.QAction(Paiements)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/document-save.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fichierEnregistrer.setIcon(icon1)
        self.fichierEnregistrer.setObjectName(_fromUtf8("fichierEnregistrer"))
        self.fichierImprimPiecesEncaissement = QtGui.QAction(Paiements)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/Imprimer.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fichierImprimPiecesEncaissement.setIcon(icon2)
        self.fichierImprimPiecesEncaissement.setObjectName(_fromUtf8("fichierImprimPiecesEncaissement"))
        self.fichierFermer = QtGui.QAction(Paiements)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/system-log-out.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fichierFermer.setIcon(icon3)
        self.fichierFermer.setObjectName(_fromUtf8("fichierFermer"))
        self.editionAnnuler = QtGui.QAction(Paiements)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/edit-undo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editionAnnuler.setIcon(icon4)
        self.editionAnnuler.setObjectName(_fromUtf8("editionAnnuler"))
        self.editionRefaire = QtGui.QAction(Paiements)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/edit-redo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editionRefaire.setIcon(icon5)
        self.editionRefaire.setObjectName(_fromUtf8("editionRefaire"))
        self.editionPremier = QtGui.QAction(Paiements)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/go-first.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editionPremier.setIcon(icon6)
        self.editionPremier.setObjectName(_fromUtf8("editionPremier"))
        self.editionPrecedent = QtGui.QAction(Paiements)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/go-previous.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editionPrecedent.setIcon(icon7)
        self.editionPrecedent.setObjectName(_fromUtf8("editionPrecedent"))
        self.editionSuivant = QtGui.QAction(Paiements)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/go-next.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editionSuivant.setIcon(icon8)
        self.editionSuivant.setObjectName(_fromUtf8("editionSuivant"))
        self.editionDernier = QtGui.QAction(Paiements)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/go-last.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editionDernier.setIcon(icon9)
        self.editionDernier.setObjectName(_fromUtf8("editionDernier"))
        self.menu_Fichier.addAction(self.fichierNouveau)
        self.menu_Fichier.addAction(self.fichierEnregistrer)
        self.menu_Fichier.addSeparator()
        self.menu_Fichier.addAction(self.fichierImprimPiecesEncaissement)
        self.menu_Fichier.addSeparator()
        self.menu_Fichier.addAction(self.fichierFermer)
        self.menu_Edition.addAction(self.editionAnnuler)
        self.menu_Edition.addAction(self.editionRefaire)
        self.menu_Edition.addSeparator()
        self.menu_Edition.addAction(self.editionPremier)
        self.menu_Edition.addAction(self.editionPrecedent)
        self.menu_Edition.addAction(self.editionSuivant)
        self.menu_Edition.addAction(self.editionDernier)
        self.menubar.addAction(self.menu_Fichier.menuAction())
        self.menubar.addAction(self.menu_Edition.menuAction())
        self.toolBar.addAction(self.fichierNouveau)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.editionPremier)
        self.toolBar.addAction(self.editionPrecedent)
        self.toolBar.addAction(self.editionSuivant)
        self.toolBar.addAction(self.editionDernier)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.editionRefaire)
        self.toolBar.addAction(self.editionAnnuler)
        self.toolBar.addAction(self.fichierEnregistrer)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.fichierImprimPiecesEncaissement)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.fichierFermer)

        self.retranslateUi(Paiements)
        QtCore.QMetaObject.connectSlotsByName(Paiements)
        Paiements.setTabOrder(self.numRecuLineEdit, self.montantPaiementLineEdit)
        Paiements.setTabOrder(self.montantPaiementLineEdit, self.numPieceLineEdit)
        Paiements.setTabOrder(self.numPieceLineEdit, self.titulaireLineEdit)
        Paiements.setTabOrder(self.titulaireLineEdit, self.cumulReglementLineEdit)
        Paiements.setTabOrder(self.cumulReglementLineEdit, self.primDueLineEdit)
        Paiements.setTabOrder(self.primDueLineEdit, self.cartRosLineEdit)
        Paiements.setTabOrder(self.cartRosLineEdit, self.autrPPLineEdit)
        Paiements.setTabOrder(self.autrPPLineEdit, self.totalAPayerLineEdit)
        Paiements.setTabOrder(self.totalAPayerLineEdit, self.cumulImputionLineEdit)
        Paiements.setTabOrder(self.cumulImputionLineEdit, self.restAImputerLineEdit)
        Paiements.setTabOrder(self.restAImputerLineEdit, self.soldOpLineEdit)

    def retranslateUi(self, Paiements):
        Paiements.setWindowTitle(_translate("Paiements", "Paiements", None))
        self.operationsNonPayeesListView.setToolTip(_translate("Paiements", "<html><head/><body><p>Liste de toutes les Operations Non Totalement Payees.</p></body></html>", None))
        self.operationsNonPayeesListView.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Liste de toutes les Operations Non Totalement Payees.</p></body></html>", None))
        self.labelOpAImputer.setText(_translate("Paiements", "Operation a Imputer", None))
        self.labelCumulsReglements.setText(_translate("Paiements", "Cumuls Reglements", None))
        self.cumulReglementLineEdit.setToolTip(_translate("Paiements", "<html><head/><body><p>Cumuls Reglements.</p></body></html>", None))
        self.cumulReglementLineEdit.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Cumuls Reglements.</p></body></html>", None))
        self.labelPrimeDue.setText(_translate("Paiements", "Prime Due", None))
        self.labelCartesRoses.setText(_translate("Paiements", "Cartes Roses", None))
        self.labelAutresPP.setText(_translate("Paiements", "Autres/PP", None))
        self.labelTotalAPayer.setText(_translate("Paiements", "Total a Payer", None))
        self.labelCumulsImputations.setText(_translate("Paiements", "Cumuls Imputations", None))
        self.primDueLineEdit.setToolTip(_translate("Paiements", "<html><head/><body><p>Prime Due.</p></body></html>", None))
        self.primDueLineEdit.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Prime Due.</p></body></html>", None))
        self.cartRosLineEdit.setToolTip(_translate("Paiements", "<html><head/><body><p>Cartes Roses.</p></body></html>", None))
        self.cartRosLineEdit.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Cartes Roses.</p></body></html>", None))
        self.autrPPLineEdit.setToolTip(_translate("Paiements", "<html><head/><body><p>Autres PP.</p></body></html>", None))
        self.autrPPLineEdit.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Autres PP.</p></body></html>", None))
        self.totalAPayerLineEdit.setToolTip(_translate("Paiements", "<html><head/><body><p>Total a Payer.</p></body></html>", None))
        self.totalAPayerLineEdit.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Total a Payer.</p></body></html>", None))
        self.cumulImputionLineEdit.setToolTip(_translate("Paiements", "<html><head/><body><p>Cumuls Imputations.</p></body></html>", None))
        self.cumulImputionLineEdit.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Cumuls Imputations.</p></body></html>", None))
        self.opAImputerComboBox.setToolTip(_translate("Paiements", "<html><head/><body><p>Operation a Imputer.</p></body></html>", None))
        self.opAImputerComboBox.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Operation a Imputer.</p></body></html>", None))
        self.labelAutresInfos.setText(_translate("Paiements", "Autres Informations", None))
        self.labelTitulaire.setText(_translate("Paiements", "Titulaire du Compte", None))
        self.labelDateEncaissementEffet.setText(_translate("Paiements", "Date Encaissement Effet", None))
        self.paiementValideComboBox.setToolTip(_translate("Paiements", "<html><head/><body><p>Paiement Valide?</p></body></html>", None))
        self.paiementValideComboBox.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Paiement Valide?</p></body></html>", None))
        self.labelModePaiement.setText(_translate("Paiements", "Mode de Paiement", None))
        self.labelPaiementValide.setText(_translate("Paiements", "Paiement Valide ?", None))
        self.labelPayeurEffet.setText(_translate("Paiements", "Payeur effet", None))
        self.numRecuLineEdit.setToolTip(_translate("Paiements", "<html><head/><body><p>Numero du Recu de Paiement.</p></body></html>", None))
        self.numRecuLineEdit.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Numero du Recu de Paiement.</p></body></html>", None))
        self.titulaireLineEdit.setToolTip(_translate("Paiements", "<html><head/><body><p>Titulaire du Compte.</p></body></html>", None))
        self.titulaireLineEdit.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Titulaire du Compte.</p></body></html>", None))
        self.payeurEffetComboBox.setToolTip(_translate("Paiements", "<html><head/><body><p>Payeur Effet.</p></body></html>", None))
        self.payeurEffetComboBox.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Payeur Effet.</p></body></html>", None))
        self.labelNumRecu.setText(_translate("Paiements", "NUMERO RECU", None))
        self.dateEncaisEffetDateEdit.setToolTip(_translate("Paiements", "<html><head/><body><p>Date Encaissement Effet.</p></body></html>", None))
        self.dateEncaisEffetDateEdit.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Date Encaissement Effet.</p></body></html>", None))
        self.labelNumPiece.setText(_translate("Paiements", "Numero de la Piece", None))
        self.modPaiementComboBox.setToolTip(_translate("Paiements", "<html><head/><body><p>Mode de Paiement.</p></body></html>", None))
        self.modPaiementComboBox.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Mode de Paiement.</p></body></html>", None))
        self.montantPaiementLineEdit.setToolTip(_translate("Paiements", "<html><head/><body><p>Montant du Paiement.</p></body></html>", None))
        self.montantPaiementLineEdit.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Montant du Paiement.</p></body></html>", None))
        self.labelMontantPaiement.setText(_translate("Paiements", "Montant du Paiement", None))
        self.numPieceLineEdit.setToolTip(_translate("Paiements", "<html><head/><body><p>Numero de la Piece.</p></body></html>", None))
        self.numPieceLineEdit.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Numero de la Piece.</p></body></html>", None))
        self.labelDatePaiement.setText(_translate("Paiements", "Date du Paiement", None))
        self.datePaiementDateEdit.setToolTip(_translate("Paiements", "<html><head/><body><p>Date du Paiement.</p></body></html>", None))
        self.datePaiementDateEdit.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Date du Paiement.</p></body></html>", None))
        self.labelSoldeOperation.setText(_translate("Paiements", "Solde Operation", None))
        self.detailsPaiementTableView.setToolTip(_translate("Paiements", "<html><head/><body><p>Details des Paiements.</p></body></html>", None))
        self.detailsPaiementTableView.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Details des Paiements.</p></body></html>", None))
        self.labelResteAImputer.setText(_translate("Paiements", "Reste a Imputer", None))
        self.labelMouvAssocies.setText(_translate("Paiements", "Mouvements associes au Paiement", None))
        self.operationProductionTableView.setToolTip(_translate("Paiements", "<html><head/><body><p>Mouvements associes au Paiement.</p></body></html>", None))
        self.operationProductionTableView.setWhatsThis(_translate("Paiements", "<html><head/><body><p>Mouvements associes au Paiement.</p></body></html>", None))
        self.menu_Fichier.setTitle(_translate("Paiements", "&Fichier", None))
        self.menu_Edition.setTitle(_translate("Paiements", "&Edition", None))
        self.toolBar.setWindowTitle(_translate("Paiements", "toolBar", None))
        self.fichierNouveau.setText(_translate("Paiements", "Nouveau", None))
        self.fichierEnregistrer.setText(_translate("Paiements", "Enregistrer", None))
        self.fichierImprimPiecesEncaissement.setText(_translate("Paiements", "Imprimer les pieces d\'Encaissement", None))
        self.fichierFermer.setText(_translate("Paiements", "Fermer", None))
        self.editionAnnuler.setText(_translate("Paiements", "Annuler", None))
        self.editionRefaire.setText(_translate("Paiements", "Refaire", None))
        self.editionPremier.setText(_translate("Paiements", "Premier", None))
        self.editionPrecedent.setText(_translate("Paiements", "Precedent", None))
        self.editionSuivant.setText(_translate("Paiements", "Suivant", None))
        self.editionDernier.setText(_translate("Paiements", "Dernier", None))

import ressources_rc
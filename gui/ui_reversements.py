# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reversements.ui'
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

class Ui_Reversements(object):
    def setupUi(self, Reversements):
        Reversements.setObjectName(_fromUtf8("Reversements"))
        Reversements.setWindowModality(QtCore.Qt.ApplicationModal)
        Reversements.resize(993, 668)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        Reversements.setFont(font)
        self.centralwidget = QtGui.QWidget(Reversements)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.progressBar_2 = QtGui.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.progressBar_2.setFont(font)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.horizontalLayout_2.addWidget(self.progressBar_2)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.operationProductionAReverserTableView = QtGui.QTableView(self.frame_3)
        self.operationProductionAReverserTableView.setMinimumSize(QtCore.QSize(400, 400))
        self.operationProductionAReverserTableView.setMaximumSize(QtCore.QSize(450, 450))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.operationProductionAReverserTableView.setFont(font)
        self.operationProductionAReverserTableView.setAlternatingRowColors(True)
        self.operationProductionAReverserTableView.setObjectName(_fromUtf8("operationProductionAReverserTableView"))
        self.verticalLayout_3.addWidget(self.operationProductionAReverserTableView)
        self.gridLayout_6.addWidget(self.frame_3, 2, 1, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 100))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.labelAgence = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.labelAgence.setFont(font)
        self.labelAgence.setObjectName(_fromUtf8("labelAgence"))
        self.gridLayout_2.addWidget(self.labelAgence, 2, 0, 1, 1)
        self.cieLineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.cieLineEdit.setFont(font)
        self.cieLineEdit.setObjectName(_fromUtf8("cieLineEdit"))
        self.gridLayout_2.addWidget(self.cieLineEdit, 1, 1, 1, 1)
        self.opLineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.opLineEdit.setFont(font)
        self.opLineEdit.setObjectName(_fromUtf8("opLineEdit"))
        self.gridLayout_2.addWidget(self.opLineEdit, 3, 1, 1, 1)
        self.labelOperateur = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.labelOperateur.setFont(font)
        self.labelOperateur.setObjectName(_fromUtf8("labelOperateur"))
        self.gridLayout_2.addWidget(self.labelOperateur, 3, 0, 1, 1)
        self.labelCompagnie = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.labelCompagnie.setFont(font)
        self.labelCompagnie.setObjectName(_fromUtf8("labelCompagnie"))
        self.gridLayout_2.addWidget(self.labelCompagnie, 1, 0, 1, 1)
        self.resAgenceLineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.resAgenceLineEdit.setFont(font)
        self.resAgenceLineEdit.setObjectName(_fromUtf8("resAgenceLineEdit"))
        self.gridLayout_2.addWidget(self.resAgenceLineEdit, 2, 1, 1, 1)
        self.labelNumBordereau = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.labelNumBordereau.setFont(font)
        self.labelNumBordereau.setObjectName(_fromUtf8("labelNumBordereau"))
        self.gridLayout_2.addWidget(self.labelNumBordereau, 0, 0, 1, 1)
        self.numBordLineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.numBordLineEdit.setFont(font)
        self.numBordLineEdit.setObjectName(_fromUtf8("numBordLineEdit"))
        self.gridLayout_2.addWidget(self.numBordLineEdit, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.montantReverseLineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.montantReverseLineEdit.setFont(font)
        self.montantReverseLineEdit.setObjectName(_fromUtf8("montantReverseLineEdit"))
        self.gridLayout_3.addWidget(self.montantReverseLineEdit, 2, 1, 1, 1)
        self.labelMontantAReverser = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.labelMontantAReverser.setFont(font)
        self.labelMontantAReverser.setObjectName(_fromUtf8("labelMontantAReverser"))
        self.gridLayout_3.addWidget(self.labelMontantAReverser, 1, 0, 1, 1)
        self.labelMontantReverse = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.labelMontantReverse.setFont(font)
        self.labelMontantReverse.setObjectName(_fromUtf8("labelMontantReverse"))
        self.gridLayout_3.addWidget(self.labelMontantReverse, 2, 0, 1, 1)
        self.dateVersementDateEdit = QtGui.QDateEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.dateVersementDateEdit.setFont(font)
        self.dateVersementDateEdit.setObjectName(_fromUtf8("dateVersementDateEdit"))
        self.gridLayout_3.addWidget(self.dateVersementDateEdit, 0, 1, 1, 1)
        self.soldeCourantLineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.soldeCourantLineEdit.setFont(font)
        self.soldeCourantLineEdit.setObjectName(_fromUtf8("soldeCourantLineEdit"))
        self.gridLayout_3.addWidget(self.soldeCourantLineEdit, 3, 1, 1, 1)
        self.montantAReverserLineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.montantAReverserLineEdit.setFont(font)
        self.montantAReverserLineEdit.setObjectName(_fromUtf8("montantAReverserLineEdit"))
        self.gridLayout_3.addWidget(self.montantAReverserLineEdit, 1, 1, 1, 1)
        self.labelDateVersement = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.labelDateVersement.setFont(font)
        self.labelDateVersement.setObjectName(_fromUtf8("labelDateVersement"))
        self.gridLayout_3.addWidget(self.labelDateVersement, 0, 0, 1, 1)
        self.labelSoldeCourant = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.labelSoldeCourant.setFont(font)
        self.labelSoldeCourant.setObjectName(_fromUtf8("labelSoldeCourant"))
        self.gridLayout_3.addWidget(self.labelSoldeCourant, 3, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.labelDesignation = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.labelDesignation.setFont(font)
        self.labelDesignation.setObjectName(_fromUtf8("labelDesignation"))
        self.gridLayout_4.addWidget(self.labelDesignation, 0, 0, 1, 1)
        self.labelCommentaires = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.labelCommentaires.setFont(font)
        self.labelCommentaires.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelCommentaires.setObjectName(_fromUtf8("labelCommentaires"))
        self.gridLayout_4.addWidget(self.labelCommentaires, 1, 0, 1, 1)
        self.designationLineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.designationLineEdit.setFont(font)
        self.designationLineEdit.setObjectName(_fromUtf8("designationLineEdit"))
        self.gridLayout_4.addWidget(self.designationLineEdit, 0, 1, 1, 1)
        self.commentTextEdit = QtGui.QTextEdit(self.frame)
        self.commentTextEdit.setMinimumSize(QtCore.QSize(100, 30))
        self.commentTextEdit.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.commentTextEdit.setFont(font)
        self.commentTextEdit.setObjectName(_fromUtf8("commentTextEdit"))
        self.gridLayout_4.addWidget(self.commentTextEdit, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 2, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.soldeGeneLineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.soldeGeneLineEdit.setFont(font)
        self.soldeGeneLineEdit.setObjectName(_fromUtf8("soldeGeneLineEdit"))
        self.gridLayout_5.addWidget(self.soldeGeneLineEdit, 2, 1, 1, 1)
        self.totalReverseLineEdit = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.totalReverseLineEdit.setFont(font)
        self.totalReverseLineEdit.setObjectName(_fromUtf8("totalReverseLineEdit"))
        self.gridLayout_5.addWidget(self.totalReverseLineEdit, 3, 1, 1, 1)
        self.labelSoldeGeneral = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.labelSoldeGeneral.setFont(font)
        self.labelSoldeGeneral.setObjectName(_fromUtf8("labelSoldeGeneral"))
        self.gridLayout_5.addWidget(self.labelSoldeGeneral, 2, 0, 1, 1)
        self.revNetCommisCheckBox = QtGui.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.revNetCommisCheckBox.setFont(font)
        self.revNetCommisCheckBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.revNetCommisCheckBox.setObjectName(_fromUtf8("revNetCommisCheckBox"))
        self.gridLayout_5.addWidget(self.revNetCommisCheckBox, 1, 0, 1, 2)
        self.labelTotalReverse = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.labelTotalReverse.setFont(font)
        self.labelTotalReverse.setObjectName(_fromUtf8("labelTotalReverse"))
        self.gridLayout_5.addWidget(self.labelTotalReverse, 3, 0, 1, 1)
        self.revSurEncaissCheckBox = QtGui.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.revSurEncaissCheckBox.setFont(font)
        self.revSurEncaissCheckBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.revSurEncaissCheckBox.setObjectName(_fromUtf8("revSurEncaissCheckBox"))
        self.gridLayout_5.addWidget(self.revSurEncaissCheckBox, 0, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_5, 0, 3, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 3)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.operationProductionTableView = QtGui.QTableView(self.frame_2)
        self.operationProductionTableView.setMinimumSize(QtCore.QSize(400, 400))
        self.operationProductionTableView.setMaximumSize(QtCore.QSize(450, 450))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Narrow"))
        font.setPointSize(11)
        self.operationProductionTableView.setFont(font)
        self.operationProductionTableView.setAlternatingRowColors(True)
        self.operationProductionTableView.setObjectName(_fromUtf8("operationProductionTableView"))
        self.verticalLayout_2.addWidget(self.operationProductionTableView)
        self.gridLayout_6.addWidget(self.frame_2, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem, 1, 0, 1, 1)
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame.raise_()
        Reversements.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Reversements)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_Fichier = QtGui.QMenu(self.menubar)
        self.menu_Fichier.setObjectName(_fromUtf8("menu_Fichier"))
        self.menu_Edition = QtGui.QMenu(self.menubar)
        self.menu_Edition.setObjectName(_fromUtf8("menu_Edition"))
        Reversements.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Reversements)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Reversements.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Reversements)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Reversements.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.fichierNouveau = QtGui.QAction(Reversements)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/document-new.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fichierNouveau.setIcon(icon)
        self.fichierNouveau.setObjectName(_fromUtf8("fichierNouveau"))
        self.fichierEnregistrer = QtGui.QAction(Reversements)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/document-save.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fichierEnregistrer.setIcon(icon1)
        self.fichierEnregistrer.setObjectName(_fromUtf8("fichierEnregistrer"))
        self.fichierImprimBordereauReversement = QtGui.QAction(Reversements)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/Imprimer.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fichierImprimBordereauReversement.setIcon(icon2)
        self.fichierImprimBordereauReversement.setObjectName(_fromUtf8("fichierImprimBordereauReversement"))
        self.fichierFermer = QtGui.QAction(Reversements)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/system-log-out.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fichierFermer.setIcon(icon3)
        self.fichierFermer.setObjectName(_fromUtf8("fichierFermer"))
        self.editionAnnuler = QtGui.QAction(Reversements)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/edit-undo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editionAnnuler.setIcon(icon4)
        self.editionAnnuler.setObjectName(_fromUtf8("editionAnnuler"))
        self.editionRefaire = QtGui.QAction(Reversements)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/edit-redo.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editionRefaire.setIcon(icon5)
        self.editionRefaire.setObjectName(_fromUtf8("editionRefaire"))
        self.editionPremier = QtGui.QAction(Reversements)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/go-first.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editionPremier.setIcon(icon6)
        self.editionPremier.setObjectName(_fromUtf8("editionPremier"))
        self.editionPrecedent = QtGui.QAction(Reversements)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/go-previous.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editionPrecedent.setIcon(icon7)
        self.editionPrecedent.setObjectName(_fromUtf8("editionPrecedent"))
        self.editionSuivant = QtGui.QAction(Reversements)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/go-next.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editionSuivant.setIcon(icon8)
        self.editionSuivant.setObjectName(_fromUtf8("editionSuivant"))
        self.editionDernier = QtGui.QAction(Reversements)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icones/go-last.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editionDernier.setIcon(icon9)
        self.editionDernier.setObjectName(_fromUtf8("editionDernier"))
        self.menu_Fichier.addAction(self.fichierNouveau)
        self.menu_Fichier.addAction(self.fichierEnregistrer)
        self.menu_Fichier.addSeparator()
        self.menu_Fichier.addAction(self.fichierImprimBordereauReversement)
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
        self.toolBar.addAction(self.fichierImprimBordereauReversement)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.fichierFermer)

        self.retranslateUi(Reversements)
        QtCore.QMetaObject.connectSlotsByName(Reversements)
        Reversements.setTabOrder(self.numBordLineEdit, self.cieLineEdit)
        Reversements.setTabOrder(self.cieLineEdit, self.resAgenceLineEdit)
        Reversements.setTabOrder(self.resAgenceLineEdit, self.opLineEdit)
        Reversements.setTabOrder(self.opLineEdit, self.dateVersementDateEdit)
        Reversements.setTabOrder(self.dateVersementDateEdit, self.montantAReverserLineEdit)
        Reversements.setTabOrder(self.montantAReverserLineEdit, self.montantReverseLineEdit)
        Reversements.setTabOrder(self.montantReverseLineEdit, self.soldeCourantLineEdit)
        Reversements.setTabOrder(self.soldeCourantLineEdit, self.designationLineEdit)
        Reversements.setTabOrder(self.designationLineEdit, self.commentTextEdit)
        Reversements.setTabOrder(self.commentTextEdit, self.revSurEncaissCheckBox)
        Reversements.setTabOrder(self.revSurEncaissCheckBox, self.revNetCommisCheckBox)
        Reversements.setTabOrder(self.revNetCommisCheckBox, self.soldeGeneLineEdit)
        Reversements.setTabOrder(self.soldeGeneLineEdit, self.totalReverseLineEdit)

    def retranslateUi(self, Reversements):
        Reversements.setWindowTitle(_translate("Reversements", "Reversements", None))
        self.labelAgence.setText(_translate("Reversements", "Reseau/Agence", None))
        self.cieLineEdit.setToolTip(_translate("Reversements", "<html><head/><body><p>Compagnie.</p></body></html>", None))
        self.cieLineEdit.setWhatsThis(_translate("Reversements", "<html><head/><body><p>Compagnie.</p></body></html>", None))
        self.opLineEdit.setToolTip(_translate("Reversements", "<html><head/><body><p>Operateur.</p></body></html>", None))
        self.opLineEdit.setWhatsThis(_translate("Reversements", "<html><head/><body><p>Operateur.</p></body></html>", None))
        self.labelOperateur.setText(_translate("Reversements", "Operateur", None))
        self.labelCompagnie.setText(_translate("Reversements", "Compagnie", None))
        self.resAgenceLineEdit.setToolTip(_translate("Reversements", "<html><head/><body><p>Reseau ou Agence.</p></body></html>", None))
        self.resAgenceLineEdit.setWhatsThis(_translate("Reversements", "<html><head/><body><p>Reseau ou Agence.</p></body></html>", None))
        self.labelNumBordereau.setText(_translate("Reversements", "Numero Bordereau", None))
        self.numBordLineEdit.setToolTip(_translate("Reversements", "<html><head/><body><p>Numero Bordereau.</p></body></html>", None))
        self.numBordLineEdit.setWhatsThis(_translate("Reversements", "<html><head/><body><p>Numero Bordereau.</p></body></html>", None))
        self.montantReverseLineEdit.setToolTip(_translate("Reversements", "<html><head/><body><p>Montant Reverse.</p></body></html>", None))
        self.montantReverseLineEdit.setWhatsThis(_translate("Reversements", "<html><head/><body><p>Montant Reverse.</p></body></html>", None))
        self.labelMontantAReverser.setText(_translate("Reversements", "Montant a reverser", None))
        self.labelMontantReverse.setText(_translate("Reversements", "Montant reverse", None))
        self.dateVersementDateEdit.setToolTip(_translate("Reversements", "<html><head/><body><p>Date de Versement.</p></body></html>", None))
        self.dateVersementDateEdit.setWhatsThis(_translate("Reversements", "<html><head/><body><p>Date de Versement.</p></body></html>", None))
        self.soldeCourantLineEdit.setToolTip(_translate("Reversements", "<html><head/><body><p>Solde Courant.</p></body></html>", None))
        self.soldeCourantLineEdit.setWhatsThis(_translate("Reversements", "<html><head/><body><p>Solde Courant.</p></body></html>", None))
        self.montantAReverserLineEdit.setToolTip(_translate("Reversements", "<html><head/><body><p>Montant A Reverse.</p></body></html>", None))
        self.montantAReverserLineEdit.setWhatsThis(_translate("Reversements", "<html><head/><body><p>Montant A Reverse.</p></body></html>", None))
        self.labelDateVersement.setText(_translate("Reversements", "Date de Versement", None))
        self.labelSoldeCourant.setText(_translate("Reversements", "Solde courant", None))
        self.labelDesignation.setText(_translate("Reversements", "Designation", None))
        self.labelCommentaires.setText(_translate("Reversements", "Commentaires", None))
        self.designationLineEdit.setToolTip(_translate("Reversements", "<html><head/><body><p>Designation.</p></body></html>", None))
        self.designationLineEdit.setWhatsThis(_translate("Reversements", "<html><head/><body><p>Designation.</p></body></html>", None))
        self.commentTextEdit.setToolTip(_translate("Reversements", "<html><head/><body><p>Commentaires.</p></body></html>", None))
        self.commentTextEdit.setWhatsThis(_translate("Reversements", "<html><head/><body><p>Commentaires.</p></body></html>", None))
        self.soldeGeneLineEdit.setToolTip(_translate("Reversements", "<html><head/><body><p>Solde General.</p></body></html>", None))
        self.soldeGeneLineEdit.setWhatsThis(_translate("Reversements", "<html><head/><body><p>Solde General.</p></body></html>", None))
        self.totalReverseLineEdit.setToolTip(_translate("Reversements", "<html><head/><body><p>Total Reverse.</p></body></html>", None))
        self.totalReverseLineEdit.setWhatsThis(_translate("Reversements", "<html><head/><body><p>Total Reverse.</p></body></html>", None))
        self.labelSoldeGeneral.setText(_translate("Reversements", "Solde General", None))
        self.revNetCommisCheckBox.setToolTip(_translate("Reversements", "<html><head/><body><p>Reversements Net de Commissions?</p></body></html>", None))
        self.revNetCommisCheckBox.setWhatsThis(_translate("Reversements", "<html><head/><body><p>Reversements Net de Commissions?</p></body></html>", None))
        self.revNetCommisCheckBox.setText(_translate("Reversements", "Reversements net de Commissions?", None))
        self.labelTotalReverse.setText(_translate("Reversements", "Total reverse", None))
        self.revSurEncaissCheckBox.setToolTip(_translate("Reversements", "<html><head/><body><p>Reversements sur Encaissements?</p></body></html>", None))
        self.revSurEncaissCheckBox.setWhatsThis(_translate("Reversements", "<html><head/><body><p>Reversements sur Encaissements?</p></body></html>", None))
        self.revSurEncaissCheckBox.setText(_translate("Reversements", "Reversements sur Encaissements?", None))
        self.menu_Fichier.setTitle(_translate("Reversements", "&Fichier", None))
        self.menu_Edition.setTitle(_translate("Reversements", "&Edition", None))
        self.toolBar.setWindowTitle(_translate("Reversements", "toolBar", None))
        self.fichierNouveau.setText(_translate("Reversements", "Nouveau", None))
        self.fichierEnregistrer.setText(_translate("Reversements", "Enregistrer", None))
        self.fichierImprimBordereauReversement.setText(_translate("Reversements", "Imprimer le bordereau de Reversement", None))
        self.fichierFermer.setText(_translate("Reversements", "Fermer", None))
        self.editionAnnuler.setText(_translate("Reversements", "Annuler", None))
        self.editionRefaire.setText(_translate("Reversements", "Refaire", None))
        self.editionPremier.setText(_translate("Reversements", "Premier", None))
        self.editionPrecedent.setText(_translate("Reversements", "Precedent", None))
        self.editionSuivant.setText(_translate("Reversements", "Suivant", None))
        self.editionDernier.setText(_translate("Reversements", "Dernier", None))

import ressources_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.graphicsView = GraphicsLayoutWidget(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 80, 1231, 721))
        self.graphicsView.setObjectName("graphicsView")
        self.startBtn = QtWidgets.QPushButton(self.centralWidget)
        self.startBtn.setGeometry(QtCore.QRect(20, 830, 1681, 171))
        self.startBtn.setText("")
        self.startBtn.setObjectName("startBtn")
        self.infoText = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.infoText.setGeometry(QtCore.QRect(1270, 80, 631, 391))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.infoText.setFont(font)
        self.infoText.setObjectName("infoText")
        self.infoLabel = QtWidgets.QLabel(self.centralWidget)
        self.infoLabel.setGeometry(QtCore.QRect(1270, 20, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.infoLabel.setFont(font)
        self.infoLabel.setObjectName("infoLabel")
        self.pcmLabel = QtWidgets.QLabel(self.centralWidget)
        self.pcmLabel.setGeometry(QtCore.QRect(20, 20, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pcmLabel.setFont(font)
        self.pcmLabel.setObjectName("pcmLabel")
        self.statusLabel = QtWidgets.QLabel(self.centralWidget)
        self.statusLabel.setGeometry(QtCore.QRect(1450, 80, 331, 371))
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.resetBtn = QtWidgets.QPushButton(self.centralWidget)
        self.resetBtn.setGeometry(QtCore.QRect(1730, 830, 171, 171))
        self.resetBtn.setText("")
        self.resetBtn.setObjectName("resetBtn")
        self.inferenceLabel = QtWidgets.QLabel(self.centralWidget)
        self.inferenceLabel.setGeometry(QtCore.QRect(1270, 480, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inferenceLabel.setFont(font)
        self.inferenceLabel.setObjectName("inferenceLabel")
        self.infereceText = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.infereceText.setGeometry(QtCore.QRect(1270, 530, 631, 271))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.infereceText.setFont(font)
        self.infereceText.setObjectName("infereceText")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1920, 37))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.infoLabel.setText(_translate("MainWindow", "Output Information :"))
        self.pcmLabel.setText(_translate("MainWindow", "Record Audio PCM :"))
        self.inferenceLabel.setText(_translate("MainWindow", "Inference Reslut :"))

from pyqtgraph import GraphicsLayoutWidget

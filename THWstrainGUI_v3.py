# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'THWstrainGUI_v3.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(219, 260)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ComConnect = QtWidgets.QPushButton(self.centralwidget)
        self.ComConnect.setGeometry(QtCore.QRect(50, 50, 121, 23))
        self.ComConnect.setObjectName("ComConnect")
        self.LeftPush = QtWidgets.QPushButton(self.centralwidget)
        self.LeftPush.setGeometry(QtCore.QRect(20, 140, 75, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.LeftPush.setFont(font)
        self.LeftPush.setObjectName("LeftPush")
        self.RightPush = QtWidgets.QPushButton(self.centralwidget)
        self.RightPush.setGeometry(QtCore.QRect(120, 140, 75, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RightPush.sizePolicy().hasHeightForWidth())
        self.RightPush.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.RightPush.setFont(font)
        self.RightPush.setObjectName("RightPush")
        self.SlideMode = QtWidgets.QComboBox(self.centralwidget)
        self.SlideMode.setGeometry(QtCore.QRect(70, 100, 81, 22))
        self.SlideMode.setObjectName("SlideMode")
        self.SlideMode.addItems(['Both','Left','Right'])
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 219, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ComConnect.setText(_translate("MainWindow", "Connect to Arduino"))
        self.LeftPush.setText(_translate("MainWindow", "<"))
        self.RightPush.setText(_translate("MainWindow", ">"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Mon Jun 15 11:44:13 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(434, 543)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scaleLabel = QtGui.QLabel(self.centralwidget)
        self.scaleLabel.setObjectName(_fromUtf8("scaleLabel"))
        self.verticalLayout_2.addWidget(self.scaleLabel)
        self.scaleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.scaleSpinBox.setAccelerated(False)
        self.scaleSpinBox.setMaximum(100.0)
        self.scaleSpinBox.setSingleStep(0.1)
        self.scaleSpinBox.setProperty("value", 1.0)
        self.scaleSpinBox.setObjectName(_fromUtf8("scaleSpinBox"))
        self.verticalLayout_2.addWidget(self.scaleSpinBox)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.thicknessLabel = QtGui.QLabel(self.centralwidget)
        self.thicknessLabel.setObjectName(_fromUtf8("thicknessLabel"))
        self.verticalLayout_9.addWidget(self.thicknessLabel)
        self.thicknessSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.thicknessSpinBox.setDecimals(0)
        self.thicknessSpinBox.setProperty("value", 10.0)
        self.thicknessSpinBox.setObjectName(_fromUtf8("thicknessSpinBox"))
        self.verticalLayout_9.addWidget(self.thicknessSpinBox)
        self.verticalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.speedLabel = QtGui.QLabel(self.centralwidget)
        self.speedLabel.setObjectName(_fromUtf8("speedLabel"))
        self.verticalLayout_3.addWidget(self.speedLabel)
        self.speedSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.speedSpinBox.setDecimals(3)
        self.speedSpinBox.setMaximum(100.0)
        self.speedSpinBox.setSingleStep(0.01)
        self.speedSpinBox.setProperty("value", 0.01)
        self.speedSpinBox.setObjectName(_fromUtf8("speedSpinBox"))
        self.verticalLayout_3.addWidget(self.speedSpinBox)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.distanceLabel = QtGui.QLabel(self.centralwidget)
        self.distanceLabel.setObjectName(_fromUtf8("distanceLabel"))
        self.verticalLayout_4.addWidget(self.distanceLabel)
        self.distanceSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.distanceSpinBox.setDecimals(1)
        self.distanceSpinBox.setMaximum(1000.0)
        self.distanceSpinBox.setProperty("value", 100.0)
        self.distanceSpinBox.setObjectName(_fromUtf8("distanceSpinBox"))
        self.verticalLayout_4.addWidget(self.distanceSpinBox)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.pRadiusLabel = QtGui.QLabel(self.centralwidget)
        self.pRadiusLabel.setObjectName(_fromUtf8("pRadiusLabel"))
        self.verticalLayout_6.addWidget(self.pRadiusLabel)
        self.pradiusSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.pradiusSpinBox.setDecimals(1)
        self.pradiusSpinBox.setMaximum(1000.0)
        self.pradiusSpinBox.setProperty("value", 10.0)
        self.pradiusSpinBox.setObjectName(_fromUtf8("pradiusSpinBox"))
        self.verticalLayout_6.addWidget(self.pradiusSpinBox)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.densityLabel = QtGui.QLabel(self.centralwidget)
        self.densityLabel.setObjectName(_fromUtf8("densityLabel"))
        self.verticalLayout_10.addWidget(self.densityLabel)
        self.densitySpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.densitySpinBox.setDecimals(3)
        self.densitySpinBox.setMaximum(100.0)
        self.densitySpinBox.setObjectName(_fromUtf8("densitySpinBox"))
        self.verticalLayout_10.addWidget(self.densitySpinBox)
        self.verticalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.viscositylabel = QtGui.QLabel(self.centralwidget)
        self.viscositylabel.setObjectName(_fromUtf8("viscositylabel"))
        self.verticalLayout_7.addWidget(self.viscositylabel)
        self.viscositySpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.viscositySpinBox.setDecimals(5)
        self.viscositySpinBox.setMaximum(1000000.0)
        self.viscositySpinBox.setObjectName(_fromUtf8("viscositySpinBox"))
        self.verticalLayout_7.addWidget(self.viscositySpinBox)
        self.verticalLayout.addLayout(self.verticalLayout_7)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.linspeedLabel = QtGui.QLabel(self.centralwidget)
        self.linspeedLabel.setObjectName(_fromUtf8("linspeedLabel"))
        self.verticalLayout_5.addWidget(self.linspeedLabel)
        self.linVelocityLcdNumber = QtGui.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.linVelocityLcdNumber.setPalette(palette)
        self.linVelocityLcdNumber.setFrameShape(QtGui.QFrame.NoFrame)
        self.linVelocityLcdNumber.setFrameShadow(QtGui.QFrame.Raised)
        self.linVelocityLcdNumber.setSmallDecimalPoint(False)
        self.linVelocityLcdNumber.setNumDigits(6)
        self.linVelocityLcdNumber.setObjectName(_fromUtf8("linVelocityLcdNumber"))
        self.verticalLayout_5.addWidget(self.linVelocityLcdNumber)
        self.verticalLayout_12.addLayout(self.verticalLayout_5)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.forcelabel = QtGui.QLabel(self.centralwidget)
        self.forcelabel.setTextFormat(QtCore.Qt.PlainText)
        self.forcelabel.setObjectName(_fromUtf8("forcelabel"))
        self.verticalLayout_8.addWidget(self.forcelabel)
        self.forceLcdNumber = QtGui.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.forceLcdNumber.setPalette(palette)
        self.forceLcdNumber.setFrameShape(QtGui.QFrame.NoFrame)
        self.forceLcdNumber.setFrameShadow(QtGui.QFrame.Raised)
        self.forceLcdNumber.setSmallDecimalPoint(False)
        self.forceLcdNumber.setNumDigits(6)
        self.forceLcdNumber.setObjectName(_fromUtf8("forceLcdNumber"))
        self.verticalLayout_8.addWidget(self.forceLcdNumber)
        self.verticalLayout_12.addLayout(self.verticalLayout_8)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.centripetalLabel = QtGui.QLabel(self.centralwidget)
        self.centripetalLabel.setTextFormat(QtCore.Qt.PlainText)
        self.centripetalLabel.setObjectName(_fromUtf8("centripetalLabel"))
        self.verticalLayout_11.addWidget(self.centripetalLabel)
        self.centripetalLcdNumber = QtGui.QLCDNumber(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.centripetalLcdNumber.setPalette(palette)
        self.centripetalLcdNumber.setFrameShape(QtGui.QFrame.NoFrame)
        self.centripetalLcdNumber.setFrameShadow(QtGui.QFrame.Raised)
        self.centripetalLcdNumber.setSmallDecimalPoint(False)
        self.centripetalLcdNumber.setNumDigits(6)
        self.centripetalLcdNumber.setObjectName(_fromUtf8("centripetalLcdNumber"))
        self.verticalLayout_11.addWidget(self.centripetalLcdNumber)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.gridLayout_2.addLayout(self.verticalLayout_12, 0, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.engagePushButton = QtGui.QPushButton(self.centralwidget)
        self.engagePushButton.setObjectName(_fromUtf8("engagePushButton"))
        self.gridLayout.addWidget(self.engagePushButton, 0, 0, 1, 1)
        self.stopPushButton = QtGui.QPushButton(self.centralwidget)
        self.stopPushButton.setObjectName(_fromUtf8("stopPushButton"))
        self.gridLayout.addWidget(self.stopPushButton, 0, 1, 1, 1)
        self.resetPushButton = QtGui.QPushButton(self.centralwidget)
        self.resetPushButton.setObjectName(_fromUtf8("resetPushButton"))
        self.gridLayout.addWidget(self.resetPushButton, 1, 0, 1, 1)
        self.recordPushButton = QtGui.QPushButton(self.centralwidget)
        self.recordPushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.recordPushButton.setObjectName(_fromUtf8("recordPushButton"))
        self.gridLayout.addWidget(self.recordPushButton, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuColor = QtGui.QMenu(self.menubar)
        self.menuColor.setObjectName(_fromUtf8("menuColor"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionInvert = QtGui.QAction(MainWindow)
        self.actionInvert.setCheckable(True)
        self.actionInvert.setObjectName(_fromUtf8("actionInvert"))
        self.menuFile.addAction(self.actionQuit)
        self.menuColor.addAction(self.actionInvert)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuColor.menuAction())
        self.scaleLabel.setBuddy(self.scaleSpinBox)
        self.thicknessLabel.setBuddy(self.thicknessSpinBox)
        self.speedLabel.setBuddy(self.speedSpinBox)
        self.distanceLabel.setBuddy(self.distanceSpinBox)
        self.pRadiusLabel.setBuddy(self.pradiusSpinBox)
        self.densityLabel.setBuddy(self.densitySpinBox)
        self.viscositylabel.setBuddy(self.viscositySpinBox)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.scaleSpinBox, self.thicknessSpinBox)
        MainWindow.setTabOrder(self.thicknessSpinBox, self.speedSpinBox)
        MainWindow.setTabOrder(self.speedSpinBox, self.distanceSpinBox)
        MainWindow.setTabOrder(self.distanceSpinBox, self.pradiusSpinBox)
        MainWindow.setTabOrder(self.pradiusSpinBox, self.densitySpinBox)
        MainWindow.setTabOrder(self.densitySpinBox, self.viscositySpinBox)
        MainWindow.setTabOrder(self.viscositySpinBox, self.engagePushButton)
        MainWindow.setTabOrder(self.engagePushButton, self.stopPushButton)
        MainWindow.setTabOrder(self.stopPushButton, self.resetPushButton)
        MainWindow.setTabOrder(self.resetPushButton, self.recordPushButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "OET", None))
        self.scaleLabel.setText(_translate("MainWindow", "&Scale", None))
        self.scaleSpinBox.setToolTip(_translate("MainWindow", "Scale of the figure", None))
        self.thicknessLabel.setText(_translate("MainWindow", "&Thickness", None))
        self.thicknessSpinBox.setToolTip(_translate("MainWindow", "Thickness of the lines", None))
        self.speedLabel.setText(_translate("MainWindow", "&Angular velocity (rps)", None))
        self.speedSpinBox.setToolTip(_translate("MainWindow", "Angular velocity in revolutions per second", None))
        self.distanceLabel.setText(_translate("MainWindow", "&Distance (um)", None))
        self.distanceSpinBox.setToolTip(_translate("MainWindow", "The distance from the center of the wheel to the center of the bead", None))
        self.pRadiusLabel.setText(_translate("MainWindow", "Bead radi&us (um)", None))
        self.pradiusSpinBox.setToolTip(_translate("MainWindow", "Radius of the bead in microns", None))
        self.densityLabel.setText(_translate("MainWindow", "Bead de&nsity (g/cm3)", None))
        self.densitySpinBox.setToolTip(_translate("MainWindow", "The density of the bead in g/cm3", None))
        self.viscositylabel.setText(_translate("MainWindow", "Dynamic &viscosity (mPa s)", None))
        self.viscositySpinBox.setToolTip(_translate("MainWindow", "Dynamic viscosity of the solution in mPa s", None))
        self.linspeedLabel.setText(_translate("MainWindow", "Linear velocity (um/s)", None))
        self.linVelocityLcdNumber.setToolTip(_translate("MainWindow", "Linear velocity of the bead in microns per second", None))
        self.forcelabel.setText(_translate("MainWindow", "DEP (pN)", None))
        self.forceLcdNumber.setToolTip(_translate("MainWindow", "Dielectrophoretic force in pN", None))
        self.centripetalLabel.setText(_translate("MainWindow", "Centripetal force (pN)", None))
        self.centripetalLcdNumber.setToolTip(_translate("MainWindow", "Centripetal force in pN", None))
        self.engagePushButton.setToolTip(_translate("MainWindow", "Start the animation", None))
        self.engagePushButton.setText(_translate("MainWindow", "&Engage", None))
        self.stopPushButton.setToolTip(_translate("MainWindow", "Stop the animation", None))
        self.stopPushButton.setText(_translate("MainWindow", "Sto&p", None))
        self.resetPushButton.setToolTip(_translate("MainWindow", "Reset the rotation of the figure to zero", None))
        self.resetPushButton.setText(_translate("MainWindow", "Reset", None))
        self.recordPushButton.setToolTip(_translate("MainWindow", "Record the current parameters to file", None))
        self.recordPushButton.setText(_translate("MainWindow", "&Record", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuColor.setTitle(_translate("MainWindow", "Color", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionInvert.setText(_translate("MainWindow", "Invert", None))
        self.actionInvert.setShortcut(_translate("MainWindow", "Alt+I", None))


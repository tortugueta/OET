# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Wed Jun 10 16:39:07 2015
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
        MainWindow.resize(189, 761)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
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
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
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
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
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
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.pRadiusLabel = QtGui.QLabel(self.centralwidget)
        self.pRadiusLabel.setObjectName(_fromUtf8("pRadiusLabel"))
        self.verticalLayout_6.addWidget(self.pRadiusLabel)
        self.pradiusSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.pradiusSpinBox.setDecimals(1)
        self.pradiusSpinBox.setMaximum(1000.0)
        self.pradiusSpinBox.setProperty("value", 10.0)
        self.pradiusSpinBox.setObjectName(_fromUtf8("pradiusSpinBox"))
        self.verticalLayout_6.addWidget(self.pradiusSpinBox)
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
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
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
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
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
        self.verticalLayout_6.addLayout(self.verticalLayout_8)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.engagePushButton = QtGui.QPushButton(self.centralwidget)
        self.engagePushButton.setObjectName(_fromUtf8("engagePushButton"))
        self.verticalLayout.addWidget(self.engagePushButton)
        self.stopPushButton = QtGui.QPushButton(self.centralwidget)
        self.stopPushButton.setObjectName(_fromUtf8("stopPushButton"))
        self.verticalLayout.addWidget(self.stopPushButton)
        self.resetPushButton = QtGui.QPushButton(self.centralwidget)
        self.resetPushButton.setObjectName(_fromUtf8("resetPushButton"))
        self.verticalLayout.addWidget(self.resetPushButton)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 189, 27))
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
        self.speedLabel.setBuddy(self.speedSpinBox)
        self.distanceLabel.setBuddy(self.distanceSpinBox)
        self.pRadiusLabel.setBuddy(self.pradiusSpinBox)
        self.viscositylabel.setBuddy(self.viscositySpinBox)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.scaleSpinBox, self.speedSpinBox)
        MainWindow.setTabOrder(self.speedSpinBox, self.distanceSpinBox)
        MainWindow.setTabOrder(self.distanceSpinBox, self.pradiusSpinBox)
        MainWindow.setTabOrder(self.pradiusSpinBox, self.viscositySpinBox)
        MainWindow.setTabOrder(self.viscositySpinBox, self.engagePushButton)
        MainWindow.setTabOrder(self.engagePushButton, self.resetPushButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "OET", None))
        self.scaleLabel.setText(_translate("MainWindow", "Scale", None))
        self.scaleSpinBox.setToolTip(_translate("MainWindow", "Scale of the figure", None))
        self.speedLabel.setText(_translate("MainWindow", "Angular velocity (rps)", None))
        self.speedSpinBox.setToolTip(_translate("MainWindow", "Angular velocity in revolutions per second", None))
        self.distanceLabel.setText(_translate("MainWindow", "Distance (um)", None))
        self.distanceSpinBox.setToolTip(_translate("MainWindow", "The distance from the center of the wheel to the center of the bead", None))
        self.pRadiusLabel.setText(_translate("MainWindow", "Bead radius (um)", None))
        self.pradiusSpinBox.setToolTip(_translate("MainWindow", "Radius of the bead", None))
        self.viscositylabel.setText(_translate("MainWindow", "Dynamic viscosity (mPa s)", None))
        self.viscositySpinBox.setToolTip(_translate("MainWindow", "Dynamic viscosity of the solution in mPa s", None))
        self.linspeedLabel.setText(_translate("MainWindow", "Linear velocity (um/s)", None))
        self.linVelocityLcdNumber.setToolTip(_translate("MainWindow", "Linear velocity of the bead in microns per second", None))
        self.forcelabel.setText(_translate("MainWindow", "DEP (pN)", None))
        self.forceLcdNumber.setToolTip(_translate("MainWindow", "Dielectrophoretic force in pN", None))
        self.engagePushButton.setToolTip(_translate("MainWindow", "Start the animation", None))
        self.engagePushButton.setText(_translate("MainWindow", "Engage", None))
        self.stopPushButton.setToolTip(_translate("MainWindow", "Stop the animation", None))
        self.stopPushButton.setText(_translate("MainWindow", "Stop", None))
        self.resetPushButton.setToolTip(_translate("MainWindow", "Reset the rotation of the figure to zero", None))
        self.resetPushButton.setText(_translate("MainWindow", "Reset", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuColor.setTitle(_translate("MainWindow", "Color", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionInvert.setText(_translate("MainWindow", "Invert", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Thu Jul 16 11:31:32 2015
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
        MainWindow.resize(333, 599)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 599))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.wheelTab = QtGui.QWidget()
        self.wheelTab.setObjectName(_fromUtf8("wheelTab"))
        self.gridLayout = QtGui.QGridLayout(self.wheelTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tab1_scaleLabel = QtGui.QLabel(self.wheelTab)
        self.tab1_scaleLabel.setObjectName(_fromUtf8("tab1_scaleLabel"))
        self.verticalLayout_2.addWidget(self.tab1_scaleLabel)
        self.tab1_scaleSpinBox = QtGui.QDoubleSpinBox(self.wheelTab)
        self.tab1_scaleSpinBox.setAccelerated(False)
        self.tab1_scaleSpinBox.setMaximum(100.0)
        self.tab1_scaleSpinBox.setSingleStep(0.1)
        self.tab1_scaleSpinBox.setProperty("value", 1.0)
        self.tab1_scaleSpinBox.setObjectName(_fromUtf8("tab1_scaleSpinBox"))
        self.verticalLayout_2.addWidget(self.tab1_scaleSpinBox)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.tab1_thicknessLabel = QtGui.QLabel(self.wheelTab)
        self.tab1_thicknessLabel.setObjectName(_fromUtf8("tab1_thicknessLabel"))
        self.verticalLayout_9.addWidget(self.tab1_thicknessLabel)
        self.tab1_thicknessSpinBox = QtGui.QDoubleSpinBox(self.wheelTab)
        self.tab1_thicknessSpinBox.setDecimals(0)
        self.tab1_thicknessSpinBox.setProperty("value", 10.0)
        self.tab1_thicknessSpinBox.setObjectName(_fromUtf8("tab1_thicknessSpinBox"))
        self.verticalLayout_9.addWidget(self.tab1_thicknessSpinBox)
        self.verticalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tab1_speedLabel = QtGui.QLabel(self.wheelTab)
        self.tab1_speedLabel.setObjectName(_fromUtf8("tab1_speedLabel"))
        self.verticalLayout_3.addWidget(self.tab1_speedLabel)
        self.tab1_speedSpinBox = QtGui.QDoubleSpinBox(self.wheelTab)
        self.tab1_speedSpinBox.setDecimals(3)
        self.tab1_speedSpinBox.setMaximum(100.0)
        self.tab1_speedSpinBox.setSingleStep(0.01)
        self.tab1_speedSpinBox.setProperty("value", 0.01)
        self.tab1_speedSpinBox.setObjectName(_fromUtf8("tab1_speedSpinBox"))
        self.verticalLayout_3.addWidget(self.tab1_speedSpinBox)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tab1_distanceLabel = QtGui.QLabel(self.wheelTab)
        self.tab1_distanceLabel.setObjectName(_fromUtf8("tab1_distanceLabel"))
        self.verticalLayout_4.addWidget(self.tab1_distanceLabel)
        self.tab1_distanceSpinBox = QtGui.QDoubleSpinBox(self.wheelTab)
        self.tab1_distanceSpinBox.setDecimals(1)
        self.tab1_distanceSpinBox.setMaximum(1000.0)
        self.tab1_distanceSpinBox.setProperty("value", 100.0)
        self.tab1_distanceSpinBox.setObjectName(_fromUtf8("tab1_distanceSpinBox"))
        self.verticalLayout_4.addWidget(self.tab1_distanceSpinBox)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.tab1_diameterLabel = QtGui.QLabel(self.wheelTab)
        self.tab1_diameterLabel.setObjectName(_fromUtf8("tab1_diameterLabel"))
        self.verticalLayout_6.addWidget(self.tab1_diameterLabel)
        self.tab1_diameterSpinBox = QtGui.QDoubleSpinBox(self.wheelTab)
        self.tab1_diameterSpinBox.setDecimals(1)
        self.tab1_diameterSpinBox.setMaximum(1000.0)
        self.tab1_diameterSpinBox.setProperty("value", 10.0)
        self.tab1_diameterSpinBox.setObjectName(_fromUtf8("tab1_diameterSpinBox"))
        self.verticalLayout_6.addWidget(self.tab1_diameterSpinBox)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.tab1_densityLabel = QtGui.QLabel(self.wheelTab)
        self.tab1_densityLabel.setObjectName(_fromUtf8("tab1_densityLabel"))
        self.verticalLayout_10.addWidget(self.tab1_densityLabel)
        self.tab1_densitySpinBox = QtGui.QDoubleSpinBox(self.wheelTab)
        self.tab1_densitySpinBox.setDecimals(3)
        self.tab1_densitySpinBox.setMaximum(100.0)
        self.tab1_densitySpinBox.setObjectName(_fromUtf8("tab1_densitySpinBox"))
        self.verticalLayout_10.addWidget(self.tab1_densitySpinBox)
        self.verticalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.tab1_viscositylabel = QtGui.QLabel(self.wheelTab)
        self.tab1_viscositylabel.setObjectName(_fromUtf8("tab1_viscositylabel"))
        self.verticalLayout_7.addWidget(self.tab1_viscositylabel)
        self.tab1_viscositySpinBox = QtGui.QDoubleSpinBox(self.wheelTab)
        self.tab1_viscositySpinBox.setDecimals(5)
        self.tab1_viscositySpinBox.setMaximum(1000000.0)
        self.tab1_viscositySpinBox.setObjectName(_fromUtf8("tab1_viscositySpinBox"))
        self.verticalLayout_7.addWidget(self.tab1_viscositySpinBox)
        self.verticalLayout.addLayout(self.verticalLayout_7)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.tab1_linspeedLabel = QtGui.QLabel(self.wheelTab)
        self.tab1_linspeedLabel.setObjectName(_fromUtf8("tab1_linspeedLabel"))
        self.verticalLayout_5.addWidget(self.tab1_linspeedLabel)
        self.tab1_linVelocityLcdNumber = QtGui.QLCDNumber(self.wheelTab)
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
        self.tab1_linVelocityLcdNumber.setPalette(palette)
        self.tab1_linVelocityLcdNumber.setFrameShape(QtGui.QFrame.NoFrame)
        self.tab1_linVelocityLcdNumber.setFrameShadow(QtGui.QFrame.Raised)
        self.tab1_linVelocityLcdNumber.setSmallDecimalPoint(False)
        self.tab1_linVelocityLcdNumber.setNumDigits(6)
        self.tab1_linVelocityLcdNumber.setObjectName(_fromUtf8("tab1_linVelocityLcdNumber"))
        self.verticalLayout_5.addWidget(self.tab1_linVelocityLcdNumber)
        self.verticalLayout_12.addLayout(self.verticalLayout_5)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.tab1_forcelabel = QtGui.QLabel(self.wheelTab)
        self.tab1_forcelabel.setTextFormat(QtCore.Qt.PlainText)
        self.tab1_forcelabel.setObjectName(_fromUtf8("tab1_forcelabel"))
        self.verticalLayout_8.addWidget(self.tab1_forcelabel)
        self.tab1_forceLcdNumber = QtGui.QLCDNumber(self.wheelTab)
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
        self.tab1_forceLcdNumber.setPalette(palette)
        self.tab1_forceLcdNumber.setFrameShape(QtGui.QFrame.NoFrame)
        self.tab1_forceLcdNumber.setFrameShadow(QtGui.QFrame.Raised)
        self.tab1_forceLcdNumber.setSmallDecimalPoint(False)
        self.tab1_forceLcdNumber.setNumDigits(6)
        self.tab1_forceLcdNumber.setObjectName(_fromUtf8("tab1_forceLcdNumber"))
        self.verticalLayout_8.addWidget(self.tab1_forceLcdNumber)
        self.verticalLayout_12.addLayout(self.verticalLayout_8)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.tab1_centripetalLabel = QtGui.QLabel(self.wheelTab)
        self.tab1_centripetalLabel.setTextFormat(QtCore.Qt.PlainText)
        self.tab1_centripetalLabel.setObjectName(_fromUtf8("tab1_centripetalLabel"))
        self.verticalLayout_11.addWidget(self.tab1_centripetalLabel)
        self.tab1_centripetalLcdNumber = QtGui.QLCDNumber(self.wheelTab)
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
        self.tab1_centripetalLcdNumber.setPalette(palette)
        self.tab1_centripetalLcdNumber.setFrameShape(QtGui.QFrame.NoFrame)
        self.tab1_centripetalLcdNumber.setFrameShadow(QtGui.QFrame.Raised)
        self.tab1_centripetalLcdNumber.setSmallDecimalPoint(False)
        self.tab1_centripetalLcdNumber.setNumDigits(6)
        self.tab1_centripetalLcdNumber.setObjectName(_fromUtf8("tab1_centripetalLcdNumber"))
        self.verticalLayout_11.addWidget(self.tab1_centripetalLcdNumber)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.gridLayout_2.addLayout(self.verticalLayout_12, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tab1_engagePushButton = QtGui.QPushButton(self.wheelTab)
        self.tab1_engagePushButton.setObjectName(_fromUtf8("tab1_engagePushButton"))
        self.horizontalLayout.addWidget(self.tab1_engagePushButton)
        self.tab1_stopPushButton = QtGui.QPushButton(self.wheelTab)
        self.tab1_stopPushButton.setObjectName(_fromUtf8("tab1_stopPushButton"))
        self.horizontalLayout.addWidget(self.tab1_stopPushButton)
        self.verticalLayout_13.addLayout(self.horizontalLayout)
        self.tab1_recordPushButton = QtGui.QPushButton(self.wheelTab)
        self.tab1_recordPushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tab1_recordPushButton.setObjectName(_fromUtf8("tab1_recordPushButton"))
        self.verticalLayout_13.addWidget(self.tab1_recordPushButton)
        self.gridLayout.addLayout(self.verticalLayout_13, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.tabWidget.addTab(self.wheelTab, _fromUtf8(""))
        self.testTab = QtGui.QWidget()
        self.testTab.setObjectName(_fromUtf8("testTab"))
        self.verticalLayout_18 = QtGui.QVBoxLayout(self.testTab)
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.tab2_sizeLabel = QtGui.QLabel(self.testTab)
        self.tab2_sizeLabel.setObjectName(_fromUtf8("tab2_sizeLabel"))
        self.verticalLayout_16.addWidget(self.tab2_sizeLabel)
        self.tab2_sizeSpinBox = QtGui.QDoubleSpinBox(self.testTab)
        self.tab2_sizeSpinBox.setDecimals(0)
        self.tab2_sizeSpinBox.setMaximum(1000.0)
        self.tab2_sizeSpinBox.setProperty("value", 100.0)
        self.tab2_sizeSpinBox.setObjectName(_fromUtf8("tab2_sizeSpinBox"))
        self.verticalLayout_16.addWidget(self.tab2_sizeSpinBox)
        self.verticalLayout_18.addLayout(self.verticalLayout_16)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.tab2_thicknessLabel = QtGui.QLabel(self.testTab)
        self.tab2_thicknessLabel.setObjectName(_fromUtf8("tab2_thicknessLabel"))
        self.verticalLayout_14.addWidget(self.tab2_thicknessLabel)
        self.tab2_thicknessSpinBox = QtGui.QDoubleSpinBox(self.testTab)
        self.tab2_thicknessSpinBox.setDecimals(0)
        self.tab2_thicknessSpinBox.setMinimum(1.0)
        self.tab2_thicknessSpinBox.setProperty("value", 10.0)
        self.tab2_thicknessSpinBox.setObjectName(_fromUtf8("tab2_thicknessSpinBox"))
        self.verticalLayout_14.addWidget(self.tab2_thicknessSpinBox)
        self.verticalLayout_18.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.tab2_travelTimeLabel = QtGui.QLabel(self.testTab)
        self.tab2_travelTimeLabel.setObjectName(_fromUtf8("tab2_travelTimeLabel"))
        self.verticalLayout_15.addWidget(self.tab2_travelTimeLabel)
        self.tab2_travelTimeSpinBox = QtGui.QDoubleSpinBox(self.testTab)
        self.tab2_travelTimeSpinBox.setDecimals(1)
        self.tab2_travelTimeSpinBox.setMinimum(0.1)
        self.tab2_travelTimeSpinBox.setSingleStep(0.1)
        self.tab2_travelTimeSpinBox.setProperty("value", 5.0)
        self.tab2_travelTimeSpinBox.setObjectName(_fromUtf8("tab2_travelTimeSpinBox"))
        self.verticalLayout_15.addWidget(self.tab2_travelTimeSpinBox)
        self.verticalLayout_18.addLayout(self.verticalLayout_15)
        self.verticalLayout_17 = QtGui.QVBoxLayout()
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.tab2_opacityLabel = QtGui.QLabel(self.testTab)
        self.tab2_opacityLabel.setObjectName(_fromUtf8("tab2_opacityLabel"))
        self.verticalLayout_17.addWidget(self.tab2_opacityLabel)
        self.tab2_opacitySpinBox = QtGui.QDoubleSpinBox(self.testTab)
        self.tab2_opacitySpinBox.setDecimals(1)
        self.tab2_opacitySpinBox.setMaximum(1.0)
        self.tab2_opacitySpinBox.setSingleStep(0.1)
        self.tab2_opacitySpinBox.setProperty("value", 0.8)
        self.tab2_opacitySpinBox.setObjectName(_fromUtf8("tab2_opacitySpinBox"))
        self.verticalLayout_17.addWidget(self.tab2_opacitySpinBox)
        self.verticalLayout_18.addLayout(self.verticalLayout_17)
        spacerItem1 = QtGui.QSpacerItem(20, 304, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem1)
        self.tabWidget.addTab(self.testTab, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 27))
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
        self.actionReset = QtGui.QAction(MainWindow)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.menuFile.addAction(self.actionQuit)
        self.menuColor.addAction(self.actionInvert)
        self.menuColor.addAction(self.actionReset)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuColor.menuAction())
        self.tab1_scaleLabel.setBuddy(self.tab1_scaleSpinBox)
        self.tab1_thicknessLabel.setBuddy(self.tab1_thicknessSpinBox)
        self.tab1_speedLabel.setBuddy(self.tab1_speedSpinBox)
        self.tab1_distanceLabel.setBuddy(self.tab1_distanceSpinBox)
        self.tab1_diameterLabel.setBuddy(self.tab1_diameterSpinBox)
        self.tab1_densityLabel.setBuddy(self.tab1_densitySpinBox)
        self.tab1_viscositylabel.setBuddy(self.tab1_viscositySpinBox)
        self.tab2_sizeLabel.setBuddy(self.tab2_sizeSpinBox)
        self.tab2_thicknessLabel.setBuddy(self.tab2_thicknessSpinBox)
        self.tab2_travelTimeLabel.setBuddy(self.tab2_travelTimeSpinBox)
        self.tab2_opacityLabel.setBuddy(self.tab2_opacitySpinBox)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tab1_scaleSpinBox, self.tab1_thicknessSpinBox)
        MainWindow.setTabOrder(self.tab1_thicknessSpinBox, self.tab1_speedSpinBox)
        MainWindow.setTabOrder(self.tab1_speedSpinBox, self.tab1_distanceSpinBox)
        MainWindow.setTabOrder(self.tab1_distanceSpinBox, self.tab1_diameterSpinBox)
        MainWindow.setTabOrder(self.tab1_diameterSpinBox, self.tab1_densitySpinBox)
        MainWindow.setTabOrder(self.tab1_densitySpinBox, self.tab1_viscositySpinBox)
        MainWindow.setTabOrder(self.tab1_viscositySpinBox, self.tab1_engagePushButton)
        MainWindow.setTabOrder(self.tab1_engagePushButton, self.tab1_stopPushButton)
        MainWindow.setTabOrder(self.tab1_stopPushButton, self.tab1_recordPushButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "OET", None))
        self.tab1_scaleLabel.setText(_translate("MainWindow", "&Scale", None))
        self.tab1_scaleSpinBox.setToolTip(_translate("MainWindow", "Scale of the figure", None))
        self.tab1_thicknessLabel.setText(_translate("MainWindow", "&Thickness", None))
        self.tab1_thicknessSpinBox.setToolTip(_translate("MainWindow", "Thickness of the lines", None))
        self.tab1_speedLabel.setText(_translate("MainWindow", "&Angular velocity (rps)", None))
        self.tab1_speedSpinBox.setToolTip(_translate("MainWindow", "Angular velocity in revolutions per second", None))
        self.tab1_distanceLabel.setText(_translate("MainWindow", "&Distance (um)", None))
        self.tab1_distanceSpinBox.setToolTip(_translate("MainWindow", "The distance from the center of the wheel to the center of the bead", None))
        self.tab1_diameterLabel.setText(_translate("MainWindow", "Bead dia&meter (um)", None))
        self.tab1_diameterSpinBox.setToolTip(_translate("MainWindow", "Radius of the bead in microns", None))
        self.tab1_densityLabel.setText(_translate("MainWindow", "Bead de&nsity (g/cm3)", None))
        self.tab1_densitySpinBox.setToolTip(_translate("MainWindow", "The density of the bead in g/cm3", None))
        self.tab1_viscositylabel.setText(_translate("MainWindow", "Dynamic &viscosity (mPa s)", None))
        self.tab1_viscositySpinBox.setToolTip(_translate("MainWindow", "Dynamic viscosity of the solution in mPa s", None))
        self.tab1_linspeedLabel.setText(_translate("MainWindow", "Linear velocity (um/s)", None))
        self.tab1_linVelocityLcdNumber.setToolTip(_translate("MainWindow", "Linear velocity of the bead in microns per second", None))
        self.tab1_forcelabel.setText(_translate("MainWindow", "DEP (pN)", None))
        self.tab1_forceLcdNumber.setToolTip(_translate("MainWindow", "Dielectrophoretic force in pN", None))
        self.tab1_centripetalLabel.setText(_translate("MainWindow", "Centripetal force (pN)", None))
        self.tab1_centripetalLcdNumber.setToolTip(_translate("MainWindow", "Centripetal force in pN", None))
        self.tab1_engagePushButton.setToolTip(_translate("MainWindow", "Start the animation", None))
        self.tab1_engagePushButton.setText(_translate("MainWindow", "&Engage", None))
        self.tab1_stopPushButton.setToolTip(_translate("MainWindow", "Stop the animation", None))
        self.tab1_stopPushButton.setText(_translate("MainWindow", "Sto&p", None))
        self.tab1_recordPushButton.setToolTip(_translate("MainWindow", "Record the current parameters to file", None))
        self.tab1_recordPushButton.setText(_translate("MainWindow", "&Record", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wheelTab), _translate("MainWindow", "The Wheel", None))
        self.tab2_sizeLabel.setText(_translate("MainWindow", "&Size", None))
        self.tab2_thicknessLabel.setText(_translate("MainWindow", "&Thickness", None))
        self.tab2_travelTimeLabel.setText(_translate("MainWindow", "T&ravel time (s)", None))
        self.tab2_opacityLabel.setText(_translate("MainWindow", "Opacity", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.testTab), _translate("MainWindow", "Select and Move", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuColor.setTitle(_translate("MainWindow", "Tools", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionInvert.setText(_translate("MainWindow", "Invert", None))
        self.actionInvert.setShortcut(_translate("MainWindow", "Alt+I", None))
        self.actionReset.setText(_translate("MainWindow", "Reset", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calibrationWindow.ui'
#
# Created: Thu Jul 16 11:31:22 2015
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

class Ui_calibrationWindow(object):
    def setupUi(self, calibrationWindow):
        calibrationWindow.setObjectName(_fromUtf8("calibrationWindow"))
        calibrationWindow.setWindowModality(QtCore.Qt.NonModal)
        calibrationWindow.resize(645, 300)
        calibrationWindow.setWindowOpacity(0.8)
        self.gridLayout = QtGui.QGridLayout(calibrationWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.retranslateUi(calibrationWindow)
        QtCore.QMetaObject.connectSlotsByName(calibrationWindow)

    def retranslateUi(self, calibrationWindow):
        calibrationWindow.setWindowTitle(_translate("calibrationWindow", "Calibration", None))


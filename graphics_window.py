# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphics_window.ui'
#
# Created: Thu Jul  2 11:39:24 2015
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

class Ui_GraphicsWindow(object):
    def setupUi(self, GraphicsWindow):
        GraphicsWindow.setObjectName(_fromUtf8("GraphicsWindow"))
        GraphicsWindow.resize(877, 649)
        self.gridLayout = QtGui.QGridLayout(GraphicsWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = ViewPort(GraphicsWindow)
        self.graphicsView.setFrameShadow(QtGui.QFrame.Plain)
        self.graphicsView.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicsView.setTransformationAnchor(QtGui.QGraphicsView.AnchorViewCenter)
        self.graphicsView.setViewportUpdateMode(QtGui.QGraphicsView.MinimalViewportUpdate)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.retranslateUi(GraphicsWindow)
        QtCore.QMetaObject.connectSlotsByName(GraphicsWindow)

    def retranslateUi(self, GraphicsWindow):
        GraphicsWindow.setWindowTitle(_translate("GraphicsWindow", "Animation", None))

from viewport import ViewPort

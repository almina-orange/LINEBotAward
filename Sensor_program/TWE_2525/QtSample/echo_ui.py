# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'echo.ui'
#
# Created by: PyQt4 UI code generator 4.12
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

class Ui_Echo(object):
    def setupUi(self, Echo):
        Echo.setObjectName(_fromUtf8("Echo"))
        Echo.resize(250, 200)
        self.textBrowser = QtGui.QTextBrowser(Echo)
        self.textBrowser.setGeometry(QtCore.QRect(40, 90, 180, 79))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.horizontalLayoutWidget = QtGui.QWidget(Echo)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 180, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.inputEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.inputEdit.setObjectName(_fromUtf8("inputEdit"))
        self.horizontalLayout.addWidget(self.inputEdit)
        self.submitButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.submitButton.setObjectName(_fromUtf8("submitButton"))
        self.horizontalLayout.addWidget(self.submitButton)

        self.retranslateUi(Echo)
        QtCore.QMetaObject.connectSlotsByName(Echo)

    def retranslateUi(self, Echo):
        Echo.setWindowTitle(_translate("Echo", "Echo", None))
        self.submitButton.setText(_translate("Echo", "Submit", None))


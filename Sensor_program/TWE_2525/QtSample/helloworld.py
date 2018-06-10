# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\helloworld.ui'
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

class Ui_HelloWorld(object):
    def setupUi(self, HelloWorld):
        HelloWorld.setObjectName(_fromUtf8("HelloWorld"))
        HelloWorld.resize(400, 300)
        self.label = QtGui.QLabel(HelloWorld)
        self.label.setGeometry(QtCore.QRect(170, 140, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(HelloWorld)
        QtCore.QMetaObject.connectSlotsByName(HelloWorld)

    def retranslateUi(self, HelloWorld):
        HelloWorld.setWindowTitle(_translate("HelloWorld", "HelloWorld", None))
        self.label.setText(_translate("HelloWorld", "Hello World!", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HelloWorld = QtGui.QWidget()
    ui = Ui_HelloWorld()
    ui.setupUi(HelloWorld)
    HelloWorld.show()
    sys.exit(app.exec_())


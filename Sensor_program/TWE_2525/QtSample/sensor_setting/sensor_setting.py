# -*- coding: utf-8 -*-
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sensor_setting_ui

class MainWindow(QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__()
        self.initMainWindow()

    def initMainWindow(self):
        self.ui = sensor_setting_ui.Ui_SensorSetting()
        self.ui.setupUi(self)
        #self.ui.pushButton.clicked.connect(self.func)

    #def func(self):
        #fp = open('test.txt', 'w')
        #fp.write(str(self.ui.horizontalSlider.value()))
        #fp.close()
        #print 'clicked ok'
        #print self.ui.checkBox.isChecked()
        #print self.ui.checkBox_2.isChecked()
        #print self.ui.checkBox_3.isChecked()

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
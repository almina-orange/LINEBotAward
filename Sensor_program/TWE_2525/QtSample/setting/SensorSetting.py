# -*- coding: utf-8 -*-
import sys
import json
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import SensorSetting_ui

class App(QWidget):
    def __init__(self, parent = None):
        super(App, self).__init__()
        self.initApp()

    def initApp(self):
        self.ui = SensorSetting_ui.Ui_SensorSetting()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.updateSet)

        data = self.loadJson()

        # 各スライダーと入力フォーラムを接続
        self.connect(self.ui.horizontalSlider, SIGNAL('valueChanged(int)'), self.on_draw)
        self.connect(self.ui.horizontalSlider_2, SIGNAL('valueChanged(int)'), self.on_draw_2)
        self.connect(self.ui.horizontalSlider_3, SIGNAL('valueChanged(int)'), self.on_draw_3)
        self.connect(self.ui.horizontalSlider_4, SIGNAL('valueChanged(int)'), self.on_draw_4)
        self.connect(self.ui.horizontalSlider_5, SIGNAL('valueChanged(int)'), self.on_draw_5)
        self.connect(self.ui.horizontalSlider_6, SIGNAL('valueChanged(int)'), self.on_draw_6)

        # 各チェックボックスとスライダー・入力フォーラムを接続
        self.connect(self.ui.checkBox, SIGNAL('stateChanged(int)'), self.on_enabled)
        self.connect(self.ui.checkBox_2, SIGNAL('stateChanged(int)'), self.on_enabled_2)
        self.connect(self.ui.checkBox_3, SIGNAL('stateChanged(int)'), self.on_enabled_3)
        self.connect(self.ui.checkBox_4, SIGNAL('stateChanged(int)'), self.on_enabled_4)
        self.connect(self.ui.checkBox_5, SIGNAL('stateChanged(int)'), self.on_enabled_5)
        self.connect(self.ui.checkBox_6, SIGNAL('stateChanged(int)'), self.on_enabled_6)

        # 各入力フォーラムとスライダーを接続
        self.connect(self.ui.lineEdit, SIGNAL('textChanged(const QString&)'), self.on_changed)
        self.connect(self.ui.lineEdit_2, SIGNAL('textChanged(const QString&)'), self.on_changed_2)
        self.connect(self.ui.lineEdit_4, SIGNAL('textChanged(const QString&)'), self.on_changed_3)
        self.connect(self.ui.lineEdit_5, SIGNAL('textChanged(const QString&)'), self.on_changed_4)
        self.connect(self.ui.lineEdit_6, SIGNAL('textChanged(const QString&)'), self.on_changed_5)
        self.connect(self.ui.lineEdit_7, SIGNAL('textChanged(const QString&)'), self.on_changed_6)

        # 各スライダーの初期値を設定
        self.ui.horizontalSlider.setValue(data["sensor"]["No.1"]["x"])
        self.ui.horizontalSlider_2.setValue(data["sensor"]["No.1"]["y"])
        self.ui.horizontalSlider_3.setValue(data["sensor"]["No.1"]["z"])
        self.ui.horizontalSlider_4.setValue(data["sensor"]["No.2"]["x"])
        self.ui.horizontalSlider_5.setValue(data["sensor"]["No.2"]["y"])
        self.ui.horizontalSlider_6.setValue(data["sensor"]["No.2"]["z"])

    # okボタンクリック時の処理
    def updateSet(self):
        # create message box
        result = QMessageBox.question(self, '確認', "センサの設定ファイルを上書きします.\nよろしいですか?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if result == QMessageBox.Yes:
            self.dumpJson()

    # jsonファイルに設定を書き込む
    def dumpJson(self):
        setData = {
            "sensor":{
                "No.1":{
                    "x": self.ui.horizontalSlider.value(),
                    "y": self.ui.horizontalSlider_2.value(),
                    "z": self.ui.horizontalSlider_3.value()
                },
                "No.2":{
                    "x": self.ui.horizontalSlider_4.value(),
                    "y": self.ui.horizontalSlider_5.value(),
                    "z": self.ui.horizontalSlider_6.value()
                }
            }
        }

        fp = open('set.json', 'w')
        json.dump(setData, fp, indent = 4, sort_keys = True)
        fp.close()

        QMessageBox.information(self, '上書き完了', "センサの設定ファイルへの変更が完了しました.")

    def loadJson(self):
        fp = open('set.json', 'r')
        setData = json.load(fp)
        fp.close()

        return setData

    # 入力フォーラムとスライダー接続用メソッド
    def on_changed(self):
        if len(self.ui.lineEdit.text()) > 0 and int(self.ui.lineEdit.text()) <= 200:
            self.ui.horizontalSlider.setValue(int(self.ui.lineEdit.text()))
        elif len(self.ui.lineEdit.text()) <= 0:
            self.ui.horizontalSlider.setValue(0)
        else:
            self.ui.horizontalSlider.setValue(200)
    def on_changed_2(self):
        if len(self.ui.lineEdit_2.text()) > 0 and int(self.ui.lineEdit_2.text()) <= 200:
            self.ui.horizontalSlider_2.setValue(int(self.ui.lineEdit_2.text()))
        elif len(self.ui.lineEdit_2.text()) <= 0:
            self.ui.horizontalSlider_2.setValue(0)
        else:
            self.ui.horizontalSlider_2.setValue(200)
    def on_changed_3(self):
        if len(self.ui.lineEdit_4.text()) > 0 and int(self.ui.lineEdit_4.text()) <= 200:
            self.ui.horizontalSlider_3.setValue(int(self.ui.lineEdit_4.text()))
        elif len(self.ui.lineEdit_4.text()) <= 0:
            self.ui.horizontalSlider_3.setValue(0)
        else:
            self.ui.horizontalSlider_3.setValue(200)
    def on_changed_4(self):
        if len(self.ui.lineEdit_5.text()) > 0 and int(self.ui.lineEdit_5.text()) <= 200:
            self.ui.horizontalSlider_4.setValue(int(self.ui.lineEdit_5.text()))
        elif len(self.ui.lineEdit_5.text()) <= 0:
            self.ui.horizontalSlider_4.setValue(0)
        else:
            self.ui.horizontalSlider_4.setValue(200)
    def on_changed_5(self):
        if len(self.ui.lineEdit_6.text()) > 0 and int(self.ui.lineEdit_6.text()) <= 200:
            self.ui.horizontalSlider_5.setValue(int(self.ui.lineEdit_6.text()))
        elif len(self.ui.lineEdit_6.text()) <= 0:
            self.ui.horizontalSlider_5.setValue(0)
        else:
            self.ui.horizontalSlider_5.setValue(200)
    def on_changed_6(self):
        if len(self.ui.lineEdit_7.text()) > 0 and int(self.ui.lineEdit_7.text()) <= 200:
            self.ui.horizontalSlider_6.setValue(int(self.ui.lineEdit_7.text()))
        elif len(self.ui.lineEdit_7.text()) <= 0:
            self.ui.horizontalSlider_6.setValue(0)
        else:
            self.ui.horizontalSlider_6.setValue(200)

    # スライダーと入力フォーラム接続用メソッド
    def on_draw(self):
        self.ui.lineEdit.setText(str(self.ui.horizontalSlider.value()))
    def on_draw_2(self):
        self.ui.lineEdit_2.setText(str(self.ui.horizontalSlider_2.value()))
    def on_draw_3(self):
        self.ui.lineEdit_4.setText(str(self.ui.horizontalSlider_3.value()))
    def on_draw_4(self):
        self.ui.lineEdit_5.setText(str(self.ui.horizontalSlider_4.value()))
    def on_draw_5(self):
        self.ui.lineEdit_6.setText(str(self.ui.horizontalSlider_5.value()))
    def on_draw_6(self):
        self.ui.lineEdit_7.setText(str(self.ui.horizontalSlider_6.value()))

    # チェックボックスとスライダー・入力フォーラム接続用メソッド
    def on_enabled(self):
        self.ui.horizontalSlider.setValue(0)
        self.ui.horizontalSlider.setEnabled(self.ui.checkBox.isChecked())
        self.ui.lineEdit.setEnabled(self.ui.checkBox.isChecked())
    def on_enabled_2(self):
        self.ui.horizontalSlider_2.setValue(0)
        self.ui.horizontalSlider_2.setEnabled(self.ui.checkBox_2.isChecked())
        self.ui.lineEdit_2.setEnabled(self.ui.checkBox_2.isChecked())
    def on_enabled_3(self):
        self.ui.horizontalSlider_3.setValue(0)
        self.ui.horizontalSlider_3.setEnabled(self.ui.checkBox_3.isChecked())
        self.ui.lineEdit_4.setEnabled(self.ui.checkBox_3.isChecked())
    def on_enabled_4(self):
        self.ui.horizontalSlider_4.setValue(0)
        self.ui.horizontalSlider_4.setEnabled(self.ui.checkBox_4.isChecked())
        self.ui.lineEdit_5.setEnabled(self.ui.checkBox_4.isChecked())
    def on_enabled_5(self):
        self.ui.horizontalSlider_5.setValue(0)
        self.ui.horizontalSlider_5.setEnabled(self.ui.checkBox_5.isChecked())
        self.ui.lineEdit_6.setEnabled(self.ui.checkBox_5.isChecked())
    def on_enabled_6(self):
        self.ui.horizontalSlider_6.setValue(0)
        self.ui.horizontalSlider_6.setEnabled(self.ui.checkBox_6.isChecked())
        self.ui.lineEdit_7.setEnabled(self.ui.checkBox_6.isChecked())

def main():
    app = QApplication(sys.argv)
    mainApp = App()
    mainApp.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
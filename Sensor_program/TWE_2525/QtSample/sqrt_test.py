# coding: utf-8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

def factorial(n):
	if n < 0:
		return -1
	elif n == 0:
		return 1
	else:
		return n * factorial(n - 1)

class UI(QWidget):
	def __init__(self, parent = None):
		super(UI, self).__init__(parent)
		self.initUI()

	def initUI(self):
		# 入出力用のフォーラム
		self.inputLine = QLineEdit()
		self.outputLine = QLineEdit()
		self.outputLine.setReadOnly(True)

		# calcボタン
		self.calcButton = QPushButton("&Calc")
		self.calcButton.clicked.connect(self.calc)

		# 入出力部分レイアウト
		lineLayout = QGridLayout()
		lineLayout.addWidget(QLabel('num'), 0, 0)
		lineLayout.addWidget(self.inputLine, 0, 1)
		lineLayout.addWidget(QLabel('result'), 1, 0)
		lineLayout.addWidget(self.outputLine, 1, 1)

		# ボタンレイアウト
		buttonLayout = QVBoxLayout()
		buttonLayout.addWidget(self.calcButton)

		# 全体レイアウト
		mainLayout = QHBoxLayout()
		mainLayout.addLayout(lineLayout)
		mainLayout.addLayout(buttonLayout)
		self.setLayout(mainLayout)

		self.setWindowTitle("Factorial")

	def calc(self):
		n = int(self.inputLine.text())
		r = factorial(n)
		self.outputLine.setText(str(r))

def main():
	app = QApplication(sys.argv)
	ui = UI()
	ui.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
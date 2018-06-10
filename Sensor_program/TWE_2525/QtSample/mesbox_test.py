# coding: utf-8
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		self.initUI()

	def initUI(self):
		# create message box
		result = QMessageBox.question(self, 'Message', u"Do you get used to PyQt?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		if result == QMessageBox.Yes:
			print "Selected Yes."
		else:
			print "Selected No."

		# warning message box
		QMessageBox.warning(self, 'Message', u"something wrong.")

		# information message box
		QMessageBox.information(self, 'Message', "Please contact at hoge@gmail.com")

		# error message box
		QMessageBox.critical(self, 'Message', "Oh my god.")

		# about box
		QMessageBox.about(self, 'About', "Ver1.0")

		self.show()

def main():
	app = QApplication(sys.argv)
	ui = UI()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
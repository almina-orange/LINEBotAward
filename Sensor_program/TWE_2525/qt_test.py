# coding: utf-8
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import datetime

class Example(QMainWindow):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		# create "Exit" Button in MenuBar
		exitGUI = QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton)
		exitAction = QAction(exitGUI, '&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(qApp.quit)

		# create "Exit" Button in MenuBar
		qtInfoGUI = QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton)
		qtInfoAction = QAction(qtInfoGUI, '&AboutQt', self)
		qtInfoAction.setShortcut('Ctrl+I')
		qtInfoAction.setStatusTip('Show Qt info')
		qtInfoAction.triggered.connect(qApp.aboutQt)

		# create MenuBar
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&Info')
		fileMenu.addAction(qtInfoAction)
		fileMenu.addAction(exitAction)
		menubar.setNativeMenuBar(False)

		# show Timer
		timer = QTimer(self)
		timer.timeout.connect(self.time_draw)
		timer.start(1000)

		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('Menubar')
		self.show()

	def time_draw(self):
		d = datetime.datetime.today()
		daystr = d.strftime("%Y-%m-%d %H:%M:%S")
		self.statusBar().showMessage(daystr)

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
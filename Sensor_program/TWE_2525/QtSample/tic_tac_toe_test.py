# coding: utf-8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class TicTacToe(QGraphicsItem):
	def __init__(self):
		super(TicTacToe, self).__init__()
		self.initT3()

	def initT3(self):
		self.board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
		self.o = 0
		self.x = 1
		self.turn = self.o 	# 描画のターンフラグ(o / x)

	def reset(self):
		for y in range(3):
			for x in range(3):
				self.board[y][x] = -1
		self.turn = self.o
		self.update()

	# マスの選択処理
	def select(self, x, y):
		if x < 0 or y < 0 or x >= 3 or y >= 3:
			return
		if self.board[y][x] == -1:
			self.board[y][x] = self.turn
			self.turn = 1 - self.turn	# ターンの切り替え

	# 描画処理
	def paint(self, painter, option, widget):
		# マス目の描画
		painter.setPen(Qt.black)
		painter.drawLine(  0, 100, 300, 100)
		painter.drawLine(  0, 200, 300, 200)
		painter.drawLine(100,   0, 100, 300)
		painter.drawLine(200,   0, 200, 300)

		for y in range(3):
			for x in range(3):
				# 丸の描画
				if self.board[y][x] == self.o:
					painter.setPen(Qt.red)
					painter.drawEllipse(QPointF(50 + x * 100, 50 + y * 100), 30, 30)
				# バツの描画
				elif self.board[y][x] == self.x:
					painter.setPen(Qt.blue)
					painter.drawLine(20 + x * 100, 20 + y * 100, 80 + x * 100, 80 + y * 100)
					painter.drawLine(20 + x * 100, 80 + y * 100, 80 + x * 100, 20 + y * 100)

	def boundingRect(self):
		return QRectF(0, 0, 300, 300)

	# クリック時のイベント処理
	def mousePressEvent(self, event):
		# クリック位置を取得 -> マス目の選択
		pos = event.pos()
		self.select(int(pos.x() / 100), int(pos.y() / 100))
		self.update()
		super(TicTacToe, self).mousePressEvent(event)

class MainWindow(QGraphicsView):
	def __init__(self):
		super(MainWindow, self).__init__()
		scene = QGraphicsScene(self)
		self.tic_tac_toe = TicTacToe()

		scene.addItem(self.tic_tac_toe)
		scene.setSceneRect(0, 0, 300, 300)
		self.setScene(scene)
		self.setCacheMode(QGraphicsView.CacheBackground)
		self.setWindowTitle("Tic Tac Toe")

	def keyPressEvent(self, event):
		key = event.key()
		if key == Qt.Key_R:
			self.tic_tac_toe.reset()
		super(MainWindow, self).keyPressEvent(event)

def main():
	app = QApplication(sys.argv)
	mainWindow = MainWindow()
	mainWindow.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

	def __init__(self):
		super().__init__()

		self.title = 'Tarot - Menu principal'

		self.left   = 100
		self.top    = 100
		self.width  = 640
		self.height = 480

		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		button = QPushButton('Nouvelle partie', self)
		button.setToolTip('Cliquez ici pour démarrer une nouvelle partie')
		button.resize(100, 100)
		button.move(100, 100)
		button.clicked.connect(self.on_click)

		self.show()

	@pyqtSlot()
	def on_click(self):
		print('Nouvelle partie cliquée')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
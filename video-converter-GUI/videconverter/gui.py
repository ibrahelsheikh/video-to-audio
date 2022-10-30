# create simple GUI for vide converter BUILDING on QT6

import PyQt6
from PyQt5.QtWidgets import QDesktopWidget
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QProgressBar, QLineEdit
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QSize, Qt
import sys


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Video Converter'
        self.left = 500
        self.top = 200
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # fixed size
        self.setFixedSize(640, 480)

        # Create a button in the window
        self.button = QPushButton('Open Video', self)
        self.button.move(20, 440)
        self.button.clicked.connect(self.on_click)

        # create convert button
        self.button = QPushButton('Convert', self)
        self.button.move(120, 440)
        self.button.clicked.connect(self.convert)

        # create text box
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 480)
        self.textbox.resize(280, 40)

        self.show()

    def pri(self):
        pass

    # create convert function
    def convert(self):
        pass

    # create convert progress bar
    def progress(self):
        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.button = QPushButton('Start', self)
        self.button.move(200, 120)
        self.button.clicked.connect(self.doAction)

        self.show()

    def on_click(self):
        # open file dialog
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Video files (*.mp4 *.avi *.mkv *.flv *.wmv *.mpg *.mpeg *.3gp *.webm *.vob *.m4v *.rmvb *.rm *.asf *.swf *.m2ts *.mts *.ts *.ogv *.ogg *.mxf *.dv *.dvr-ms *.amv *.qt *.f4v *.flv *.f4p *.f4a *.f4b)")
        # display image
        self.label.setPixmap(QPixmap(file_name[0]))
        self.resize(self.label.pixmap().size())

    # initilize int postion of the window
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



# call app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())


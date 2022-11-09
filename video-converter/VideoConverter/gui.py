# create simple GUI for vide converter BUILDING on QT6

import sys

from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLineEdit, QLabel

global process


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
        self.setFixedSize(610, 375)

        # line
        self.line = QLineEdit(self)
        self.line.move(20, 20)
        self.line.resize(280, 25)

        # open video button
        self.button = QPushButton('Open Video', self)
        self.button.move(330, 20)
        self.button.clicked.connect(self.on_click)

        # open folder button
        self.button = QPushButton('Open Folder', self)
        self.button.move(420, 20)
        self.button.clicked.connect(self.open_folder)

        # create convert button
        self.button = QPushButton('Convert', self)
        self.button.move(510, 20)
        self.button.clicked.connect(self.convert)

        # create labal

        self.label = QLabel("Python GUI Development - Geekscoders.com", self)
        #self.label.setText("New Text is Here")
        self.label.move(20,100)
        self.setFont(QFont("Sanserif"))
        self.label.setStyleSheet('color:red')



        self.show()

    # create convert function


    def convert(self):

        pass

    def on_click(self):
        # open file dialog
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',
                                                "Video files (*.mp4 *.avi *.mkv *.flv *.wmv *.mpg *.mpeg *.3gp *.webm *.vob *.m4v *.rmvb *.rm *.asf *.swf *.m2ts *.mts *.ts *.ogv *.ogg *.mxf *.dv *.dvr-ms *.amv *.qt *.f4v *.flv *.f4p *.f4a *.f4b)")
        # display image
        self.label.setPixmap(QPixmap(file_name[0]))
        self.resize(self.label.pixmap().size())

    def open_folder(self):
        # open folder dialog
        folder_name = QFileDialog.getExistingDirectory(self, 'Open folder', 'c:\\')
        # display folder name
        self.label.setText(folder_name)

    # initialize int position of the window
    def center(self):  # TODO: center window
        pass


# call app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())

# TODO find good icon for app
# TODO : change the icon of the window
# TODO : center the window by using windows api

# TODO : add a label to show all process


# TODO : build function to get path from textbox

# TODO : ren all project by cmd
# TODO : add a label to show all process

#TODO : clear textbox


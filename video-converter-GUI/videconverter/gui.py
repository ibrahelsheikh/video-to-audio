# create simple GUI for vide converter BUILDING on QT6

import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLineEdit


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

        # open video button
        self.button = QPushButton('Open Video', self)
        self.button.move(20, 440)
        self.button.clicked.connect(self.on_click)

        # open folder button
        self.button = QPushButton('Open Folder', self)
        self.button.move(120, 440)
        self.button.clicked.connect(self.open_folder)

        # create convert button
        self.button = QPushButton('Convert', self)
        self.button.move(220, 440)
        self.button.clicked.connect(self.convert)


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

    # initilize int postion of the window
    def center(self) :                                   #TODO: center window
        pass


# call app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())

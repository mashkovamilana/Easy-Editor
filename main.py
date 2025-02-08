import os
from PIL import Image, ImageQt
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGroupBox, QVBoxLayout, QHBoxLayout, QTextEdit, \
    QMessageBox, QListWidget, QFileDialog

workdir = ' '

app = QApplication([])
main_win = QWidget()
main_win.setFixedSize(800, 600)

main_win.setWindowTitle('Easy Editor')
picture_list_widget = QListWidget()
picture = QLabel('картинка')
left_button = QPushButton('Лево')
right_button = QPushButton('Право')
mirror_button = QPushButton('Зеркало')
sharpness_button = QPushButton('Резкость')
black_and_white_button = QPushButton('Ч/Б')
folder_button = QPushButton('Папка')

layout_main = QHBoxLayout()
layout3 = QHBoxLayout()
layout2 = QVBoxLayout()
layout4 = QVBoxLayout()

layout2.addWidget(folder_button)
layout2.addWidget(picture_list_widget)
layout4.addWidget(picture)
layout3.addWidget(left_button)
layout3.addWidget(right_button)
layout3.addWidget(mirror_button)
layout3.addWidget(sharpness_button)
layout3.addWidget(black_and_white_button)

layout_main.addLayout(layout2)
layout4.addLayout(layout3)
layout_main.addLayout(layout4)
main_win.setLayout(layout_main)


class Image_processor():

    def __init__(self):
        self.filename = None
        self.image = None
        self.pixmap = None
        self.image_path = None

    def load_image(self, filename):
        self.filename = filename
        self.image_path = os.path.join(workdir, filename)
        self.image = Image.open(self.image_path)
        #self.pixmap = QPixmap(self.image_path)
        image_qt = ImageQt.ImageQt(self.image)
        self.pixmap = QPixmap.fromImage(image_qt)
        width, height = picture.width(), picture.height()
        self.pixmap = self.pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)

    def show_image(self):
        picture.setPixmap(self.pixmap)

image_processor = Image_processor()

def open_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def filter(files, extensions):
    result = []
    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                result.append(filename)
    return result


def show_filenames_list():
    open_workdir()
    files = os.listdir(workdir)
    extensions = ['.jpg', '.jpeg', '.png', '.gif']
    files = filter(files, extensions)
    picture_list_widget.clear()
    picture_list_widget.addItems(files)

def show_picture():
    filename = picture_list_widget.selectedItems()[0].text()
    image_processor.load_image(filename)
    image_processor.show_image()

picture_list_widget.itemClicked.connect(show_picture)
folder_button.clicked.connect(show_filenames_list)

main_win.show()
app.exec()

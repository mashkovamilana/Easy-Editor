import os
from PIL import Image, ImageQt, ImageFilter
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
picture = QLabel('')
left_button = QPushButton('Left')
right_button = QPushButton('Right')
mirror_button = QPushButton('Mirror')
sharpness_button = QPushButton('Sharpness')
detail_button = QPushButton('Detail')
contour_button = QPushButton('Contour')
emboss_button = QPushButton('Emboss')
edge_enhance_button = QPushButton('Edge enhance')
save_picture_button = QPushButton('Save')
save_picture_button.setStyleSheet('QPushButton {background-color: green; color: white;}')
black_and_white_button = QPushButton('B/W')
blur_button = QPushButton('Blur')
folder_button = QPushButton('Folder')

layout_main = QHBoxLayout()
layout3 = QHBoxLayout()
layout5 = QHBoxLayout()
layout2 = QVBoxLayout()
layout4 = QVBoxLayout()

layout2.addWidget(folder_button)
layout2.addWidget(picture_list_widget)
layout4.addWidget(picture)
layout3.addWidget(save_picture_button)
layout3.addWidget(left_button)
layout5.addWidget(blur_button)
layout5.addWidget(detail_button)
layout5.addWidget(contour_button)
layout5.addWidget(emboss_button)
layout5.addWidget(edge_enhance_button)
layout3.addWidget(right_button)
layout3.addWidget(mirror_button)
layout3.addWidget(sharpness_button)
layout3.addWidget(black_and_white_button)

layout_main.addLayout(layout2)
layout4.addLayout(layout5)
layout4.addLayout(layout3)
layout_main.addLayout(layout4)
main_win.setLayout(layout_main)




class Image_processor():

    def __init__(self):
        self.filename = None
        self.image = None
        self.pixmap = None
        self.image_path = None


    def reload_image(self):
        image_qt = ImageQt.ImageQt(self.image)
        self.pixmap = QPixmap.fromImage(image_qt)
        width, height = picture.width(), picture.height()
        self.pixmap = self.pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)


    def load_image(self, filename):
        self.filename = filename
        self.image_path = os.path.join(workdir, filename)
        self.image = Image.open(self.image_path)
        self.reload_image()

    def show_image(self):
        picture.setPixmap(self.pixmap)


    def greyscale(self):
        if self.image is None:
            error_popup = QMessageBox()
            error_popup.setText('Select a picture to apply the effect to it')
            error_popup.setWindowTitle('Error')
            error_popup.exec()
        else:
            self.image = self.image.convert('L')
            self.reload_image()
            self.show_image()


    def mirror(self):
        if self.image is None:
            error_popup = QMessageBox()
            error_popup.setText('Select a picture to apply the effect to it')
            error_popup.setWindowTitle('Error')
            error_popup.exec()
        else:
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.reload_image()
            self.show_image()


    def left(self):
        if self.image is None:
            error_popup = QMessageBox()
            error_popup.setText('Select a picture to apply the effect to it')
            error_popup.setWindowTitle('Error')
            error_popup.exec()
        else:
            self.image = self.image.transpose(Image.ROTATE_90)
            self.reload_image()
            self.show_image()


    def right(self):
        if self.image is None:
            error_popup = QMessageBox()
            error_popup.setText('Select a picture to apply the effect to it')
            error_popup.setWindowTitle('Error')
            error_popup.exec()
        else:
            self.image = self.image.transpose(Image.ROTATE_270)
            self.reload_image()
            self.show_image()


    def sharpness(self):
        if self.image is None:
            error_popup = QMessageBox()
            error_popup.setText('Select a picture to apply the effect to it')
            error_popup.setWindowTitle('Error')
            error_popup.exec()
        else:
            self.image = self.image.filter(ImageFilter.SHARPEN)
            self.reload_image()
            self.show_image()


    def blur(self):
        if self.image is None:
            error_popup = QMessageBox()
            error_popup.setText('Select a picture to apply the effect to it')
            error_popup.setWindowTitle('Error')
            error_popup.exec()
        else:
            self.image = self.image.filter(ImageFilter.BLUR)
            self.reload_image()
            self.show_image()


    def detail(self):
        if self.image is None:
            error_popup = QMessageBox()
            error_popup.setText('Select a picture to apply the effect to it')
            error_popup.setWindowTitle('Error')
            error_popup.exec()
        else:
            self.image = self.image.filter(ImageFilter.DETAIL)
            self.reload_image()
            self.show_image()


    def contour(self):
        if self.image is None:
            error_popup = QMessageBox()
            error_popup.setText('Select a picture to apply the effect to it')
            error_popup.setWindowTitle('Error')
            error_popup.exec()
        else:
            self.image = self.image.filter(ImageFilter.CONTOUR)
            self.reload_image()
            self.show_image()


    def emboss(self):
        if self.image is None:
            error_popup = QMessageBox()
            error_popup.setText('Select a picture to apply the effect to it')
            error_popup.setWindowTitle('Error')
            error_popup.exec()
        else:
            self.image = self.image.filter(ImageFilter.EMBOSS)
            self.reload_image()
            self.show_image()


    def edge_enhance(self):
        if self.image is None:
            error_popup = QMessageBox()
            error_popup.setText('Select a picture to apply the effect to it')
            error_popup.setWindowTitle('Error')
            error_popup.exec()
        else:
            self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
            self.reload_image()
            self.show_image()


    def save_picture(self):
        if self.image is None:
            error_popup = QMessageBox()
            error_popup.setText('Select a picture to save it')
            error_popup.setWindowTitle('Error')
            error_popup.exec()
        else:
            path, _ =  QFileDialog.getSaveFileName(
                    main_win, "SaveFileName", "",
                    "Image Files (*.png *.jpg *.jpeg *.bmp)",)
            self.image.save(path)


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



save_picture_button.clicked.connect(image_processor.save_picture)
edge_enhance_button.clicked.connect(image_processor.edge_enhance)
emboss_button.clicked.connect(image_processor.emboss)
contour_button.clicked.connect(image_processor.contour)
detail_button.clicked.connect(image_processor.detail)
blur_button.clicked.connect(image_processor.blur)
right_button.clicked.connect(image_processor.right)
sharpness_button.clicked.connect(image_processor.sharpness)
left_button.clicked.connect(image_processor.left)
mirror_button.clicked.connect(image_processor.mirror)
black_and_white_button.clicked.connect(image_processor.greyscale)
picture_list_widget.itemClicked.connect(show_picture)
folder_button.clicked.connect(show_filenames_list)

main_win.show()
app.exec()

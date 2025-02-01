from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGroupBox, QVBoxLayout, QHBoxLayout, QTextEdit, QMessageBox, QListWidget
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

main_win.show()
app.exec()
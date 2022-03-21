from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidget, QFileDialog
import os

def provodnik():
    workdir = QFileDialog.getExistingDirectory()
    filenames = os.listdir(workdir)
    extensions = ['jpg', 'png', 'bmp', 'svg', 'eps']
    res = []
    for filename in filenames:
        for extension in extensions:
            if filename.endswith(extension):
                res.append(filename)
    pictureList.clear()
    pictureList.addItems(res)
    

easyEdit = QApplication([])
window = QWidget()

folderLayout = QVBoxLayout()
editLayout = QVBoxLayout()
mainLayout = QHBoxLayout()

folderButton = QPushButton('Папка')
folderLayout.addWidget(folderButton)

pictureList = QListWidget()
folderLayout.addWidget(pictureList)

pictureLabel = QLabel('please.png')
editLayout.addWidget(pictureLabel)

buttonLayout = QHBoxLayout()
leftButton = QPushButton()
rightButton = QPushButton()
mirrorButton = QPushButton()
sharpButton = QPushButton()
wbButton = QPushButton()

buttonLayout.addWidget(leftButton)
buttonLayout.addWidget(rightButton)
buttonLayout.addWidget(mirrorButton)
buttonLayout.addWidget(sharpButton)
buttonLayout.addWidget(wbButton)

editLayout.addLayout(buttonLayout)

folderButton.clicked.connect(provodnik)

mainLayout.addLayout(folderLayout, stretch = 1)
mainLayout.addLayout(editLayout, stretch = 5)
window.setLayout(mainLayout)

window.show()
easyEdit.exec_()
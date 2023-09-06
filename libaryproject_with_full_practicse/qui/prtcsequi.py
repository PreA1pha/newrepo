import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
def sclicked():
    print("clicked")
def Window():

    man= QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(500,500,600,600)
    win.setWindowTitle("uygulama")
    menu = win.menuBar()

    label= QtWidgets.QLabel(win)#maijn windowda yer alan bir yazı
    label.setText("bu bir yazı")
    label.move(100,100)#konum

    button=QtWidgets.QPushButton(win)#main windowda bulunan bi button
    button.setText("bu bir button")
    button.clicked.connect(sclicked)#when cillecek arekete geçir


    win.show()
    sys.exit(man.exec())

Window()
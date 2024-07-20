from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from screen2 import Ui_Form

class Ui_MainWindow(object):
    def openWindow(self):
        genre = self.DropDown.currentText()
        books = self.get_books_by_genre(genre)
        self.window=QtWidgets.QWidget()
        self.ui=Ui_Form()
        self.ui.setupUi(self.window, books)  
        self.window.show()

    def get_books_by_genre(self, genre):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mySQL@3131",
            database="books"
        )
        cursor = connection.cursor()

        if genre == 'Fiction':
            cursor.execute("SELECT * FROM fiction")
        elif genre == 'Mystery':
            cursor.execute("SELECT * FROM mystery")
        elif genre == 'Romance':
            cursor.execute("SELECT * FROM romance")
        elif genre == 'Sci-Fi':
            cursor.execute("SELECT * FROM science_fiction")
        elif genre == 'Horror':
            cursor.execute("SELECT * FROM horror")

        books = cursor.fetchall()  

        cursor.close()
        connection.close()

        return books

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("BookaMend")
        MainWindow.resize(509, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(70, 60, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.Genre = QtWidgets.QLabel(self.centralwidget)
        self.Genre.setGeometry(QtCore.QRect(80, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Genre.setFont(font)
        self.Genre.setObjectName("Genre")
        self.DropDown = QtWidgets.QComboBox(self.centralwidget)
        self.DropDown.setGeometry(QtCore.QRect(160, 210, 271, 31))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.DropDown.setFont(font)
        self.DropDown.setObjectName("DropDown")
        self.DropDown.addItem("")
        self.DropDown.addItem("")
        self.DropDown.addItem("")
        self.DropDown.addItem("")
        self.DropDown.addItem("")
        self.OK = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.openWindow())
        self.OK.setGeometry(QtCore.QRect(220, 300, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.OK.setFont(font)
        self.OK.setObjectName("OK")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("BookaMend", "BookaMend"))
        self.Title.setText(_translate("BookaMend", "Book \'a\' Mend"))
        self.Genre.setText(_translate("BookaMend", "Genre :"))
        self.DropDown.setItemText(0, _translate("BookaMend", "Fiction"))
        self.DropDown.setItemText(1, _translate("BookaMend", "Mystery"))
        self.DropDown.setItemText(2, _translate("BookaMend", "Romance"))
        self.DropDown.setItemText(3, _translate("BookaMend", "Sci-Fi"))
        self.DropDown.setItemText(4, _translate("BookaMend", "Horror"))
        self.OK.setText(_translate("BookaMend", "OK"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

BOOK’A’MEND CODE
MMAIN WINDOW CODE:
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


SCREEN 2 CODE:
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


MYSQL QUERIES:
-- CREATE DATABASE books;

USE books;

-- DROP TABLE fiction;

CREATE TABLE fiction(
        SNo INT,
        Title VARCHAR(255),
        Author VARCHAR(255),
        Year_of_Publication INT       
);

INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (1, 'To Kill a Mockingbird', 'Harper Lee', 1960);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (2, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (3, '1984', 'George Orwell', 1949);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (4, 'Pride and Prejudice', 'Jane Austen', 1813);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (5, 'The Catcher in the Rye', 'J.D. Salinger', 1951);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (6, 'The Hobbit', 'J.R.R. Tolkien', 1937);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (7, 'The Lord of the Rings', 'J.R.R. Tolkien', 1954);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (8, 'Animal Farm', 'George Orwell', 1945);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (9, 'The Chronicles of Narnia', 'C.S. Lewis', 1950);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (10, 'Brave New World', 'Aldous Huxley', 1932);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (11, 'The Hunger Games', 'Suzanne Collins', 2008);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (12, 'The Da Vinci Code', 'Dan Brown', 2003);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (13, 'Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', 1997);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (14, 'Gone with the Wind', 'Margaret Mitchell', 1936);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (15, 'The Kite Runner', 'Khaled Hosseini', 2003);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (16, 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 2005);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (17, 'The Fault in Our Stars', 'John Green', 2012);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (18, 'The Road', 'Cormac McCarthy', 2006);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (19, 'The Alchemist', 'Paulo Coelho', 1988);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (20, 'Twilight', 'Stephenie Meyer', 2005);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (21, 'Catch-22', 'Joseph Heller', 1961);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (22, 'The Bell Jar', 'Sylvia Plath', 1963);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (23, 'The Hitchhiker''s Guide to the Galaxy', 'Douglas Adams', 1979);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (24, 'The Secret History', 'Donna Tartt', 1992);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (25, 'Watership Down', 'Richard Adams', 1972);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (26, 'Middlemarch', 'George Eliot', 1871);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (27, 'Les Misérables', 'Victor Hugo', 1862);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (28, 'Ulysses', 'James Joyce', 1922);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (29, 'Dracula', 'Bram Stoker', 1897);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (30, 'Frankenstein', 'Mary Shelley', 1818);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (31, 'The Shining', 'Stephen King', 1977);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (32, 'The Count of Monte Cristo', 'Alexandre Dumas', 1844);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (33, 'The Three Musketeers', 'Alexandre Dumas', 1844);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (34, 'The Sound and the Fury', 'William Faulkner', 1929);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (35, 'Lolita', 'Vladimir Nabokov', 1955);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (36, 'Heart of Darkness', 'Joseph Conrad', 1899);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (37, 'The Scarlet Letter', 'Nathaniel Hawthorne', 1850);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (38, 'The Picture of Dorian Gray', 'Oscar Wilde', 1890);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (39, 'The Adventures of Huckleberry Finn', 'Mark Twain', 1884);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (40, 'The Adventures of Tom Sawyer', 'Mark Twain', 1876);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (41, 'Alice''s Adventures in Wonderland', 'Lewis Carroll', 1865);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (42, 'Moby-Dick', 'Herman Melville', 1851);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (43, 'Emma', 'Jane Austen', 1815);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (44, 'Crime and Punishment', 'Fyodor Dostoevsky', 1866);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (45, 'War and Peace', 'Leo Tolstoy', 1869);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (46, 'The Odyssey', 'Homer', 800);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (47, 'The Iliad', 'Homer', 800);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (48, 'Anna Karenina', 'Leo Tolstoy', 1878);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (49, 'Wuthering Heights', 'Emily Bronte', 1847);
INSERT INTO fiction (SNo, Title, Author, Year_of_Publication) VALUES (50, 'Don Quixote', 'Miguel de Cervantes', 1605);

-- DROP TABLE mystery;

CREATE TABLE mystery(
        SNo INT,
        Title VARCHAR(255),
        Author VARCHAR(255),
        Year_of_Publication INT        
);

INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (1, 'The Adventures of Sherlock Holmes', 'Arthur Conan Doyle', 1892);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (2, 'And Then There Were None', 'Agatha Christie', 1939);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (3, 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 2005);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (4, 'The Da Vinci Code', 'Dan Brown', 2003);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (5, 'The Girl on the Train', 'Paula Hawkins', 2015);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (6, 'In the Woods', 'Tana French', 2007);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (7, 'Sharp Objects', 'Gillian Flynn', 2006);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (8, 'The Cuckoo''s Calling', 'Robert Galbraith (J.K. Rowling)', 2013);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (9, 'Big Little Lies', 'Liane Moriarty', 2014);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (10, 'The Hound of the Baskervilles', 'Arthur Conan Doyle', 1902);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (11, 'Murder on the Orient Express', 'Agatha Christie', 1934);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (12, 'The Secret History', 'Donna Tartt', 1992);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (13, 'The Silent Patient', 'Alex Michaelides', 2019);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (14, 'The Woman in White', 'Wilkie Collins', 1859);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (15, 'The Maltese Falcon', 'Dashiell Hammett', 1930);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (16, 'The No. 1 Ladies'' Detective Agency', 'Alexander McCall Smith', 1998);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (17, 'The Woman in Cabin 10', 'Ruth Ware', 2016);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (18, 'The Name of the Rose', 'Umberto Eco', 1980);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (19, 'In Cold Blood', 'Truman Capote', 1966);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (20, 'Rebecca', 'Daphne du Maurier', 1938);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (21, 'The Secret Adversary', 'Agatha Christie', 1922);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (22, 'The Girl with the Dragon Tattoo', 'Stieg Larsson', 2005);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (23, 'The Lost Symbol', 'Dan Brown', 2009);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (24, 'Before I Go to Sleep', 'S.J. Watson', 2011);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (25, 'The Hound of the Baskervilles', 'Arthur Conan Doyle', 1902);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (26, 'The Alienist', 'Caleb Carr', 1994);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (27, 'The Moonstone', 'Wilkie Collins', 1868);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (28, 'The Talented Mr. Ripley', 'Patricia Highsmith', 1955);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (29, 'The Secret Place', 'Tana French', 2014);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (30, 'Behind Closed Doors', 'B.A. Paris', 2016);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (31, 'I Am Watching You', 'Teresa Driscoll', 2017);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (32, 'The Girl Who Played with Fire', 'Stieg Larsson', 2006);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (33, 'The Murder of Roger Ackroyd', 'Agatha Christie', 1926);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (34, 'The Dry', 'Jane Harper', 2016);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (35, 'The Death of Mrs. Westaway', 'Ruth Ware', 2018);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (36, 'The Postman Always Rings Twice', 'James M. Cain', 1934);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (37, 'The Thirteenth Tale', 'Diane Setterfield', 2006);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (38, 'The Secret Keeper', 'Kate Morton', 2012);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (39, 'Before I Go to Sleep', 'S.J. Watson', 2011);
INSERT INTO mystery (SNo, Title, Author, Year_of_Publication) VALUES (40, 'The Moonstone', 'Wilkie Collins', 1868);

-- DROP TABLE romance;

CREATE TABLE romance(
        SNo INT,
        Title VARCHAR(255),
        Author VARCHAR(255),
        Year_of_Publication INT        
);

INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (1, 'Pride and Prejudice', 'Jane Austen', 1813);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (2, 'Jane Eyre', 'Charlotte Brontë', 1847);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (3, 'Gone with the Wind', 'Margaret Mitchell', 1936);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (4, 'The Notebook', 'Nicholas Sparks', 1996);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (5, 'Outlander', 'Diana Gabaldon', 1991);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (6, 'Me Before You', 'Jojo Moyes', 2012);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (7, 'A Walk to Remember', 'Nicholas Sparks', 1999);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (8, 'Anna Karenina', 'Leo Tolstoy', 1877);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (9, 'The Fault in Our Stars', 'John Green', 2012);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (10, 'Wuthering Heights', 'Emily Brontë', 1847);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (11, 'The Time Traveler''s Wife', 'Audrey Niffenegger', 2003);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (12, 'Dear John', 'Nicholas Sparks', 2006);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (13, 'Water for Elephants', 'Sara Gruen', 2006);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (14, 'The Rosie Project', 'Graeme Simsion', 2013);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (15, 'Atonement', 'Ian McEwan', 2001);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (16, 'The Princess Bride', 'William Goldman', 1973);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (17, 'PS, I Love You', 'Cecelia Ahern', 2004);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (18, 'One Day', 'David Nicholls', 2009);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (19, 'Call Me by Your Name', 'André Aciman', 2007);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (20, 'The Bridges of Madison County', 'Robert James Waller', 1992);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (21, 'Love in the Time of Cholera', 'Gabriel García Márquez', 1985);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (22, 'Like Water for Chocolate', 'Laura Esquivel', 1989);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (23, 'It Ends With Us', 'Colleen Hoover', 2016);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (24, 'Eleanor & Park', 'Rainbow Rowell', 2013);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (25, 'The Hating Game', 'Sally Thorne', 2016);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (26, 'The Choice', 'Nicholas Sparks', 2007);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (27, 'The Last Song', 'Nicholas Sparks', 2009);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (28, 'Safe Haven', 'Nicholas Sparks', 2010);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (29, 'The Lucky One', 'Nicholas Sparks', 2008);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (30, 'The Best of Me', 'Nicholas Sparks', 2011);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (31, 'The Wedding', 'Nicholas Sparks', 2003);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (32, 'The Longest Ride', 'Nicholas Sparks', 2013);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (33, 'Two by Two', 'Nicholas Sparks', 2016);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (34, 'The Guardian', 'Nicholas Sparks', 2003);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (35, 'The Horse Whisperer', 'Nicholas Evans', 1995);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (36, 'The Rescue', 'Nicholas Sparks', 2000);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (37, 'Red, White & Royal Blue', 'Casey McQuiston', 2019);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (38, 'A Bend in the Road', 'Nicholas Sparks', 2001);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (39, 'The Lake House', 'James Patterson', 2003);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (40, 'Meant to Be', 'Lauren Morrill', 2012);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (41, 'If Only It Were True', 'Marc Levy', 2000);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (42, 'P.S. from Paris', 'Marc Levy', 2017);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (43, 'The Flatshare', 'Beth O''Leary', 2019);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (44, 'The Sun Is Also a Star', 'Nicola Yoon', 2016);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (45, 'Every Breath', 'Nicholas Sparks', 2018);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (46, 'Walk to Beautiful', 'Jimmy Wayne', 2014);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (47, 'The Christmas Train', 'David Baldacci', 2002);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (48, 'The Art of Racing in the Rain', 'Garth Stein', 2008);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (49, 'One Day in December', 'Josie Silver', 2018);
INSERT INTO romance (SNo, Title, Author, Year_of_Publication) VALUES (50, 'A Man Called Ove', 'Fredrik Backman', 2012);

-- DROP TABLE science_fiction;

CREATE TABLE science_fiction(
        SNo INT,
        Title VARCHAR(255),
        Author VARCHAR(255),
        Year_of_Publication INT        
);

INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (1, 'Dune', 'Frank Herbert', 1965);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (2, 'Neuromancer', 'William Gibson', 1984);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (3, 'Foundation', 'Isaac Asimov', 1951);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (4, 'Snow Crash', 'Neal Stephenson', 1992);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (5, 'The Hitchhiker''s Guide to the Galaxy', 'Douglas Adams', 1979);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (6, 'Hyperion', 'Dan Simmons', 1989);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (7, 'The War of the Worlds', 'H.G. Wells', 1898);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (8, 'The Left Hand of Darkness', 'Ursula K. Le Guin', 1969);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (9, 'Starship Troopers', 'Robert A. Heinlein', 1959);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (10, 'Ender''s Game', 'Orson Scott Card', 1985);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (11, 'Do Androids Dream of Electric Sheep?', 'Philip K. Dick', 1968);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (12, '1984', 'George Orwell', 1949);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (13, 'The Martian Chronicles', 'Ray Bradbury', 1950);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (14, 'Altered Carbon', 'Richard K. Morgan', 2002);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (15, 'The Time Machine', 'H.G. Wells', 1895);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (16, 'I, Robot', 'Isaac Asimov', 1950);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (17, 'The Expanse: Leviathan Wakes', 'James S.A. Corey', 2011);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (18, 'The Three-Body Problem', 'Liu Cixin', 2008);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (19, 'The Hunger Games', 'Suzanne Collins', 2008);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (20, 'Ready Player One', 'Ernest Cline', 2011);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (21, 'The Handmaid''s Tale', 'Margaret Atwood', 1985);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (22, 'Brave New World', 'Aldous Huxley', 1932);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (23, 'The Stand', 'Stephen King', 1978);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (24, 'The Forever War', 'Joe Haldeman', 1974);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (25, 'Contact', 'Carl Sagan', 1985);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (26, 'Rendezvous with Rama', 'Arthur C. Clarke', 1973);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (27, 'Foundation and Empire', 'Isaac Asimov', 1952);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (28, 'The Day of the Triffids', 'John Wyndham', 1951);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (29, 'Childhood''s End', 'Arthur C. Clarke', 1953);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (30, 'Ringworld', 'Larry Niven', 1970);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (31, 'The Dispossessed', 'Ursula K. Le Guin', 1974);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (32, 'Altered Carbon', 'Richard K. Morgan', 2002);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (33, 'The Diamond Age', 'Neal Stephenson', 1995);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (34, 'The Fifth Season', 'N.K. Jemisin', 2015);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (35, 'Gateway', 'Frederik Pohl', 1977);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (36, 'Old Man''s War', 'John Scalzi', 2005);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (37, 'The Man in the High Castle', 'Philip K. Dick', 1962);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (38, 'The City and the Stars', 'Arthur C. Clarke', 1956);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (39, 'The Hyperion Cantos', 'Dan Simmons', 1989);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (40, 'Fahrenheit 451', 'Ray Bradbury', 1953);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (41, 'Starship Troopers', 'Robert A. Heinlein', 1959);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (42, 'The Stars My Destination', 'Alfred Bester', 1956);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (43, 'Ubik', 'Philip K. Dick', 1969);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (44, 'The Lathe of Heaven', 'Ursula K. Le Guin', 1971);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (45, 'The Left Hand of Darkness', 'Ursula K. Le Guin', 1969);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (46, 'The Forever War', 'Joe Haldeman', 1974);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (47, 'Altered Carbon', 'Richard K. Morgan', 2002);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (48, 'Dune Messiah', 'Frank Herbert', 1969);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (49, 'Snow Crash', 'Neal Stephenson', 1992);
INSERT INTO science_fiction (SNo, Title, Author, Year_of_Publication) VALUES (50, 'Red Mars', 'Kim Stanley Robinson', 1992);

-- DROP TABLE horror;

CREATE TABLE horror(
        SNo INT,
        Title VARCHAR(255),
        Author VARCHAR(255),
        Year_of_Publication INT        
);

INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (1, 'Dracula', 'Bram Stoker', 1897);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (2, 'Frankenstein', 'Mary Shelley', 1818);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (3, 'The Exorcist', 'William Peter Blatty', 1971);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (4, 'The Shining', 'Stephen King', 1977);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (5, 'Psycho', 'Robert Bloch', 1959);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (6, 'The Haunting of Hill House', 'Shirley Jackson', 1959);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (7, 'It', 'Stephen King', 1986);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (8, 'Carrie', 'Stephen King', 1974);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (9, 'Pet Sematary', 'Stephen King', 1983);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (10, 'Misery', 'Stephen King', 1987);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (11, 'The Amityville Horror', 'Jay Anson', 1977);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (12, 'The Turn of the Screw', 'Henry James', 1898);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (13, 'The Stand', 'Stephen King', 1978);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (14, 'The Silence of the Lambs', 'Thomas Harris', 1988);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (15, 'The Call of Cthulhu', 'H.P. Lovecraft', 1928);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (16, 'Interview with the Vampire', 'Anne Rice', 1976);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (17, 'American Psycho', 'Bret Easton Ellis', 1991);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (18, 'House of Leaves', 'Mark Z. Danielewski', 2000);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (19, 'The Girl with All the Gifts', 'M.R. Carey', 2014);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (20, 'Bird Box', 'Josh Malerman', 2014);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (21, 'The Ritual', 'Adam Nevill', 2011);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (22, 'The Woman in Black', 'Susan Hill', 1983);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (23, 'Ghost Story', 'Peter Straub', 1979);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (24, 'Rosemary''s Baby', 'Ira Levin', 1967);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (25, 'The Troop', 'Nick Cutter', 2014);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (26, 'The Fisherman', 'John Langan', 2016);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (27, 'Hell House', 'Richard Matheson', 1971);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (28, 'The Ruins', 'Scott Smith', 2006);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (29, 'Heart-Shaped Box', 'Joe Hill', 2007);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (30, 'The Dark Tower: The Gunslinger', 'Stephen King', 1982);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (31, 'The Last House on Needless Street', 'Catriona Ward', 2021);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (32, 'The Southern Book Club''s Guide to Slaying Vampires', 'Grady Hendrix', 2020);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (33, 'The Twisted Ones', 'T. Kingfisher', 2019);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (34, 'The Girl Next Door', 'Jack Ketchum', 1989);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (35, 'The Little Stranger', 'Sarah Waters', 2009);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (36, 'The Elementals', 'Michael McDowell', 1981);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (37, 'The Haunting of Hill House', 'Shirley Jackson', 1959);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (38, 'The Cabin at the End of the World', 'Paul Tremblay', 2018);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (39, 'The Silent Companions', 'Laura Purcell', 2017);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (40, 'The Hunger', 'Alma Katsu', 2018);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (41, 'The Institute', 'Stephen King', 2019);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (42, 'I'm Thinking of Ending Things', 'Iain Reid', 2016);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (43, 'The Takibling of Annie Thorne', 'C.J. Tudor', 2019);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (44, 'My Best Friend''s Exorcism', 'Grady Hendrix', 2016);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (45, 'Kill Creek', 'Scott Thomas', 2017);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (46, 'Mexican Gothic', 'Silvia Moreno-Garcia', 2020);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (47, 'Heart-Shaped Box', 'Joe Hill', 2007);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (48, 'Let the Right One In', 'John Ajvide Lindqvist', 2004);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (49, 'Something Wicked This Way Comes', 'Ray Bradbury', 1962);
INSERT INTO horror (SNo, Title, Author, Year_of_Publication) VALUES (50, 'Salem''s Lot', 'Stephen King', 1975);

SELECT * FROM fiction;
SELECT * FROM mystery;
SELECT * FROM romance;
SELECT * FROM science_fiction;
SELECT * FROM horror;

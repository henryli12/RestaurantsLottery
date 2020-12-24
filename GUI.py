import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from search import search


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setFixedSize(900, 500)
        self.setWindowTitle("Random Restaurant Generator")
        self.home()

    def home(self):
        self.btn = QtWidgets.QPushButton("Generate", self)
        self.btn.setShortcut("Return")
        self.find = QtWidgets.QLineEdit(self)
        self.find1 = QtWidgets.QLabel("Find: ", self)
        self.loc = QtWidgets.QLineEdit(self)
        self.loc1 = QtWidgets.QLabel("Near: ", self)
        self.name = QtWidgets.QLabel("Name: ", self)
        self.url = QtWidgets.QLabel("Url: ", self)
        self.stars = QtWidgets.QLabel("Stars: ", self)
        self.dollars = QtWidgets.QLabel("Dollars: ", self)
        self.phone = QtWidgets.QLabel("Phone: ", self)
        self.address = QtWidgets.QLabel("Address: ", self)
        self.categ = QtWidgets.QLabel("Categories: ", self)
        self.name1 = QtWidgets.QLabel(self)
        self.url1 = QtWidgets.QLabel(self)
        self.stars1 = QtWidgets.QLabel(self)
        self.dollars1 = QtWidgets.QLabel(self)
        self.phone1 = QtWidgets.QLabel(self)
        self.address1 = QtWidgets.QLabel(self)
        self.categ1 = QtWidgets.QLabel(self)
        self.find.setGeometry(150, 160, 150, 30)
        self.find1.move(100, 160)
        self.loc1.move(320, 160)
        self.loc.setGeometry(370, 160, 150, 30)
        self.btn.move(550, 160)
        self.name.move(100, 200)
        self.name1.setGeometry(180, 200, 300, 30)
        self.url.move(100, 350)
        self.url1.setGeometry(180, 350, 1000, 30)
        self.stars.move(100, 260)
        self.stars1.setGeometry(180, 260, 200, 30)
        self.dollars.move(100, 230)
        self.dollars1.setGeometry(180, 230, 200, 30)
        self.phone.move(100, 320)
        self.phone1.setGeometry(180, 320, 200, 30)
        self.address.move(100, 290)
        self.address1.setGeometry(180, 290, 300, 30)
        self.categ.move(100, 380)
        self.categ1.setGeometry(180, 380, 1000, 30)
        self.btn.clicked.connect(self.search)
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Enter"), self)
        self.shortcut.activated.connect(self.search)
        self.show()

    def search(self):
        result = search(self.find.text(), self.loc.text())
        self.name1.setText(result.name)
        url = "<a href=\"{}\">{}</a>"
        url = url.format(result.url, result.url)
        self.url1.setOpenExternalLinks(True)
        self.url1.setText(url)
        self.stars1.setText(result.stars)
        self.dollars1.setText(result.dollars)
        self.phone1.setText(result.phone)
        self.address1.setText(result.address)
        cate = ""
        for c in result.categ:
            cate += c + ", "
        self.categ1.setText(cate)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Gui = Window()
    sys.exit(app.exec_())

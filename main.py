import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.load_data()

    def load_data(self):
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        data = cur.execute(f"""SELECT * from coffee""").fetchall()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(('ID', 'Title', 'Degree', 'Type', 'Description',
                                              'Price', 'Volume'))
        self.table.setRowCount(0)
        for i, row in enumerate(data):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.table.verticalHeader().hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

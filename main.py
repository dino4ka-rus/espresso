import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication, QHeaderView


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)

        self.con = sqlite3.connect('coffee.sqlite')

        self.load_table()

    def load_table(self):
        cur = self.con.cursor()
        res = cur.execute("""SELECT c.id, c.sort, r.title, p.title, c.taste_description, c.price, c.pack_volume FROM
        coffee as c JOIN processes as p ON c.processing_method = p.id
        JOIN roasting as r ON c.degree_of_roasting = r.id""").fetchall()

        self.tableWidget.setRowCount(len(res))

        for i, row in enumerate(res):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Coffee()
    ex.show()

    sys.exit(app.exec())
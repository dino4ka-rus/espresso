import sqlite3
import sys

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication, QHeaderView, QWidget, QMessageBox

from main_window import Ui_MainWindow
from addEditCoffeeForm import Ui_Form


class AddEditForm(QWidget, Ui_Form):
    def __init__(self, parent=None, coffee_id=None):
        super().__init__(parent=None)
        self.setupUi(self)

        self.con = sqlite3.connect('data\coffee.sqlite')

        self.roasts = self.select_roasts()
        self.processes = ["Молотый", "В зернах"]
        self.cb_roast.addItems(self.roasts)
        self.cb_process.addItems(self.processes)

        self.parent = parent
        self.coffee_id = coffee_id
        if coffee_id is not None:
            self.pb_save.clicked.connect(self.edit_coffee)
            self.setWindowTitle('Редактирование')
            self.get_info()
        else:
            self.pb_save.clicked.connect(self.add_coffee)

        self.message = QMessageBox()
        self.message.setText('Форма заполнена неверно')

    def edit_coffee(self):
        cur_sort = self.le_sort.text()
        cur_roast = self.cb_roast.currentText()
        cur_process = self.cb_process.currentText()
        cur_taste = self.pte_taste.toPlainText()
        cur_price = self.le_price.text()
        cur_volume = self.le_volume.text()

        cur = self.con.cursor()
        try:
            que = """UPDATE coffee
            SET sort = ?, degree_of_roasting = ?, processing_method = ?,
             taste_description = ?, price = ?, pack_volume = ? 
            WHERE id = ?"""
            cur.execute(que, (cur_sort, self.roasts.index(cur_roast) + 1, self.processes.index(cur_process) + 1, cur_taste,
                              int(cur_price), int(cur_volume), self.coffee_id))
        except ValueError as ve:
            self.message.show()
            print(ve)
        else:
            self.con.commit()
            self.parent.update_table()
            self.close()

    def add_coffee(self):
        cur_sort = self.le_sort.text()
        cur_roast = self.cb_roast.currentText()
        cur_process = self.cb_process.currentText()
        cur_taste = self.pte_taste.toPlainText()
        cur_price = self.le_price.text()
        cur_volume = self.le_volume.text()

        cur = self.con.cursor()
        try:
            id_off = cur.execute("SELECT max(id) FROM coffee").fetchone()[0]
            new_data = (id_off + 1, cur_sort, self.roasts.index(cur_roast) + 1,
                        self.processes.index(cur_process) + 1, cur_taste, int(cur_price), int(cur_volume))
            cur.execute("INSERT INTO coffee VALUES (?,?,?,?,?,?,?)", new_data)
        except ValueError as ve:
            self.message.show()
            print(ve)
        else:
            self.con.commit()
            self.parent.update_table()
            self.close()

    def get_info(self):
        cur = self.con.cursor()
        info = cur.execute("""SELECT c.sort, r.title, p.title, c.taste_description, c.price, c.pack_volume FROM
                coffee as c JOIN processes as p ON c.processing_method = p.id
                JOIN roasting as r ON c.degree_of_roasting = r.id
                WHERE c.id = ?""", self.coffee_id).fetchone()
        self.le_sort.setText(info[0])
        self.cb_roast.setCurrentText(info[1])
        self.cb_process.setCurrentText(info[2])
        self.pte_taste.setPlainText(info[3])
        self.le_price.setText(str(info[4]))
        self.le_volume.setText(str(info[5]))

    def select_roasts(self):
        cur = self.con.cursor()
        res = cur.execute("""SELECT title FROM roasting""").fetchall()
        return [x[0] for x in res]


class Coffee(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)

        self.con = sqlite3.connect('data\coffee.sqlite')

        self.update_table()

        self.pb_add.clicked.connect(self.show_add_form)
        self.pb_edit.clicked.connect(self.edit_coffee)

    def show_add_form(self):
        self.add_edit_form = AddEditForm(self)
        self.add_edit_form.show()

    def update_table(self):
        cur = self.con.cursor()
        que = """SELECT c.id, c.sort, r.title, p.title, c.taste_description, c.price, c.pack_volume FROM
        coffee as c JOIN processes as p ON c.processing_method = p.id
        JOIN roasting as r ON c.degree_of_roasting = r.id"""
        res = cur.execute(que).fetchall()

        self.tableWidget.setRowCount(len(res))

        for i, row in enumerate(res):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

    def edit_coffee(self):
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        self.dialog = AddEditForm(self, coffee_id=ids[0])
        self.dialog.show()

    def closeEvent(self, event):
        self.con.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Coffee()
    ex.show()

    sys.excepthook = except_hook
    sys.exit(app.exec())
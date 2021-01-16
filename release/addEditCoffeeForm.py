# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(373, 243)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.le_price = QtWidgets.QLineEdit(Form)
        self.le_price.setObjectName("le_price")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.le_price)
        self.le_volume = QtWidgets.QLineEdit(Form)
        self.le_volume.setObjectName("le_volume")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.le_volume)
        self.le_sort = QtWidgets.QLineEdit(Form)
        self.le_sort.setObjectName("le_sort")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_sort)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cb_roast = QtWidgets.QComboBox(Form)
        self.cb_roast.setObjectName("cb_roast")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cb_roast)
        self.cb_process = QtWidgets.QComboBox(Form)
        self.cb_process.setObjectName("cb_process")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cb_process)
        self.pte_taste = QtWidgets.QPlainTextEdit(Form)
        self.pte_taste.setObjectName("pte_taste")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pte_taste)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.pb_save = QtWidgets.QPushButton(Form)
        self.pb_save.setObjectName("pb_save")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.pb_save)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление"))
        self.label.setText(_translate("Form", "Название сорта"))
        self.label_2.setText(_translate("Form", "Степень обжарки"))
        self.label_3.setText(_translate("Form", "Обработка"))
        self.label_6.setText(_translate("Form", "Описание вкуса"))
        self.label_4.setText(_translate("Form", "Цена, руб"))
        self.label_5.setText(_translate("Form", "Вес упаковки, г"))
        self.pb_save.setText(_translate("Form", "Сохранить"))

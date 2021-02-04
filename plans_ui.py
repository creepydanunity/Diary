# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plans.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Plans(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(901, 608)
        Form.setMinimumSize(QtCore.QSize(901, 608))
        Form.setMaximumSize(QtCore.QSize(901, 608))
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 881, 541))
        self.tableWidget.setMaximumSize(QtCore.QSize(901, 611))
        self.tableWidget.setStyleSheet("\n"
                                       "color: #5555ff;\n"
                                       "")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.add_new_comm = QtWidgets.QPushButton(Form)
        self.add_new_comm.setGeometry(QtCore.QRect(10, 560, 435, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_new_comm.setFont(font)
        self.add_new_comm.setStyleSheet("QPushButton {\n"
                                           "    background-color: #e1e1e1;\n"
                                           "    border:2px solid #3e3e3e;\n"
                                           "    border-radius: 5;\n"
                                           "    color: #5555ff\n"
                                           "}\n"
                                           "\n"
                                           "QPushbutton:pressed {\n"
                                           "    background-color: #bebebe\n"
                                           "}\n"
                                           "QPushButton:hover { background-color: #a2a2d0; }\n"
                                           "QPushButton:pressed { background-color: #baacc7; }")
        self.add_new_comm.setObjectName("add_new_comm")
        self.exit_button = QtWidgets.QPushButton(Form)
        self.exit_button.setGeometry(QtCore.QRect(460, 560, 431, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("QPushButton {\n"
                                           "    background-color: #e1e1e1;\n"
                                           "    border:2px solid #3e3e3e;\n"
                                           "    border-radius: 5;\n"
                                           "    color: #5555ff\n"
                                           "}\n"
                                           "\n"
                                           "QPushbutton:pressed {\n"
                                           "    background-color: #bebebe\n"
                                           "}\n"
                                           "QPushButton:hover { background-color: #a2a2d0; }\n"
                                           "QPushButton:pressed { background-color: #baacc7; }")
        self.exit_button.setObjectName("exit_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "01.01"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "02.01"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "03.01"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Form", "11"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Событие"))
        self.add_new_comm.setText(_translate("Form", "Добавить новую запись"))
        self.exit_button.setText(_translate("Form", "Выход"))

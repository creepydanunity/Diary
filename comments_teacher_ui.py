# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comments_teacher.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Teacher_comm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1120, 902)
        self.button_exit = QtWidgets.QPushButton(Form)
        self.button_exit.setEnabled(True)
        self.button_exit.setGeometry(QtCore.QRect(70, 810, 971, 81))
        self.button_exit.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_exit.setFont(font)
        self.button_exit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.button_exit.setMouseTracking(False)
        self.button_exit.setAutoFillBackground(False)
        self.button_exit.setStyleSheet("QPushButton {\n"
                                       "    background-color: #f1f1f1;\n"
                                       "    border:2px solid #e1e1e1;\n"
                                       "    border-radius: 5;\n"
                                       "    color: #5555ff\n"
                                       "}\n"
                                       "\n"
                                       "QPushbutton:pressed {\n"
                                       "    background-color: #bebebe\n"
                                       "}")
        self.button_exit.setCheckable(False)
        self.button_exit.setAutoDefault(True)
        self.button_exit.setDefault(False)
        self.button_exit.setFlat(False)
        self.button_exit.setObjectName("button_exit")
        self.msg_table = QtWidgets.QTableWidget(Form)
        self.msg_table.setGeometry(QtCore.QRect(0, 0, 1121, 801))
        self.msg_table.setObjectName("msg_table")
        self.msg_table.setColumnCount(0)
        self.msg_table.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_exit.setText(_translate("Form", "Выйти"))

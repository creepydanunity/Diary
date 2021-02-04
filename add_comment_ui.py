# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_comment.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Add_comment_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 279)
        Form.setMinimumSize(QtCore.QSize(400, 279))
        Form.setMaximumSize(QtCore.QSize(400, 279))
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5555ff")
        self.label_2.setObjectName("label_2")
        self.input_comment = QtWidgets.QLineEdit(Form)
        self.input_comment.setGeometry(QtCore.QRect(10, 60, 381, 151))
        self.input_comment.setMaximumSize(QtCore.QSize(381, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_comment.setFont(font)
        self.input_comment.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.input_comment.setObjectName("input_comment")
        self.button_ok = QtWidgets.QPushButton(Form)
        self.button_ok.setEnabled(True)
        self.button_ok.setGeometry(QtCore.QRect(140, 230, 121, 40))
        self.button_ok.setMaximumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_ok.setFont(font)
        self.button_ok.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.button_ok.setMouseTracking(False)
        self.button_ok.setAutoFillBackground(False)
        self.button_ok.setStyleSheet("QPushButton {\n"
                                     "    background-color: #f1f1f1;\n"
                                     "    border:2px solid #e1e1e1;\n"
                                     "    border-radius: 5;\n"
                                     "    color: #5555ff\n"
                                     "}\n"
                                     "\n"
                                     "QPushbutton:pressed {\n"
                                     "    background-color: #bebebe\n"
                                     "}")
        self.button_ok.setCheckable(False)
        self.button_ok.setAutoDefault(True)
        self.button_ok.setDefault(False)
        self.button_ok.setFlat(False)
        self.button_ok.setObjectName("button_ok")
        self.button_cancel = QtWidgets.QPushButton(Form)
        self.button_cancel.setEnabled(True)
        self.button_cancel.setGeometry(QtCore.QRect(270, 230, 121, 40))
        self.button_cancel.setMaximumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_cancel.setFont(font)
        self.button_cancel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.button_cancel.setMouseTracking(False)
        self.button_cancel.setAutoFillBackground(False)
        self.button_cancel.setStyleSheet("QPushButton {\n"
                                         "    background-color: #f1f1f1;\n"
                                         "    border:2px solid #e1e1e1;\n"
                                         "    border-radius: 5;\n"
                                         "    color: #5555ff\n"
                                         "}\n"
                                         "\n"
                                         "QPushbutton:pressed {\n"
                                         "    background-color: #bebebe\n"
                                         "}")
        self.button_cancel.setCheckable(False)
        self.button_cancel.setAutoDefault(True)
        self.button_cancel.setDefault(False)
        self.button_cancel.setFlat(False)
        self.button_cancel.setObjectName("button_cancel")
        self.students_combobox = QtWidgets.QComboBox(Form)
        self.students_combobox.setGeometry(QtCore.QRect(270, 27, 125, 21))
        self.students_combobox.setStyleSheet("QComboBox {\n"
                                             "    background-color: #f1f1f1;\n"
                                             "    border:2px solid #e1e1e1;\n"
                                             "    border-radius: 5;\n"
                                             "    color: #5555ff\n"
                                             "}\n"
                                             "\n"
                                             "QPushbutton:pressed {\n"
                                             "    background-color: #bebebe\n"
                                             "}")
        self.students_combobox.setObjectName("students_combobox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Написать сообщение:"))
        self.button_ok.setText(_translate("Form", "OK"))
        self.button_cancel.setText(_translate("Form", "Отмена"))

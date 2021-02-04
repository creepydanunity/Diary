# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'class_selection.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Class_select_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 178)
        Form.setMinimumSize(QtCore.QSize(400, 178))
        Form.setMaximumSize(QtCore.QSize(400, 178))
        self.button_enter = QtWidgets.QPushButton(Form)
        self.button_enter.setEnabled(True)
        self.button_enter.setGeometry(QtCore.QRect(70, 120, 260, 40))
        self.button_enter.setMaximumSize(QtCore.QSize(260, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_enter.setFont(font)
        self.button_enter.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.button_enter.setMouseTracking(False)
        self.button_enter.setAutoFillBackground(False)
        self.button_enter.setStyleSheet("QPushButton {\n"
                                        "    background-color: #e1e1e1;\n"
                                        "    border:2px solid #3e3e3e;\n"
                                        "    border-radius: 5;\n"
                                        "    color: #5555ff\n"
                                        "}\n"
                                        "\n"
                                        "QPushbutton:pressed {\n"
                                        "    background-color: #bebebe\n"
                                        "}")
        self.button_enter.setCheckable(False)
        self.button_enter.setAutoDefault(True)
        self.button_enter.setDefault(False)
        self.button_enter.setFlat(False)
        self.button_enter.setObjectName("button_enter")
        self.button_enter.setStyleSheet("QPushButton {\n"
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
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 50, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #5555ff")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.username = QtWidgets.QLabel(Form)
        self.username.setGeometry(QtCore.QRect(0, 10, 400, 30))
        self.username.setStyleSheet("background-color: #e5e5e5")
        self.username.setText("")
        self.username.setObjectName("username")
        font.setPointSize(14)
        self.username.setFont(font)
        self.username.setStyleSheet("color: #000000")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 40, 381, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(10, 60, 381, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.classes__box = QtWidgets.QComboBox(Form)
        self.classes__box.setGeometry(QtCore.QRect(140, 80, 111, 22))
        self.classes__box.setObjectName("classes__box")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_enter.setText(_translate("Form", "Войти"))
        self.label.setText(_translate("Form", "Класс:"))

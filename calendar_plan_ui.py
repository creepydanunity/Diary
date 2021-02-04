# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar_plan.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Calendar_plan(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 401, 231))
        self.calendarWidget.setObjectName("calendarWidget")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 250, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.button_enter = QtWidgets.QPushButton(Form)
        self.button_enter.setEnabled(True)
        self.button_enter.setGeometry(QtCore.QRect(269, 249, 121, 31))
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
                                           "}\n"
                                           "QPushButton:hover { background-color: #a2a2d0; }\n"
                                           "QPushButton:pressed { background-color: #baacc7; }")
        self.button_enter.setCheckable(False)
        self.button_enter.setAutoDefault(True)
        self.button_enter.setDefault(False)
        self.button_enter.setFlat(False)
        self.button_enter.setObjectName("button_enter")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_enter.setText(_translate("Form", "Добавить"))

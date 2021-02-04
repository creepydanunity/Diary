from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 180)
        Form.setMinimumSize(QtCore.QSize(400, 180))
        Form.setMaximumSize(QtCore.QSize(400, 180))
        Form.setStyleSheet("background-color: #ffffff")
        self.button_exit = QtWidgets.QPushButton(Form)
        self.button_exit.setEnabled(True)
        self.button_exit.setGeometry(QtCore.QRect(140, 130, 121, 40))
        self.button_exit.setMaximumSize(QtCore.QSize(260, 40))
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
        self.username = QtWidgets.QLabel(Form)
        self.username.setGeometry(QtCore.QRect(0, 10, 400, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setStyleSheet("background-color: #f1f1f1")
        self.username.setText("")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5555ff")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 50, 381, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 90, 381, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.button_cancel = QtWidgets.QPushButton(Form)
        self.button_cancel.setEnabled(True)
        self.button_cancel.setGeometry(QtCore.QRect(270, 130, 121, 40))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_exit.setText(_translate("Form", "Выйти"))
        self.label_2.setText(_translate("Form", "Вы действительно хотите выйти?"))
        self.button_cancel.setText(_translate("Form", "Отмена"))

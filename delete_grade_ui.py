from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 180)
        Form.setMinimumSize(QtCore.QSize(400, 180))
        Form.setMaximumSize(QtCore.QSize(400, 180))
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 391, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #5555ff")
        self.label_2.setObjectName("label_2")
        self.button_ok = QtWidgets.QPushButton(Form)
        self.button_ok.setEnabled(True)
        self.button_ok.setGeometry(QtCore.QRect(140, 120, 121, 40))
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
        self.button_cancel.setGeometry(QtCore.QRect(270, 120, 121, 40))
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
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(10, 20, 381, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 90, 381, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Вы действительно хотите удалить оценку?"))
        self.button_ok.setText(_translate("Form", "OK"))
        self.button_cancel.setText(_translate("Form", "Отмена"))

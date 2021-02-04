from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(330, 350)
        Login.setMinimumSize(QtCore.QSize(330, 350))
        Login.setMaximumSize(QtCore.QSize(330, 350))
        Login.setStyleSheet("backgroung-color: white")
        self.input_ID = QtWidgets.QLineEdit(Login)
        self.input_ID.setGeometry(QtCore.QRect(40, 100, 260, 35))
        self.input_ID.setMaximumSize(QtCore.QSize(1000, 1000))
        self.input_ID.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.input_ID.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_ID.setStyleSheet("border:1px solid #000000;\n""border-radius: 10;")
        self.input_ID.setFrame(True)
        self.input_ID.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_ID.setAlignment(QtCore.Qt.AlignCenter)
        self.input_ID.setDragEnabled(False)
        self.input_ID.setClearButtonEnabled(True)
        self.input_ID.setObjectName("input_ID")
        self.input_password = QtWidgets.QLineEdit(Login)
        self.input_password.setGeometry(QtCore.QRect(40, 170, 260, 35))
        self.input_password.setMaximumSize(QtCore.QSize(260, 35))
        self.input_password.setStyleSheet("border:1px solid #000000;\n"
                                          "border-radius: 10;")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setAlignment(QtCore.Qt.AlignCenter)
        self.input_password.setClearButtonEnabled(True)
        self.input_password.setObjectName("input_password")
        self.button_enter = QtWidgets.QPushButton(Login)
        self.button_enter.setEnabled(True)
        self.button_enter.setGeometry(QtCore.QRect(40, 240, 260, 40))
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
        self.button_register = QtWidgets.QPushButton(Login)
        self.button_register.setGeometry(QtCore.QRect(100, 300, 141, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_register.sizePolicy().hasHeightForWidth())
        self.button_register.setSizePolicy(sizePolicy)
        self.button_register.setMinimumSize(QtCore.QSize(0, 0))
        self.button_register.setMaximumSize(QtCore.QSize(141, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.button_register.setFont(font)
        self.button_register.setStyleSheet("QPushButton {\n"
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
        self.button_register.setObjectName("button_register")
        self.text_enter = QtWidgets.QLabel(Login)
        self.text_enter.setGeometry(QtCore.QRect(70, 10, 201, 71))
        self.text_enter.setMaximumSize(QtCore.QSize(201, 71))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.text_enter.setFont(font)
        self.text_enter.setStyleSheet("color: #5555ff")
        self.text_enter.setObjectName("text_enter")
        self.text_ID = QtWidgets.QLabel(Login)
        self.text_ID.setGeometry(QtCore.QRect(160, 80, 21, 16))
        self.text_ID.setMaximumSize(QtCore.QSize(21, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.text_ID.setFont(font)
        self.text_ID.setStyleSheet("color: #5555ff")
        self.text_ID.setObjectName("text_ID")
        self.text_password = QtWidgets.QLabel(Login)
        self.text_password.setGeometry(QtCore.QRect(140, 145, 61, 16))
        self.text_password.setMaximumSize(QtCore.QSize(61, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.text_password.setFont(font)
        self.text_password.setStyleSheet("color: #5555ff")
        self.text_password.setObjectName("text_password")
        self.line_2 = QtWidgets.QFrame(Login)
        self.line_2.setGeometry(QtCore.QRect(10, 60, 311, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Login)
        self.line_3.setGeometry(QtCore.QRect(10, 20, 311, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Login)
        self.line_4.setGeometry(QtCore.QRect(10, 210, 311, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Login)
        self.line_5.setGeometry(QtCore.QRect(10, 330, 311, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.button_enter.setText(_translate("Login", "Войти"))
        self.button_register.setText(_translate("Login", "Регистрация"))
        self.text_enter.setText(_translate("Login", "Вход в систему"))
        self.text_ID.setText(_translate("Login", "ID"))
        self.text_password.setText(_translate("Login", "Пароль"))

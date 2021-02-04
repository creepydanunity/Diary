from PyQt5 import QtCore, QtGui, QtWidgets


class Student_UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1140, 809)
        Form.setMinimumSize(QtCore.QSize(1140, 809))
        Form.setMaximumSize(QtCore.QSize(1140, 809))
        Form.setStyleSheet("background-color: #ffffff;")
        self.username = QtWidgets.QLabel(Form)
        self.username.setGeometry(QtCore.QRect(10, 10, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(False)
        self.username.setFont(font)
        self.username.setStyleSheet("border:1px solid #000000;\n"
                                    "color: #5555ff;\n"
                                    "border-radius: 5;")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.class_ruk_name = QtWidgets.QLabel(Form)
        self.class_ruk_name.setGeometry(QtCore.QRect(10, 70, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.class_ruk_name.setFont(font)
        self.class_ruk_name.setStyleSheet("border:1px solid #000000;\n"
                                          "color: #5555ff;\n"
                                          "border-radius: 5;")
        self.class_ruk_name.setAlignment(QtCore.Qt.AlignCenter)
        self.class_ruk_name.setObjectName("class_ruk_name")
        self.ID = QtWidgets.QLabel(Form)
        self.ID.setGeometry(QtCore.QRect(380, 10, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ID.setFont(font)
        self.ID.setStyleSheet("border:1px solid #000000;\n"
                              "color: #5555ff;\n"
                              "border-radius: 5;")
        self.ID.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ID.setAlignment(QtCore.Qt.AlignCenter)
        self.ID.setObjectName("ID")
        self.date = QtWidgets.QLabel(Form)
        self.date.setGeometry(QtCore.QRect(950, 10, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.date.setFont(font)
        self.date.setStyleSheet("border:1px solid #000000;\n"
                                "color: #5555ff;\n"
                                "border-radius: 5;")
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setObjectName("date")
        self.all_marks = QtWidgets.QPushButton(Form)
        self.all_marks.setEnabled(True)
        self.all_marks.setGeometry(QtCore.QRect(1010, 120, 121, 41))
        self.all_marks.setStyleSheet("QPushButton {\n"
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
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.all_marks.setFont(font)
        self.all_marks.setMouseTracking(False)
        self.all_marks.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.all_marks.setCheckable(False)
        self.all_marks.setChecked(False)
        self.all_marks.setAutoDefault(False)
        self.all_marks.setDefault(False)
        self.all_marks.setObjectName("all_marks")
        self.month_name = QtWidgets.QLabel(Form)
        self.month_name.setGeometry(QtCore.QRect(120, 120, 881, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.month_name.setFont(font)
        self.month_name.setStyleSheet("border:1px solid #000000;\n"
                                      "color: #5555ff;\n"
                                      "border-radius: 5;")
        self.month_name.setAlignment(QtCore.Qt.AlignCenter)
        self.month_name.setObjectName("month_name")
        self.add_comm = QtWidgets.QPushButton(Form)
        self.add_comm.setEnabled(True)
        self.add_comm.setGeometry(QtCore.QRect(760, 750, 181, 50))
        self.add_comm.setStyleSheet("QPushButton {\n"
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
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.add_comm.setFont(font)
        self.add_comm.setMouseTracking(False)
        self.add_comm.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.add_comm.setCheckable(False)
        self.add_comm.setChecked(False)
        self.add_comm.setAutoDefault(False)
        self.add_comm.setDefault(False)
        self.add_comm.setObjectName("add_comm")
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setEnabled(True)
        self.exit.setGeometry(QtCore.QRect(950, 750, 181, 50))
        self.exit.setStyleSheet("QPushButton {\n"
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
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.exit.setFont(font)
        self.exit.setMouseTracking(False)
        self.exit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exit.setCheckable(False)
        self.exit.setChecked(False)
        self.exit.setAutoDefault(False)
        self.exit.setDefault(False)
        self.exit.setObjectName("exit")
        self.left_pushbutton = QtWidgets.QPushButton(Form)
        self.left_pushbutton.setGeometry(QtCore.QRect(130, 130, 131, 21))
        self.left_pushbutton.setStyleSheet("QPushButton {\n"
                                           "    background-color: #ffffff;\n"
                                           "    border:1px solid #3e3e3e;\n"
                                           "    border-radius: 5;\n"
                                           "    color: #5555ff\n"
                                           "}\n"
                                           "\n"
                                           "QPushbutton:pressed {\n"
                                           "    background-color: #bebebe\n"
                                           "}\n"
                                           "QPushButton:hover { background-color: #a2a2d0; }\n"
                                           "QPushButton:pressed { background-color: #baacc7; }")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.left_pushbutton.setFont(font)
        self.left_pushbutton.setStyleSheet("QPushButton {\n"
                                           "    background-color: #ffffff;\n"
                                           "    border:1px solid #3e3e3e;\n"
                                           "    border-radius: 5;\n"
                                           "    color: #5555ff\n"
                                           "}\n"
                                           "\n"
                                           "QPushbutton:pressed {\n"
                                           "    background-color: #bebebe\n"
                                           "}\n"
                                           "QPushButton:hover { background-color: #a2a2d0; }\n"
                                           "QPushButton:pressed { background-color: #baacc7; }")
        self.left_pushbutton.setObjectName("left_pushbutton")
        self.right_pushbutton = QtWidgets.QPushButton(Form)
        self.right_pushbutton.setGeometry(QtCore.QRect(860, 130, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.right_pushbutton.setFont(font)
        self.right_pushbutton.setStyleSheet("QPushButton {\n"
                                            "    background-color: #ffffff;\n"
                                            "    border:1px solid #3e3e3e;\n"
                                            "    border-radius: 5;\n"
                                            "    color: #5555ff\n"
                                            "}\n"
                                            "\n"
                                            "QPushbutton:pressed {\n"
                                            "    background-color: #bebebe\n"
                                            "}\n"
                                            "QPushButton:hover { background-color: #a2a2d0; }\n"
                                            "QPushButton:pressed { background-color: #baacc7; }")
        self.right_pushbutton.setObjectName("right_pushbutton")
        self.lessons = QtWidgets.QTableWidget(Form)
        self.lessons.setGeometry(QtCore.QRect(680, 10, 261, 101))
        self.lessons.setStyleSheet("\n"
                                   "color: #5555ff;\n"
                                   "")
        self.lessons.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lessons.setProperty("showDropIndicator", False)
        self.lessons.setDragDropOverwriteMode(False)
        self.lessons.setObjectName("lessons")
        self.lessons.setColumnCount(8)
        self.lessons.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(1, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(2, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessons.setItem(2, 7, item)
        self.lessons.horizontalHeader().setDefaultSectionSize(40)
        self.lessons.horizontalHeader().setMinimumSectionSize(40)
        self.lessons.verticalHeader().setDefaultSectionSize(20)
        self.lessons.verticalHeader().setMinimumSectionSize(20)
        self.timetable_link = QtWidgets.QPushButton(Form)
        self.timetable_link.setGeometry(QtCore.QRect(380, 70, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setUnderline(True)
        self.timetable_link.setFont(font)
        self.timetable_link.setStyleSheet("QPushButton {\n"
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
        self.timetable_link.setObjectName("timetable_link")
        self.minimum_link = QtWidgets.QPushButton(Form)
        self.minimum_link.setGeometry(QtCore.QRect(10, 750, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setUnderline(True)
        self.minimum_link.setFont(font)
        self.minimum_link.setStyleSheet("QPushButton {\n"
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
        self.minimum_link.setObjectName("minimum_link")
        self.marks = QtWidgets.QTableWidget(Form)
        self.marks.setGeometry(QtCore.QRect(10, 170, 1121, 571))
        self.marks.setObjectName("marks")
        self.marks.setColumnCount(10)
        self.marks.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.marks.setHorizontalHeaderItem(9, item)
        self.marks.horizontalHeader().setDefaultSectionSize(50)
        self.marks.horizontalHeader().setMinimumSectionSize(50)
        self.absence = QtWidgets.QLabel(Form)
        self.absence.setGeometry(QtCore.QRect(10, 120, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.absence.setFont(font)
        self.absence.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.absence.setStyleSheet("border:1px solid #000000;\n"
                                   "color: #5555ff;\n"
                                   "border-radius: 5;")
        self.absence.setAlignment(QtCore.Qt.AlignCenter)
        self.absence.setObjectName("absence")
        self.news = QtWidgets.QLabel(Form)
        self.news.setGeometry(QtCore.QRect(190, 750, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.news.setFont(font)
        self.news.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.news.setStyleSheet("border:1px solid #000000;\n"
                                "color: #5555ff;\n"
                                "border-radius: 5;")
        self.news.setAlignment(QtCore.Qt.AlignCenter)
        self.news.setObjectName("news")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.username.setText(_translate("Form", "Васильев Даниил И."))
        self.class_ruk_name.setText(_translate("Form", "Уланова Ирина Дмитреевна"))
        self.ID.setText(_translate("Form", "0139, 10 \"З\""))
        self.date.setText(_translate("Form", "22.01.2021 16:04"))
        self.all_marks.setText(_translate("Form", "Выписка оценок"))
        self.month_name.setText(_translate("Form", "Сентябрь"))
        self.add_comm.setText(_translate("Form", "Сообщения"))
        self.exit.setText(_translate("Form", "Выйти"))
        self.left_pushbutton.setText(_translate("Form", "<-"))
        self.right_pushbutton.setText(_translate("Form", "->"))
        item = self.lessons.verticalHeaderItem(0)
        item.setText(_translate("Form", "Предмет"))
        item = self.lessons.verticalHeaderItem(1)
        item.setText(_translate("Form", "Время"))
        item = self.lessons.verticalHeaderItem(2)
        item.setText(_translate("Form", "Кабинет"))
        item = self.lessons.horizontalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.lessons.horizontalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.lessons.horizontalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.lessons.horizontalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.lessons.horizontalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.lessons.horizontalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.lessons.horizontalHeaderItem(6)
        item.setText(_translate("Form", "7"))
        item = self.lessons.horizontalHeaderItem(7)
        item.setText(_translate("Form", "8"))
        __sortingEnabled = self.lessons.isSortingEnabled()
        self.lessons.setSortingEnabled(False)
        item = self.lessons.item(0, 0)
        item.setText(_translate("Form", "abc"))
        item = self.lessons.item(0, 1)
        item.setText(_translate("Form", "abc"))
        item = self.lessons.item(0, 2)
        item.setText(_translate("Form", "abc"))
        item = self.lessons.item(0, 3)
        item.setText(_translate("Form", "abc"))
        item = self.lessons.item(0, 4)
        item.setText(_translate("Form", "abc"))
        item = self.lessons.item(0, 5)
        item.setText(_translate("Form", "abc"))
        item = self.lessons.item(0, 6)
        item.setText(_translate("Form", "abc"))
        item = self.lessons.item(0, 7)
        item.setText(_translate("Form", "abc"))
        item = self.lessons.item(1, 0)
        item.setText(_translate("Form", "12345"))
        item = self.lessons.item(1, 1)
        item.setText(_translate("Form", "23456"))
        item = self.lessons.item(1, 2)
        item.setText(_translate("Form", "23456"))
        item = self.lessons.item(1, 3)
        item.setText(_translate("Form", "23456"))
        item = self.lessons.item(1, 4)
        item.setText(_translate("Form", "23456"))
        item = self.lessons.item(1, 5)
        item.setText(_translate("Form", "23456"))
        item = self.lessons.item(1, 6)
        item.setText(_translate("Form", "23456"))
        item = self.lessons.item(1, 7)
        item.setText(_translate("Form", "23456"))
        item = self.lessons.item(2, 0)
        item.setText(_translate("Form", "123"))
        item = self.lessons.item(2, 1)
        item.setText(_translate("Form", "123"))
        item = self.lessons.item(2, 2)
        item.setText(_translate("Form", "123"))
        item = self.lessons.item(2, 3)
        item.setText(_translate("Form", "123"))
        item = self.lessons.item(2, 4)
        item.setText(_translate("Form", "123"))
        item = self.lessons.item(2, 5)
        item.setText(_translate("Form", "123"))
        item = self.lessons.item(2, 6)
        item.setText(_translate("Form", "123"))
        item = self.lessons.item(2, 7)
        item.setText(_translate("Form", "123"))
        self.lessons.setSortingEnabled(__sortingEnabled)
        self.timetable_link.setText(_translate("Form", "Расписание"))
        self.minimum_link.setText(_translate("Form", "Минимумы"))
        item = self.marks.verticalHeaderItem(0)
        item.setText(_translate("Form", "предмет"))
        item = self.marks.verticalHeaderItem(1)
        item.setText(_translate("Form", "предмет"))
        item = self.marks.verticalHeaderItem(2)
        item.setText(_translate("Form", "предмет"))
        item = self.marks.verticalHeaderItem(3)
        item.setText(_translate("Form", "предмет"))
        item = self.marks.verticalHeaderItem(4)
        item.setText(_translate("Form", "предмет"))
        item = self.marks.verticalHeaderItem(5)
        item.setText(_translate("Form", "предмет"))
        item = self.marks.verticalHeaderItem(6)
        item.setText(_translate("Form", "предмет"))
        item = self.marks.verticalHeaderItem(7)
        item.setText(_translate("Form", "предмет"))
        item = self.marks.verticalHeaderItem(8)
        item.setText(_translate("Form", "предмет"))
        item = self.marks.horizontalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.marks.horizontalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.marks.horizontalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.marks.horizontalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.marks.horizontalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.marks.horizontalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.marks.horizontalHeaderItem(6)
        item.setText(_translate("Form", "7"))
        item = self.marks.horizontalHeaderItem(7)
        item.setText(_translate("Form", "8"))
        item = self.marks.horizontalHeaderItem(8)
        item.setText(_translate("Form", "9"))
        item = self.marks.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Ср. зн."))
        self.absence.setText(_translate("Form", "Н-ки"))
        self.news.setText(_translate("Form", ""))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../Scripts/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class ToggleButton(QtWidgets.QPushButton): 
    def __init__(self, parent): 
        QtWidgets.QPushButton.__init__(self, parent) 
        self.checked = False
        self.clicked.connect(self.toggle) 

    def check(self): 
        self.checked = True 
        self.update()

    def uncheck(self): 
        self.checked = False 
        self.update() 

    def toggle(self): 
        self.checked = not self.checked 
        self.update() 

    def isChecked(self): 
        return self.checked

    def update(self): 
        if self.checked: 
            self.setStyleSheet("background:lightblue; color:white") 
        else: 
            self.setStyleSheet("background:dimgray; color:white")


class MyTextEdit(QtWidgets.QTextEdit):
    def __init__(self, parent, onFocus=None, onBlur=None): 
        QtWidgets.QTextEdit.__init__(self, parent)
        self.onFocus = onFocus
        self.onBlur = onBlur

    def focusInEvent(self, event):
        if self.onFocus is not None: 
            self.onFocus() 
        super(MyTextEdit, self).focusInEvent(event)

    def focusOutEvent(self, event):
        if self.onBlur is not None: 
            self.onBlur() 
        super(MyTextEdit, self).focusOutEvent(event)


class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent, onFocus=None, onBlur=None): 
        QtWidgets.QLineEdit.__init__(self, parent)
        self.onFocus = onFocus
        self.onBlur = onBlur

    def focusInEvent(self, event):
        if self.onFocus is not None: 
            self.onFocus() 
        super(MyLineEdit, self).focusInEvent(event)

    def focusOutEvent(self, event):
        if self.onBlur is not None: 
            self.onBlur() 
        super(MyLineEdit, self).focusOutEvent(event)


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self): 
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(860, 970)
        self.move(10,10)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -197, 877, 890))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 11)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.view_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.view_button.setObjectName("view_button")
        self.horizontalLayout_2.addWidget(self.view_button)
        self.edit_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.edit_button.setObjectName("edit_button")
        self.horizontalLayout_2.addWidget(self.edit_button)
        self.create_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.create_button.setObjectName("create_button")
        self.horizontalLayout_2.addWidget(self.create_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.loading_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.loading_label.setMinimumSize(QtCore.QSize(0, 0))
        self.loading_label.setObjectName("loading_label")
        self.loading_label.setStyleSheet("color:red") 
        self.loading_label.setVisible(False)
        self.horizontalLayout_2.addWidget(self.loading_label)
        self.submit_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.submit_button.setEnabled(False)
        self.submit_button.setStyleSheet("")
        self.submit_button.setObjectName("submit_button")
        self.horizontalLayout_2.addWidget(self.submit_button)
        self.cancel_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.cancel_button.setEnabled(False)
        self.cancel_button.setStyleSheet("")
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.patient_name = QtWidgets.QLineEdit(self.groupBox)
        self.patient_name.setEnabled(False)
        self.patient_name.setObjectName("patient_name")
        self.gridLayout_2.addWidget(self.patient_name, 1, 2, 1, 1)
        self.patient_age = QtWidgets.QLineEdit(self.groupBox)
        self.patient_age.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patient_age.sizePolicy().hasHeightForWidth())
        self.patient_age.setSizePolicy(sizePolicy)
        self.patient_age.setMinimumSize(QtCore.QSize(50, 0))
        self.patient_age.setMaximumSize(QtCore.QSize(50, 16777215))
        self.patient_age.setObjectName("patient_age")
        self.gridLayout_2.addWidget(self.patient_age, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.patient_id = MyLineEdit(self.groupBox)
        self.patient_id.setEnabled(False)
        self.patient_id.setObjectName("patient_id")
        self.gridLayout_2.addWidget(self.patient_id, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.patient_doctor = QtWidgets.QLineEdit(self.groupBox)
        self.patient_doctor.setEnabled(False)
        self.patient_doctor.setObjectName("patient_doctor")
        self.gridLayout_2.addWidget(self.patient_doctor, 2, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 3, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.medicine_list = QtWidgets.QListWidget(self.groupBox_2)
        self.medicine_list.setEnabled(True)
        self.medicine_list.setObjectName("medicine_list")
        self.verticalLayout_3.addWidget(self.medicine_list)
        self.add_button = QtWidgets.QPushButton(self.groupBox_2)
        self.add_button.setEnabled(False)
        self.add_button.setObjectName("add_button")
        self.verticalLayout_3.addWidget(self.add_button)
        self.dose_frame = QtWidgets.QFrame(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dose_frame.sizePolicy().hasHeightForWidth())
        self.dose_frame.setSizePolicy(sizePolicy)
        self.dose_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dose_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dose_frame.setObjectName("dose_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.dose_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.medicine_id = MyLineEdit(self.dose_frame)
        self.medicine_id.setObjectName("medicine_id")
        self.gridLayout_3.addWidget(self.medicine_id, 0, 1, 1, 1)
        self.medicine_name = MyLineEdit(self.dose_frame)
        self.medicine_name.setObjectName("medicine_name")
        self.gridLayout_3.addWidget(self.medicine_name, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.dose_frame)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.description = MyTextEdit(self.dose_frame)
        self.description.setObjectName("description")
        self.gridLayout_3.addWidget(self.description, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.dose_frame)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 5, 0, 1, 1)
        self.start_date = MyLineEdit(self.dose_frame)
        self.start_date.setObjectName("start_date")
        self.gridLayout_3.addWidget(self.start_date, 3, 1, 1, 1)
        self.end_date = MyLineEdit(self.dose_frame)
        self.end_date.setObjectName("end_date")
        self.gridLayout_3.addWidget(self.end_date, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.dose_frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.dose_frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.dose_frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.dose_frame)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.friday_button = ToggleButton(self.dose_frame)
        self.friday_button.setStyleSheet("background: dimgray; color: white")
        self.friday_button.setObjectName("friday_button")
        self.gridLayout.addWidget(self.friday_button, 0, 5, 1, 1)
        self.sunday_button = ToggleButton(self.dose_frame)
        self.sunday_button.setStyleSheet("background: dimgray; color: white")
        self.sunday_button.setObjectName("sunday_button")
        self.gridLayout.addWidget(self.sunday_button, 0, 0, 1, 1)
        self.monday_button = ToggleButton(self.dose_frame)
        self.monday_button.setStyleSheet("background: dimgray; color: white")
        self.monday_button.setObjectName("monday_button")
        self.gridLayout.addWidget(self.monday_button, 0, 1, 1, 1)
        self.tuesday_button = ToggleButton(self.dose_frame)
        self.tuesday_button.setStyleSheet("background: dimgray; color: white")
        self.tuesday_button.setObjectName("tuesday_button")
        self.gridLayout.addWidget(self.tuesday_button, 0, 2, 1, 1)
        self.saturday_button = ToggleButton(self.dose_frame)
        self.saturday_button.setStyleSheet("background: dimgray; color: white")
        self.saturday_button.setObjectName("saturday_button")
        self.gridLayout.addWidget(self.saturday_button, 0, 6, 1, 1)
        self.wednesday_button = ToggleButton(self.dose_frame)
        self.wednesday_button.setStyleSheet("background: dimgray; color: white")
        self.wednesday_button.setObjectName("wednesday_button")
        self.gridLayout.addWidget(self.wednesday_button, 0, 3, 1, 1)
        self.thursday_button = ToggleButton(self.dose_frame)
        self.thursday_button.setStyleSheet("background: dimgray; color: white")
        self.thursday_button.setObjectName("thursday_button")
        self.gridLayout.addWidget(self.thursday_button, 0, 4, 1, 1)
        self.select_all_button = QtWidgets.QPushButton(self.dose_frame)
        self.select_all_button.setObjectName("select_all_button")
        self.gridLayout.addWidget(self.select_all_button, 1, 0, 1, 1)
        self.deselect_all_button = QtWidgets.QPushButton(self.dose_frame)
        self.deselect_all_button.setObjectName("deselect_all_button")
        self.gridLayout.addWidget(self.deselect_all_button, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.dose_frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 6, 0, 1, 1)
        self.consume_time = MyLineEdit(self.dose_frame)
        self.consume_time.setObjectName("consume_time")
        self.gridLayout_3.addWidget(self.consume_time, 6, 1, 1, 1)
        self.ok_button = QtWidgets.QPushButton(self.dose_frame)
        self.ok_button.setObjectName("ok_button")
        self.gridLayout_3.addWidget(self.ok_button, 8, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.dose_frame)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.view_button.setText(_translate("MainWindow", "View"))
        self.edit_button.setText(_translate("MainWindow", "Edit"))
        self.create_button.setText(_translate("MainWindow", "Create New"))
        self.loading_label.setText(_translate("MainWindow", "Loading..."))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.groupBox.setTitle(_translate("MainWindow", "Patient Info"))
        self.label_4.setText(_translate("MainWindow", "Patient ID"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Age"))
        self.label_3.setText(_translate("MainWindow", "Doctor-in-charge"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dose Timetable"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.label_6.setText(_translate("MainWindow", "Description"))
        self.label_9.setText(_translate("MainWindow", "Repeat"))
        self.label_8.setText(_translate("MainWindow", "End date"))
        self.label_5.setText(_translate("MainWindow", "Medicine name"))
        self.label_7.setText(_translate("MainWindow", "Start date"))
        self.label_11.setText(_translate("MainWindow", "Medicine ID"))
        self.friday_button.setText(_translate("MainWindow", "Friday"))
        self.sunday_button.setText(_translate("MainWindow", "Sunday"))
        self.monday_button.setText(_translate("MainWindow", "Monday"))
        self.tuesday_button.setText(_translate("MainWindow", "Tuesday"))
        self.saturday_button.setText(_translate("MainWindow", "Saturday"))
        self.wednesday_button.setText(_translate("MainWindow", "Wednesday"))
        self.thursday_button.setText(_translate("MainWindow", "Thursday"))
        self.select_all_button.setText(_translate("MainWindow", "Select All"))
        self.deselect_all_button.setText(_translate("MainWindow", "Deselect all"))
        self.ok_button.setText(_translate("MainWindow", "OK"))
        self.label_10.setText(_translate("MainWindow", "Consume time"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(app.exec())
import sys
sys.path.append("./Scripts/ui")
sys.path.append("./Scripts/main")
sys.path.append("./Scripts/actions")
sys.path.append("./Scripts")

import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from main_ui import ToggleButton

import numpy as np 

def getDaysString(sundayBtn, mondayBtn, tuesdayBtn, wednesdayBtn, thursdayBtn, fridayBtn, saturdayBtn): 
	s = []
	for i, b in enumerate([sundayBtn, mondayBtn, tuesdayBtn, wednesdayBtn, thursdayBtn, fridayBtn, saturdayBtn]): 
		if b.isChecked(): 
			s.append(str(i)) 
	return ",".join(s)


def setDaysButton(sundayBtn, mondayBtn, tuesdayBtn, wednesdayBtn, thursdayBtn, fridayBtn, saturdayBtn, string): 
	s = string.split(",") 
	l = [sundayBtn, mondayBtn, tuesdayBtn, wednesdayBtn, thursdayBtn, fridayBtn, saturdayBtn]
	resetDaysButton(sundayBtn, mondayBtn, tuesdayBtn, wednesdayBtn, thursdayBtn, fridayBtn, saturdayBtn)
	for i in s: 
		l[int(i)].check() 


def resetDaysButton(sundayBtn, mondayBtn, tuesdayBtn, wednesdayBtn, thursdayBtn, fridayBtn, saturdayBtn): 
	for b in [sundayBtn, mondayBtn, tuesdayBtn, wednesdayBtn, thursdayBtn, fridayBtn, saturdayBtn]: 
		b.uncheck()


def resetFields(list_of_element): 
	for element in list_of_element: 
		if type(element) == ToggleButton: 
			element.uncheck() 
		elif type(element) == QtWidgets.QListWidget: 
			element.clear() 
		else: 
			element.setText("")


def disableFields(list_of_element): 
	for element in list_of_element: 
		element.setEnabled(False)

def enableFields(list_of_element): 
	for element in list_of_element: 
		element.setEnabled(True)


def checkAll(list_of_element): 
	for element in list_of_element: 
		element.check() 

def uncheckAll(list_of_element): 
	for element in list_of_element: 
		element.uncheck() 
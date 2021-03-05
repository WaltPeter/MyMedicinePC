import sys
sys.path.append("./Scripts/ui")
sys.path.append("./Scripts/main")
sys.path.append("./Scripts/actions")
sys.path.append("./Scripts")

import datetime
from functools import partial 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox

from main_ui import Ui_MainWindow
from AssistantAction import AssistantWindow
from utils.mysqlConnector import MySqlConnector
import utils.multithreading as thread
from utils.doseDict import DoseDict
from utils.utils import * 


class MainWindow(Ui_MainWindow): 
	def __init__(self):
		Ui_MainWindow.__init__(self) 

		self.ass = AssistantWindow(self)
		self.ass.show()

		self.dose_dict = DoseDict(self.medicine_list) 
		self.dose_frame.hide()
		self.view_button.clicked.connect(self.viewFunction)
		self.edit_button.clicked.connect(self.editFunction) 
		self.create_button.clicked.connect(self.createFunction) 
		self.submit_button.clicked.connect(self.submitFunction)
		self.cancel_button.clicked.connect(partial(self.cancelFunction, True))
		self.select_all_button.clicked.connect(partial(checkAll, [self.sunday_button, self.monday_button, 
					   self.tuesday_button, self.wednesday_button, self.thursday_button, 
					   self.friday_button, self.saturday_button]))
		self.deselect_all_button.clicked.connect(partial(uncheckAll, [self.sunday_button, self.monday_button, 
					   self.tuesday_button, self.wednesday_button, self.thursday_button, 
					   self.friday_button, self.saturday_button]))
		self.add_button.clicked.connect(self.addFunction)
		self.ok_button.clicked.connect(self.addMedicineFunction)
		self.medicine_list.clicked.connect(self.viewMedicineFunction)

		self.patient_id.onFocus = partial(self.ass.submitted.emit, "patient_id", True)
		self.patient_id.onBlur = partial(self.ass.submitted.emit, "patient_id", False)
		self.start_date.onFocus = partial(self.ass.submitted.emit, "start_date", True)
		self.start_date.onBlur = partial(self.ass.submitted.emit, "start_date", False)
		self.end_date.onFocus = partial(self.ass.submitted.emit, "end_date", True)
		self.end_date.onBlur = partial(self.ass.submitted.emit, "end_date", False)
		self.medicine_id.onFocus = self.lockMedicineName
		self.medicine_id.onBlur = self.updateMedicineName 
		self.medicine_name.onFocus = self.lockMedicineId
		self.medicine_name.onBlur = self.updateMedicineId
		self.description.onFocus = self._getDescriptionText
		self.description.onBlur = partial(self.ass.submitted.emit, "description", False) 
		self.consume_time.onFocus = self._getConsumeTimeText
		self.consume_time.onBlur = partial(self.ass.submitted.emit, "consume_time", False)

		disableFields([self.medicine_name, self.medicine_id, self.description, self.start_date, 
					   self.end_date, self.consume_time, self.sunday_button, self.monday_button, 
					   self.tuesday_button, self.wednesday_button, self.thursday_button, 
					   self.friday_button, self.saturday_button, self.patient_id, self.patient_name,
					   self.patient_age, self.patient_doctor, self.submit_button, self.cancel_button, 
					   self.add_button])

	def closeEvent(self, event):
		self.ass.close() 
		event.accept() 

	def viewFunction(self): 
		self.mode = "view"
		self.startMode() 

	def editFunction(self): 
		try: 
			if self.mode == "view": 
				self.mode = "edit"
				self.startMode() 
			else: 
				msg = QMessageBox()
				msg.setIcon(QMessageBox.Information)
				msg.setText("Please 'View' a record first.")
				msg.exec_()
		except: 
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Information)
			msg.setText("Please 'View' a record first.")
			msg.exec_()

	def createFunction(self): 
		self.mode = "create"
		self.startMode() 

	def addFunction(self): 
		self.dose_frame.show() 
		self.add_button.setEnabled(False)
		self.ok_button.setText("Insert")
		enableFields([self.medicine_name, self.medicine_id, self.description, self.start_date, 
					  self.end_date, self.consume_time, self.sunday_button, self.monday_button, 
					  self.tuesday_button, self.wednesday_button, self.thursday_button, 
					  self.friday_button, self.saturday_button, self.select_all_button, 
					  self.deselect_all_button])

	def addMedicineFunction(self): 
		med_name = self.medicine_name.text() 
		med_id = self.medicine_id.text() 
		desc = self.description.toPlainText() 
		med_start_date = self.start_date.text() 
		med_end_date = self.end_date.text() 
		time = self.consume_time.text() 
		bol = (self.ok_button.text() == "Update")
		days = getDaysString(self.sunday_button, self.monday_button, 
							 self.tuesday_button, self.wednesday_button, 
							 self.thursday_button, self.friday_button, 
							 self.saturday_button)
		self.dose_dict.add(med_id, med_name, desc, med_start_date, med_end_date, days, time, bol)
		resetFields([self.medicine_name, self.medicine_id, self.description, self.start_date, 
					 self.end_date, self.consume_time, self.sunday_button, self.monday_button, 
					 self.tuesday_button, self.wednesday_button, self.thursday_button, 
					 self.friday_button, self.saturday_button])
		self.dose_frame.hide() 
		if not self.mode == "view": self.add_button.setEnabled(True)

	def viewMedicineFunction(self): 
		try: 
			t = self.medicine_list.currentItem().text().split(" - ")
			self.medicine_id.setText(t[0]) 
			self.medicine_name.setText(t[1])
			self.description.setText(self.dose_dict.getDesc(t[0]))
			self.consume_time.setText(self.dose_dict.getTime(t[0]))
			self.end_date.setText(self.dose_dict.getEndDate(t[0]))
			self.start_date.setText(self.dose_dict.getStartDate(t[0]))
			setDaysButton(self.sunday_button, self.monday_button, 
						  self.tuesday_button, self.wednesday_button, 
						  self.thursday_button, self.friday_button, 
						  self.saturday_button, self.dose_dict.getDays(t[0]))
			self.dose_frame.show() 
			self.add_button.setEnabled(False)
			if not self.mode == "view":  
				enableFields([self.medicine_name, self.medicine_id, self.description, self.start_date, 
						  self.end_date, self.consume_time, self.sunday_button, self.monday_button, 
						  self.tuesday_button, self.wednesday_button, self.thursday_button, 
						  self.friday_button, self.saturday_button, self.select_all_button, 
						 self.deselect_all_button])
				self.ok_button.setText("Update")
		except Exception as e: 
			print(e)

	def cancelFunction(self, clear=True): 
		disableFields([self.medicine_name, self.medicine_id, self.description, self.start_date, 
					   self.end_date, self.consume_time, self.sunday_button, self.monday_button, 
					   self.tuesday_button, self.wednesday_button, self.thursday_button, 
					   self.friday_button, self.saturday_button, self.select_all_button, 
					   self.deselect_all_button, self.patient_id, self.patient_name,
					   self.patient_age, self.patient_doctor, self.submit_button, self.cancel_button, 
					   self.add_button])
		enableFields([self.view_button, self.edit_button, self.create_button])
		self.dose_frame.hide()

		if clear: 
			resetFields([self.medicine_name, self.medicine_id, self.description, self.start_date, 
						 self.end_date, self.consume_time, self.sunday_button, self.monday_button, 
						 self.tuesday_button, self.wednesday_button, self.thursday_button, 
						 self.friday_button, self.saturday_button, self.patient_id, self.patient_name,
						 self.patient_age, self.patient_doctor, self.medicine_list])

	def startMode(self): 
		self.view_button.setEnabled(False) 
		self.edit_button.setEnabled(False)
		self.create_button.setEnabled(False)
		self.submit_button.setEnabled(True)
		self.cancel_button.setEnabled(True)
		self.dose_frame.hide()

		if self.mode in ["edit", "create"]: 
			self.patient_name.setEnabled(True)
			self.patient_age.setEnabled(True)
			self.patient_doctor.setEnabled(True)
			self.add_button.setEnabled(True)
		elif self.mode == "view": 
			self.patient_id.setEnabled(True)

	def submitFunction(self): 
		self.loading_label.setVisible(True)
		self.ssThread = thread.myThread(2, "sqlThread", self._submitFunction, delay=0, once=True) 
		self.ssThread.start() 

	def _submitFunction(self): 
		disableFields([self.submit_button, self.cancel_button])
		db = MySqlConnector() 
		if self.mode == "create": 
			name = self.patient_name.text() 
			age = self.patient_age.text() 
			in_charge = self.patient_doctor.text() 
			db.insertPatientInfo(name, age, in_charge, self.dose_dict.getRawString())
			id = str(db.getPatientIdByName(name)[0])
			self.patient_id.setText(id) 

		elif self.mode == "view": 
			id = self.patient_id.text() 
			result = db.getPatientInfo(id) 
			if result is not None: 
				self.patient_name.setText(result[1])
				self.patient_age.setText(str(result[2])) 
				self.patient_doctor.setText(result[3])
				self.dose_dict.fromRawString(result[4].replace("'", '"'))
			else: 
				msg = QMessageBox()
				msg.setIcon(QMessageBox.Information)
				msg.setText("No result found.")
				msg.exec_()

		elif self.mode == "edit": 
			id = self.patient_id.text() 
			name = self.patient_name.text() 
			age = self.patient_age.text() 
			in_charge = self.patient_doctor.text() 
			db.updatePatientInfo(id, name, age, in_charge, self.dose_dict.getRawString())

		self.cancelFunction(False) 
		self.ssThread.end() 
		self.loading_label.setVisible(False)

	def lockMedicineName(self): 
		self.ass.submitted.emit("medicine_id", True)
		self.medicine_name.setEnabled(False)

	def lockMedicineId(self): 
		self.medicine_id.setEnabled(False)

	def updateMedicineName(self): 
		self.ssThread = thread.myThread(2, "sqlThread", self._updateMedicineName, delay=0, once=True) 
		self.ssThread.start() 

	def updateMedicineId(self): 
		self.ssThread = thread.myThread(2, "sqlThread", self._updateMedicineId, delay=0, once=True) 
		self.ssThread.start() 

	def _updateMedicineName(self): 
		self.ass.submitted.emit("medicine_id", False)
		self.medicine_name.setText("Loading...")
		db = MySqlConnector() 
		result = db.getMedicineName(self.medicine_id.text())
		if result is not None: 
			self.medicine_name.setText(result[0])
		else: 
			self.medicine_name.setText("")
		self.ssThread.end() 

	def _updateMedicineId(self): 
		self.medicine_id.setText("Loading...")
		db = MySqlConnector() 
		result = db.getMedicineId(self.medicine_name.text())
		if result is not None: 
			self.medicine_id.setText(result[0])
		else: self.medicine_id.setText("")
		self.ssThread.end() 

	def _getDescriptionText(self): 
		self.ass.submitted.emit("description", True) 
		self.ssThread = thread.myThread(2, "sqlThread", self._getText, delay=0, once=True) 
		self.ssThread.start() 

	def _getText(self): 
		db = MySqlConnector()
		result = db.getMedicineDirection(self.medicine_id.text())
		if result is not None: 
			self.ass.richTextSlot.emit(result[0])
		else: self.ass.richTextSlot.emit("")
		self.ssThread.end() 

	def _getConsumeTimeText(self): 
		self.ass.submitted.emit("consume_time", True) 
		self.ssThread = thread.myThread(2, "sqlThread", self._getText2, delay=0, once=True) 
		self.ssThread.start() 

	def _getText2(self): 
		db = MySqlConnector()
		result = db.getMedicineTime(self.medicine_id.text())
		if result is not None: 
			self.ass.richTextSlot.emit(result[0])
		else: self.ass.richTextSlot.emit("")
		self.ssThread.end() 


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec())
import sys
sys.path.append("./Scripts/ui")
sys.path.append("./Scripts/main")
sys.path.append("./Scripts/actions")
sys.path.append("./Scripts")

import datetime
from functools import partial 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from pyzbar import pyzbar
import cv2

import utils.multithreading as thread
from utils.mysqlConnector import MySqlConnector
from assistant_ui import Ui_AssistantWindow
from utils.utils import * 


class AssistantWindow(Ui_AssistantWindow): 
	submitted = QtCore.pyqtSignal(str, bool)
	richTextSlot = QtCore.pyqtSignal(str)

	def __init__(self, parent):
		Ui_AssistantWindow.__init__(self) 
		self.parent = parent
		self.submitted.connect(self.update) 
		self.richTextSlot.connect(self.updateRichText)
		self.qr_button.clicked.connect(self.qrScanner)
		self.cancel_button.clicked.connect(self.cancelScan)
		self.calendarWidget.clicked.connect(self.sendDate)
		self.insert_button.clicked.connect(self.insertText)
		for element in [self.after_breakfast, self.after_dinner,\
        				self.after_lunch, self.before_breakfast,\
        				self.before_dinner, self.before_lunch, self.am, self.pm]: 
			element.clicked.connect(partial(self.insertPhrase, element.text()))
	
	def scanner(self): 
		self.idle_label.setVisible(False)
		self.qr_button.setVisible(True)

	def qrScanner(self): 
		self.imshow.setVisible(True)
		self.qr_button.setVisible(False)
		self.cancel_button.setVisible(True)
		self.cam = cv2.VideoCapture(0) 
		self.ssThread = thread.myThread(1, "ssThread", self._qrScanner, delay=0) 
		self.ssThread.start() 

	def _qrScanner(self): 
		_, img = self.cam.read() 
		img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
		m = min(img.shape[1], img.shape[0]) 
		img = img[:m, :m, :]
		img = cv2.resize(img, (240,240))
		barcodes = pyzbar.decode(img)
		for barcode in barcodes: 
			(x, y, w, h) = barcode.rect
			cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 50), 3)
			cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
			barcodeData = barcode.data.decode("utf-8")
			barcodeType = barcode.type
			if self.name == "patient_id": 
				self.parent.patient_id.setText(barcodeData)
				self.parent.submit_button.clicked.emit() 
			elif self.name == "medicine_id": 
				self.parent.medicine_id.setText(barcodeData)
				self.parent.updateMedicineName() 
			self.cancelScan(True) 
		height, width, channel = img.shape
		bytesPerLine = 3 * width
		qImg = QtGui.QImage(img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888) 
		self.imshow.setPixmap(QtGui.QPixmap.fromImage(qImg)) 
		cv2.waitKey(1)

	def cancelScan(self, success=False): 
		self.ssThread.end() 
		if success: 
			img = cv2.imread("Resources/tick.jpg")
			img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
			height, width, channel = img.shape
			bytesPerLine = 3 * width
			qImg = QtGui.QImage(img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888) 
			self.imshow.setPixmap(QtGui.QPixmap.fromImage(qImg)) 
			cv2.waitKey(500)
			self.bringIdle() 
		self.imshow.setVisible(False)
		self.qr_button.setVisible(True)
		self.cancel_button.setVisible(False)
		self.cam.release() 

	def datePicker(self): 
		self.idle_label.setVisible(False)
		self.calendarWidget.setVisible(True)

	def sendDate(self): 
		d = str(self.calendarWidget.selectedDate().toString("MM-dd-yyyy"))
		if self.name == "start_date": 
			self.parent.start_date.setText(d)
		elif self.name == "end_date": 
			self.parent.end_date.setText(d)

	def textPicker(self): 
		self.richText.setText("Loading...")
		self.idle_label.setVisible(False)
		self.label.setVisible(True)
		self.richText.setVisible(True)
		self.insert_button.setVisible(True)

	def insertText(self): 
		if self.name == "description": 
			self.parent.description.setText(self.richText.toPlainText())
		elif self.name == "consume_time": 
			self.parent.consume_time.setText(self.richText.toPlainText()) 

	def pickTime(self): 
		self.after_breakfast.setVisible(True)
		self.after_dinner.setVisible(True)
		self.after_lunch.setVisible(True)
		self.before_breakfast.setVisible(True)
		self.before_dinner.setVisible(True)
		self.before_lunch.setVisible(True)
		self.label1.setVisible(True)
		self.label2.setVisible(True)
		self.time_textbox.setVisible(True)
		self.am.setVisible(True)
		self.pm.setVisible(True)

	def insertPhrase(self, text): 
		if text in ["AM", "PM"]: 
			text += " " + self.time_textbox.text()
		if self.name == "consume_time": 
			t = self.parent.consume_time.text() 
			if len(t) > 0: 
				self.parent.consume_time.setText(t + "," + text)
			else: self.parent.consume_time.setText(text)

	def bringIdle(self): 
		self.idle_label.setVisible(True)
		self.qr_button.setVisible(False)
		self.calendarWidget.setVisible(False)
		self.label.setVisible(False)
		self.richText.setVisible(False)
		self.insert_button.setVisible(False)
		self.after_breakfast.setVisible(False)
		self.after_dinner.setVisible(False)
		self.after_lunch.setVisible(False)
		self.before_breakfast.setVisible(False)
		self.before_dinner.setVisible(False)
		self.before_lunch.setVisible(False)
		self.label1.setVisible(False)
		self.label2.setVisible(False)
		self.time_textbox.setVisible(False)
		self.am.setVisible(False)
		self.pm.setVisible(False)

	@QtCore.pyqtSlot(str, bool) 
	def update(self, name, focus):
		if focus: 
			self.name = name 
			if name in ["patient_id", "medicine_id"]: 
				self.scanner() 
			elif name == "start_date": 
				self.datePicker() 
			elif name == "end_date": 
				self.datePicker() 
			elif name in ["description", "consume_time"]: 
				self.textPicker() 
				if name == "consume_time": 
					self.pickTime()
			self.name = name

		elif not self.isActiveWindow(): 
			self.name = ""
			self.bringIdle() 

	@QtCore.pyqtSlot(str)
	def updateRichText(self, text): 
		self.richText.setText(text)
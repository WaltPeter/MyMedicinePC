import sys 
sys.path.append("./Scripts/ui")
sys.path.append("./Scripts/main")
sys.path.append("./Scripts/actions")
sys.path.append("./Scripts")

import mysql.connector
from utils import DBStructure


class MySqlConnector: 

	def __init__(self): 
		self.mydb = mysql.connector.connect(
		  host = "remotemysql.com",
		  user = "JcoNLt0I6V",
		  password = "uY12VfydAr", 
		  database = "JcoNLt0I6V", 
		  port = "3306"
		)
		self.mycursor = self.mydb.cursor()

	def insertPatientInfo(self, name, age, in_charge, raw_json):
		cmd = "INSERT INTO `patient_info` (`ID`, `name`, `age`, `doctor_in_charge`, `raw_json`) VALUES (NULL, %s, %s, %s, %s);"
		val = (name, age, in_charge, raw_json)
		self.mycursor.execute(cmd, val)
		self.mydb.commit() 

	def updatePatientInfo(self, id, name, age, in_charge, raw_json):
		cmd = "UPDATE patient_info SET name = %s, age = %s, doctor_in_charge = %s, raw_json = %s WHERE ID = %s"
		val = (name, age, in_charge, raw_json, id)
		self.mycursor.execute(cmd, val)
		self.mydb.commit() 

	def getPatientInfo(self, patient_id): 
		cmd = 'SELECT * FROM `patient_info` WHERE `ID`=' + str(patient_id)
		self.mycursor.execute(cmd)
		return self.mycursor.fetchone()

	def getPatientIdByName(self, name): 
		cmd = 'SELECT * FROM `patient_info` WHERE `name`="' + name + '"'
		self.mycursor.execute(cmd)
		return self.mycursor.fetchone()

	def getMedicineId(self, medicine_name): 
		cmd = 'SELECT `id` FROM `medicine_info` WHERE `name`="' + medicine_name + '"'
		self.mycursor.execute(cmd) 
		return self.mycursor.fetchone() 

	def getMedicineName(self, medicine_id): 
		cmd = 'SELECT `name` FROM `medicine_info` WHERE `id`="' + medicine_id + '"'
		self.mycursor.execute(cmd) 
		return self.mycursor.fetchone() 

	def getMedicineDirection(self, medicine_id): 
		cmd = 'SELECT `direction` FROM `medicine_info` WHERE `id`="' + medicine_id + '"'
		self.mycursor.execute(cmd) 
		return self.mycursor.fetchone() 

	def getMedicineTime(self, medicine_id): 
		cmd = 'SELECT `consume_time` FROM `medicine_info` WHERE `id`="' + medicine_id + '"'
		self.mycursor.execute(cmd) 
		return self.mycursor.fetchone() 

	def createEventTable(self, tableName): 
		cmd = "CREATE TABLE " + tableName + "(ID INTEGER PRIMARY KEY AUTOINCREMENT, "\
            + DBStructure.EVENT + " TEXT, " + DBStructure.TIME + " TEXT, " + DBStructure.DATE + " TEXT, " + DBStructure.MONTH + " TEXT, "\
            + DBStructure.YEAR + " TEXT);" 


if __name__ == '__main__':
	db = MySqlConnector() 
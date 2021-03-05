import sys
sys.path.append("./Scripts/ui")
sys.path.append("./Scripts/main")
sys.path.append("./Scripts/actions")
sys.path.append("./Scripts")

import json
import numpy as np 

class DoseDict: 
	def __init__(self, medicine_list):
		self.data = {} 
		self.medicine_list = medicine_list 

	def add(self, id, name, desc, start_date, end_date, days, time, update=False): 
		bol = id in self.data
		if update: bol = not bol 
		if bol: 
			return False 
		else: 
			self.data[id] = {} 
			self.data[id]["id"] = id 
			self.data[id]["name"] = name 
			self.data[id]["desc"] = desc
			self.data[id]["time"] = time 
			self.data[id]["days"] = days 
			self.data[id]["start_date"] = start_date 
			self.data[id]["end_date"] = end_date

			self._updateList() 
		return True 

	def update(self, id, name, desc, start_date, end_date, time): 
		return self.add(id, name, desc, start_date, end_date, time, True)

	def _updateList(self): 
		self.medicine_list.clear() 
		for id in self.data: 
			self.medicine_list.addItem(str(id) + " - " + self.data[id]["name"])

	def getName(self, id): 
		return self.data[id]["name"] 

	def getDesc(self, id): 
		return self.data[id]["desc"]

	def getTime(self, id): 
		return self.data[id]["time"]

	def getStartDate(self, id): 
		return self.data[id]["start_date"]

	def getEndDate(self, id): 
		return self.data[id]["end_date"] 

	def getDays(self, id): 
		return self.data[id]["days"]


	def getRawString(self): 
		return str(self.data)


	def fromRawString(self, string): 
		try: self.data = json.loads(string) 
		except: self.data = {} 
		self._updateList() 
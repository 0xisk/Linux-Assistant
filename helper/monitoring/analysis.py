from database import db;
from datetime import datetime, timedelta;
from os.path import isfile;
from files import *;

class Collect :
	def __init__(self , start , end) :
		start = "-".join(start);
		end   = "-".join(end);
		if not self._isDateAscending(start, end) : raise ValueError("data should be in ascending order");
		self.start = start;
		self.end   = end;
		self.fileNames = self.getFilesName()

	def getFilesName(self) :
		start = datetime.strptime(self.start, "%Y-%m-%d")
		end = datetime.strptime(self.end, "%Y-%m-%d")
		delta = end - start
		names = [];
		for i in range(delta.days + 1) :
			dateDir = join(*(str(start + timedelta(days=i)).split(" ")[0].split("-")))
			dateDir = join(ROOTPATH,FOLDERNAME,dateDir+".db");
			names.append(dateDir)
		return names;

	def calculate(self) :
		collected = {};
		for path in self.fileNames :
			if isfile(path) :
				d = db(path)
				collected = d.append(d.get() , collected)
		return collected
				

	@staticmethod
	def _isDateAscending(d1, d2) :
		d1 = datetime.strptime(d1, "%Y-%m-%d")
		d2 = datetime.strptime(d2, "%Y-%m-%d")
		return (d2 > d1)



# c = Collect(["2018","03","22"] , ["2022","01","02"])
# print(c.calculate())



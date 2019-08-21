class report:
	def __init__(self,adno,name,marks,avg,getavg):
		self.__adno=adno
		self.__name=name
		self.__marks=marks
		self.__avg=avg
		self.__getavg()
	def readinfo(self,adno,name,marks):
		self.__getavg()
	def getinfo(self,adno,name,marks,avg):
		print(self.__adno)
		print(self.__name)
		print(self.__marks)
		print(self.__avg)
		print(self.__getavg())
		

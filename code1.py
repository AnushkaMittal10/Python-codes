class worker:

	def __init__(self,wno,wname,hrwrk,wgrate):
		self.__wn0=wno
		self.__wname=wname
		self.__hrwrk=hrwrk
		self.__wgrate=wgrate
		self.__towage=hrwrk*wgrate
		self.__calwg()
	def __calwg(self):
		return float(self.__hrwrk*self.__wgrate)

	def In_data(self,wno,wname,hrwrk,wgrate,towage):
		self.__calwg()
	def Out_data(self,wno,wname,hrwrk,wgrate,towage):
		print(self.__wno)
		print(self.__wname)
		print(self.__hrwrk)
		print(self.__wgrate)
		print(self.__towage)
		print(self.__calwg())

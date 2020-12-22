from atm_card import ATMCard

nominal = 10000
class Customer:  
	def __init__(self, id='', custPin='', custBalance=10000):
		self.id = id
		self.custPin = custPin
		self.custBalance = custBalance

	def debet (self, nominal):
		self.custBalance -= nominal

	def simpan (self, nominal):
		self.custBalance += nominal

	#def dump(self):
		#s = '%s, %s, custBalance: %s' %\
		#	(self.id, self.custPin, self.custBalance)
		#print (s)


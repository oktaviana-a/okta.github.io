class ATMCard:

	def __init__(defaultPin, defaultBalance):
		self.defaultPin=defaultPin
		self.defaultBalance=defaultBalance

	def info():
		return defaultPin + defaultBalance
		
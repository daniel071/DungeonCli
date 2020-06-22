# Some common classes that we have,
# Currently the class 'item' is unused

class Item:
	def __init__(self):
		self.amount=0

	def add(self, number):
		self.amount+=number

	def remove(self, number):
		self.amount-=number

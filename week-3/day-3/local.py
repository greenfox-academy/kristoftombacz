class BankAccount:
	def __init__(self, name, amount = 0):
		self.balance = amount
		self.name = name		

	def deposit(self, amount):
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance

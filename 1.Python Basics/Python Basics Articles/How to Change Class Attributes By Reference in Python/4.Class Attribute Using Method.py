class BankAccount:
	interest_rate = 0.03

	@classmethod
	def increase_interest_rate(cls, percentage):
		# Modify class attribute by reference through a method
		cls.interest_rate += percentage

# Increase interest rate by 1%
BankAccount.increase_interest_rate(0.01)

# Accessing the updated interest rate
print(BankAccount.interest_rate)

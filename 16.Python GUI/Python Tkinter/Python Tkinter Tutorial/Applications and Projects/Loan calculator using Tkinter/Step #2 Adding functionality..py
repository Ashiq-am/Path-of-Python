def computePayment(self):
	# compute the total payment.
	monthlyPayment = self.getMonthlyPayment(float(self.loanAmountVar.get()),
					float(self.annualInterestRateVar.get()) / 1200,
					int(self.numberOfYearsVar.get()))

	self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
	totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
						* int(self.numberOfYearsVar.get())
	self.totalPaymentVar.set(format(totalPayment, '10.2f'))

# compute the monthly payment.
def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
	monthlyPayment = loanAmount * monthlyInterestRate /(1- 1 / (1 + monthlyInterestRate) **
					(numberOfYears * 12))

	return monthlyPayment

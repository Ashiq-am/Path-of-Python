def calculate_tax(income):
  if income < 10000:
    rate = 0.1
  elif income < 20000:
    rate = 0.15
  elif income < 30000:
    rate = 0.2
  else:
    # Set a higher tax rate for higher incomes
    rate = 0.25

  tax = rate * income
  return tax

# Test the function with a few different incomes
print(calculate_tax(5000))   # Should print 500
print(calculate_tax(15000))  # Should print 2250
print(calculate_tax(25000))  # Should print 5000
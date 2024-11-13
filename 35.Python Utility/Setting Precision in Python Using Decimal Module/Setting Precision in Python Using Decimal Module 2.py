# Import required module
import decimal

# Set precision to a fixed value
decimal.getcontext().prec = 6

# Create Decimal object
ob1 = decimal.Decimal(5).sqrt()
ob2 = decimal.Decimal(7).sqrt()

# Display value up to 6 significant figures
print(ob1)
print(ob2)

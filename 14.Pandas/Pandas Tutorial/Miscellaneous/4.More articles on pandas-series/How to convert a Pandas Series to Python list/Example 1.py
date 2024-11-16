import pandas as pd


evenNumbers = [2, 4, 6, 8, 10]

evenNumbersDs = pd.Series(evenNumbers)
print("Pandas Series and type")
print(evenNumbersDs)
print(type(evenNumbersDs))

print("\nConvert Pandas Series to Python list")
print(evenNumbersDs.tolist())
print(type(evenNumbersDs.tolist()))

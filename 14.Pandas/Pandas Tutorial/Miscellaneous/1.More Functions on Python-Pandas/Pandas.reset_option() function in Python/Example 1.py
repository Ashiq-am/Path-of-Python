# importing the module
import pandas as pd

# setting the values
pd.set_option("display.max_rows", 10)
pd.set_option("display.min_rows", 2)
pd.set_option("display.max_columns", 5)
pd.set_option("display.html.border", 3)
pd.set_option("io.excel.xlsm.reader", "openpyxl")

# displaying the values
print("The altered values are : ")
print("Value of max_rows : " +
	str(pd.get_option("display.max_rows")))

print("Value of min_rows : " +
	str(pd.get_option("display.max_columns")))

print("Value of max_columns : " +
	str(pd.get_option("display.max_columns")))

print("Value of border : " +
	str(pd.get_option("display.html.border")))

print("Value of xlsm reader : " +
	str(pd.get_option("io.excel.xlsm.reader")))

# resetting the values to default
pd.reset_option("display.max_rows")
pd.reset_option("display.min_rows")
pd.reset_option("display.max_columns")
pd.reset_option("display.html.border")
pd.reset_option("io.excel.xlsm.reader")

# displaying the default values
print("\nThe default values are : ")

print("Value of max_rows : " +
	str(pd.get_option("display.max_rows")))

print("Value of min_rows : " +
	str(pd.get_option("display.max_columns")))

print("Value of max_columns : " +
	str(pd.get_option("display.max_columns")))

print("Value of border : " +
	str(pd.get_option("display.html.border")))

print("Value of xlsm reader : " +
	str(pd.get_option("io.excel.xlsm.reader")))

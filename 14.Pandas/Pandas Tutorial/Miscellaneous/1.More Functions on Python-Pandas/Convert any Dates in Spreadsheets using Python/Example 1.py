# This code converts any dates in spreadsheet

import pandas as pd

# Read the file and specify which column is the date
sample_dates = pd.read_excel("sample_dates.xlsx")

# Export output with dates converted to YYYY-MM-DD
sample_dates["Date"] = pd.to_datetime(
	sample_dates["Date"]).dt.strftime("%Y-%m-%d")
sample_dates.to_excel("sample_dates_formated.xlsx")

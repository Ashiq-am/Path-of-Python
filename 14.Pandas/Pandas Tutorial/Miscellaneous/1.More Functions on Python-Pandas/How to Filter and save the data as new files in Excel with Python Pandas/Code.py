# Python code to filter and save the
# data with different file names
import pandas


data = pandas.read_excel("datasets.xlsx")

speciesdata = data["Species"].unique()

for i in speciesdata:
	a = data[data["Species"].str.contains(i)]
	a.to_excel(i+".xlsx")

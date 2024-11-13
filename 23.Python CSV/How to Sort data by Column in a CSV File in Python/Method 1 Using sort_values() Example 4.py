# importing pandas package
import pandas as pandasForSortingCSV

# assign dataset
csvData = pandasForSortingCSV.read_csv("sample.csv")

# displaying unsorted data frame
print("\nBefore sorting:")
print(csvData)

# sort data frame
csvData.sort_values([csvData.columns[4], csvData.columns[2]],
					axis=0,
					ascending=[False, True],
					inplace=True)

# displaying sorted data frame
print("\nAfter sorting:")
print(csvData)

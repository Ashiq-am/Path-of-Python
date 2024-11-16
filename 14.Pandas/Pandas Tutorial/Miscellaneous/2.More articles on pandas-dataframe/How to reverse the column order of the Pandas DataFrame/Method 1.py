# importing required modules
import pandas as pd


dataframe = pd.DataFrame([[1, 'A', "Student"],
						[2, 'B', "Tutor"],
						[3, 'C', "Instructor"]])

print("Original DataFrame")
display(dataframe)

# revesing the dataframe
print("Revesed DataFrame")
display(dataframe[dataframe.columns[::-1]])

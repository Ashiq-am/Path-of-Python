# Python program to convert .tsv file to .csv file
# importing pandas library
import pandas as pd

tsv_file='GfG.tsv'

# readinag given tsv file
csv_table=pd.read_table(tsv_file,sep='\t')

# converting tsv file into csv
csv_table.to_csv('GfG.csv',index=False)

# output
print("Successfully made csv file")

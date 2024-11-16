# Import pandas library
import pandas as pd

# Read first two csv files with '\t' separator
tsv1 = pd.read_csv("Documents/Customer.tsv", sep='\t')
tsv2 = pd.read_csv("Documents/Account.tsv", sep='\t')

# store the result in Output_df dataframe.
# Here common column is 'ID' column
Output_df = pd.merge(tsv1, tsv2, on='ID',
					how='inner')

# store remaning file names in list
tsv_files = ["Branch.tsv", "Loan.tsv"]

# One by one read tsv files and merge with
# 'Output_df' dataframe and again store
# the final result in Output_df
for i in tsv_files:
	path = "Documents/"+i
	tsv = pd.read_csv(path, sep='\t')
	Output_df = pd.merge(Output_df, tsv,
						on='ID', how='inner')

# Now store the 'Output_df'
# in tsv file 'Output.tsv'
Output_df.to_csv("Documents/Output.tsv",
				sep="\t", header=True,
				index=False)

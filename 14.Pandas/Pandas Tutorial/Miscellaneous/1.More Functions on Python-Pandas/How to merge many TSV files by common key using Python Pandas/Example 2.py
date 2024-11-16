# Import pandas library
import pandas as pd

# Read first two csv files with '\t' separator
tsv3 = pd.read_csv("Documents/Course.tsv", sep='\t')
tsv4 = pd.read_csv("Documents/Teacher.tsv", sep='\t')

# store the result in Output_df dataframe.
# Here common column is 'Course_ID' column
Output_df2 = pd.merge(tsv3, tsv4, on='Course_ID', how='outer')

# store remaning file names in list
tsv_files = ["Credits.tsv", "Marks.tsv"]

# One by one read tsv files and merge with
# 'Output_df2' dataframe and again store
# the final result in 'Output_df2'
for i in tsv_files:
	path = "Documents/"+i
	tsv = pd.read_csv(path, sep='\t')
	Output_df2 = pd.merge(Output_df2, tsv,
						on='Course_ID', how='outer')


# Now store the 'Output_df2' in tsv file 'Output_outer.tsv'
# Here we replacing nan values with NA
Output_df2.to_csv("Documents/Output_outer.tsv", sep="\t",
				header=True, index=False, na_rep="NA")

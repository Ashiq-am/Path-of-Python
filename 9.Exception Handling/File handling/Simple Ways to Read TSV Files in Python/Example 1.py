# Simple Way to Read TSV Files in Python using pandas
# importing pandas library
import pandas as pd

# Passing the TSV file to
# read_csv() function
# with tab separator
# This function will
# read data from file
interviews_df = pd.read_csv('GeekforGeeks.tsv', sep='\t')

# printing data
print(interviews_df)

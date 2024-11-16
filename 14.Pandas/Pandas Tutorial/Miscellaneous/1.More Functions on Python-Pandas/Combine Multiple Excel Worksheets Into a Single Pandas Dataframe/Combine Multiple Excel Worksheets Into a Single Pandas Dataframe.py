# import module
import pandas as pd

# Read excel file
# and store into a DataFrame
df1 = pd.read_excel('excel_work\sample_data\Book_1.xlsx')
df2 = pd.read_excel('excel_work\sample_data\Book_2.xlsx')

# concat both DataFrame into a single DataFrame
df = pd.concat([df1, df2])

# Export Dataframe into Excel file
df.to_excel('final_output.xlsx', index=False)

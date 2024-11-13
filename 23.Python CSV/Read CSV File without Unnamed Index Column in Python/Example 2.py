# Read the CSV file removing unnamed columns
df = pd.read_csv('student_data.csv', index_col=0)
print('Dataframe after removing unnamed columns:')
print(df)

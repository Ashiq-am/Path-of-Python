# using pivot_table
df = df.pivot_table(index ='Name', columns =['Grade'],
						values =['Exam']).reset_index()

# Defining columns
df.columns =['Name', 'Maths', 'Physics', 'Chemistry']

# print dataframe
print(df)

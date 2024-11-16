# Creating a dataframe called df_final
df_final = []
df_final = pd.DataFrame(df_final)

# Merging the Employee Names
Name = []
for i in range(len(abc)):
	for j in range(len(final_in[i])):
		Name.append(abc[2][i])
df_final['Name'] = Name

# Zipping the Employee Name, Punch -IN
# records and Punch - OUT records
zippedList2 = list(zip(df_final['Name'], aa, bb))
abc2 = pd.DataFrame(zippedList2)

# Renaming the dataframe
abc2.columns = ['Emp Code', 'Punch - IN', 'Punch - OUT']
abc2.to_excel('output.xlsx', index=False)

# Print the table
display(abc2)

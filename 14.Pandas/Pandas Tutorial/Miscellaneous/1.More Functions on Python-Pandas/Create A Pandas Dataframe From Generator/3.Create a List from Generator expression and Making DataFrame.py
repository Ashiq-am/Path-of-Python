# Generator expression within a for loop to create a list of alphabets
alphabet_list = [chr(ord('A') + i) for i in range(5)]

# Creating a DataFrame from the list
df = pd.DataFrame({'Alphabets': alphabet_list})

# Display the DataFrame
print(df)

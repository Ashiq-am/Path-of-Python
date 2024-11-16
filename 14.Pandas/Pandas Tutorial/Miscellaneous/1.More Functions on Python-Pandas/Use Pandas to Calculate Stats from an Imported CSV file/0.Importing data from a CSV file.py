# Import Pandas library
import pandas as pd

url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240208132839/student_data2.csv'
# Read the CSV file
df=pd.read_csv(url)

# Print the data frame
print(df)

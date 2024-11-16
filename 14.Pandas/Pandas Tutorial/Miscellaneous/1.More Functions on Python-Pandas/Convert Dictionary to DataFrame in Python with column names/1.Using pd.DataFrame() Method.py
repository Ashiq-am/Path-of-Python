import pandas as pd

students = {"Shravan": 90, "Jeetu": 91, "Ram": 32, "Pankaj": 95}

# Convert the dictionary to a Pandas DataFrame
df = pd.DataFrame(students.items(), columns=['Name', 'Marks'])

print(df)

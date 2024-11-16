import pandas as pd

students = {"Shravan": 90, "Jeetu": 91, "Ram": 32, "Pankaj": 95}

# Convert dictionary to DataFrame
df = pd.DataFrame(list(students.items()), columns=['Name', 'Marks'])

print(df)

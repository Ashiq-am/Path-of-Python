# importing pandas
import pandas as pd

# Creating new dataframe
initial_data = {'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'],
                'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'],
                'Marks': [12, 52, 36, 85, 23]}

df = pd.DataFrame(initial_data, columns=['First_name', 'Last_name', 'Marks'])

# Generate result using pandas
result = []
for value in df["Marks"]:
    if value >= 33:
        result.append("Pass")
    elif value < 0 and value > 100:
        result.append("Invalid")
    else:
        result.append("Fail")

df["Result"] = result
print(df)

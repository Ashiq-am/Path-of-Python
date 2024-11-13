import pandas as pd
#taking the json file .

string = '{"names":["Harsha","Krishna","Vardhan"],"subject":["Physics","Maths","Java"]}'
#using the read_json method in the pandas
dataFrame = pd.read_json(string)
#Converting into the list

print(type(string))
print(list(dataFrame["names"]))
print(type(list(dataFrame["names"])))

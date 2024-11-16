# import library
import pandas as pd

# create a Dataframe
df = pd.DataFrame({
    'height': [165, 165, 164,
               158, 167, 160,
               158, 165],

    'weight': [63.5, 64, 63.5,
               54, 63.5, 62,
               64, 64],

    'age': [20, 22, 22,
            21, 23, 22,
            20, 21]},

    index=['Steve', 'Ria', 'Nivi',
           'Jane', 'Kate', 'Lucy',
           'Ram', 'Niki'])

# variable to hold the count
cnt = 0

# list to hold visited values
visited = []

# loop for counting the unique
# values in height
for i in range(0, len(df['height'])):

    if df['height'][i] not in visited:
        visited.append(df['height'][i])

        cnt += 1

print("No.of.unique values :",
      cnt)

print("unique values :",
      visited)

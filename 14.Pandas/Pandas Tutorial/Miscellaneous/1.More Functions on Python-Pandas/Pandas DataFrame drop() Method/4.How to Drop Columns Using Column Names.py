import pandas as pd
df = pd.DataFrame({'Name': ['Alice', 'Bob'],'Age': [25, 30],'City': ['New York', 'Los Angeles'],'Country': ['USA', 'USA']})

# Drop the columns 'Age' and 'Country'
df.drop(columns=['Age', 'Country'],inplace=True)
print(df)
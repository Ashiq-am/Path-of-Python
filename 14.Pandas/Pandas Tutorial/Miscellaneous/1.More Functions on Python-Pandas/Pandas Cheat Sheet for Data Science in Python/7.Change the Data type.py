df['Quantity'] = df['Quantity'].astype('int32')
df['Fruits'] = df['Fruits'].astype('str')
df['Price'] = df['Price'].astype('float')

df.info()

# prints first five rows including 5th index and every columns of df
df.loc[0:5,:]
# prints from 5th rows onwards and entire columns
df = df.loc[5:,:]






"""The above doesn’t actually look much different from df.iloc[0:5,:]. This is because while row labels can 
take on any values, our row labels match the positions exactly"""

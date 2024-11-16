# splitting dataframe by row index
df_1 = df.iloc[:1000,:]
df_2 = df.iloc[1001:,:]
print("Shape of new dataframes - {} , {}".format(df_1.shape, df_2.shape))

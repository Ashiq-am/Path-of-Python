# dataframe df_3 to contain only mean_area,Cat_mean_area and target
df_3 = df_2[['mean area', 'Cat_mean_area', 'target']]

# applying groupby sum
gr2 = df_3.groupby(df_2['Cat_mean_area']).sum()
gr2

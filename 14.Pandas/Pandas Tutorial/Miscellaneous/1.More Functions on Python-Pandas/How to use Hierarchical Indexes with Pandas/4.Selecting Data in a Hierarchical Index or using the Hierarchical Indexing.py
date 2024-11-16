# selecting the 'Pacific' and 'Mountain'
# region from the dataframe.

# selecting data using level(0) index or main index.
df_ind3_region = df_ind3.loc[['Pacific', 'Mountain']]

print(df_ind3_region.head(10))

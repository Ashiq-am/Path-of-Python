# multiple unpivot columns
pd.melt(df, id_vars =['Name'], value_vars =['Course', 'Age'])

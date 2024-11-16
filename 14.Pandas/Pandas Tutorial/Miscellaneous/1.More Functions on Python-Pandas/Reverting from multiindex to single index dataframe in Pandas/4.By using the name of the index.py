# using the reset_index(), reverting
# the 'region' and 'state' indexes.
df_si_name = df_mi.reset_index([ 'region' , 'state' ])

print(df_si_name.head())

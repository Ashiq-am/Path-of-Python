# using the reset_index(), reverting the
# level 0 and level 2 indexes.
df_si_level = df_mi.reset_index( level = [0 , 2] )

print(df_si_level.head())

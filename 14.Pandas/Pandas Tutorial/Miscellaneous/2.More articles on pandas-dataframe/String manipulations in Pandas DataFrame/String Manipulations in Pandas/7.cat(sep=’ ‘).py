# cat(sep=pattern)
print(df)

print("\nafter using cat:")
print(df.str.cat(sep='_'))

print("\nworking with NaN using cat:")
print(df.str.cat(sep='_', na_rep='#'))

# We can change multiple column names by
# passing a dictionary of old names and
# new names, to the rename() function.
df = df.rename({"Mod_col":"Col_1","B":"Col_2"}, axis='columns')

df

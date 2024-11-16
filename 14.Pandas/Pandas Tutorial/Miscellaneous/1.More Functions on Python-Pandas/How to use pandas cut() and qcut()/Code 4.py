df.loc[0, 'Year'] = np.nan

# these are the 'unique' years in
# the data
np.array(sorted(df.Year.unique()))

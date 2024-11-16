# Grouping with only status
grouped1 = df.groupby("Status")

# Grouping with temperature and status
grouped3 = df.groupby(["Temperature", "Status"])

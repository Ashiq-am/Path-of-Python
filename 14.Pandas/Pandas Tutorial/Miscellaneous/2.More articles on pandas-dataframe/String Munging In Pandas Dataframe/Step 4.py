pattern = "([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})"
print(df["email"].str.findall(pattern, flags=re.IGNORECASE))

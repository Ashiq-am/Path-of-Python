# Appending Different Columns
z = pd.DataFrame([["1.3", "9.2"]], columns = ["E", "F"])
t = t.append(z)
print(t)
print(t.dtypes)
print()

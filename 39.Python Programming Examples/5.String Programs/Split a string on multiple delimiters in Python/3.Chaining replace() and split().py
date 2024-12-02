s = "apple, banana; orange grape"

# Replace each delimiter by chaining
s = s.replace(',', ' ').replace(';', ' ')

# split string on whitespace.
res = s.split()
print(res)
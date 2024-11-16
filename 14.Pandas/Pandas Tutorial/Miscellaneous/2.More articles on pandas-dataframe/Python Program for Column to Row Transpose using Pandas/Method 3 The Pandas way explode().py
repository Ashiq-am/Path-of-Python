df = pd.read_csv(r'GFG.txt')

# seperate values using split()
# transpose is performed by explode
# function explode function overcomes
# the method1 shortcomings incase we
# have many columns we explode will do
# the task in no time and with no hassle
df1 = df.assign(name = df['name'].str.split('|')).explode('name')
df1

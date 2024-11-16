data = {'item1': df1, 'item2': df2}

# creating Panel
panel = pd.Panel.from_dict(data, orient='minor')
print("panel['b'] is - \n\n", panel['b'], '\n')

print("\nSize of panel['b'] is - ", panel['b'].size)

import matplotlib.pyplot as plt

data = [
    ['Year', 'Sales', 'Profit'],
    [2021, 15000, 3000],
    [2022, 20000, 5000],
    [2023, 25000, 7000]
]

fig, ax = plt.subplots()
ax.axis('tight')
ax.axis('off')

# Create the table with row and column labels
table = ax.table(cellText=data,
                 colLabels=['Year', 'Sales', 'Profit'],
                 loc='center',
                 cellLoc='center',
                 rowColours=['lightgrey']*4)

plt.title("Customized Sales Data Table")
plt.show()
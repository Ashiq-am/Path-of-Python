# Loading structured data from a CSV file
structured_data = np.genfromtxt('data.csv', delimiter=',', names=True)
print("Structured Data:\n", structured_data)
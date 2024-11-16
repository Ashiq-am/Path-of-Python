# import package
import pandas as pd

# define data
data = pd.DataFrame(
{'ID': {0: 105, 1: 102, 2: 101, 3: 106, 4: 103, 5: 104, 6: 107},

'Name': {0: 'Ram Kumar', 1: 'Jack Wills', 2: 'Deepanshu Rustagi',
		3: 'Thomas James', 4: 'Jenny Advekar', 5: 'Yash Raj',
		6: 'Raman Dutt Mishra'},

'Age': {0: 40, 1: 23, 2: 20, 3: 34, 4: 18, 5: 56, 6: 35},

'Country': {0: 'India', 1: 'Uk', 2: 'India', 3: 'Australia',
			4: 'Uk', 5: 'India', 6: 'India'}
}
)

# view data
data

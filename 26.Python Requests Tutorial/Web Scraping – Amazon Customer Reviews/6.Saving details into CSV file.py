import pandas as pd

# intialise data of lists.
data = {'Name': cus_res,
		'review': rev_result}

# Create DataFrame
df = pd.DataFrame(data)

# Save the output.
df.to_csv('amazon_review.csv')

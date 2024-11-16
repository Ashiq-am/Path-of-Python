import pandas as pd

# intialise data of lists.
data = [['Raghav', 'Jeeva', 'Imon', 'Sandeep'],
		['Deloitte', 'Apple', 'Amazon', 'Flipkart'],
		[2,3,7,8]]

# Create DataFrame
df = pd.DataFrame(data)
left_aligned_df = df.style.set_properties(**{'text-align': 'left'})
display(left_aligned_df)

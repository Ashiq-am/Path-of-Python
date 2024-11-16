import pandas as pd

# intialise data of lists.
data = [['Raghav', 'Jeeva', 'Imon', 'Sandeep'],
		['Deloitte', 'Apple', 'Amazon', 'Flipkart'],
		[2,3,7,8]]

# Create DataFrame
df = pd.DataFrame(data)
left_aligned_df = df.style.set_properties(**{'text-align': 'left'})

left_aligned_df = left_aligned_df.set_table_styles(
[dict(selector = 'th', props=[('text-align', 'left')])])

display(left_aligned_df)

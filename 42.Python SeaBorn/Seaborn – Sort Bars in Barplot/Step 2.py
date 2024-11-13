# Initialize data
State = ["Rajasthan", "Bihar", "Madhya Pradesh",
		"Gujarat", "Maharashtra"]
growth = [342239, 94163, 308245, 196024, 307713]

# Create a pandas dataframe
df = pd.DataFrame({"State": State,
				"Growth": growth})

# Display Dataframe
df

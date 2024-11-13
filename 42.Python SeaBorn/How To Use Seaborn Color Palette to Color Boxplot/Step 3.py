# Create boxplot and add palette
# with predefined values like Paired, Set1, etc
sns.boxplot(x="Pulses", y="Tons Consumed",
			data=data_df, palette="Paired")

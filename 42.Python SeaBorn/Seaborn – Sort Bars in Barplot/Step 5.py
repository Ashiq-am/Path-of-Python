# make barplot and sort bars
sns.barplot(x='State',
			y="Growth", data=df,
			order=df.sort_values('Growth',ascending = False).State)

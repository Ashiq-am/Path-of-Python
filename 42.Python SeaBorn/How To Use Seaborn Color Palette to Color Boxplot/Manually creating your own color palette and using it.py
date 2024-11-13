#create your own color array
my_colors = ["#9b59b6", "#3498db",
			"#2ecc71", "#006a4e"]

# add color array to set_palette
# function of seaborn
sns.set_palette( my_colors )

# make boxplot
sns.boxplot( x = "Pulses", y = "Tons Consumed",
			data = data_df)

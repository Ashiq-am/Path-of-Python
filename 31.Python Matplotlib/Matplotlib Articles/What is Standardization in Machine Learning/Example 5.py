# Calculating the Z-Score for each
# Value of dataset_1
final_z_score = []
print("Calculating Z-Score of Each Value in dataset_1")

for i in dataset_1:
	z_score = (i-mean)/standard_deviation
	final_z_score.append("{:.20f}".format(z_score))

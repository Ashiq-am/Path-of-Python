total_all_count = 0
total_hem_count = 0
for dirname, _, filenames in os.walk('.../C-NMC_Leukemia/training_data'):
	for filename in filenames:
		all_count = 0
		hem_count = 0
		if "training" in dirname:
			if "all" in dirname:
				all_count = len(filenames)
			elif "hem" in dirname:
				hem_count = len(filenames)
			total_all_count += all_count
			total_hem_count += hem_count
			break
print(
	f"HEM(Normal) Cell Count {total_hem_count} \nALL(Leukemia) Cell Count {total_all_count}")

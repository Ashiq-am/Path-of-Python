from natsort import natsorted

case_insensitive_data = ["Apple", "banana", "Orange", "grape"]
sorted_case_insensitive = natsorted(case_insensitive_data, alg=natsorted.IC)
print(sorted_case_insensitive)

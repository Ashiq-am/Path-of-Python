from deepdiff import DeepDiff

a = {'Name': 'asif', 'Age': 5}
b = {'Name': 'lalita', 'Age': 78}

diff = DeepDiff(a, b)

print(diff)

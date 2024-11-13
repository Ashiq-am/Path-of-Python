from collections import defaultdict

Details = defaultdict(list)
print("Original:", Details)

Details["Country"].append("India")
Details["Country"].append("Pakistan")
print("Modified:", Details)

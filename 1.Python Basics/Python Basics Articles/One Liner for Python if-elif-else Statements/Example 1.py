x = 87

result = {x > 190: "First condition satisfied!",
		x == 87: "Second condition satisfied!"}.get(
True, "Third condition satisfied")

print(result)

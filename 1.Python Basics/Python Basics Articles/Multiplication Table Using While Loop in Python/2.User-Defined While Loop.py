# User-Defined While Loop
multiplier = int(input("Enter the multiplier: "))
start = 1
end = int(input("Enter the range end: "))

while start <= end:
	result = start * multiplier
	print(f"{start} x {multiplier} = {result}")
	start += 1

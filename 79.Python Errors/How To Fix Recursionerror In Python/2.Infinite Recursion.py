def countdown(n):
	if n > 0:
# Here we dont reduce n so it leads to infinite loop
		print(n)
		countdown(n)
# Example usage with n=5
n=5
countdown(n)

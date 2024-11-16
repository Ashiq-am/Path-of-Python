# return values between the passed time duration
# skip the start and end time
result = sr.between_time(start_time = '10:45', end_time = '15:45',
					include_start = False, include_end = False)

# Print the result
print(result)

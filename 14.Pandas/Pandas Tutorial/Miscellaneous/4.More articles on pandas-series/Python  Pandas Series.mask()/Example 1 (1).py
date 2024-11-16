# replace 'Rio' with 'Tokyo'
result = sr.mask(lambda x : x =='Rio', other = 'Tokyo')

# Print the result
print(result)

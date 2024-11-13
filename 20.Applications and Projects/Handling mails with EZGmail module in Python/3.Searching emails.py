import ezgmail

# searching for specific emails
results = ezgmail.search('geeksforgeeks')
print(results[0])

# special searches
results = ezgmail.search('has:attachment')
print(results[0])

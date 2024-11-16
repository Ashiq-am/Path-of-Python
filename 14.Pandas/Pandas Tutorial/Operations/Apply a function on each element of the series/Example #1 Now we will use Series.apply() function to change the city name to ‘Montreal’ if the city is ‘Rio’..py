# change 'Rio' to 'Montreal'
# we have used a lambda function
import sr as sr

result = sr.apply(lambda x : 'Montreal' if x =='Rio' else x )

# Print the result
print(result)

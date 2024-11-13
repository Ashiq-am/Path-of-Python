# Python Program to demonstrate use of strip() method

str1 = 'geeks for geeks'
# Print the string without striping.
print(str1)

# String whose set of characters are to be
# remove from original string at both its ends.
str2 = 'ekgs'

# Print string after striping str2 from str1 at both its end.
print(str1.strip(str2))










"""

Working of above code :

We first construct a string str1 = ‘geeks for geeks’

Now we call strip method over str1 and pass str2 = ‘ekgs’ as arguement.

Now python interpreter trace str1 from left.It remove the character of str1 if it is present in str2.

Otherwise it stops tracing.

Now python interpreter trace str1 from right. It remove the character of str1 if it is present in str2.

Otherwise it stop tracing.

Now at last it returns the resultant string.

When we call strip() without argument, it removes leading and trailing spaces.


"""
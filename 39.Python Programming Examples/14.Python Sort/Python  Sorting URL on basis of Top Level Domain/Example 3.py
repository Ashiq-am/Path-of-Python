#Python code to sort the URL in the list based on the top-level domain.

#Url list initialization
Input = ["https://www.isb.edu", "www.google.com", "http://cyware.com",
"https://www.gst.in", "https://www.coursera.org",
"https://www.create.net", "https://www.ontariocolleges.ca"]

#Internal function for reversed
def internal(string):
	return list(reversed(string.split('.')))

#Using sorted and calling internal for reversed
Output = sorted(Input, key=internal)

#Printing output
print("Initial list is :")
print(Input)
print("sorted list according to TLD is")
print(Output)

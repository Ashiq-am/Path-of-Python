#Python code to sort the URL in the list based on the top-level domain.

#Url list initialization
Input = ["https://www.isb.edu", "www.google.com", "http://cyware.com",
"https://www.gst.in", "https://www.coursera.org",
"https://www.create.net", "https://www.ontariocolleges.ca"]

#Function to sort in tld order
def tld(Input):
	return Input.split('.')[-1]

#Using sorted and calling function
Output = sorted(Input,key=tld)

#Printing output
print("Initial list is :")
print(Input)
print("sorted list according to TLD is")
print(Output)

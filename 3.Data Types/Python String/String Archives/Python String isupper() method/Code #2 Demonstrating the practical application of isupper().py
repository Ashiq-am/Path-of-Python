# Python3 code to demonstrate
# application of isupper()

# checking for abbreviations.
# short form of work/phrase
test_str = "Cyware is US based MNC and works in IOT technology"

# splitting string
list_str = test_str.split()

count = 0

# counting upper cases
for i in list_str:
	if (i.isupper()):
		count = count + 1

# printing abbreviations count
print ("Number of abbreviations in this sentence is : " + str(count))

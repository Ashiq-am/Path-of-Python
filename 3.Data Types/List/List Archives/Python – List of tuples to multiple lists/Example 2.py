# list of tuple for student
# data with both integer and strings
a = [(1, 2,3,4,5),
	("sravan","bobby","ojaswi","rohith","Gnanesh"),
	(96,89,78,90,78),
	("kakumanu","kakumanu","hyd","hyd","hyd")]

# convert list of tuple to multiple lists
data = map(list, zip(*a))

# display
for i in data:
    print(i)

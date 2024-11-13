''''''





"""string1 and string2 both point to same object or same location.Now if someone try to modify any one of the 
string results will be different."""





# Modifying a string

string1 = "Hello"

# identity of string1
print(id(string1))

string1 += "World"
print(string1)

# identity of modified string1
print(id(string1))
















"""String1 is modified which contradict the fact that strings are immutable, but the identity before and after 
modification are different.

It means a new object of the string1 is created after modification which confirms the fact that strings are 
immutable as no change was made in previous object of string1 rather a new one is created."""
